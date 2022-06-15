
import itertools
import pandas as pd

def coSo(x) -> str:
    s = ""
    for _ in range(5):
        r = int(x % 3)
        s = "".join((str(r), s))
        x = int(x / 3)
    return s

if __name__ == "__main__":
    l = []
    # f = open("diem.txt", "a")
    for i in range(0, 243):
        s = coSo(i)
        s = s.replace("0", "_")
        s = s.replace("1", "x")
        s = s.replace("2", "o")
        l.append(s)
        print("{} {}".format(i, s))
    df = pd.DataFrame()
    df["td"] = l
    df.to_excel("diem.xlsx", sheet_name="S1")
    # f.writelines(l)
    # print(l)

