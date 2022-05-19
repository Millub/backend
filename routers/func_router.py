import boto3, os, hashlib, io

from typing import List, Optional
from fastapi import APIRouter, Request, File, UploadFile, Depends, HTTPException

from db.dals.func_dto import FuncDTO
from routers.dependencies import get_func_dto

from db.schemas.response import StoreModel, StoreDetailModel
from db.schemas.schemas import StoreSchemas

router = APIRouter(
    #dependencies=[Depends(get_token_header)],
    #responses={404: {"description": "Not found"}}
)


@router.post("/store", 
    response_model=StoreModel,
    description="""
    군장병 우대업소 확인

    last_idx(int): 마지막 idx (초기 0)
    loc_keyword(str): 지역 필터
    name_keyword(str): 상호명 필터
    store_type(List[int]): 1:일반음식점, 2:휴게음식점, 3:제과점, 4:소매업, 5:서비스업, 6:숙박업소, 7:농어촌민박, 8:미용업
    """)
async def post_store(
    s: StoreSchemas,
    func_dto: FuncDTO = Depends(get_func_dto)):

    response = await func_dto.post_store(s)

    return response


@router.get("/store/detail",
    response_model=StoreDetailModel,
    description="""
    군장병 우대업소 상세정보 확인

    store_idx(int): 우대업소 식별정보
    """)
async def get_store_detail(
    store_idx: int,
    request: Request,
    func_dto: FuncDTO = Depends(get_func_dto)):

    response = await func_dto.get_store_detail(store_idx, request.client.host)

    return response