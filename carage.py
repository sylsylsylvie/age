driving = input('你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('just say yes or no')
	raise SystemExit

age = input('你的年齡是？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('怎麼這麼小會有開過車？')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照了')
	else:
		print('再過幾年就可以考駕照了')
else:
	print('just say yes or no')