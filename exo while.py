print('veuillez saisir le mot de passe')
password=input()
while password!="admin":
    print('incorrect,reessayer')
    password=input()
    if password=="admin":
        print('Acces autoriser')