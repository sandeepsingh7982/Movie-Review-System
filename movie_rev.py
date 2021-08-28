#created on 25 april 2021
#@ author- Sandeep Singh

positive=['finest','great','perfect','amazing','awesome',
          'good','absolute','brilliant','best','gem','wonderfull']
negative=['bad','wrost','greedy','overacting','unnecessary','lame',
          'average','cheap','stupid','unrealistic','disappointment']
un_s=['\n',',','%','.','?','!','(',')','-',';',"'"]
print('----------MOVIE NAME= GOLD------------\n')
with open('label.txt','w',encoding='utf-8') as f2:
    f2.write('FILE NAME'+'\t')
    f2.write('REVIEW'+'\t\t\t\t')
    f2.write('PATH'+'\n')
    import os
    path=os.getcwd()
    for i in range(1,11):
        with open(str(i)+'.txt',encoding='UTF-8') as f1:
            rew=str(i)+'.txt'
            print('FILE NAME=',rew,'\n')
            f2.write(rew+'\t\t')
            psum=0
            nsum=0
            l=[]
            for line in f1:
                for i in un_s:
                    line=line.replace(i,'')
                line1=line.split(' ')
                print(line1)
                for word in line1:
                    for j in positive:
                        if word.lower()==j:
                             psum=psum+1
                    for k in negative:
                        if word.lower()==k:
                            nsum=nsum+1
                            
            print('POSITIVE=',psum)
            print('NEGATIVE=',nsum)
               
            if psum>nsum:
                print('\nGOOD REVIEW\n')
                f2.write('good review'+'\t\t')
                f2.write(path+'\n')
            elif psum<nsum:
                print('\nBAD REVIEW\n')
                f2.write('bad review'+'\t\t')
                f2.write(path+'\n')
            elif psum==nsum:
                print("\nNUETRAL REVIEW\n")
                f2.write('nuetral review'+'\t\t')
                f2.write(path+'\n')


with open('label.txt',encoding='utf-8') as f:
    l=[]
    un_s=['C',':','\t']
    for line in f:
        print(line)
        b=line[7:21]
        for i in un_s:
            b=b.replace(i,'')
        l.append(b)      
    a_=l.count('good review')
    b_=l.count('bad review')
    print('\nTOTAL GOOD REVIEW=',a_)
    print('\nTOTAL BAD REVIEW=',b_)
    if l.count('good review')>l.count('bad review'):
        print('\n\n--------------MOVIE IS AWESOME--------------')
    if l.count('good review')<l.count('bad review'):
        print('\n\n---------MOVIE IS FLOP---------')
    
    


            
            
      
            
                        
                
