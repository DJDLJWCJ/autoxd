�ز���
------

�؜yʹ�õ��˻�Ϊһ������ģ���˻�(��account.py)�� �ӿں�ʵ�̽ӿ�һ�£� <br>
����ز�����Ҫ��ע����Ľ���ϸ�ڣ� �ʺ�T+0����

1. ����Դ<br>
   �뵽 [����](http://pan.baidu.com/s/1bpto0wv) ����һ������Դ�� ����300033�����ߣ�5�����ߣ�����ʱ��, <br>
   ���ظ�Ŀ¼���õ�python_strategy\datasĿ¼��<br>
   Ҫʹ��ȫ������Դ������ϵ���߻����޸Ŀ��ʹ�õ���������Դ, �����stock.DataSources<br>
   stock_createThs.searialΪͬ��˳F10ȫ������<br>
   �Զ����أ� ʹ�ü�stock.py���StockInfoThs<br>
   ǰ��Ȩʹ��ͬ��˳�ķֺ�� �����stock.py���calc_fuquan_use_fenhong<br>

2. ���������⣬ ������Ҫʹ��anaconda 32bit python2.7�汾�� ��Ҫ�Ŀ�Ϊta-lib, redis, charade��<br>
   64λ python3.xҲ��ʹ�ã�������Ҫ�޸Ĳ��ִ���; ����ֻ��windows�²���ͨ����linux����������<br>
   ����ʹ��WingIDE��������Ŀ��ִ�У� ʹ��������ִ�п��ܻ��������������

3. ִ��
   �ز�������ģʽ�� hisdat_mode|tick_mode�ֱ������ߺͷ�ʱ, ����ģʽִ�бȽϿ죬 ÿ������ʱ�ɽ�,<br>
   ��ʱִ��ʱ��Ƚϳ����ɽ�Ϊʵ�ʵ�ʱ��<br>
   1> ��ʱ������<br>
   ��ide��ȱʡ����boll_pramid.py��ִ��<br>

   �м�����ʾTickReport<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_tick_1.png)<br>
   �ɿ�������Ľ��ͼ<br>
   �ʽ�0��ʾû��ӯ���� ��ֵ��ʾ���� ��ֵ��ʾӯ��, �ʽ�Ͳ�λΪ��һ�����<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)<br>
   ������ڿ��Կ���������ϸ<br>

   <br>
   2>���ߵ�����<br>
   ֧�ֲ���<br>
   boll_fenchang.py<br>
   ͼ��ʾ��<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result_kline.png)<br>

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
    #ִ�в���
    backtest_policy.test_strategy(codes, BollFenCangKline, setParams, day_num=20, mode=myenum.hisdat_mode, 
                                  start_day='2016-10-20', end_day='2017-10-1'
                                  )    

```
	
