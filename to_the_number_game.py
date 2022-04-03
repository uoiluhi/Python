aterukazu = 0
yosou = 0
kaisuu = 1
print("数当てゲーム")
aterukazu = int(input("好きな数を入れてください"))
for i in range(0, 60):
    print("             ")
print("上は見ちゃダメ")
print(" ")

while True:
    print("前の人が書き込んだ数を当ててください")
    yosou = int(input("考えた数を書き込んでください"))
    
    if yosou == aterukazu:
        print("あたりです", "あなたは", kaisuu, "回で数を当てることができました")
        break
    elif yosou <= aterukazu:
vc        kaisuu += 1
    else:
        print(yosou, "よりは小さいです")
        kaisuu += 1
        
