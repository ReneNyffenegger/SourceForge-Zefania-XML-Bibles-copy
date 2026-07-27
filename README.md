The [Bibles](./Bibles) directory contains a copy the Zefania XML bibles found in the
[SourceForge project zefania-sharp](https://sourceforge.net/projects/zefania-sharp/files/Bibles/) ("Zefania XML Bible Markup Language Files").

The XML files were downloaded and extracted with [`download.py`](./download.py) on 2026-07-26.

`download.py` is dependent on the Python module [SourceForgeDownloader](https://github.com/ReneNyffenegger/py-tool-SourceForgeDownloader).

# Corrections

[Commit 0cd58ff](https://github.com/ReneNyffenegger/SourceForge-Zefania-XML-Bibles-copy/commit/0cd58ff) removed the malformed XML tag `<XMLBIBLE version="3.0.0.9.1" p1:noNamespaceSch` which
was followed by the correct tag `<XMLBIBLE version="3.0.0.9.1" p1:noNamespaceSchemaLocation="zef2005.xsd" biblename="Westcott and Hort with NA27 UBS4 variants" type="x-bible" status="v" revision="241" xmlns:p1="http://www.w3.org/2001/XMLSchema-instance">`.
