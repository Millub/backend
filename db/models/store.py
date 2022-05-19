import datetime

from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from db.config import Base

class Store(Base):
    __tablename__ = 'store'
    __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'}

    store_idx = Column(Integer, primary_key=True, index=True)
    # 1:일반음식점, 2:휴게음식점, 3:제과점, 4:소매업
    # 5:서비스업, 6:숙박업소, 7:농어촌민박, 8:미용업
    store_type = Column(Integer, nullable=False)
    # 상호명
    store_name = Column(String(50), nullable=False)
    # 주소
    store_address = Column(String(100), nullable=False)
    # 전화번호
    store_number = Column(String(40), nullable=True)
    store_datetime = Column(DateTime, default=datetime.datetime.utcnow)

    detail_idx = relationship("StoreDetail", backref="store")
    view_idx = relationship("StoreView", backref="store")


class StoreDetail(Base):
    __tablename__ = 'store_detail'
    __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'}

    detail_idx = Column(Integer, primary_key=True)
    store_idx = Column(Integer, ForeignKey('store.store_idx'))
    detail_name = Column(String(40), nullable=False)
    detail_price = Column(Integer, nullable=False)
    detail_datetime = Column(DateTime, default=datetime.datetime.utcnow)


class StoreView(Base):
    __tablename__ = 'store_view'
    __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'}

    view_idx = Column(Integer, primary_key=True)
    store_idx = Column(Integer, ForeignKey('store.store_idx'))
    view_ip = Column(String(40), nullable=False)
    view_datetime = Column(DateTime, default=datetime.datetime.utcnow)