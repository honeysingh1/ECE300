
%proj3.m
% altered to include error
%
I = sqrt(-1);
%in0 = input('Enter ACTUAL IMAGE:... ');
%in0=imread('lena.jpg'); in0=double(in0);
in0=letter_g;
N = length(in0);
M = 2*N;
in0l = zeros(M,M);
x = -M/2:1:M/2-1;
y = x;
[X,Y] = meshgrid(x,y); 
R = sqrt(X.^2+Y.^2);
filter = cyl(R/N);
filter=zeros(M,M);
filter(M/2+1 - N/2:M/2+N/2,M/2+1 - N/2:M/2+N/2) = ones(N,N);
%keyboard

in0l(M/2+1 - N/2:M/2+N/2,M/2+1 - N/2:M/2+N/2) = in0;
figure(1)
imagesc ( in0l );colormap gray

in1 = abs(fftshift(fft2(fftshift(in0l))));
%in12 = zeros(M,M);
%inl2(M/2 - N/2:M/2+N/2-1,M/2 - N/2:M/2+N/2-1) = in1;

rect = zeros(M,M);
rect(M/2 - M/4:M/2 + M/4 - 1,M/2 - M/4:M/2 + M/4 - 1) = ones(M/2,M/2); % 72:181, 72::
Ao = in1;
a = cos(2*pi*rand(M,M));	
a = a.*filter;

iter = 1;
maxiter=3000;
while(iter < maxiter)
%iter
a1 = a;
A = fftshift(fft2(fftshift(a)));
PHASE = angle(A);
A = Ao.*exp(I*PHASE);
a = (fftshift(ifft2(fftshift(A)))); %P2
%P1P2 = a;

a = abs(a).*filter; % P1P2
%P1P2 = a;
%err = sum(sum(sqrt(abs(abs(a) - abs(al)))))/sum(sum(abs(a))) 
err = abs((sum(sum(abs(a1-a).^2))/(sum(sum(abs(Ao).^2))))) 
E(iter) = err;
iter = iter + 1;
figure(2)
imagesc ( abs (a) );colormap gray
pause( .001)
end

