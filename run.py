import os
import train
# os.system('python training_v3.py -p0')
# os.system('python training_v3.py -p1')
# os.system('python training_v3.py -p2')
# os.system('python training_v3.py -p3')
# os.system('python training_v3.py -p4')
# os.system('python training_v3.py -p4')
# os.system('python training_v3.py -p5')
def compute_file_name(pcov, pfc):
    name += 'cov' + str(int(pcov[0] * 10))
    name += 'cov' + str(int(pcov[1] * 10))
    name += 'fc' + str(int(pfc[0] * 10))
    name += 'fc' + str(int(pfc[1] * 10))
    name += 'fc' + str(int(pfc[2] * 10))
    return name
    
acc_list = []
count = 0
pcov = [0., 0.]
pfc = [0., 0., 0.]
retrain = 0
keys_cov = ['cov1', 'cov2']
keys_fc = ['fc1', 'fc2', 'fc3']
name = ''
for key in keys_cov:
    name += 'cov' + str(int(0))
for key in keys_fc:
    name += 'fc' + str(int(0))
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

run = 1

level1 = 1
level2 = 2
level3 = 3
working_level = level1
hist = [(pcov, pfc, test_acc)]
pcov = [10., 10.]
pfc = [10., 10., 10.]
while (run):
    # Prune
    param = [
        ('-pcov1',pcov[0]),
        ('-pcov2',pcov[1]),
        ('-pfc1',pfc[0]),
        ('-pfc2',pfc[1]),
        ('-pfc3',pfc[2]),
        ('-first_time', False),
        ('-file_name', f_name),
        ('-train', False),
        ('-prune', True)
        ]
    _ = train.main(param)
    # pruning saves the new models, masks
    f_name = compute_file_name(pcov, pfc)

    # TRAIN
    param = [
        ('-pcov1',pcov[0]),
        ('-pcov2',pcov[1]),
        ('-pfc1',pfc[0]),
        ('-pfc2',pfc[1]),
        ('-pfc3',pfc[2]),
        ('-first_time', False),
        ('-file_name', f_name),
        ('-train', True),
        ('-prune', False)
        ]
    _ = train.main(param)

    # TEST

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
    acc = train.main(param)
    hist.append((pcov, pfc, acc))
    if (working_level == level1):
        if (acc >= 0.8):
            f_name = compute_file_name(pcov, pfc)
            pcov = pcov + [10., 10.]
            pfc =  pfc +[10., 10., 10.]
        else:
            pcov = pcov - [10., 10.]
            pfc =  pfc -[10., 10., 10.]
            f_name = compute_file_name(pcov, pfc)
            pcov = pcov + [1., 1.]
            pfc =  pfc +[1., 1., 1.]
            working_level = level2
    if (working_level == level2):
        if (acc >= 0.8):
            f_name = compute_file_name(pcov, pfc)
            pcov = pcov + [1., 1.]
            pfc =  pfc +[1., 1., 1.]
        else:
            pcov = pcov - [1., 1.]
            pfc =  pfc -[1., 1., 1.]
            f_name = compute_file_name(pcov, pfc)
            pcov = pcov + [0.1, 0.1]
            pfc =  pfc +[0.1, 0.1, 0.1]
            working_level = level3
    if (working_level == level3):
        if (acc >= 0.8):
            f_name = compute_file_name(pcov, pfc)
            pcov = pcov + [0.1, 0.1]
            pfc =  pfc +[0.1, 0.1, 0.1]
        else:
            run = 0
            print('finished')



    acc_list.append(acc)
    count = count + 1
    print (acc)

print('accuracy summary: {}'.format(acc_list))
# acc_list = [0.82349998, 0.8233, 0.82319999, 0.81870002, 0.82050002, 0.80400002, 0.74940002, 0.66060001, 0.5011]
with open("acc_cifar.txt", "w") as f:
    for item in acc_list:
        f.write("%s\n"%item)
