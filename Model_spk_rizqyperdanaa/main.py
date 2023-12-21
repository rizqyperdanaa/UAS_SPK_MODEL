import sys
from colorama import Fore, Style
from models import Base, Smartphones
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import MEREK_SCALE,DEV_SCALE_reputasi,DEV_SCALE_prosesor,DEV_SCALE_baterai,DEV_SCALE_harga,DEV_SCALE_ukuran_layar

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-5
        self.raw_weight = {
            'nama_hp': 3, 
            'reputasi_brand': 3, 
            'processor_antutu': 5, 
            'baterai': 4, 
            'ukuran_layar': 4, 
            'harga': 1
            }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k,v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Smartphones)
        return [{'id': smartphones.id, 
        'nama_hp': MEREK_SCALE[smartphones.nama_hp], 
        'reputasi_brand': DEV_SCALE_reputasi[smartphones.reputasi_brand], 
        'processor_antutu': DEV_SCALE_prosesor[smartphones.processor_antutu], 
        'baterai': DEV_SCALE_baterai[smartphones.baterai], 
        'ukuran_layar': DEV_SCALE_ukuran_layar[smartphones.ukuran_layar], 
        'harga': DEV_SCALE_harga[smartphones.harga]} for smartphones in session.scalars(query)]
    
    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        nama_hp = [] # max
        reputasi_brand = [] # max
        processor_antutu = [] # max
        baterai = [] # max
        ukuran_layar = [] # max
        harga = [] # min
        for data in self.data:
            nama_hp.append(data['nama_hp'])
            reputasi_brand.append(data['reputasi_brand'])
            processor_antutu.append(data['processor_antutu'])
            baterai.append(data['baterai'])
            ukuran_layar.append(data['ukuran_layar'])
            harga.append(data['harga'])

        max_nama_hp = max(nama_hp)
        max_reputasi_brand = max(reputasi_brand)
        max_processor_antutu = max(processor_antutu)
        max_baterai = max(baterai)
        max_ukuran_layar = max(ukuran_layar)
        min_harga = min(harga)

        return [
            {   'id': data['id'],
                'nama_hp': data['nama_hp']/max_nama_hp, # benefit
                'reputasi_brand': data['reputasi_brand']/max_reputasi_brand, # benefit
                'processor_antutu': data['processor_antutu']/max_processor_antutu, # benefit
                'baterai': data['baterai']/max_baterai, # benefit
                'ukuran_layar': data['ukuran_layar']/max_ukuran_layar, # benefit
                'harga': min_harga/data['harga'] # cost
                }
            for data in self.data
        ]

class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result =  {row['id']:
            round(
        row['nama_hp'] ** weight['nama_hp'] *
        row['reputasi_brand'] ** weight['reputasi_brand'] *
        row['processor_antutu'] ** weight['processor_antutu'] *
        row['baterai'] ** weight['baterai'] *
        row['ukuran_layar'] ** (-weight['ukuran_layar']) *
        row['harga'] ** weight['harga']
        , 2
    )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result =  {row['id']:
            round(row['nama_hp'] * weight['nama_hp'] +
            row['reputasi_brand'] * weight['reputasi_brand'] +
            row['processor_antutu'] * weight['processor_antutu'] +
            row['baterai'] * weight['baterai'] +
            row['ukuran_layar'] * weight['ukuran_layar'] +
            row['harga'] * weight['harga'], 2)
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)
    

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)
    pass

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
