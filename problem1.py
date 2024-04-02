strt="a=b;c=d;e=f;g=h"
def strtolist3(strt):
  values=[(key.strip(),value.strip()) for key,value in (i.split("=") for i in (remcol for remcol in strt.split(";")))]
  return values
print(strtolist3(strt))
