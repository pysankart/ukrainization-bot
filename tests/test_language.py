import pytest

from bot.languages.core import UkrainianLanguage, RussianLanguage


class BaseLanguageTest:
    @property
    def language(self):
        raise NotImplementedError

    SOURCE_WORDS = []
    TARGET_WORDS = []

    def setup_method(self):
        self.TEST_VECTORS = list(zip(self.SOURCE_WORDS, self.TARGET_WORDS))

    @pytest.mark.asyncio
    async def test_traslate(self):
        for vector in self.TEST_VECTORS:
            source_text = vector[0]
            target_text = vector[1]

            translated_text = await self.language.translate(source_text)
            assert translated_text == target_text

    @pytest.mark.asyncio
    async def test_detect(self):
        for word in self.TARGET_WORDS:
            assert await self.language.detect(word) is True


class TestUkrainianLanguage(BaseLanguageTest):
    language = UkrainianLanguage()
    SOURCE_WORDS = ['тетрадь', 'цветок', 'пирог']
    TARGET_WORDS = ['зошит', 'квітка', 'пиріг']


class TestRussianLanguage(BaseLanguageTest):
    language = RussianLanguage()
    SOURCE_WORDS = ['horse', 'door', 'brain']
    TARGET_WORDS = ['лошадь', 'дверь', 'мозг']
