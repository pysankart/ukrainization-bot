from abc import ABC, abstractstaticmethod
from googletrans import Translator


class AbstractLanguage(ABC):
    """Abstract language. You can inherit it to create your own logic."""
    translator = Translator()

    @abstractstaticmethod
    def detect(text: str) -> bool:
        """Detect the language."""
        pass 

    @abstractstaticmethod
    def translate(text: str) -> str:
        """Translate to the language."""
        pass 


class LanguageProvider:
    """Provider for languages."""
    langs: list[AbstractLanguage] = []
    dest: AbstractLanguage = None 

    def register_languages(self, *langs: type[AbstractLanguage]) -> None:
        """Register languages."""
        for lang in langs:
            self.langs.append(lang)

    def register_destination(self, dest: AbstractLanguage) -> None:
        """Register destination language."""
        self.dest = dest

    def translate(self, text: str) -> str:
        """Translate to destination language if text in forbidden language or return this text."""
        for lang in self.langs:
            if lang.detect(text):
                return self.dest.translate(text)
        return text


class RussianLanguage(AbstractLanguage):
    """Russian language class."""
    language = "ru"

    def detect(text: str) -> bool:
        """Detect if text language is Russian."""
        return RussianLanguage.translator.detect(text).lang == RussianLanguage.language

    def translate(text: str) -> str:
        """Translate text to russian language."""
        return RussianLanguage.translator.translate(text, dest=RussianLanguage.language).text


class UkrainianLanguage(AbstractLanguage):
    """Ukrainina language class."""
    language = "uk"

    def detect(text: str) -> bool:
        """Detect if text language is Ukrainian."""
        return UkrainianLanguage.translator.detect(text).lang == UkrainianLanguage.language

    def translate(text: str) -> str:
        """Translate text to ukrainian language."""
        return UkrainianLanguage.translator.translate(text, dest=UkrainianLanguage.language).text
