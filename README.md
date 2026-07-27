The [Bibles](./Bibles) directory contains a copy the Zefania XML bibles found in the
[SourceForge project zefania-sharp](https://sourceforge.net/projects/zefania-sharp/files/Bibles/) ("Zefania XML Bible Markup Language Files").

The XML files were downloaded and extracted with [`download.py`](./download.py) on 2026-07-26.

`download.py` is dependent on the Python module [SourceForgeDownloader](https://github.com/ReneNyffenegger/py-tool-SourceForgeDownloader).

# Observerations

## Format

[Torrey's Topical Textbook](https://github.com/ReneNyffenegger/SourceForge-Zefania-XML-Bibles-copy/blob/master/Bibles/ENG/Torreys%20Topical%20Textbook/SF_2006-03-02_ENG_TTB_(TORREY'S%20TOPICAL%20TEXTBOOK).xml) is the only “Bible” with
format set to `Zefania XML Dictionary Markup Language`. All other bibles have `Zefania XML Bible Markup Language`.

# Corrections

**GRC/Westcott-Hort Greek NT/Westcott and Hort with NA27 UBS4 variants/SF_2022-09-19_GRC_WHNU_(Westcott and Hort with NA27 UBS4 variants).xml**:\
[Commit 0cd58ff](https://github.com/ReneNyffenegger/SourceForge-Zefania-XML-Bibles-copy/commit/0cd58ff) removed the malformed XML tag `<XMLBIBLE version="3.0.0.9.1" p1:noNamespaceSch` which
was followed by the correct tag `<XMLBIBLE version="3.0.0.9.1" p1:noNamespaceSchemaLocation="zef2005.xsd" biblename="Westcott and Hort with NA27 UBS4 variants" type="x-bible" status="v" revision="241" xmlns:p1="http://www.w3.org/2001/XMLSchema-instance">`.
