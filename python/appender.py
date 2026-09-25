"""

https://atcoder.jp/contests/abc476/tasks/abc476_a

A - Appender  / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 
100 点

問題文
英小文字からなる文字列 
S が与えられます。

以下のようにして決まる文字列 
T を出力してください。

S の末尾の文字が e である場合、
T は 
S の末尾に r を付け加えた文字列である。
S の末尾の文字が e でない場合、
T は 
S の末尾に er を付け加えた文字列である。
制約
S は英小文字からなる文字列
S の長さは 
1 以上 
10 以下
入力
入力は以下の形式で標準入力から与えられる。

S
出力
答えを出力せよ。

入力例 1
Copy
live
出力例 1
Copy
liver
live の末尾の文字は e なので、live の末尾に r を付け加えた文字列 liver が出力するべき文字列 
T です。

入力例 2
Copy
femur
出力例 2
Copy
femurer
femur の末尾の文字は e ではないので、femur の末尾に er を付け加えた文字列 femurer が出力するべき文字列 
T です。

入力例 3
Copy
chimpanzee
出力例 3
Copy
chimpanzeer
chimpanzee の末尾の文字は e なので、chimpanzee の末尾に r を付け加えた文字列 chimpanzeer が出力するべき文字列 
T です。
"""

s = input()

if s[-1] == 'e':
    print(s + 'r')
else:
    print(s + 'er')

