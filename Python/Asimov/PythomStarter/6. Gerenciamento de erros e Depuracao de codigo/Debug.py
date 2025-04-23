try: 'teste execução'
except: 'caso teste falhe segue outro caminho'
#except Exception as e: 'variavel except'
finally: 'executa ignorando o erro'

import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG) # vide apostila pdf
log = logging.getLogger()




