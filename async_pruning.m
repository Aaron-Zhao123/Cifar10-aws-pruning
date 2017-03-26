% prue_percent = [0,10,20,30,40,50,60,70,80,90];
% accs = [0.82350004,0.82270002,0.83240008,0.83420008,0.83220005,0.83060002,0.82890004,0.82850003,0.82460004,0.80690002];
% plot(prue_percent, accs);


layer_size = [0.5, 25, 400, 5];
prune_percent = [0.01, 0.008, 0.006, 0.005, 0.004, 0.001] * 400 + 5.5 + 25*0.2;
accs = [0.99360, 0.99240, 0.99360, 0.99360, 0.99240, 0.98190];
plot(prune_percent, accs);
