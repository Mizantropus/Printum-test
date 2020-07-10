def parser(s=None):
    response = None
    try:
        if type(s) is str:
            response = {}
            s_splitted = s.split(":")
            count = 1
            key = ""
            for item in s_splitted:
                if count % 2 == 0:
                    response[key] = item
                else:
                    key = item
                    response[key] = ""
                count += 1
        else:
            return response
        return response
    except:
        return response

class Fow:
    name = "fgb"

def func():
    return "sdfv"

print(parser(None))
print(parser(False))
print(parser(0))
print(parser(NameError))
print(parser(1.1))
print(parser({"key":"val"}))
print(parser((1,2)))
print(parser([1,2]))
print(parser({1,2}))
print(parser(Fow))
print(parser(func))
print(parser("key1:"))
print(parser("key1:val1"))
print(parser("key1:val1:key2:val2"))
print(parser("key1:val1:key2:val2:"))
print(parser("::::::::"))