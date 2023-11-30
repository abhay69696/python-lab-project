mse1=input('enter mse1 marks')
mse2=input('enter mse2 marks')
internal=input('enter internal  marks') 
cgpa=input('enter req cgpa')
CGPA=int(cgpa)
tot=int(mse1)+int(mse2)+int(internal)
if(tot<=50):

    see=(CGPA*10)-(tot)
    if(see<=50):
       print('req marks ins SEE=',see)
    else:
        print('not possible to get desired cgpa')

else:
    print("internal marks not entered correctly")