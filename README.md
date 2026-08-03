The [Bibles](./Bibles) directory contains a copy the Zefania XML bibles found in the
[SourceForge project zefania-sharp](https://sourceforge.net/projects/zefania-sharp/files/Bibles/) ("Zefania XML Bible Markup Language Files").

The XML files were downloaded and extracted with [`download.py`](./download.py) on 2026-07-26.\
The downloaded files are stored in the [download/2026-07-26](https://github.com/ReneNyffenegger/SourceForge-Zefania-XML-Bibles-copy/tree/download/2026-07-26) branch.

`download.py` is dependent on the Python module [SourceForgeDownloader](https://github.com/ReneNyffenegger/py-tool-SourceForgeDownloader).

# Observations

## Format

[Torrey's Topical Textbook](https://github.com/ReneNyffenegger/SourceForge-Zefania-XML-Bibles-copy/blob/master/Bibles/ENG/Torreys%20Topical%20Textbook/SF_2006-03-02_ENG_TTB_(TORREY'S%20TOPICAL%20TEXTBOOK).xml) is the only “Bible” with
format set to `Zefania XML Dictionary Markup Language`. All other bibles have `Zefania XML Bible Markup Language`.

## Identifiers

The following identifiers are not unique and appear at least twice: `BWE`, `BZY2000`, `Byz`, `CPDV`, `CZBKR`, `CZEB21`, `CZECEP`, `GB`, `GERNEUE`, `GerNeUe` (4x), `KJV`, `LUT.1545.LH`, `NHEB`, `NHEBJE`, `NHEBME`, `OffBiLe`, `OffBiSt`, `PAT80`, `RWEBSTER`, `SCH1951`, `TB`, `TISCHENDORF` (3x), `luth1912`.

The identifier `Allioli_Arndt_1914_nur_Bibeltext_alte_Psalmennr_deutsch` is exceptionally long.

## Languages

Language codes are applied inconsistently.

German appears primarily as `GER` but also as `DEUTSCH` and `DE`.

Dutch is represented solely by the two-letter code `NL`.

In addition, some codes are rendered in lowercase rather than uppercase.

# Corrections

**GRC/Westcott-Hort Greek NT/Westcott and Hort with NA27 UBS4 variants/SF_2022-09-19_GRC_WHNU_(Westcott and Hort with NA27 UBS4 variants).xml**:\
[Commit 0cd58ff](https://github.com/ReneNyffenegger/SourceForge-Zefania-XML-Bibles-copy/commit/0cd58ff) removed the malformed XML tag `<XMLBIBLE version="3.0.0.9.1" p1:noNamespaceSch` which
was followed by the correct tag `<XMLBIBLE version="3.0.0.9.1" p1:noNamespaceSchemaLocation="zef2005.xsd" biblename="Westcott and Hort with NA27 UBS4 variants" type="x-bible" status="v" revision="241" xmlns:p1="http://www.w3.org/2001/XMLSchema-instance">`.
