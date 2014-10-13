% downloading data with matlab
conn = yahoo; %connect to Yahoo
name='IBM';
begindate='2-january-2014';
enddate='14-may-2014';
data1 =fetch(conn,name,{'High','Low','Close'},begindate,enddate);% downloading data with matlab
dataq1=data1(:,4); % closing prices
plot(dataq1)

