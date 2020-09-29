import json
import re

variable = {
"login": "courte_e",
"exercice": "strlen"
}

def main():
    i = 0
    fail = []
    tmp = None
    with open("./source/c.json", 'r') as f:
            norme = json.load(f)
    with open("./code/exercice.c", 'r') as f:
            code = f.read()

    while (i < len(norme)):
        tmp = test(norme[i], code)
        if tmp["number"] > 0:
            fail.append(tmp)
        i += 1
    print(fail)

def test(norme, code):
    fail = 0
    if "var" in norme and norme["var"] is not None:
        for i in norme["var"]:
            for i2 in ["should", "should_not"]:
                try:
                    norme[i2] = norme[i2].replace('{{' + i + '}}', variable[i])
                except:
                    pass;
    if "filter" in norme and norme["filter"] is not None:
        for i in norme["filter"]:
            exec(i, globals())
            code = fil(code)
    if "script" in norme:
        exec(norme["script"], globals())
        fail = fun(code)
    elif "should" in norme and "should_not" in norme:
        if norme["should"] is not None and norme["should_not"] is not None:
            s = re.compile(norme["should"])
            s2 = re.compile(norme["should_not"])
            fail = len(s2.findall(code)) - len(s.findall(code))
        elif norme["should"] is not None:
            s = re.compile(norme["should"])
            fail += (0 if len(s.findall(code)) > 0 else 1)
        elif norme["should_not"] is not None:
            s = re.compile(norme["should_not"])
            fail += len(s.findall(code))
    return {"name": norme["ref"], "number": fail}

main()
