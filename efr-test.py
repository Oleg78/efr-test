#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  EFRtest.py
#  
#  Copyright 2012 Oleg <oleg@triangulum>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import os
import Image

def get_exif_EFR(jpg_file):
	image = Image.open(jpg_file)
	EFR = -1 #Значение по умолчанию, вернётся если exif-а нет
	if hasattr(image, '_getexif'):
		exifdata = image._getexif()
		try:
			EFR = exifdata[0x920A][0] / 100.0
		except:
			EFR = -2 #Ошибка чтения тега
	return EFR

def scan_scr_dir(src_dir):
	dir_list = [os.path.join(src_dir, d) for d in os.listdir(src_dir)
					if os.path.isdir(os.path.join(src_dir, d))]
					
	for d in dir_list:
		scan_scr_dir(d)

	file_list = [os.path.join(src_dir, f) for f in os.listdir(src_dir)
					if os.path.isfile(os.path.join(src_dir, f))
					and os.path.splitext(f)[1].upper() == '.JPG']
	
	for jpg_file in file_list:
		print jpg_file+';'+str(get_exif_EFR(jpg_file))
	
def main():
	scan_scr_dir('./')

if __name__ == "__main__":
	main()
