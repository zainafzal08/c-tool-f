import requests
import base64
import sys
import json

def decodeSession(s):
    s = s.split(".")
    res = "<"
    for e in s:
        if len(e) % 4 != 0:
            e += "="*(len(e) % 4)
        try:
            res += base64.b64decode(e).decode("utf-8")
        except:
            res += "????"
        res += "><"
    res = res[:-1]
    return res

def fudgeCookie(c,e,n,cookies):
    s = cookies.get(c)
    s = s.split(".")
    s[e] = base64.b64encode(bytearray(n,"utf-8")).decode("utf-8")
    s = ".".join(s)
    cookies.clear()
    cookies.set(c,s)

def status(r):
    code = r.status_code
    if code == 200:
        return '\033[92m'+"200"+'\033[0m'
    elif code == 404:
        return '\033[91m'+"404"+'\033[0m'
    else:
        return '\033[93m'+"%d"%code+'\033[0m'

def POST(root,sub,cookies,formData,cookieTarget):
    url = root+sub
    session = requests.Session()
    if cookies:
        r = session.post(url, data=formData, cookies=cookies)
    else:
        r = session.post(url, data=formData)
    print(">> [%s]"%status(r))
    if cookies:
        print(">> %s Parsed: %s"%(cookieTarget,decodeSession(cookies.get(cookieTarget))))
        print(">> %s Raw: %s"%(cookieTarget,cookies.get(cookieTarget)))
    j = None
    try:
        j = r.json()
        print(">> Json: True")
    except:
        print(">> Json: False")
    return (r.text,j,r.cookies)

def PUT(root,sub,cookies,formData,cookieTarget):
    url = root+sub
    if cookies:
        r = requests.put(url, data=formData, cookies=cookies)
    else:
        r = requests.put(url, data=formData)
    print(">> [%s]"%status(r))
    if cookies:
        print(">> %s Parsed: %s"%(cookieTarget,decodeSession(cookies.get(cookieTarget))))
        print(">> %s Raw: %s"%(cookieTarget,cookies.get(cookieTarget)))
    j = None
    try:
        j = r.json()
        print(">> Json: True")
    except:
        print(">> Json: False")
    return (r.text,j,r.cookies)

def GET(root,sub,cookies,cookieTarget):
    url = root+sub
    if cookies:
        r = requests.get(url, cookies=cookies)
    else:
        r = requests.get(url)
    print(">> [%s]"%status(r))
    if cookies:
        print(">> %s Parsed: %s"%(cookieTarget,decodeSession(cookies.get(cookieTarget))))
        print(">> %s Raw: %s"%(cookieTarget,cookies.get(cookieTarget)))
    j = None
    try:
        j = r.json()
        print(">> Json: True")
    except:
        print(">> Json: False")
    return (r.text,j)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 api.py <api target> (<cookie target>)?")
        exit(1)
    root = sys.argv[1]
    cookieTarget = "SESSION"
    if len(sys.argv) > 2:
        cookieTarget = sys.argv[2]
    cookies = None
    saved = {}
    res = None
    while(True):
        l = input("> ")
        cmd = l.split(" ")[0].upper()
        args = l.split(" ")[1:]
        if(cmd == "R"):
            l = saved[args[0]]
            cmd = l.split(" ")[0].upper()
            args = l.split(" ")[1:]
        if cmd == "HELP":
            print("    GET <sub>")
            print("    POST <sub> (<form_key>=<form_val>)*")
            print("    SHOW")
            print("    JSON")
            print("    SAVE <nickname>")
            print("    R <nickname>")
        elif cmd == "GET":
            res = GET(root, args[0], cookies, cookieTarget)
        elif cmd == "POST":
            data = {}
            for x in args[1:]:
                data[x.split("=")[0]] = x.split("=")[1]
            res = POST(root, args[0], cookies, data, cookieTarget)
            cookies = res[2]
        elif cmd == "PUT":
            data = {}
            for x in args[1:]:
                data[x.split("=")[0]] = x.split("=")[1]
            res = PUT(root, args[0], cookies, data, cookieTarget)
            cookies = res[2]
        elif cmd == "SHOW":
            print(">> "+("="*60))
            print(res[0])
            print(">> "+("="*60))
        elif cmd == "SAVE":
            saved[args[0]] = " ".join(args[1:])
        elif cmd == "QUIT":
            break
        elif cmd == "JSON":
            print(">> "+("="*60))
            if(res[1]):
                 print(json.dumps(res[1], sort_keys=True, indent=4, separators=(',', ': ')))
            else:
                print("None")
            print(">> "+("="*60))
        else:
            print(">> Unknown Command")
        print("")
