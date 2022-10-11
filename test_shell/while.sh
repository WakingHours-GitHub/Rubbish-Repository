#!D:\A_Toos\Git\bin\bash
#案例1: 从命令行输入一个数n, 统计从1+...+n
SUM=0
i=0
while [ $i -le $1 ]
do
    SUM=$[$SUM+$i]
    #i自增
    i=$[$i+1]
done
echo "sum = $SUM"
