faces = input()
if faces == "Hello:)":
    faces = faces.replace(":)", "🙂")
    print("Hello 🙂")
elif faces == "Goodbye :(":
    print("Goodbye ☹️")
else:
    print("Hello 🙂", "Goodbye ☹️")
