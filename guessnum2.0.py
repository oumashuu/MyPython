#python猜数字小游戏版本2.0 功能猜数字，记录成绩（成绩存在grade.txt中）
from random import randint
def read_file():
  f=open('grade.txt')
  lines=f.readlines()
  su=lines[0]
  scor=lines[1]
  sum=int(su)
  score=int(scor)
  f.close()
  def guess_num(score):
    answer=randint(1,100)
    print(answer)
    new_score=0
    bool=True
    print('开始猜数字吧！')
    while(bool):
      new_score=new_score+1
      ans=int(input())
      if(ans<answer):
        print('太小了')
      elif(ans>answer):
        print('太大了')
      else:
        print('猜对啦！')
        bool=False
    if(new_score<score):
      score=new_score
    print('当前成绩：',new_score)
    return score
  score=guess_num(score)
  def write_file(sum,score):
    f=open('grade.txt','w')
    sum=sum+1
    data=str(sum)+'\n'+str(score)
    f.write(data)
    f.close
  write_file(sum,score)
  print('总局数：',sum+1,'  最好成绩：',score)
read_file()

  