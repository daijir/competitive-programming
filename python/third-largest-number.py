# Third Largest Number
# https://atcoder.jp/contests/abc476/tasks/abc476_c

import sys

def main():
  input = sys.stdin.read
  data = input().split()
  
  if not data:
    return
  
  N = int(data[0])
  A = [int(x) for x in data[1:]]
  
  top3 = sorted(A[:3], reverse=True)
  
  results = []
  
  results.append(str(top3[2]))
  
  for i in range(3, N):
    val = A[i]
    if val > top3[2]:
      top3[2] = val
      top3.sort(reverse=True)
    results.append(str(top3[2]))
      
  print("\n".join(results))

if __name__ == "__main__":
  main()
