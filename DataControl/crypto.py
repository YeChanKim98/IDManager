from cryptography.fernet import Fernet

key = b'_cG8iyvDR5hhAOC0GE-fW_XswIn2kRAda0S8Y_p2_gc='

def encrypto(data) :
    data = bytes(data,'utf-8')
    fernet = Fernet(key)
    encrypt_str = fernet.encrypt(data)
    return encrypt_str


def decrypto(data) :
    data = bytes(data,'utf-8')
    fernet = Fernet(key)
    decrypt_str = fernet.decrypt(data)
    return decrypt_str

# Cryption 함수 하나로 통일 후 데이터와 같이 온 값이 'de'이면 복호화, 디폴트값은 암호화
# 변수에 따른 동작 변경 -> 코드 간소화