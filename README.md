autoxd v0.4 �ز���
------

�򵥿�ݵ�A�ɻز⻷���� �ʺϱ�дT+0����

- ����
  * ʹ��pandas��д����
  * ���������ҳ����ʾ�� ����matlab��publish
  * ����ִ�в���
  * �����˻��� ģ��ʵ�̽���ϸ�ڣ� ֧��T+0�� ���׳ɱ�����
  * �Դ�FOURָ�꣬ �򵥼�����

- ���
  * v0.4.1 ֧��macos
  * v0.4 ����Ż��ٶ�
  * v0.3 python3֧��

- ����

```
	python boll_fencang.py
```

   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result_kline.png)

- ����
1. redis
	window����ȥ[����](https://pan.baidu.com/s/1pMoB83h) ����һ��, ���������bat���ɰ�װ
2. ֧��py2��py3 windows; macos֧��py3�� linuxδ֪
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
                      pl=publish.Publish()	#������ҳ��, ע���򲻷���
                      )
  backtest_policy.test_strategy(codes, BollFenCangKline, setParams, mode=myenum.hisdat_mode,
                                start_day='2017-4-10', end_day='2018-9-15',
                                datasource_mode=DataSources.datafrom.custom,
                                datasource_fn=fnSample
                                )
```
