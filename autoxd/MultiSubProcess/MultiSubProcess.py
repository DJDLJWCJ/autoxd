#-*- coding:utf-8 -*-
#把主目录放到路径中， 这样可以支持不同目录中的库
from __future__ import print_function
import os
import numpy as np
import pandas as pd
import sys, subprocess, math
from autoxd import myredis

"""手工实现并行， 用单个subprocess来跑"""

def getMainDir():
    add_path = os.path.dirname(__file__) + '/..'
    add_path = os.path.abspath(add_path)
    return add_path    

def getResultName(i):
    return 'multi_'+str(i)
class MultiSubProcess():
    """
    任务执行表task_id, module, fn, arg, result
    先生成任务表，再把task_id通过命令行传入
    """
    def __init__(self):
        self.pd_task = pd.DataFrame([])
        self.task_id = 0
        self._Clear()
    def __del__(self):
        self._Clear()
    def Map(self, cpus, fname, fn, *args, **kwargs):
        """map参数, 分解后记录到map目录中, 
        回调函数必须符合函数声明fn(codes, taskid)
        注意， 回调函数必须是公开函数不能是内部函数或类函数， 模块要在根目录执行
        fname : 调用者文件路径, 包含fn函数
        fn: 执行函数名称 fn(list, int)
        args: map的参数
        kwargs: 保留, 暂时未用
        return:df"""
        # 根据加载路径计算import路径
        root = os.path.abspath(os.path.dirname(__file__)+'/../../')
        from_str = os.path.abspath(os.path.dirname(fname))
        assert(root.lower() == from_str[:len(root)].lower())
        #from_str = from_str.replace(root, '')[1:]
        from_str = from_str[len(root)+1:]
        if sys.platform == 'win32':
            from_str = from_str.replace('\\','.')
        else:
            from_str = from_str.replace('/','.')
        bname = os.path.basename(fname)
        module = bname.split('.')[0]
        from_module = 'from %s import %s'%(from_str, module)
        
        #分割参数
        splitted_args = pp_func_param(None, *args, cpu=cpus)._split(*args)
        for arg in splitted_args:
            self.pd_task = pd.concat([self.pd_task, pd.DataFrame([self.task_id, from_module, fn.__name__, arg]).T])
        self.task_id += 1
    def Run(self):
        self.pd_task.index = range(len(self.pd_task))
        print(self.pd_task)
        #保存任务表
        myredis.set_obj('multi', self.pd_task)
        cmd = sys.executable
        fname = 'MultiSubProcess_exec2.py'
        if sys.version > '3':
            fname = 'pinyin/MultiSubProcess_exec.py'
        cmd += ' '+getMainDir()+'/'+fname
        process = []
        for i in range(len(self.pd_task)):
            cur_cmd = cmd + ' ' + str(i)
            #print cur_cmd
            if sys.platform != 'win32':
                cur_cmd = cur_cmd.split(' ')
            p = subprocess.Popen(cur_cmd)
            process.append(p)
        for p in process:            
            p.wait()
    def Reduce(self):
        """合并结果, 返回各任务的df
        return: list, 有几个Map list里就有几个元素"""
        df = self.pd_task
        #按task_id来排序
        max_id = np.max(df[0])
        result = []
        for task_id in range(max_id+1):
            df_result = pd.DataFrame([])
            for i in df[df[0]==task_id].index:
                r = myredis.get_obj(getResultName(i))
                assert(isinstance(r, pd.DataFrame))
                df_result = pd.concat([df_result, r])
            result.append(df_result)
        return result
    def _Clear(self):
        """清空redis中的记录"""
        count = len(self.pd_task)
        for i in range(count):
            key = getResultName(i)
            myredis.delkey(key)
        myredis.delkey('multi')
        
class pp_func_param:
    """自动根据cpu个数裁剪参数长度 func, param, sub_func, func_import_modul, cpu"""
    def __init__(self, func, param, sub_func=None, func_import_modul=None, cpu=7):
        """"""
        self.func = func
        self.cpu = cpu
        self.params = self._split(param)
        if isinstance(sub_func, type(None)):
            sub_func = tuple()
        self.sub_funcs = sub_func
    def _split(self, params):
        """分割参数
        param: 如果是list， 那么就直接拆解， 如果是tuple，那么就拆解第一个，后面的合并上去"""
        other = None
        if isinstance(params, tuple):
            other = params[1:]
            params = params[0]
        # 1维
        if len(params) < self.cpu:
            self.cpu = len(params)
            return params
        r = []
        splitted_size = math.ceil(float(len(params))/self.cpu)
        for i in range(self.cpu):
            left = int(splitted_size*i)
            right = int(splitted_size*(i+1))
            if i == self.cpu-1:
                right = len(params)
            param = params[left:right]
            if len(param)>0:
                if other != None:
                    param =tuple([param]+list(other))
                r.append(param)
            else:
                self.cpu -= 1
        return r
        
def test(a, task_id):
    print('pid=',os.getpid(), a)
    return pd.DataFrame(a)
def test2(b, task_id):
    print('test2', b)
    return pd.DataFrame(b)
def main(args):
    multi = MultiSubProcess()
    multi.Map(3,__file__, test, list(range(100)))
    multi.Map(1, __file__, test2, list(range(20)))
    multi.Run()
    df1, df2 = multi.Reduce()
    print(df1)
    
if __name__ == "__main__":
    try:
        args = sys.argv[1:]
        main(args)
    except:
        main(None)