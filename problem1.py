str="a=b;c=d;e=f;g=h"
def strtolist(str):
  remcol=str.split(";")
  values=[]
  for i in remcol:
    key,value=i.split("=")
    values.append((key.strip(),value.strip()))
  return values

print(strtolist(str))
  
