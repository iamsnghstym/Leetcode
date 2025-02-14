from collections import deque
from typing import List

class Pair:
    def __init__(self, word, transformations):
        self.word = word
        self.transformations = transformations

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque()
        visited = set()
        visited.add(beginWord)
        q.append(Pair(beginWord, 1))

        while q:
            pair = q.popleft()
            word, transformations = pair.word, pair.transformations
            if word == endWord:
                return transformations

            neighbours = self.getNeighbours(word)
            for neigh in neighbours:
                if neigh not in visited and neigh in wordSet:
                    visited.add(neigh)
                    q.append(Pair(neigh, transformations+1))

        return 0
    def getNeighbours(self, startWord: str) -> List[str]:
        neighbours = []
        for i in range(len(startWord)):
            for alphabet in "abcdefghijklmnopqrstuvwxyz":
                newWord = startWord[:i] + alphabet + startWord[i+1:]
                neighbours.append(newWord)
        return neighbours
