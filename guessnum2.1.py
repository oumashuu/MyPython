from random import randint# 该版本实现的功能有：1、根据玩家姓名进行游戏数据的记录（存在save.txt中）
import datetime,time      #2、游戏记录中添加了一项猜出数字最短时间的记录

name=input('请输入玩家名字：')

f=open('save.txt')
lines=f.readlines()
f.close()

scores={}
for l in lines:
  s=l.split()
  scores[s[0]]=s[1:]
score=scores.get(name)
if(score is None):
  score=[0,0,0,0]

game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
min_t=int(score[3])
if(game_times > 0):
  avg_times=float(total_times)/game_times
else:
  avg_times=0
if(game_times==0):
  print('欢迎你玩这个游戏')
else:
  print('%s,你已经玩了%d次了，最少%d轮猜出答案，平均%.2f轮猜出答案，最少用%d秒猜出答案。' % (name,game_times,min_times,avg_times,min_t))

num=randint(1,100)
times=0
bingo=True
while(bingo):
  times+=1
  if(times==1):
    answer=int(input('输入数字开始游戏：'))
    start=datetime.datetime.now()
  else:
    answer=int(input('请猜数字：'))
  if(answer>num):
    print('太大')
  elif(answer<num):
    print('太小')
  else:
    end=datetime.datetime.now()
    t=(end-start).seconds
    print('猜对啦,%d轮猜出答案' % times)
    print('用时：'+str(t)+'秒')
    bingo=False

if(game_times==0 or min_times>times):
  min_times=times
if(game_times==0 or min_t>t):
  min_t=t
total_times+=times
game_times+=1


scores[name]=[str(game_times),str(min_times),str(total_times),str(min_t)]
result=''
for n in scores:
  line=n+' '+' '.join(scores[n])+'\n'
  result += line
  
f=open('save.txt','w')
f.write(result)
f.close()