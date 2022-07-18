from google.cloud import translate_v2
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"google_api_key.json"

def translate_text(text, target_language):
    tranlate_client = translate_v2.Client()
    translation = tranlate_client.translate(text, target_language)
    return translation["translatedText"]
    
#print(translate_text("testing testing", "es"))