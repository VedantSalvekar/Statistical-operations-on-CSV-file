
import pandas as pd

df = pd.read_csv(r'file_name')

df

def mode():
    a = []
    print("Mode : \n")
    for i in df:
      if i != "id" and df[i].dtype != "object":
        a.append(i)
    for j in a:
      dict = {}
      b = list(df[j])
      for k in b:
        if k in dict:
          dict[k] += 1
        else:
          dict[k] = 1
      keyMax = max(dict.keys(), key=(lambda k: dict[k]))
      print(keyMax, "-->", j)

def median():
  a = []
  print("Median : \n")
  for i in df:
    if i != "id" and df[i].dtype != "object":
      a.append(i)
  for j in a:
    k = list(df[j].sort_values())
    l = len(df[j])
    if l % 2 != 0:
      m = (l + 1) // 2
      print(j, "-->", k[m])
    else:
      n = l // 2
      z = n - 1
      g = (k[n] + k[z]) / 2
    print(j, "-->", g)
  print()

def mean():
    a = []
    print("Mean : \n")
    for i in df:
      if i != "id" and df[i].dtype != "object":
        a.append(i)
    for j in a:
      s = 0
      l = 0
      for k in df[j]:
        s += k
        l += 1
      print(j, "-->", s / l)
    print()

mean()
mode()
median()