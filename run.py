import os
import train
# os.system('python training_v3.py -p0')
# os.system('python training_v3.py -p1')
# os.system('python training_v3.py -p2')
# os.system('python training_v3.py -p3')
# os.system('python training_v3.py -p4')
# os.system('python training_v3.py -p4')
# os.system('python training_v3.py -p5')

acc_list = []
count = 0
while (count < 10):
    param = [
        ('-p',count)]
    acc = train.main(param)
    print (acc)
    acc_list.append(acc)
    count = count + 1
print('accuracy summary: {}'.format(acc_list))
