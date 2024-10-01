def greet_user(name, title=""):
    return f"Hello, {title} {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_title = input("Enter your title (Mr./Ms./etc.): ")
    print(greet_user(user_name, user_title))
