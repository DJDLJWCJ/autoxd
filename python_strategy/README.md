�ز�
------

�؜yʹ�õ��˻�Ϊһ������ģ���˻�(��account.py)�� �ӿں�ʵ�̽ӿ�һ�£� ����б�Ҫ�ڻ؜yϵͳ����һ�²���

1. ����Դ<br>
   �뵽 [����](http://pan.baidu.com/s/1bpto0wv) ����һ������Դ�� ����300033�����ߣ�5�����ߣ�����ʱ��, ���غ���õ�<br>
   python_strategy\datasĿ¼��<br>
   (���ڵ�����Դ��������һ��demo�����ã� Ҫʹ��ȫ������Դ������ϵ���߻����޸Ŀ��ʹ�õ���������Դ)<br>
   stock_createThs.searialΪͬ��˳F10ȫ������, ����������2017-9-6<br>
   �Զ����أ� ʹ�ü�stock.py���StockInfoThs<br>
   ǰ��Ȩʹ��ͬ��˳�ķֺ�� �����stock.py���calc_fuquan_use_fenhong<br>

2. ���������⣬ ���ʹ���Լ���anaconda�� ��Ҫ32bit python2.7�汾�ģ� �����Ҫ�Ŀ�Ϊta-lib, redis, charade��<br>
   �������ذ�װ���� �����һ��anaconda�� �Ѿ�����������Ҫ�Ŀ⣬ ʹ�ø�Ŀ¼����

3. ִ��
   ��ide��ȱʡ����boll_pramid.py��ִ��<br>
   �ɿ�������Ľ��ͼ<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_result.png)
   Ҳ֧���м�����ʾTickReport<br>
   ![image](https://github.com/nessessary/autoxd/raw/master/pics/autoxd_backtest_tick_1.png)

<br>

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

