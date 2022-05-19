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

class StoreDetailModel(BaseModel):
    result: str
    data: StoreData