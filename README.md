autoxd v0.3 �ز���
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
2. ֧��py2��py3 windows; linux��macosδ֪
3. �Ƽ�ʹ��wingide�� ��ֱ�Ӽ���wpr��Ŀ�ļ�
4. ��pip install -r requirement.txt��װ���������

- ʹ��

1. ����Դ,ʹ���������ַ�ʽ����; ע��,��ʹ��ths�ֺ�������ǰ��Ȩ<br>
   1) ʹ��[�ͻ���](https://pan.baidu.com/s/1pMoB83h) ��������, ����config.ini��д��Ҫ���صĴ���, 
      ���غ���õ�redis��, ��datasource_mode=stock.DataSources.datafrom.livedata
   2) ʹ���Զ���ĵ���������Դ�� ��ʵ����һ������tushare������, 
      datasource_mode=stock.DataSources.datafrom.custom

2. ����
```python
    #���ò��Բ���
    def setParams(s):
	s.setParams(trade_num = 300, 
                    pl=publish.Publish()	#������ҳ��
                    )
    backtest_policy.test_strategy(codes, BollFenCangKline, setParams, mode=myenum.hisdat_mode, 
                                  start_day='2017-4-10', end_day='2018-9-15',
                                  datasource_mode=DataSources.datafrom.custom,
                                  datasource_fn=fnSample
                                  )    
```
	
