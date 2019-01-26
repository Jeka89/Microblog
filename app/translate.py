import json
import requests
from flask import current_app

def translate(text, source_language, dest_language):
  if 'MULTILLECT_ACCOUNT_ID' not in current_app.config or not current_app.config['MULTILLECT_ACCOUNT_ID'] or\
    'MULTILLECT_SECRET_KEY' not in current_app.config or not current_app.config['MULTILLECT_SECRET_KEY'] or\
    'MULTILLECT_URL' not in current_app.config or not current_app.config['MULTILLECT_URL']:
      return ('Error: the translation service is not configured.')

  multisellect_url = current_app.config['MULTILLECT_URL']
  multisellect_secret_key = current_app.config['MULTILLECT_SECRET_KEY']
  multisellect_account_id = current_app.config['MULTILLECT_ACCOUNT_ID']

  r = requests.get('{}{}?method=translate/api/translate&from={}&to={}&text={}&sig={}'.format(\
    multisellect_url, multisellect_account_id, source_language, dest_language, text, multisellect_secret_key))
  if r.status_code != 200:
      return ('Error: the translation service failed.')
  return json.loads(r.content.decode('utf-8-sig'))['result']['translated']