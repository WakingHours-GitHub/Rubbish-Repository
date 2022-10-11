#!D:\A_Toos\Git\bin\bash
#案例1: 打印命令行输入的参数,
for i in "$*"
do
    echo "num is $i"
done


#使用$@, 来获取输入的参数, 注意, 此时是分别对待,
#所以有几个参数, 就输出几句
echo "========================"
for j in "$@"
do
    echo "\$@ form, num is $j"
done