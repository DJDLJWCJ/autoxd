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

- ��������

```
	python boll_fencang.py
```

   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result_kline.png)

- 5��������

```
	python five_chengben.py
```

   <img src="https://github.com/nessessary/autoxd/raw/master/pics/five.png"></img>


- ����
1. redis
	window����ȥ[����](https://pan.baidu.com/s/1pMoB83h) ����һ��, ���������bat���ɰ�װ
2. ֧��py2��py3 windows; macos֧��py3�� linuxδ֪
3. �Ƽ�ʹ��wingide�� ��ֱ�Ӽ���wpr��Ŀ�ļ�
4. ��pip install -r requirements.txt��װ���������

- ��װ
  * ��װAnaconda
  * ����autoxd, git clone https://github.com/nessessary/autoxd.git
  * ִ��pip install -r requirements.txt
  * ������������pip��װ�İ��� ��ִ��������װ������ֻ��һ��pyH��Ҫ�ֶ���װ��
  * ��װredis
  * ��python_strategy/strategy/five_changben.py, ���Զ����ڸ�Ŀ¼

- ʹ��

1. ����Դ,ʹ���Զ��������; ע��,��ʹ��ths�ֺ�������ǰ��Ȩ<br>
      * ʹ���Զ���ĵ���������Դ�� ��ʵ����һ������tushare������,
      datasource_mode=stock.DataSources.datafrom.custom
      * 5������ʹ�õ���pytdx������

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
