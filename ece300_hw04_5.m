% Honey Singh
% Question 5
p1 = [1;1];
t1 = 1;
p2 = [1;-1];
t2 = -1;

w1 = [-1:0.1:1];
w2 = [-1:0.1:1];

[w1,w2] =meshgrid(w1,w2);

f = (t1-w1-w2).^2 + (t2-w1+w2).^2
surf(w1,w2,f)