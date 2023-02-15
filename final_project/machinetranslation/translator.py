import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']
VERSION = os.environ['version']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(URL)


def english_to_french(english_text):
    """Translate English to French."""
    if english_text is None:
        return ""
    translation_response = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = translation_response['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """Translate French to English."""
    if french_text is None:
        return ""
    translation_response = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = translation_response['translations'][0]['translation']
    return english_text
