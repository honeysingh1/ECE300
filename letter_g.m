function letter_g=letter_g
xi=zeros(64,64);
iny1=10:50;
iny2=10:18;
iny3=18:54;
iny4=46:54;
iny5=28:46;
inx1=10:18;
inx2=18:54;
inx3=47:54;
inx4=30:46;
inx5=30:38;
xi(inx1,iny1)=1; % no 1
xi(inx2,iny2)=1; % no 2
xi(inx3,iny3)=1; % no 3
xi(inx4,iny4)=1; % no 4
xi(inx5,iny5)=1; % no 5
%inxi=65-(1:64);
letter_g=xi;







