def print_book_details():
    pass

print_book_details(title="Bible", author="Jeff Bezos", genre="autobiography")
print_book_details(
    price=20.0, title="Kill people, get money",
    genre="guide", author="Jeff Bezos"
)
print_book_details(
    "Jak rozjechać babę na pasach i nie ponieść żadnych konsekwencji",
    author="Tomasz Hajto"
)


"""
oczekiwany output:
title: Bible; author: Jeff Bezos; genre: autobiography
title: Kill people, get money; author: Jeff Bezos; price: 20.00, genre: guide
title: Jak rozjechać babę na pasach i nie ponieść żadnych konsekwencji, author: Tomasz Hajto
"""
