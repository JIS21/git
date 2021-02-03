# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:09:10 2020

@author: seiji
"""

import os

# Movieのディレクトリmac
dir_name = '/Users/seiji/Movies'

# ファイル名を指定
file_m_name = "アオキ・川越図書館・スロー"

# mp4ファイルのみを対象にする
is_mp4_files = os.listdir(dir_name)
files = [i for i in is_mp4_files if ".MP4" in i]

for file in files:
# 拡張子なしのファイル名を取得
    file_name01 = file.split('_')[-2]
    file_name02 = file.split('_')[-1]

    new_filename =f"{file_name01}_{file_name02}"
    
    os.rename(os.path.join(dir_name,file),os.path.join(dir_name,new_filename))