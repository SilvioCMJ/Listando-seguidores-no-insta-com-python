from datetime import datetime
import instaloader

#fazendo login
l = instaloader.Instaloader()
l.login('teu user no insta', 'tua senha')

#carregando dados
followers = instaloader.Profile.from_username(l.context, 'teu insta sem @').get_followers()
followees = instaloader.Profile.from_username(l.context, 'teu insta sem @').get_followees()

#resultados
print('\n')
print('Seguidores: '+ str(followers._data['count']))
print('Seguindo: '+ str(followees._data['count']))
print('\n\n')
print('lista e  informacoes de seguidores:')
print('\n')
print(followers._data['edges'])