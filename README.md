Autoxd
======

A-share automated trading tool

һ��A�ɵ��Զ������׹���

����
----
�������еĹ�����������̫˳�֣� �������������Զ����׷����ֱȽ����� ��˱�д�˸��������������к��ʲ��Ե�����£� �����Զ����н��ף� ������python��д��
�ʺ�ʹ�ø������Ŀ����Ⱥ<br>
1. ϣ��ʹ��quant��ʽ���׵�Ͷ���ߣ� 
2. ��һ����python��̾���, ��������ʵ�ֲ��Ե� 
3. ϣ�������ڱ���ִ�еģ� �������ŵ���ϴ��κ��û�����

����
----
1. ���飬 ϵͳ�Զ��������鱣�浽���ݳ���
2. ���׽ӿڣ� ��ʱֻ֧�����Ž�Ͷ֤ȯ
3. ��pythonʵ�ֵĲ��ԣ� ͨ����д���ԴӶ�ʵ���Զ�������

ʹ��
----
1. ���ذ�װ�ļ� [����](http://pan.baidu.com/s/1i5BrNKh)
2. ��װ�����У� ��Ҫ����Ӳ��Ҫ������<br>
	WIN7 8G�ڴ� Ӳ��10G���Ͽռ�
3. һ�����͵�ִ�й�������
	1) ��д�ʽ��˺ţ� �ɹ����´β���������
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_main.png)
	2) �˺������ ϵͳ����ʼ���У� �������飬����¼�����˺�, �ɹ���������ͼ
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_enter.png)
	3) ����������ɺ󼴻�ִ�в��ԣ� Ĭ�ϲ�����һ���򵥵�demo�� �����Ƕ�ȡ�����˻��й�Ʊ�б�ĵ�һ�У� ����������Ʊ�Ļ�
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_stocklist.png)

	4) ί���µ�
	![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_weituo.png)

����
----
1. Python����
	1) ��װ�ļ�����һ��Anaconda2
	2) ����Redisһ�ݣ� ������ذ�װ�˽�����Ч
	3) ��Ҫʹ��pandas��
	4) ����Ŀ¼��python_strategy\strategy
	   Ĭ��ʹ�õĲ����ļ�Ϊboll_pramid.py
2. �������, ��boll_pramid.py<br>
	ע�⣺ϵͳ��װ���������Ḳ��Ĭ�ϲ��ԣ� ������ʹ���µ��ļ��� ����Ƿǰ�װĿ¼�� ɾ��ʱ����Ŀ¼Ҳ��ɾ��
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

3. ����
	1) ��ֻ��ȡ��k��, 5�����ߺͷ�ʱ��
	2) �����ȡ�Ĺ�Ʊ�����config.ini, һ���ֻ��Թ�ע�Ĺ�Ʊ��ȡ���鲢ִ�в��Ի��ܶ�, �޸ĺ��´�������ִ��<br>
	   �޸�listinfo_codes�еĹ�ƱΪ�����ѡ��
```python
#ȡ�б�ʽ 0/1		ȡȫ����ȡ����
listinfo_type=1
listinfo_codes="002074|002108|300399|300384|300033|300059"
```

4. ��ε��ý��׽ӿ�
	1) ��ȷ�����˺Ž���ϵͳ�� �����˺ż����¼�� �ұ������ߣ� ע�⣬ ��ϵͳʹ�õ���ͨ��Э���¼��ʽ����Ӱ�����������
	   Ҳ����һ�������Ͽ��Զ�����ͬʱ��½
	2) ��������ӿ��Կ���ʹ���˹�Ʊ�б��ѯaccount.StockList(), ������account.Order(0, code, cur_price, 100)
	   ȫ���Ľ��׽ӿڼ�tc.py
	3) ʹ�������з�ʽ���ýӿ�
	   ��ipython��
```python
import tc
tc.Buy('300033', 60.1, 100)
#tc.Buy(tc.ths, 60.1, 100)
```

5. �؜y<br>
	�؜yʹ�õ��˻�Ϊһ������ģ���˻�(��account.py)�� �ӿں�ʵ�̽ӿ�һ�£� ����б�Ҫ�ڻ؜yϵͳ����һ�²���

	1) ʵ��һ��������溯��

	2) Tick���㱨����<br>
	   ��δʵ��

	3) ����Դ<br>
	   ���е�����Դ������mysql���ݿ⣬ δ���ᴴ��һ��pickle�ļ��ύ�����̣� ʹ�ø�pickle����Ϊ�؜y����Դ<br>
	   �����û������޸Ŀ��ʹ�õ���������Դ
	
	4) ִ��
	   ��pythonֱ��ִ�в���py<br>
	   �ɿ�������Ľ��ͼ<br>
	   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)

```python
    def Report(self, start_day, end_day):
	"""�؜y����"""
	self._getAccount().Report(end_day)
	#return
	#����ͼ��
	#end_day = help.MyDate.s_Dec(end_day, 1)
	bars = stock.CreateFenshiPd(self.code, start_day, end_day)
	if len(bars) == 0:
	    return
	bars = bars.resample('1min').mean()
	bars['positions'] = 0
	bars['c'] = bars['p']
	bars = bars.dropna()
	df = self._getAccount().ChengJiao()
	df_zhijing = self._getAccount().ZhiJing()
	df_zhijing = df_zhijing[bars.index[0]:]
	df_changwei = self._getAccount().ChengJiao()
	cols = ['������־','ί������']
	df_flag = df_changwei[cols[0]].map(lambda x: agl.where(int(x), -1, 1))
	df_changwei[cols[1]] *= df_flag
	changwei = stock.GuiYiHua(df_changwei[cols[1]].cumsum())
	for i in range(len(df)):
	    index = df.index[i]
	    bSell = bool(df.iloc[i]['������־']=='1')
	    if index in bars.index:
		#bars.ix[index]['positions'] = agl.where(bSell, -1, 1)
		bars.set_value(index, 'positions', agl.where(bSell, -1, 1))
	trade_positions = np.array(bars['positions'])
	ui.TradeResult_Boll(self.code, bars, trade_positions, \
	    stock.GuiYiHua(df_zhijing['�ʲ�']), changwei)
```



����
----
������ִ��ڲ����ڣ� ���ܱȽϼ򵥣� bugҲ�������⣬ϣ��ʹ���˵�ͬѧ���ṩ��������� �������м���������ȥ�Ķ���<br>
���������� ��Ѱ�װĿ¼�µ�dmp�ļ��ύ��Ⱥ��, ������ϵ���ߣ����߻���bug<br>


�������qqȺ 213155151 <br>
