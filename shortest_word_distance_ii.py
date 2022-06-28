# MEDIUM
#
# This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your
# method will be called repeatedly many times with different parameters. How would you optimize it?
#
# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1
# and word2 and return the shortest distance between these two words in the list.
#
# For example, Assume that words = [“practice”, “makes”, “perfect”, “coding”, “makes”].
#
# Given word1 = “coding”, word2 = “practice”, return 3. Given word1 = “makes”, word2 = “coding”, return 1.
#
# Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

from typing import List


class WordDistance:
    def __init__(self, words: List[str]):
        self.words = {}
        for i in range(len(words)):
            self.words[words[i]] = self.words.get(words[i], [])
            self.words[words[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        dist = float("inf")

        for idx1 in self.words.get(word1):
            for idx2 in self.words.get(word2):
                dist = min(dist, abs(idx2 - idx1))

        return dist


if __name__ == "__main__":
    wd1 = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(wd1.shortest("coding", "practice"))
    wd2 = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(wd2.shortest("makes", "coding"))
