from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.length = len(foods)

        self.cuisine_food = {}
        for i in range(self.length):
            self.cuisine_food[cuisines[i]] = []

        for i in range(self.length):
            self.cuisine_food[cuisines[i]].append({
                'food': foods[i],
                'rating': ratings[i]
            })

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = ''
        for i in range(self.length):
            if self.foods[i] == food:
                cuisine = self.cuisines[i]
                break

        for each_food in self.cuisine_food[cuisine]:
            if each_food['food'] == food:
                each_food['rating'] = newRating
                break

        return

    def highestRated(self, cuisine: str) -> str:
        max_rating = 0
        max_food = ''

        for each_food in self.cuisine_food[cuisine]:
            if each_food['rating'] > max_rating:
                max_rating = each_food['rating']
                max_food = each_food['food']
            elif each_food['rating'] == max_rating:
                max_food = min(each_food['food'], max_food)

        return max_food


# Your FoodRatings object will be instantiated and called as such:
funcs = ["FoodRatings","changeRating","highestRated","highestRated","highestRated"]
values = [[["cpctxzh","bryvgjqmj","wedqhqrmyc","ee","lafzximxh","lojzxfel","flhs"],
           ["wbhdgqphq","wbhdgqphq","mxxajogm","wbhdgqphq","wbhdgqphq","mxxajogm","mxxajogm"],
           [15,5,7,16,16,10,13]],
          ["lojzxfel",1],["mxxajogm"],["wbhdgqphq"],["mxxajogm"]]

foods = values[0][0]
cuisines = values[0][1]
ratings = values[0][2]

obj = FoodRatings(foods, cuisines, ratings)
results = [None]

for i in range(1, len(funcs)):
    if funcs[i] == 'highestRated':
        results.append(obj.highestRated(values[i][0]))
    else:
        results.append(obj.changeRating(values[i][0], values[i][1]))

print(results)
