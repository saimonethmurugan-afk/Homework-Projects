
# MY LIBRARY BOOK ORGANISER

# DATA STRUCTURES AND LISTS

books = ["Harry Potter", "Matilda", "Diary of a Wimpy Kid", "Charlie and the Chocolate Factory", "Fantastic Beasts"]

print("Available Book List:", books)


#  LIST OPERATIONS

print("Total Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])

books.append("Quidditch Through The Ages")
print("Updated Available Book List(Update No.579842): ", books)

books.remove("Matilda")
print("Updated Book List(Update No.375982): ", books)

books.sort()
print("Books Sorted Alphabetically:", books)

books.reverse()
print("Books in Reverse Order:", books)


#DICTIONARIES

librarian = {"name": "Mr.Jack","section": "Novels and Comics","experience": 7.8}

print("Librarian Profile:", librarian)


# DICTIONARY OPERATIONS

print("Librarian Name:", librarian["name"])
print("Library Section:", librarian["section"])
print("Experience:", librarian.get("experience"))

librarian["experience"] = 6
print("Updated Experience:", librarian)

librarian["email"] = "mrjack@schoollibrary.com"
print("After Adding Email:", librarian)

librarian.pop("experience")
print("After Removing Experience:", librarian)


# CONVERTING A LIST INTO A DICTIONARY

book_ids = [983,642,525,734,]
book_names = ["Matilda", "Fantastic Beasts", "Harry Potter","Diary of a Wimpy Kid","Charlie and the Chocolate Factory"]

book_directory = dict(zip(book_ids, book_names))

print("Book Directory:", book_directory)


# FINAL SUMMARY

print("================================")
print("LIBRARY ORGANISER SUMMARY")
print("================================")
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)
print("================================")

