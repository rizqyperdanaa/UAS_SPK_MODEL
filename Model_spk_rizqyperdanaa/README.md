
# spk_model

Nama : Muhammad Rizqy Perdana
NIM  : 201011400890
Kelas: 07TPLP13

## Virtualenv
install, create, activate virtual environment using virtualenv

https://medium.com/analytics-vidhya/virtual-environment-6ad5d9b6af59

## Install depedencies
run `pip install -r requirements.txt`

## create postgresql database

create database in your locals

modify settings.py 

## create table

run:
    python main.py create_table

## create data

run this query in your db client

    INSERT INTO smartphones (nama_hp,reputasi_brand,processor_antutu,baterai,harga,ukuran_layar) VALUES
	 ('Realme 10 Pro 5G','Lumayan Terkenal',424500,'5000 mAh','4,3 jutaan',6.72),
	 ('Samsung Galaxy A34','Terkenal',538000,'5000 mAh','5 jutaan',6.60),
	 ('Samsung Galaxy A33','Terkenal',415448,'5000 mAh','4,5 jutaan',6.40),
	 ('Oppo Reno 8 5G','Cukup Terkenal',402916,'4800 mAh','4,4 jutaan',6.70),
	 ('Vivo T1 Pro 5G','Cukup Terkenal',568448,'4700 mAh','4,5 jutaan',6.44),
	 ('Poco F5','Lumayan Terkenal',1134558,'5000 mAh','5 jutaan',6.67),
	 ('iQOO Z7','Kurang Terkenal',670439,'5000 mAh','4,3 jutaan',6.60),
	 ('Redmi Note 12 Pro 5G','Sangat Terkenal',538000,'5000 mAh','4,3 jutaan',6.67),
	 ('Oppo A78 5G','Cukup Terkenal',324000,'5000 mAh','4 jutaan',6.56),
	 ('Realme GT Neo 3T','Lumayan Terkenal',789376,'5000 mAh','5,5 jutaan',6.62);
  
## Hasil
<img src='screenshot/SAW dan WP.png' alt='Screenshot Hasil'/>
<img src='screenshot/database.png' alt='Screenshot Hasil'/>
