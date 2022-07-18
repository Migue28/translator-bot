from urllib import request, response
from google.cloud import translate

def translate_text(text='', project_id=''):
    client = translate.TranslationServiceClient()
    location = 'global'
    parent = f"project/{project_id}/locations/{location}"

    response = client.translate_text(
        request = {
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_languaje_code":"en-US",
            "target_language_code": "es",
        }
    )

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))