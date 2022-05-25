from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, constr

class StoreData(BaseModel):
    store_idx: int
    store_type: int
    store_name: str
    store_address: str
    store_number: str

class StoreList(BaseModel):
	store_list: List[StoreData]

class StoreModel(BaseModel):
    result: str
    data: StoreList


class StoreDetailData(BaseModel):
    store_idx: int
    store_type: int
    store_name: str
    store_address: str
    store_number: str
    store_detail_cnt: int

class StoreDetailModel(BaseModel):
    result: str
    data: StoreDetailData


class StoreListData(BaseModel):
    detail_idx: int
    detail_name: str
    detail_price: int

class StoreDetailList(BaseModel):
    detail_list: List[StoreListData]

class StoreDetailListModel(BaseModel):
    result: str
    data: StoreDetailList