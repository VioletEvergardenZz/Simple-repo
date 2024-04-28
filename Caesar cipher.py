def encryption(str,k):
    result = ""
    for i in range(len(str)):
        if str[i].isupper():
            result += chr((ord(str[i]) + k-65) % 26 + 65)
        else:
            result += chr((ord(str[i]) + k - 97) % 26 + 97)
    return result
 
def decryption(str,k):
    result = ""
    for i in range(len(str)):
        if str[i].isupper():
            result += chr((ord(str[i]) - k - 65) % 26 + 65)
        else:
            result += chr((ord(str[i]) - k - 97) % 26 + 97)
    return result
 
if __name__ == '__main__':
    while True:
        choice = input("请选择加密或解密：\n1.加密\n2.解密\n3.退出\n")
        if choice == '1':
            str = input("请输入需要加密的字符串：")
            k = int(input("请输入加密密钥："))
            print("加密后的字符串为：", encryption(str,k),"\n")
        elif choice == '2':
            str = input("请输入需要解密的字符串：")
            k = int(input("请输入解密密钥："))
            print("解密后的字符串为：", decryption(str,k),"\n")
        elif choice == '3':
            break