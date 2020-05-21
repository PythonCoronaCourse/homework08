def print_book_details(title, author, **kwargs):
    dict_book = {title: title, author: author}
#    print("title: " + title)
#    print("author: " + author)
    price = kwargs.get("price")
    genre = kwargs.get("genre")
#    if price:
#        print("price: ", price)
#    if genre:
#        print("genre: ", genre)
    if genre:
            if price:
                print("title:", title, "; author:", author, "; price:", price, "; genre:", genre)
            else:
                print("title:", title, "; author:", author, "; genre:", genre)
    else:
        print("title:", title, "; author:", author)
    return


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
title: Bible; author: Jeff Bezos; genre: autobiography;
title: Kill people, get money; author: Jeff Bezos; price: 20.00, genre: guide;
title: Jak rozjechać babę na pasach i nie ponieść żadnych konsekwencji, author: Tomasz Hajto;
"""
