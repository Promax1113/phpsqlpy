import random

def storyName(name):
    story = ["happy", "sad", "excited", "tired", "angry", "hungry", "brave", "calm", "charming", "clever", "cool", "courageous", "creative", "determined", "elegant", "energetic", "enthusiastic", "friendly", "funny", "generous", "gentle", "glorious", "good", "great", "handsome", "honest", "humorous", "important", "interesting", "kind", "loving", "lucky", "nice", "optimistic", "proud", "relaxed", "reliable", "sincere", "smart", "successful", "thoughtful", "understanding", "vibrant", "warm", "witty", "wonderful", "zealous"]
    return story[random.randint(1, len(story))].capitalize() + " " + name

print(storyName("Gerald"))
