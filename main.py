s=input()
#taking input string
i=0
l=""
#defining the function
def strength(n):
  a=0
  value=0
  while(n[a]!=-1):
#writing different cases possible and telling how to function in each case
    if(n[a] in ("A","B","C") and n[a+1] not in (2,3,4,5,6,7,8,9)):
      if(n[a]=="A"):
        value=value+1
      if(n[a]=="B"):
        value=value+2
      if(n[a]=="C"):
        value=value+3
    if(n[a] in ("A","B","C") and n[a+1] in (2,3,4,5,6,7,8,9)):
      if(n[a]=="A"):
        value=value+1*n[a+1]
      if(n[a]=="B"):
        value=value+2*n[a+1]
      if(n[a]=="C"):
        value=value+3*n[a+1]
#a very special case when we incor a "(". So i asked the computer to search for the next")". And then asked it to save all the content inside this () into a new string say l. Now i performed our function for l again. 
    if(n[a]=="("):
      k=a+1
      while(n[k]!=-1):
        if(n[k]==")"):
          l=n[a+1:k]
          if(n[k+1] in (2,3,4,5,6,7,8,9)):
            y=strength(l)*n[k+1]
          else:
            y=strength(l)
          value = value +y
          break
        else:
          k=k+1
#at the end the function returns the value of strength of string
  print("The value of strenth is ",value)
  
while(s[i]!=-1):
  if(s[i] in ("A","B","C","(",")",2,3,4,5,6,7,8,9)):
    if ((s[i] in ("A","B","C","(",")")) or (s[i] in(2,3,4,5,6,7,8,9) and s[i+1] not in (2,3,4,5,6,7,8,9))):
      i=i+1
    else:
      print("invalid string entry")
      break
  else:
    print("invalid string entry")
    break
if(s[i]==-1):
  strength(s)