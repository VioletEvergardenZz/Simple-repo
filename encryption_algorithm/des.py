from pyDes import des,PAD_PKCS5,ECB

def des_encrypt(text,key):
    # 加密器实例
    des_cipher=des(key,ECB,padmode=PAD_PKCS5)
    encrypted_text=des_cipher.encrypt(text)
    return encrypted_text

def des_decrypt(encrypted_text,key):
    # 解密器实例
    des_cipher=des(key,ECB,padmode=PAD_PKCS5)
    decrypted_text=des_cipher.decrypt(encrypted_text)  
    # 将解密后的字节序列转换为字符串对象
    return decrypted_text.decode()


if __name__=='__main__':
    while True:
        choose=input('请选择加密或解密: \n1.加密\n2.解密\n3.退出\n')
        if choose=='1':
            text=input('明文: ')
            key=input('密钥: ').strip()  # 去除字符串两端空白，保证长度准确
            if len(key)!=8:
                print("密钥长度必须为8个字符")
                continue
            encrypted_text=des_encrypt(text,key)
            print(f'密文: {encrypted_text.hex()}')
        elif choose=='2':
            text=input('密文: ')
            # 将十六进制字符串转换为字节序列
            encrypted_text=bytes.fromhex(text)
            key=input('密钥: ').strip()
            if len(key)!=8:
                print("密钥长度必须为8个字符")
                continue
            decrypted_text=des_decrypt(encrypted_text,key)
            print(f'明文: {decrypted_text}')
        elif choose=='3':
            break   
        else:
            print("无效的选择，请重新输入。")
