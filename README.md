�ز���
------

�؜yʹ�õ��˻�Ϊһ������ģ���˻�(��account.py)�� �ӿں�ʵ�̽ӿ�һ�£� <br>
����ز�����Ҫ��ע����Ľ���ϸ�ڣ� �ʺ�T+0����

- ����
	python boll_fencang.py<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result_kline.png)<br><br>

- ����
1. redis
	window����ȥ[����](https://pan.baidu.com/s/1pMoB83h) ����һ��, ���������bat���ɰ�װ
2. ֧��py2��py3 windows�� linux��macosδ֪
3. �Ƽ�ʹ��wingide�� ��ֱ�Ӽ���wpr��Ŀ�ļ�
4. ��pip install -r requirement.txt��װ���������

- ʹ��

1. ����Դ<br>
   1) ʹ��[�ͻ���](https://pan.baidu.com/s/1pMoB83h) ��������, ����config.ini��д��Ҫ���صĴ���, 
      ���غ���õ�redis��, ��datasource_mode=stock.DataSources.datafrom.livedata
   2) ʹ���Զ���ĵ���������Դ�� ��ʵ����һ������tushare������, 
      datasource_mode=stock.DataSources.datafrom.custom

2. ����
```python
    #���ò��Բ���
    def setParams(s):
	s.setParams(trade_num = 300, 
                    #pl=publish.Publish()	#������ʽ
                    )
    #ִ�в���, 5������
    backtest_policy.test_strategy(codes, BollFenCangKline, setParams,
				  mode=BackTestPolicy.enum.hisdat_mode|BackTestPolicy.enum.hisdat_five_mode, 
                                  #start_day='2016-10-20', end_day='2017-10-1',
				  datasource_mode=stock.DataSources.datafrom.online	#���������ز�������
                                  )    

```
	
