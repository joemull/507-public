def req_url(base,params):
    s = base + "?"
    kvs = []
    for k in list(params.keys()):
        kvs.append(str(k) + "=" + str(params[k]))
    return s + "&".join(kvs)
