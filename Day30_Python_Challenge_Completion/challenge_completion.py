# 30-day Python challenge
print("------ 30-Day Python Challenge 30/30 ------")
print("🎉 Congratulations 🎉")

def get_user_name():
    name = input("Enter your name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return None
    return name

def create_certificate(name):
    message = (
        f"Hello {name},\n\n"
        "Congratulations on successfully completing the 30-Day Python Challenge!\n"
        "Your dedication and consistency have paid off.\n\n"
        "This is not the end — it’s the beginning of a new journey.\n"
        "Keep learning, keep building, and keep growing.\n\n"
        "🚀 New chapters await!"
    )

    with open("congrats.txt", "w", encoding="utf-8") as file:
        file.write(message)

    print("✅ Congratulations file created successfully!")


def main():
    name = get_user_name()
    if name:
        create_certificate(name)

main()
