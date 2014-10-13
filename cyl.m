function y=cyl(r)
% cylinder function
[n1,n2]=size(r);
for i=1:n1
    for j=1:n2
        rt=r(i,j);
        if rt <=1
            y(i,j)=1;
            elsey(i,j)=0;
        end
    end
end