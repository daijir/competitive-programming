"""
https://atcoder.jp/contests/abs/tasks/arc065_a

ABC049C - 白昼夢  / 
実行時間制限: 2 sec / メモリ制限: 256 MiB

配点 : 
300 点

問題文
英小文字からなる文字列 
S が与えられます。 
Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで 
S=T とすることができるか判定してください。

T の末尾に dream dreamer erase eraser のいずれかを追加する。
制約
1 ≦ ∣S∣ ≦ 10 
5
 
S は英小文字からなる。
入力
入力は以下の形式で標準入力から与えられる。

S
出力
S=T とすることができる場合 YES を、そうでない場合 NO を出力せよ。

入力例 1

erasedream
出力例 1

YES
erase dream の順で 
T の末尾に追加することで 
S=T とすることができます。

入力例 2

dreameraser
出力例 2

YES
dream eraser の順で 
T の末尾に追加することで 
S=T とすることができます。

入力例 3

dreamerer
出力例 3

NO
"""
import re

s = input()
if re.fullmatch(r"(dream|dreamer|erase|eraser)+", s):
    print("YES")
else:
    print("NO")

"""
re.fullmatch(パターン, 文字列)
文字列全体がパターンに最初から最後まで完全に一致しているかを調べる関数です。
・完全に一致していればMatchオブジェクトが返される
・一部でも合わなかったり、余計な文字が残ってたりすると、Noneが返される

r"(dream|dreamer|erase|eraser)+" の意味
r"..." - raw文字列。エスケープを無効化して正規表現を安全に書くために使う
(...) - 選択肢をひとつのグループにまとめる。つまり「dream または dreamer または erase または eraser のいずれか1つ」という意味です。
+ - 直前のグループの一回以上の繰り返しを表します。
"""

