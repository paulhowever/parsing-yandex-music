import requests
from pprint import pprint

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'yandexuid=5515509341646335463; yuidss=5515509341646335463; is_gdpr=0; is_gdpr_b=CMrGBxCkdSgC; mda=0; my=YwA=; gdpr=0; L=CQhSc28MA3BeYkpxVXNiAU53UF1gYX1BFw9EXQdWWkIgHSYYCTomDA==.1656013115.15017.320218.ced652acb68465c619999ffa88d888ba; yandex_login=pavel230tishenko; font_loaded=YSv1; ymex=1961695463.yrts.1646335463#1981746028.yrtsi.1666386028; _ym_uid=1668292740895046439; yashr=882210461674054412; i=ZKTGg2qpUJYIQMWnikGF6t/6+MGXy+CpCnt1inVvtKfTA4OMiDVvCwpRRZWb84gpPYpG4nqWy+moejkgDmz9d0tgUlg=; yandex_gid=2; yp=1715286648.p_sw.1683750647#1971373115.udn.cDrQn9Cw0LLQtdC7INCi0LjRidC10L3QutC%2B#1999166985.pcs.1#1683917217.szm.1_25:1536x864:1536x746#1684173438.mcv.0#1684173438.mcl.ovnonn#1686247038.hdrc.0#1686342515.ygu.1; _ym_d=1683806986; AMP_MKTG_332f8b000f=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; AMP_332f8b000f=JTdCJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJkZXZpY2VJZCUyMiUzQSUyMjg0MzYyZjc3LTg2MjMtNDI1Yy05YzJmLTZiNzM1ZmJjODRmNiUyMiUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNjg0ODY0ODYwMTQzJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTY4NDg2NDg1ODQyMiUyQyUyMnVzZXJJZCUyMiUzQTE1OTA0OTM1JTdE; skid=6044507551685185405; device_id=a6995582c51048aa789cae0be258693f782b9999e; active-browser-timestamp=1685819065891; Session_id=3:1685819058.5.0.1656013115373:mbfzvA:2b.1.2:1|852290303.-1.2.1:169048061|3:10270811.823495.giBlGwVYNUzkTiM5RLRChokFZYE; sessar=1.99.CiD0i5gcEbQ6m6vntxL4HyqCbOYMiRFfnM05x5NPyCrAkw.j7Gj6ltbjRdCe_TzPab2IbnpLKrKTVJC_GchfQdvMhE; sessionid2=3:1685819058.5.0.1656013115373:mbfzvA:2b.1.2:1|852290303.-1.2.1:169048061|3:10270811.823495.fakesign0000000000000000000; _ym_isad=2; _ym_visorc=b; lastVisitedPage=%7B%7D; _yasc=hPqXP6GbmkjId7Ia2ghenDki4BrKNfUxkkQy5+rIF5SLV0DiBWx4ov5Ql7spyy1GhFSXADCXZwcRtW7WLJo=; bh=EkEiR29vZ2xlIENocm9tZSI7dj0iMTEzIiwgIkNocm9taXVtIjt2PSIxMTMiLCAiTm90LUEuQnJhbmQiO3Y9IjI0IhoFIng4NiIiECIxMTMuMC41NjcyLjEyOSIqAj8wOgkiV2luZG93cyJCCCIxNS4wLjAiSgQiNjQiUlwiR29vZ2xlIENocm9tZSI7dj0iMTEzLjAuNTY3Mi4xMjkiLCJDaHJvbWl1bSI7dj0iMTEzLjAuNTY3Mi4xMjkiLCJOb3QtQS5CcmFuZCI7dj0iMjQuMC4wLjAiIg==',
    'Referer': 'https://music.yandex.ru/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'X-Current-UID': '852290303',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.ru/chart',
    'X-Yandex-Music-Client-Now': '2023-06-03T22:06:33+03:00',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.9250514114937041',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, headers=headers)
pprint(response.status_code)
#pprint(response.json()['chartPositions'])
for track in response.json()['chartPositions']:
    position = track['chartPosition']['position']
    title = track['track']['title']
    author = track['track']['artists'][0]['name']
    artist = [artist['name'] for artist in track['track']['artists']]
    authors = ','.join(artist)

    print(f'№-{position} - {title} - {authors}')

