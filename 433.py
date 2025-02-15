from collections import deque
from typing import List

class Pair:
    def __init__(self, word, mutations):
        self.word = word
        self.mutations = mutations

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        wordSet = set(bank)
        q = deque()
        visited = set()
        visited.add(startGene)
        q.append(Pair(startGene, 0))

        while q:
            pair = q.popleft()
            word, mutations = pair.word, pair.mutations
            if word == endGene:
                return mutations

            neighbours = self.getNeighbours(word)
            print("neighbours - ", neighbours)
            for neigh in neighbours:
                if neigh not in visited and neigh in wordSet:
                    visited.add(neigh)
                    q.append(Pair(neigh, mutations+1))

        return -1

    def getNeighbours(self, startGene: str) -> List[str]:
        neighbours = []
        for i in range(len(startGene)):
            for alphabet in "ACGT":
                newWord = startGene[:i] + alphabet + startGene[i+1:]
                neighbours.append(newWord)
        return neighbours
