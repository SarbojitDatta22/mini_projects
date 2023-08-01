import random

def generate_random_story():
    # Lists of story elements
    characters = ["Alice", "Bob", "Charlie", "Eve", "Grace", "Harry", "Isabella", "Jack", "Lily", "Max"]
    settings = ["in a magical forest", "on a deserted island", "in a futuristic city", "in a small village", "on a distant planet"]
    conflicts = ["searching for a hidden treasure", "solving a mysterious riddle", "fighting against an evil sorcerer", "surviving a dangerous journey"]
    resolutions = ["and they lived happily ever after.", "and they became best friends.", "and they discovered the true meaning of friendship."]

    # Generate a random story
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    resolution = random.choice(resolutions)

    story = f"Once upon a time, there was a brave adventurer named {character}. "
    story += f"They found themselves {setting}, where they encountered a great challenge of {conflict}. "
    story += f"After facing many obstacles, {character} successfully completed the challenge, "
    story += resolution

    return story

def main():
    num_stories = 3  # You can change the number of stories to generate

    print("Random Stories\n")
    for i in range(num_stories):
        story = generate_random_story()
        print(f"Story {i+1}:")
        print(story)
        print("\n")

if __name__ == "__main__":
    main()
