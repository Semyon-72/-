import json
file = 'input.json'


def task(a=0) -> float:
    with open(file) as ch:
        prog = json.load(ch)
        for tex in prog:
            score = tex['score']
            weight = tex['weight']
            b = score * weight
            a += b
    return a


print(round(task(), ndigits=3))



