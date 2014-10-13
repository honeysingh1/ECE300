WINDOW = 10;
%data = [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5]
weightings= (10:-1:1)
sumofweight = 55;
weightavg = weightings./sumofweight
y=conv(dataq1, weightavg,'valid')
plot(y)
title('Weighted Moving Average')