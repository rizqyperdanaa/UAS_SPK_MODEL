from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Smartphones(Base):
    __tablename__ = 'smartphones'
    id = Column(Integer, primary_key=True)
    nama_hp = Column(String(50))
    reputasi_brand = Column(String(50)) 
    processor_antutu = Column(String(50))
    baterai = Column(String(10))
    ukuran_layar = Column(String(20))
    harga = Column(String(20))

    def __repr__(self):
        return f"smartphones(id={self.id!r}, brand={self.brand!r}"
