�ز�
------
	
	�؜yʹ�õ��˻�Ϊһ������ģ���˻�(��account.py)�� �ӿں�ʵ�̽ӿ�һ�£� ����б�Ҫ�ڻ؜yϵͳ����һ�²���

	1) ʵ��һ��������溯��

	2) Tick���㱨����<br>
	   ��δʵ��

	3) ����Դ<br>
	   �뵽 [����](http://pan.baidu.com/s/1kVsr8aV) ����һ������Դ�� ����300033�����ߣ�5�����ߣ�����ʱ��, ���غ���õ�python_strategy\datasĿ¼��
	
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

