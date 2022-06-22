time = int(input("数値を入れてください："))

if time >= 6 and time <= 11:
  print("おはよう")
elif time >= 12 and time <= 17:
  print("こんにちは")
elif time >= 18 and time <= 23:
  print("こんばんは")
else:
  print("6~23の値で入力してください")