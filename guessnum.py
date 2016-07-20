from random import randint
answer=randint(1,100)
score=0
bool=True
print('开始猜数字吧！')
while(bool):
  score=score+1
  ans=int(input())
  if(ans<answer):
    print('太小了')
  elif(ans>answer):
    print('太大了')
  else:
    print('猜对啦！')
    bool=False
print('成绩为：',score)
  