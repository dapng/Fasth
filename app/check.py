from fastapi import Depends, Header, HTTPException
import logging


logging.basicConfig(level=logging.INFO)


def check_flag(x_flag: str = Header(None)):
    return x_flag