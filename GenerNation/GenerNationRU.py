import random
def version():
      version = "0.1"
      print(version)
      return version
def gensteam1(output="no", outprint="no", namefile="genernation.txt"):
      keys = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
      a1 = random.choice(keys)
      a2 = random.choice(keys)
      a3 = random.choice(keys)
      a4 = random.choice(keys)
      a5 = random.choice(keys)
      b1 = random.choice(keys)
      b2 = random.choice(keys)
      b3 = random.choice(keys)
      b4 = random.choice(keys)
      b5 = random.choice(keys)
      c1 = random.choice(keys)
      c2 = random.choice(keys)
      c3 = random.choice(keys)
      c4 = random.choice(keys)
      c5 = random.choice(keys)
      genoutprint = a1 + a2 + a3 + a4 + a5 + "-" + b1 + b2 + b3 + b4 + b5 + "-" +  c1 + c2 + c3 + c4 + c5
      if outprint == "yes":
         print(genoutprint)
      elif outprint == "no":
         pass
      else: 
         print("Для outprint не существует такого значения")
      if output == "yes":
         anomalokarisfile = namefile
         anomalokaris = open(anomalokarisfile, mode='a', encoding='utf-8')
         anomalokaris.write(str(genoutprint) + "\n")
      elif output == "no":
         pass
      else:
         print("Для output не существует такого значения")
      return genoutprint
def gensteam2(output="no", outprint="no", namefile="genernation.txt"):
      keys = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
      a1 = random.choice(keys)
      a2 = random.choice(keys)
      a3 = random.choice(keys)
      a4 = random.choice(keys)
      a5 = random.choice(keys)
      b1 = random.choice(keys)
      b2 = random.choice(keys)
      b3 = random.choice(keys)
      b4 = random.choice(keys)
      b5 = random.choice(keys)
      c1 = random.choice(keys)
      c2 = random.choice(keys)
      c3 = random.choice(keys)
      c4 = random.choice(keys)
      c5 = random.choice(keys)
      d1 = random.choice(keys)
      d2 = random.choice(keys)
      d3 = random.choice(keys)
      d4 = random.choice(keys)
      d5 = random.choice(keys)
      e1 = random.choice(keys)
      e2 = random.choice(keys)
      e3 = random.choice(keys)
      e4 = random.choice(keys)
      e5 = random.choice(keys)
      genoutprint = a1 + a2 + a3 + a4 + a5 + "-" + b1 + b2 + b3 + b4 + b5 + "-" +  c1 + c2 + c3 + c4 + c5 + "-" +  d1 + d2 + d3 + d4 + d5 + "-" +  e1 + e2 + e3 + e4 + e5
      if outprint == "yes":
         print(genoutprint)
      elif outprint == "no":
         pass
      else: 
         print("Для outprint не существует такого значения")
      if output == "yes":
         anomalokarisfile = namefile
         anomalokaris = open(anomalokarisfile, mode='a', encoding='utf-8')
         anomalokaris.write(str(genoutprint) + "\n")
      elif output == "no":
         pass
      else:
         print("Для output не существует такого значения")
      return genoutprint
      
def gensteam3(output="no", outprint="no", namefile="genernation.txt"):
    #237ABCDGHJLPRST 23
    keys = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    numbers = "1234567890"
    a1 = random.choice(keys)
    a2 = random.choice(keys)
    a3 = random.choice(keys)
    a4 = random.choice(keys)
    a5 = random.choice(keys)
    a6 = random.choice(keys)
    a7 = random.choice(keys)
    a8 = random.choice(keys)
    a9 = random.choice(keys)
    a10 = random.choice(keys) 
    a11 = random.choice(keys)
    a12 = random.choice(keys)
    a13 = random.choice(keys)
    a14 = random.choice(keys)
    a15 = random.choice(keys)
    two = random.choice(numbers)
    three = random.choice(numbers)
    genoutprint = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a15 + " " + two + three
    if outprint == "yes":
         print(genoutprint)
    elif outprint == "no":
         pass
    else: 
         print("Для outprint не существует такого значения")
    if output == "yes":
         anomalokarisfile = namefile
         anomalokaris = open(anomalokarisfile, mode='a', encoding='utf-8')
         anomalokaris.write(str(genoutprint) + "\n")
    elif output == "no":
         pass
    else:
         print("Для output не существует такого значения")
    return genoutprint     
         
def genpass(length=15, output="no", outprint="no", namefile="genernation.txt", chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    try:
     length = int(length)
     password=''
     for i in range(length):
        password += random.choice(chars)
     if outprint == "yes":
         print(password)
     elif outprint == "no":
         pass
     else: 
         print("Для outprint не существует такого значения")
     if output == "yes":
         anomalokarisfile = namefile
         anomalokaris = open(anomalokarisfile, mode='a', encoding='utf-8')
         anomalokaris.write(str(password) + "\n")
     elif output == "no":
         pass
     else:
         print("Для output не существует такого значения")
    except:
     print("Для значения length могут использоваться только цифры")
    return password 
     
def magicball(predictions=["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется — «да»", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят — «да»", "Да", "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ — «нет»", "По моим данным — «нет»", "Перспективы не очень хорошие", "Весьма сомнительно"], whatpred="no"):
    if whatpred == "yes":
       input("Напиши мне то что я должен предсказать: ")
    else:
       pass
    printpred = random.choice(predictions)
    return printpred
    
