from gpytranslate import Translator


class Language:
    """
    Common logic for language objects.
    """
    translator = Translator()

    @property
    def language(self):
        raise NotImplementedError

    async def detect(self, text: str) -> bool:
        detected_language = await self.translator.detect(text)
        return detected_language == self.language

    async def translate(self, text: str) -> str:
        translation = await self.translator.translate(text, targetlang=self.language)
        return translation.text


class RussianLanguage(Language):
    """
    Russian language.
    """
    language = 'ru'


class UkrainianLanguage(Language):
    """
    Ukrainian language.
    """
    language = 'uk'
