#!/usr/bin/env python3

import zipfile
import SourceForgeDownloader

zips = SourceForgeDownloader.download('zefania-sharp', '/Bibles')
for zip in zips:
    if zip.suffix.lower() == '.zip':
       with zipfile.ZipFile(zip) as zip_:
            zip_.extractall(zip.parent)
