#!D:\A_Toos\Git\bin\bash
#案例, 使用for实现1累加到100, 并输出变量

SUM=0
for ((i=1; i<=$1; i++))
do
    #业务代码
    SUM=$[$SUM+$i]
done
echo "$SUM"