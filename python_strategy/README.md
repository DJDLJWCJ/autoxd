�ز�
------

�؜yʹ�õ��˻�Ϊһ������ģ���˻�(��account.py)�� �ӿں�ʵ�̽ӿ�һ�£� ����б�Ҫ�ڻ؜yϵͳ����һ�²���
����ز�����Ҫ��ע����Ľ���ϸ�ڣ� �ʺ�T+0����

1. ����Դ<br>
   �뵽 [����](http://pan.baidu.com/s/1bpto0wv) ����һ������Դ�� ����300033�����ߣ�5�����ߣ�����ʱ��, ���غ���õ�<br>
   python_strategy\datasĿ¼��<br>
   Ҫʹ��ȫ������Դ������ϵ���߻����޸Ŀ��ʹ�õ���������Դ, �����stock.DataSources<br>
   stock_createThs.searialΪͬ��˳F10ȫ������, �ɲ���, ����������2017-9-6<br>
   �Զ����أ� ʹ�ü�stock.py���StockInfoThs<br>
   ǰ��Ȩʹ��ͬ��˳�ķֺ�� �����stock.py���calc_fuquan_use_fenhong<br>

2. ���������⣬ ���ʹ���Լ���anaconda�� ��Ҫ32bit python2.7�汾�ģ� �����Ҫ�Ŀ�Ϊta-lib, redis, charade��<br>
   �������ذ�װ���� �����һ��anaconda�� �Ѿ�����������Ҫ�Ŀ⣬ ʹ�ø�Ŀ¼����

3. ִ��
   �ز�������ģʽ�� hisdat_mode|tick_mode�ֱ������ߺͷ�ʱ, ����ģʽִ�бȽϿ죬 ÿ������ʱ�ɽ�,<br>
   ��ʱִ��ʱ��Ƚϳ����ɽ�Ϊʵ�ʵ�ʱ��<br>
   1> ��ʱ������<br>
   ��ide��ȱʡ����boll_pramid.py��ִ��<br>
   ������������<br>
   python boll_pramid.py<br>

   �м�����ʾTickReport<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_tick_1.png)<br>
   �ɿ�������Ľ��ͼ<br>
   �ʽ�0��ʾû��ӯ���� ��ֵ��ʾ���� ��ֵ��ʾӯ��, �ʽ�Ͳ�λΪ��һ�����<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)<br>
   ������ڿ��Կ���������ϸ<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result_kline.png)<br>
   <br>
   2>���ߵ�����<br>
   ֧�ֲ���<br>
   boll_fenchang.py<br>

4. ����
   ��boll_fencang.py
   ����������ݵ�webҳ��
```python
    #���ò��Բ���
    def setParams(s):
	s.setParams(trade_num = 300, 
                    #pl=publish.Publish()	#������ʽ
                    )
    if codes == '':
	codes = [u'300033']
    #ִ�в���
    backtest_policy.test_strategy(codes, BollFenCangKline, setParams, day_num=20, mode=myenum.hisdat_mode, 
                                  start_day='2016-10-20', end_day='2017-10-1'
                                  )    

```
	
