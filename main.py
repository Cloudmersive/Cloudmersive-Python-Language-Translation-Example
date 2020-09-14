from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR-API-KEY-HERE'



# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.LanguageTranslationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
input = cloudmersive_nlp_api_client.LanguageTranslationRequest() # LanguageTranslationRequest | Input translation request
input.text_to_translate = "Am Morgen war Armin Laschet in seiner Heimatstadt Aachen wählen gegangen."

try:
    # Translate German to English text with Deep Learning AI
    api_response = api_instance.language_translation_translate_deu_to_eng(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageTranslationApi->language_translation_translate_deu_to_eng: %s\n" % e)