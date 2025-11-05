import requests, json, sys

try:
    r = requests.post(
        "https://trends.google.com/_/TrendsUi/data/batchexecute",
        data={
            "f.req": '[[["i0OFE","[null,null,\\"JP\\",0,\\"ja\\",48,1]",null,"generic"]]]'
        },
        timeout=10,
    )
    r.raise_for_status()
    print(*[x[0] for x in json.loads(json.loads(r.text[5:])[0][2])[1]], sep="\n")
except Exception as e:
    print("エラー:", e, file=sys.stderr)
