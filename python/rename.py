# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 07:58:34 2020

@author: seiji
"""

import os
import datetime

# SDカードのディレクトリ
dir_name = 'E:/DCIM/100MEDIA'

file_m_name = "坂戸図書館・ベルク_スロー"

files = os.listdir(dir_name)

for file in files:
    # 拡張子なしのファイル名を取得
    file_name = file.split('.')[0]
    # 拡張子を取得
    ext = file.split('.')[1]

    created_time = os.path.getctime(os.path.join(dir_name, file))

    date = datetime.datetime.fromtimestamp(created_time)

    date = date.strftime('%Y%m%d%a')

    new_filename = f"{date}_{file_m_name}_{file_name}.{ext}"

    os.rename(os.path.join(dir_name, file),
              os.path.join(dir_name, new_filename))
