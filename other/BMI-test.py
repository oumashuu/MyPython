height=float(input('身高（m）：'))
weight=float(input('体重（kg）：'))
bmi=weight/(height*height)
if bmi<18.5:
  str='过轻'
elif 18.5<=bmi<25:
  str='正常'
elif 25<=bmi<28:
  str='过重'
elif 28<=bmi<32:
  str='肥胖'
elif bmi>=32:
  str='严重肥胖'
else:
  str='出错'
print('身体素质：',str,'\nBMI指数：%.4f' %bmi)