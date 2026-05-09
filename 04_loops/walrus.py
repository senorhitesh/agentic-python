# value  = 10;
# remainder = value % 3;

# if remainder:
#     print(f"The remainder is {remainder}")

# value = 12

# if (remainder := value % 2):
#     print(remainder)

chapters = [304, 180, 130, 75]

if (selected_chapters := int(input("Your Fav Chapters: "))) in chapters:
    print(f"You Got Your Chapter {selected_chapters}")
else:
    print("You Failed")
    