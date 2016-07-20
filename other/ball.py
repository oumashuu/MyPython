from random import choice
direction=['w','a','s','d']
score=0
count=range(1,6)
for x in count:
  print(x,'请输入你的射门方向：')
  you=input()
  com=choice(direction)
  print('电脑扑救方向：',com)
  if(com!=you):
    print('命中啦！')
    score=score+1
  else:
    print('失败了')
    score=score-1
print('游戏结束！\n你的成绩为：',score)