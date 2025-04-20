def unique_names(names):
    result=[] for n in names:
        if n not in result:
            result.append(n)
    return result