------------------------------------------------
-- 2017/8/26 for sqlite
-- ������ʷ����


-- ��¼��Ʊ��ʱ����
drop table if exists fenshi;
create table fenshi (
id  INT PRIMARY KEY     NOT NULL,
stock_code char(7) not null,			--��Ʊ����, ��blob�ֶκ���������
fenshi_day date not null,							--��ʱ����
fenshi_data blob not null							--��ʱ����
);
create index idt_stock_code on fenshi(stock_code);

--��k������
drop table if exists kline;
create table kline (
id  INT PRIMARY KEY     NOT NULL,
stock_code char(7) not null,				--��Ʊ����
kline_time date not null,					--k������
kline_open float,							--���̼�
kline_high float,							--��߼�
kline_low float,							--��ͼ�
kline_close float,							--���̼�
kline_volume float,							--�ɽ���
kline_amount float							--�ɽ����
);
create index idt1_stock_code on kline(stock_code);
create index idt2_kline_time on kline(kline_time);

--5����k������
drop table if exists kline5min;
create table kline5min (
id  INT PRIMARY KEY     NOT NULL,
stock_code char(7) not null,				--��Ʊ����
kline_time date not null,					--k������
kline_open float,							--���̼�
kline_high float,							--��߼�
kline_low float,							--��ͼ�
kline_close float,							--���̼�
kline_volume float							--�ɽ���
);
create index idt3_stock_code on kline5min(stock_code);
create index idt4_kline_time on kline5min(kline_time);