import hashlib
import uuid
 
def hash_password(password): 
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Şifreni gir : ')
hashed_password = hash_password(new_pass)
print('Şifrenin SHA256 ile hashlenmiş hali: ' + hashed_password)
old_pass = input('Tekrar şifreni gir: ')
if check_password(hashed_password, old_pass):
    print('Terikler Şifre Doğru!')
else:
    print('Hata Şifre Yanlış!')
