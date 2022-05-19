import bcrypt
from typing import List, Optional
from datetime import datetime, timedelta

from utils.exception import *

from fastapi import Depends, Request

from sqlalchemy import update, text, delete, func, insert, or_, and_
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from db.models.store import Store, StoreDetail, StoreView

from db.schemas.schemas import StoreSchemas

class FuncDTO():
    def __init__(self, session: sessionmaker):
        self.session = session

    async def query(self, statement):
        q = await self.session.execute(statement)

        data = []
        for row in q:
            data.append(dict(row))

        return data


    # 군장병 우대업소 확인
    # GET /function/store
    async def post_store(self, s: StoreSchemas):

        response = {
            "result":"success",
            "data": {}
        }

        if s.last_idx == 0:
            statement = select(
                Store.store_idx,
                Store.store_type,
                Store.store_name,
                Store.store_address,
                Store.store_number
                ).where(
                Store.store_address.like(f'%{s.loc_keyword}%'),
                Store.store_name.like(f'%{s.name_keyword}%'),
                Store.store_type.in_(s.store_type)
            ).order_by(
                Store.store_idx
            ).limit(20)
        else:
            statement = select(
                Store.store_idx,
                Store.store_type,
                Store.store_name,
                Store.store_address,
                Store.store_number
                ).where(
                Store.store_idx > s.last_idx,
                Store.store_address.like(f'%{s.loc_keyword}%'),
                Store.store_name.like(f'%{s.name_keyword}%'),
                Store.store_type.in_(s.store_type)
            ).order_by(
                Store.store_idx.desc()
            ).limit(20)
        data = await self.query(statement)

        response['data']['store_list'] = []

        if data:
            for d in data:
                store_list = {}
                store_list['store_idx'] = d['store_idx']
                store_list['store_type'] = d['store_type']
                store_list['store_name'] = d['store_name']
                store_list['store_address'] = d['store_address']
                store_list['store_number'] = d['store_number']

                response['data']['store_list'].append(store_list)

        return response


    # 군장병 우대업소 상세정보 확인
    # GET /function/store/detail?store_idx={int}
    async def get_store_detail(self, store_idx, host_ip):

        response = {
            "result":"success",
            "data": {}
        }

        statement = select(
            Store.store_idx,
            Store.store_type,
            Store.store_name,
            Store.store_address,
            Store.store_number
            ).where(
            Store.store_idx == store_idx
        )
        data = await self.query(statement)

        if not data:
            raise exception_40601

        response['data']['store_idx'] = data[0]['store_idx']
        response['data']['store_type'] = data[0]['store_type']
        response['data']['store_name'] = data[0]['store_name']
        response['data']['store_address'] = data[0]['store_address']
        response['data']['store_number'] = data[0]['store_number']

        # 조회수 로직
        statement = select(
            StoreView.view_idx
            ).where(
            StoreView.store_idx == store_idx,
            StoreView.view_ip == host_ip,
            StoreView.view_datetime >= datetime.utcnow() - timedelta(hours=10)
        )
        view_check = await self.query(statement)

        if not view_check:
            try:
                self.session.begin_nested()
                statement = insert(
                    StoreView
                    ).values(
                    store_idx=store_idx,
                    view_ip=host_ip
                )
                await self.session.execute(statement)
            except:
                self.session.rollback()
                raise exception_40601

        return response