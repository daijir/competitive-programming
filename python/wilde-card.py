"""

https://atcoder.jp/contests/abc476/tasks/abc476_b

B - Wild Card  / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 
200 点

問題文
S は英小文字からなる長さ 
N の文字列です。
T は英小文字および * からなる長さ 
N の文字列です。
S が 
T にマッチするとは、
T に含まれる * をそれぞれ好きな英小文字で置き換えることで 
T を 
S に一致させられることをいいます。
S が 
T にマッチするかどうかを判定してください。

制約
1≤N≤100
S は英小文字からなる長さ 
N の文字列
T は英小文字および * からなる長さ 
N の文字列
入力
入力は以下の形式で標準入力から与えられる。

N  
S  
T  
出力
S が 
T にマッチするならば Yes を、マッチしないならば No を 
1 行で出力せよ。

入力例 1
Copy
8
chokudai
**o*u*ai
出力例 1
Copy
Yes
T の 
1,2,4,6 文字目の * をそれぞれ c,h,k,d に置き換えることで 
T を 
S に一致させることができます。

入力例 2
Copy
5
snuke
snake
出力例 2
Copy
No
入力例 3
Copy
5
yiwiy
*****
出力例 3
Copy
Yes
"""

n = input()
s = input()
t = input()

n = int(input())
s = input()
t = input()

ans = "Yes"
for i in range(n):
  if t[i] != "*" and t[i] != s[i]:
    ans = "No"
    break

print(ans)