from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, constr

class StoreSchemas(BaseModel):
    last_idx: Optional[int] = 0
    loc_keyword: Optional[str] = ''
    name_keyword: Optional[str] = ''
    store_type: Optional[List[int]] = [1,2,3,4,5,6,7,8]