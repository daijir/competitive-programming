"""

https://paiza.jp/challenges/942/retry

パイザさんは、白黒のハンカチをたくさん持っています。コレクションの中には同じ柄のハンカチもあるため、何種類のハンカチを持っているかが気になりました。

それぞれのハンカチの大きさと模様は、縦が H マス横が W マスの HxW マスで表され、各マス目について '#' は黒色、 '.' は白色で塗りつぶされていることを表します。

N 枚のハンカチの情報が与えられるので、何種類のハンカチを持っているかを求めるプログラムを作成してください。

回転・反転するとすべて同じ模様になるものとします。

例えば、入力例 1 の場合、図のように所持しているハンカチの種類は 1 種類となります。

評価ポイント
10個のテストケースを入力し、正答数と解答の提出までに要した時間を測定し得点が決まります。
※提出いただいたコードは複数回実行され、一度の実行では1つのテストケースのみ入力
※制限時間を超えるとテストケースが通っても失格(0点)となります。
得点の計算方法：正解数得点(50点) ＋ 正解率×解答時間得点(2時間以内で50点、4時間以内で25点、6時間で0点と線形に点数が落ちます)
10個のテストケースで正しい出力がされるか評価 (50点)
解答の提出までに要した時間による評価 (50点)
入力される値
入力は次のフォーマットで与えられます。
N
X_1
X_2
...
X_N

・1 行目には、持っているハンカチの枚数 N が与えられます。
・2 行目以降は、k 番目のハンカチの情報 X_k (1 ≦ k ≦ N) が与えられます。

また、k 番目のハンカチの情報 X_k は以下のフォーマットで与えられます。

H W
p_1
p_2
...
p_H

・1 行目には、 k 番目のハンカチの縦横の大きさ H, W がこの順でスペース区切りで与えられます。
・続く H 行のうち i 行目 (1 ≦ i ≦ H) には長さ W の文字列 p_i が与えられます。 i 行目の j 番目 (1 ≦ j ≦ W) の文字 p_{i,j} は、 k 番目のハンカチの i 行 j 列目のマスの色を表します。

入力最終行の末尾に改行が 1 つ入ります。

文字列は標準入力から渡されます。標準入力からの値取得方法はこちらをご確認ください
期待する出力
所持しているハンカチの種類数を出力してください。

期待する出力は 1 行からなります。
整数で出力してください。
末尾に改行を入れ、余計な文字、空行を含んではいけません。
条件
すべてのテストケースにおいて、以下の条件をみたします。
・1 ≦ N ≦ 10
・1 ≦ H_i, W_i ≦ 100 (1 ≦ i ≦ N)
・p_{i, j} は '.' か '#' のいずれか

言語別実行時間制限の詳細は こちら をご確認ください。
入力例1
5
3 3
.#.
.#.
##.
3 3
...
###
#..
3 3
.#.
.#.
.##
3 3
..#
###
...
3 3
...
###
#..
出力例1
1
例えば、 3 番目の列車と 4 番目の列車について、 L_3 ≦ L_4 かつ R_4 ≦ R_3 の関係が成立しているため、答えは No となります。
入力例2
5
3 2
##
..
.#
3 2
.#
.#
#.
2 1
.
#
2 1
#
.
2 3
#..
.##
出力例2
3
"""

import sys

def rotate(pattern):
    return ["".join(row) for row in zip(*pattern[::-1])]
    
def get_canonical(pattern):
    candidates = []
    curr = pattern
    
    for _ in range(2):
        for _ in range(4):
            candidates.append(tuple(curr))
            curr = rotate(curr)
        
        curr = [row[::-1] for row in curr]
        
    return min(candidates)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    index = 1
    unique_patterns = set()
    
    for i in range(N):
        H = int(input_data[index])
        W = int(input_data[index + 1])
        index += 2
        
        pattern = []
        for _ in range(H):
            pattern.append(input_data[index])
            index += 1
            
        canonical = get_canonical(pattern)
        unique_patterns.add(canonical)
        
    print(len(unique_patterns))

            
if __name__ == "__main__":
    main()