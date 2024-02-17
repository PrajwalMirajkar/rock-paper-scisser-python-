import random
print("*******************************************************")
print("*             * PAPER * ROCK * SCISSOR*               *")
print("*******************************************************")
print(" Lets start the game!!...... ")
point=0
ai=0
hs=0
cs=0
ma=0
while(True):
  if(ma>5):
    print("####################################################")
    print("Total match:",ma)
    print("human score",hs)
    print("ai score:",cs)
    if(hs>cs):
      print("congrats you won")
    elif(cs>hs):
      print("ai won....Better luck next time")
    else:
        print("MATCH DRAW")
    print("####################################################")
    break
  c=input("chose paper->p  rock->r  scissor->s stop->stop: ")
  if(c=="p"):
    print("paper")
    point=10+random.randint(1,3)
    match point:
      case 11:
        ma=ma+1
        hs=hs+1
        print("human: paper","ai:rock")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("human wins","ai lost the match")
        print("_______________________________________________________")

      case 12:
        ma=ma+1
        cs=cs+1
        print("human: paper","ai:scissor")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("human lost","ai won the match")
        print("_______________________________________________________")

      case 13:
        ma=ma+1
        hs=hs+1
        cs=cs+1
        print("human: paper","ai:paper")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("match draw")
        print("_______________________________________________________")


  elif(c=="r"):
    print("rock")
    point=20+random.randint(1,3)
    match point:
      case 21:
        ma=ma+1
        hs=hs+1

        print("human: rock","ai:scisser")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("human wins","ai lost the match")
        print("_______________________________________________________")
      case 22:
        ma=ma+1
        cs=cs+1
        print("human: rock","ai:paper")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("human lost","ai won the match")
        print("_______________________________________________________")
      case 23:
        ma=ma+1
        hs=hs+1
        cs=cs+1
        print("human: rock","ai:rock")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("match draw")
        print("________________________________________________________")
  elif(c=="s"):
    print("sissor")
    point=30+random.randint(1,3)
    match point:
      case 31:
        ma=ma+1
        hs=hs+1
        print("human: sisser","ai:paper")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("human wins","ai lost the match")
        print("_______________________________________________________")
      case 32:
        ma=ma+1
        cs=cs+1
        print("human: sisser","ai:rock")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("human lost","ai won the match")
        print("_______________________________________________________")
      case 33:
        ma=ma+1
        hs=hs+1
        cs=cs+1
        print("human: sisser","ai:scsser")
        print("match: ",ma,"human score: ",hs,"ai score: ",cs)
        print("match draw")
        print("________________________________________________________")
  elif(c=="stop"):
    break
print("program end")