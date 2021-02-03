# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 07:58:34 2020

@author: seiji
"""

import os
import datetime

# Movieのディレクトリ
dir_name = '/Users/seiji/Movies'

# ファイル名を指定
file_m_name = "アオキ・川越図書館_スローx6"

# mp4ファイルのみを対象にする
is_mp4_files = os.listdir(dir_name)
files = [i for i in is_mp4_files if ".MP4" in i]

for file in files:
    # 拡張子なしのファイル名を取得
    file_name = file.split('.')[0]
    # 拡張子を取得
    ext = file.split('.')[1]

    created_time = os.stat(os.path.join(dir_name, file)).st_birthtime

    date = datetime.datetime.fromtimestamp(created_time)

    date = date.strftime('%Y%m%d%a')

    new_filename = f"{date}_{file_m_name}_{file_name}.{ext}"

    os.rename(os.path.join(dir_name, file),
              os.path.join(dir_name, new_filename))
