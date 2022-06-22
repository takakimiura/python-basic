temp = int(input("体温を入力してください："))

if temp < 37:
  print("仕事に行く")
elif temp >= 38:
  print("病院へ行く")
else:
  print("仕事を休む")