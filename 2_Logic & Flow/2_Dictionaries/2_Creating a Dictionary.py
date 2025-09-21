def create_book_dict(title, author, year):
    # Write code here
    book_dict = {}

    book_dict["title"] = title
    book_dict["author"] = author
    book_dict["year"] = year

    return book_dict

print(create_book_dict("To kill a Mockingbird", "Harper Lee", 1960))
