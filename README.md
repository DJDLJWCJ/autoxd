Autoxd
======

A��ʵ���Զ�������ϵͳ

����
----
�����˺ż���ִ�еĿ��ٽ���ϵͳ�����鼰���׽ӿ���c++��д��ͨ��Э�鷽ʽ��ȡ����API��ʽ�� ������python��д��
�ʺ�ʹ�ø������Ŀ����Ⱥ<br>
1. ϣ��ʹ��quant��ʽ���׵�Ͷ���ߣ� 
2. ��һ����python��̾���, ��������ʵ�ֲ��Ե� 
3. ϣ�������ڱ���ִ�еģ� �������ŵ���ϴ��κ��û�����

����
----
1. ���飬 ϵͳ�Զ��������鱣�浽redis��, �����ȶ��� ֧�ֶ�������
2. ���׽ӿڣ� ��ʱֻ֧�����Ž�Ͷ֤ȯ, ����ͨ���ţ� ����ͨ����ͬʱ������ ��������
3. ��pythonʵ�ֵĲ��ԣ� ͨ����д���ԴӶ�ʵ���Զ�������, 0.2�汾�Ժ�python�����齻�ײ��ַ��룬 �ɿͻ��˻�ȡ���ݲ����뵽redis�У�
   ���Դ�redis�ж�ȡ���飬 ����ʱ��ͻ��˷���֪ͨ����ɽ���.

�ز�
----
ʹ�ø�ϵͳǰ�����Ƚ��в��ԵĻز⿪��, �Ͼ���һ���õĲ��Բ��ܽ����Զ�������
��Ǩ��python_strategyĿ¼�� ���ڸ�Ŀ¼����һ���ز⣬ ִ��boll_pramid.py���õ�һ��Ĭ�ϻز�
������̲�ѯ [�ز��ĵ�](https://github.com/nessessary/autoxd/blob/master/python_strategy/README.md)

ʹ��
----
1. ���ذ�װ�ļ� [����](https://pan.baidu.com/s/1pMoB83h)
	1) ����redis, ��װ�ú��ٰ�װ�ͻ���
	2) ��������pythonִ�л���, �Ƽ�anaconda
2. ��װ�����У� ��Ҫ����Ӳ��Ҫ������<br>
	WIN7 8G�ڴ� Ӳ��5G���Ͽռ�
3. һ�����͵�ִ�й�������
	1) ��д�ʽ��˺ţ� �ɹ����´β���������, �ʺ��Լ�����ʽ�洢�ڱ��أ� ��������й¶
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_main.png)
	2) �˺������ ϵͳ����ʼ���У� �������飬����¼�����˺�, �ɹ���������ͼ
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_enter.png)
	3) ����������ɺ󼴻�ִ�в��ԣ� Ĭ�ϲ�����һ���򵥵�demo�� �����Ƕ�ȡ�����˻��й�Ʊ�б�ĵ�һ�У� ����������Ʊ�Ļ�
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_stocklist.png)

	4) ί���µ�
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_weituo.png)
4. �������ʹ�ý��׽ӿڣ� ֻʹ�����鲿�ֵĻ��� ֻ��Ҫ����һ�����ʺţ������û���Ϊ1�� ����Ϊ1�� ��ô�´ξͲ�����ʾ���뽻���ʺ��ˡ�


����
----
�������ʱ��֧�������� ���ֶ����ذ�װ�ļ����°�װ


����
----
1. Python����
	1) ���а�װAnaconda
	2) ���а�װRedis��Ҳ�ɴ�����������ɫ�氲װ
	3) ��Ҫʹ��pandas��, �ز��������д����
	4) ����Ŀ¼��python_strategy\strategy
	   Ĭ��ʹ�õĲ����ļ�Ϊboll_pramid.py
2. ����ִ��run.bat<br>
	���Ծ�����ز��ĵ�, �����ɿͻ��˻�ȡ����������redis��
	�Զ��������ʺϸ�ƵһЩ�Ĳ��ԣ� ���Ĭ�ϲ��Ծ���һ������boll�����佻�ײ��ԣ� ���һ�����Ż���ֱ�������ȶ���ִ��
	1) ϵͳ��������صĹ�Ʊ�� ͬʱ����Run
	2) �������Դ���Ĺ�Ʊ�� ��дAllowCode���list

```python
class Strategy_Boll_Pre(qjjy.Strategy):
    """Ϊ��ʵ��Ԥ��"""
    def AllowCode(self, code):
	codes = ['300033']		 #�Լ��뽻�׵Ĺ�Ʊ
	return code in codes
    
    #��ں���
    def Run(self):
	"""ÿ����Ʊ����һ�θú���, ���ú���ͷţ� ��˲���ʹ�ü򵥵�ȫ�ֱ����� ����Ҫʹ��redis��������
	���⣬ ���׽ӿ�Ҫ���ã� �����б��ѯ�� �ɱ�����redis�� 
	��Ҫÿ���뺯������ѯһ�£� �µ�������������� ��Ϊ�������������� ����ֱ�ӵ�����
	"""
        #self._log('Strategy_Boll_Pre')
	account = self._getAccount()	#��ȡ�����˻�
	def run_stocklist():
	    df = account.StockList()	#��ѯ��Ʊ�б�
	    self._log(df.iloc[0])
	PostTask(run_stocklist,	100)	#ÿ100��ִ��һ��
	
	#����Ϊ���ײ���
        code = self.data.get_code()	#��ǰ���Դ���Ĺ�Ʊ
	if not self.is_backtesting and not self.AllowCode(code):
	    return

        self._log(code)
	df_hisdat = pd_help.Df(self.data.get_hisdat(code))	#��k��
	df_fenshi = pd_help.Df(self.data.get_fenshi(code))	#�շ�ʱ
	if len(df_fenshi.df) == 0:
	    self.data.log(code+u"ͣ��")
	    return
	price = df_fenshi.getLastPrice()    #��ǰ�ɼ�
        closes = df_hisdat.getCloses()
	yestoday_close = closes[-2]	    #�������̼�
	self._log(price)
	self._log(yestoday_close)
	
	def buy_at_price_once():
	    """��ĳһ����λ��һ����"""
	    cur_price = price * (1-0.02)
	    if cur_price < yestoday_close*0.901:
		cur_price = yestoday_close*0.901
		cur_price = agl.FloatToStr(cur_price)
	    account.Order(0, code, cur_price, 100)	#����
	#�����µ���ſ����е�ע��
	#PostTask(buy_at_price_once, 60*60*3)	
	return	
```
	3)���Լ��أ� ��live_policy_runner.py
```python
	p.Regist(boll_pramid.Strategy_Boll_Pre(live_policy.Live()))
```

3. ����
	1) ��ֻ��ȡ��k��, 5�����ߺͷ�ʱ��
	2) �����ȡ�Ĺ�Ʊ�����config.ini, һ���ֻ��Թ�ע�Ĺ�Ʊ��ȡ���鲢ִ�в��Ի��ܶ�, �޸ĺ��´�������ִ��<br>
	   �޸�listinfo_codes�еĹ�ƱΪ�����ѡ��
```python
#ȡ�б�ʽ 0/1		ȡȫ����ȡ����
listinfo_type=1
listinfo_codes="002074|002108|300399|300384|300033|300059|002174"
```

4. ��ε��ý��׽ӿ�
	1) ��ȷ�����˺Ž���ϵͳ�� �����˺ż����¼�� �ұ������ߣ���autoxd�µ�����ͨ����ˢ�¿��Կ���
	2) ��������ӿ��Կ���ʹ���˹�Ʊ�б��ѯaccount.StockList(), ������account.Order(0, code, cur_price, 100)
	   ȫ���Ľ��׽ӿڼ�tc.py
	3) ʹ�������з�ʽ���ýӿ�
	   ��ide��, �Ƽ�wingide, ����shell��������
```python
import tc, stock_pinyin as jx
tc.Buy('300033', 60.1, 100)
#��ƴ����д����
tc.Buy(jx.THS, 60.1, 100)
#������д��ͻ�����, ide����Զ������ʾ�����[a,a#����ɷ�,b, b#����ɷ�], ѡ����Ӧ��a,b,�����ͻ�Ĵ���
tc.Buy(jx.JRGF.a, 15, 100)
```


����
----
�������qqȺ 213155151 <br>
