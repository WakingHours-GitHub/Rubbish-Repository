#!D:\A_Toos\Git\bin\bash # 指定解释器
# 案例1: 当命令行参数是1时, 输出"周一", 是2则输出"周二", 其他情况就输出"other"
case $1 in 
"1")
echo "周一"
;;
"2")
echo "周二"
;;
*)
echo "其他"
;;



esac