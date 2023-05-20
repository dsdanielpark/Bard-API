from googletrans import Translator
from googletrans.constants import LANGUAGES

def translate(text: str, translate_to: str):
    """
    Translates the given text using the Google translation engine.

    :param text: The text to translate.
    :type text: str
    :param translate_to: The language to translate to.
    :type translate_to: str
    :return: The translated text.
    :rtype: str
    """
    translator = Translator()
    try:
        return translator.translate(text, dest=translate_to).text
    except ValueError:
        possible_languages = [lang for lang in LANGUAGES.values() if lang[0] == translate_to[0]] or [lang for lang in LANGUAGES.keys() if lang[0] == translate_to[0]]
        if possible_languages:
            suggestion = ', '.join(possible_languages)
            print(f"No translation available for the requested language. Did you mean any of these languages? {suggestion}")
        else:
            print("No translation available for the requested language.")
