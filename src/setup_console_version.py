# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="payroll",
    version="1.0",
    description="Automatic process of salary adjustments ",
    author="Clay Lancini",
    author_email="clay.lancini@proton.me",
    url="url del proyecto",
    license="none",
    scripts=["payroll.py"],
    console=[{"script": "payroll.py",
             "icon_resources": [(1, "icons8-payroll-64.ico")]}],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)
