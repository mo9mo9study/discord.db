# coding: UTF-8

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

"""==============================
DB info
=============================="""
DB_user=os.environ.get("DB_USER")
DB_password=os.environ.get("DB_PASSWORD")
DB_host=os.environ.get("DB_HOST")
DB_port=os.environ.get("DB_PORT")
DB_database=os.environ.get("DB_DATABASE")