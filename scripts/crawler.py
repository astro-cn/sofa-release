import requests
from bs4 import BeautifulSoup
from os import path

SOFA_HOST = "http://www.iausofa.org/"

# IAU SOFA sources (version, src, changelog)
sofa_meta = [
    ("20090201_c", "2009_0201_C/sofa_c-20090201_c.tar.gz", "changes_2009_0201.html"),
    ("20091231_c", "2009_1231_C/sofa_c-20091231_c.tar.gz", "changes_2009_1231.html"),
    ("20101201", "2010_1201_C/sofa_c-20101201.tar.gz", "changes_2010_1201.html"),
    ("20120301_a", "2012_0301_C/sofa_c-20120301_a.tar.gz", "changes_2012_0301.html"),
    ("20131202_d", "2013_1202_C/sofa_c-20131202_d.tar.gz", "changes_2013_1202.html"),
    ("20150209_a", "2015_0209_C/sofa_c-20150209_a.tar.gz", "changes_2015_0209.html"),
    ("20160503_c", "2016_0503_C/sofa_c-20160503_c.tar.gz", "changes_2016_0503.html"),
    ("20170420", "2017_0420_C/sofa_c-20170420.tar.gz", "changes_2017_0420.html"),
    ("20180130", "2018_0130_C/sofa_c-20180130.tar.gz", "changes_2018_0130.html"),
    ("20190722", "2019_0722_C/sofa_c-20190722.tar.gz", "changes_2019_0722.html"),
    ("20200721", "2020_0721_C/sofa_c-20200721.tar.gz", "changes_2020_0721.html"),
    ("20210125_a", "2021_0125_C/sofa_c-20210125_a.tar.gz", "changes_2021_0125.html"),
    ("20210512", "2021_0512_C/sofa_c-20210512.tar.gz", "changes_2021_0512.html"),
    ("20231011", "2023_1011_C/sofa_c-20231011.tar.gz", "changes_2023_1011.html"),
]

def crawling_changelogs(output_dir: str = "CHANGELOG/"):
    for version, _, changelog in sofa_meta:
        filename = path.join(output_dir, f"CHANGELOG-{version}.md")
        url = f'{SOFA_HOST}{changelog}'
        with requests.get(url, stream=True) as r:
            # parse html use BeautifulSoup
            soup = BeautifulSoup(r.text, "html.parser")
            html = soup.select_one("div#textbox")
            # remove all img tag in html
            for t in html.find_all("img"):
                t.decompose()
            if not html:
                print(f"Failed to parse {url}")
                continue
            with open(filename, "w", encoding="utf-8") as f:
                # write headers
                f.write(f'> The original link of the following content: [{url}]({url})\n')
                # write html
                f.write(html.prettify())

if __name__ == "__main__":
    crawling_changelogs(path.join(__file__, "../../", "CHANGELOG/"))
        