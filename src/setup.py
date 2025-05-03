# -*- coding: utf-8 -*-
import sys
from distutils.core import setup

if len(sys.argv) == 1:
    sys.argv.append("py2exe")

setup(
    name="payroll",
    version="1.0",
    description="Automatic process of salary adjustments ",
    author="Clay Lancini",
    author_email="clay.lancini@proton.me",
    url="url del proyecto",
    license="none",
    scripts=["payroll.py"],
    options={"py2exe": {"includes": ["tkinter"], "bundle_files": 3}},
    windows=[{"script": "payroll.py",
              "icon_resources": [(1, "icons8-payroll-64.ico")]}],
    zipfile=None,
)
