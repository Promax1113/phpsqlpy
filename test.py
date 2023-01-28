import randint


def create_story_name(name):
    story = ["mighty", "desperate", "giant"]


    return story[random.randint(0, story.len())] + name

print(create_story_name(Albert))