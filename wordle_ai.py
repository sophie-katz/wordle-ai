from typing import List, Union, Optional
import itertools
import functools
import pandas as pd

WORD_LENGTH = 5

class WordSet(object):
    def __init__(self, *args: Union[List[str], str]) -> None:
        self.words = set(itertools.chain(*args))

        assert not any([len(i) != WORD_LENGTH for i in self.words])

    @functools.cached_property
    def letter_frequency(self) -> pd.DataFrame:
        data = {}

        for word in self.words:
            for letter in word:
                if letter in data:
                    data[letter] += 1
                else:
                    data[letter] = 1
        
        df = pd.DataFrame([{"letter": key, "count": value} for key, value in data.items()]) \
            .sort_values("count", ascending = False)
        
        df["frequency"] = df["count"] / df["count"].max()

        return df
    
    def word_matches_mask(self, word: str, mask: List[Optional[str]]) -> bool:
        assert len(mask) == WORD_LENGTH
        assert not any([len(i) != 1 for i in mask if i is not None])

        for i in range(WORD_LENGTH):
            if mask[i] is None:
                continue
            elif mask[i] != word[i]:
                return False
        
        return True

    def get_words_by_letter_frequency_sum(self, mask: List[Optional[str]] = [None, None, None, None, None]) -> pd.DataFrame:
        data = []

        for word in self.words:
            if self.word_matches_mask(word, mask):
                frequency_sum = self.letter_frequency.loc[self.letter_frequency["letter"].isin(list(word))]["frequency"].sum()
                data.append({"word": word, "frequency_sum": frequency_sum})
        
        df = pd.DataFrame(data) \
            .sort_values("frequency_sum", ascending = False)
        
        return df
