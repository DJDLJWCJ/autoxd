�ز���
------

�؜yʹ�õ��˻�Ϊһ������ģ���˻�(��account.py)�� �ӿں�ʵ�̽ӿ�һ�£� <br>
����ز�����Ҫ��ע����Ľ���ϸ�ڣ� �ʺ�T+0����

1. ����Դ<br>
   �뵽 [����](http://pan.baidu.com/s/1bpto0wv) ����һ������Դ<br>
   ���ظ�Ŀ¼���õ�python_strategy\datasĿ¼��<br>
   Ҫʹ��ȫ������Դ�޸Ŀ��ʹ�õ���������Դ, �����stock.DataSources<br>
   huge_dictĿ¼Ϊͬ��˳F10ȫ������<br>
   �Զ����أ� ʹ�ü�stock.py���StockInfoThs<br>
   ǰ��Ȩʹ��ͬ��˳�ķֺ�� �����stock.py���calc_fuquan_use_fenhong<br>

2. ���������⣬ ������Ҫʹ��anaconda 32bit python2.7�汾�� ��Ҫ�Ŀ�Ϊta-lib, redis, charade��<br>
   ,����ֻ��windows�²���ͨ����linux����������<br>
   ����ʹ��WingIDE��������Ŀ��ִ�У� ʹ��������ִ�п��ܻ��������������

3. ִ��
   �ز���3��ģʽ�����ߺ�5�����ߺͷ�ʱ, ����ģʽִ�бȽϿ죬 ÿ������ʱ�ɽ�,<br>
   ��ʱִ��ʱ��Ƚϳ����ɽ�Ϊʵ�ʵ�ʱ��<br>
   ����ʹ��5������<br>
   1> ��ʱ������<br>
   ��ide��ȱʡ����boll_pramid.py��ִ��<br>

   �м�����ʾTickReport<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_tick_1.png)<br>
   �ɿ�������Ľ��ͼ<br>
   �ʽ�0��ʾû��ӯ���� ��ֵ��ʾ���� ��ֵ��ʾӯ��, �ʽ�Ͳ�λΪ��һ�����<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)<br>
   ������ڿ��Կ���������ϸ<br>

   2>���ߵ�����<br>
   ֧�ֲ���<br>
   boll_fenchang.py<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result_kline.png)<br><br>

4. ����
   ��boll_fencang.py
   ����������ݵ�webҳ��, 
   [����](http://autoxd.applinzi.com/html/boll_fencang_setParams6100.html)
```python
    #���ò��Բ���
    def setParams(s):
	s.setParams(trade_num = 300, 
                    #pl=publish.Publish()	#������ʽ
                    )
    if codes == '':
	codes = [u'300033']
    #ִ�в���, 5������
    backtest_policy.test_strategy(codes, BollFenCangKline, setParams,
				  mode=BackTestPolicy.enum.hisdat_mode|BackTestPolicy.enum.hisdat_five_mode, 
                                  #start_day='2016-10-20', end_day='2017-10-1',
				  datasource_mode=stock.DataSources.datafrom.online	#���������ز�������
                                  )    

```
	
5. ʹ��autoxd�ͻ�����������
   Windows�ͻ�������������redis, ʹ��autoxdʵ�̽���
   [��ת������ҳ��](http://autoxd.applinzi.com)