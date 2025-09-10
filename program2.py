# formatting_issue_big.py
def process(data):
  result=[]
  for i in range(len(data)):
      if data[i]%2==0:
       result.append(data[i]*2)
      else:
        result.append(data[i]+1)
  return result
def main():
 data=[1,2,3,4,5,6]
 print(process(data))
main()