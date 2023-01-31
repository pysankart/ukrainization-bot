from .core import Language


class LanguageProvider:
    """
    Provider for languages.
    """

    def __init__(self, languages: list[Language], destination: Language):
        self.languages = languages
        self.destination = destination

    async def traslate(self, text: str) -> str:
        """
        Translate to destination language if text in forbidden language or return this text.
        """
        for language in self.languages:
            if await language.detect(text):
                return await self.destination.translate(text)
        return text
