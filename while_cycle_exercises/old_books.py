name_of_the_searched_book = input()
counter = 0

while True:
    current_book_name = input()

    if current_book_name == name_of_the_searched_book:
        print(f'You checked {counter} books and found it.')
        break

    elif current_book_name == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {counter} books.')
        break

    counter += 1