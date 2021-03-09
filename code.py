Coding:
  
def forbid(s,w):
    if w not in s:
      return 0
    else:
      return 1
s=str(input())
w=str(input())
if forbid(s,w):
  print("YES")
else:
  print("NO")
