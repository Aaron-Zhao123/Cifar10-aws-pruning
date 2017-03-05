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
pcov = [0., 0.]
pfc = [0., 0., 0.]
retrain = 0
keys_cov = ['cov1', 'cov2']
keys_fc = ['fc1', 'fc2', 'fc3']
name = ''
for key in keys_cov:
    name += key + str(int(0*10))
for key in keys_fc:
    name += key + str(int(0*10))
f_name = name
# initial run
param = [
    ('-pcov1',pcov[0]),
    ('-pcov2',pcov[1]),
    ('-pfc1',pfc[0]),
    ('-pfc2',pfc[1]),
    ('-pfc3',pfc[2]),
    ('-first_time', True),
    ('-file_name', f_name),
    ('-train', True),
    ('-prune', False)
    ]
acc = train.main(param)
param = [
    ('-pcov1',pcov[0]),
    ('-pcov2',pcov[1]),
    ('-pfc1',pfc[0]),
    ('-pfc2',pfc[1]),
    ('-pfc3',pfc[2]),
    ('-first_time', False),
    ('-file_name', f_name),
    ('-train', False),
    ('-prune', False)
    ]
test_acc = train.main(param)
print("first train")
acc_list.append(test_acc)

while (run):
    pcov = [0., 0.]
    pfc = [10., 0., 0.]
    # Prune
    param = [
        ('-pcov1',pcov1),
        ('-pcov2',pcov2),
        ('-pfc1',pfc1),
        ('-pfc2',pfc2),
        ('-pfc3',pfc3),
        ('-first_time', False),
        ('-file_name', f_name),
        ('-train', False),
        ('-prune', True)
        ]
    _ = train.main(param)

    # TRAIN
    param = [
        ('-pcov1',pcov1),
        ('-pcov2',pcov2),
        ('-pfc1',pfc1),
        ('-pfc2',pfc2),
        ('-pfc3',pfc3),
        ('-first_time', False),
        ('-file_name', f_name),
        ('-train', True),
        ('-prune', False)
        ]
    _ = train.main(param)

    # TEST

    param = [
        ('-pcov1',pcov1),
        ('-pcov2',pcov2),
        ('-pfc1',pfc1),
        ('-pfc2',pfc2),
        ('-pfc3',pfc3),
        ('-first_time', False),
        ('-file_name', f_name),
        ('-train', False),
        ('-prune', False)
        ]

    run = 0
    acc = train.main(param)
    pcov = pcov+10
    pfc = pfc+10
    acc_list.append(acc)
    retrain = 0
    count = count + 1
    print (acc)

print('accuracy summary: {}'.format(acc_list))
# acc_list = [0.82349998, 0.8233, 0.82319999, 0.81870002, 0.82050002, 0.80400002, 0.74940002, 0.66060001, 0.5011]
with open("acc_cifar.txt", "w") as f:
    for item in acc_list:
        f.write("%s\n"%item)
