class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._royalty = 0.0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            self._royalty = 0.10 * self._price * copies_sold
        elif copies_sold <= 1500:
            self._royalty = (0.10 * self._price * 500) + (0.125 * self._price * (copies_sold - 500))
        else:
            self._royalty = (0.10 * self._price * 500) + (0.125 * self._price * 1000) + (0.15 * self._price * (copies_sold - 1500))
        return self._royalty

    def __str__(self):
        return f"Book(title='{self._title}', author='{self._author}', publisher='{self._publisher}', price={self._price})"


class Ebook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self._ebook_format = ebook_format

    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, value):
        self._ebook_format = value

    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        gst_deduction = 0.12 * base_royalty
        return base_royalty - gst_deduction

    def __str__(self):
        return f"Ebook(title='{self._title}', author='{self._author}', publisher='{self._publisher}', price={self._price}, format='{self._ebook_format}')"

if __name__ == "__main__":
    # Create book instance
    physical_book = Book("OOP Principles", "John Doe", "TechBooks Inc.", 500)
    print(physical_book)
    print("Royalty for 2000 copies (Physical Book):", physical_book.royalty(2000))

    # Create ebook instance
    digital_book = Ebook("OOP Principles", "John Doe", "TechBooks Inc.", 500, "PDF")
    print(digital_book)
    print("Royalty for 2000 copies (Ebook):", digital_book.royalty(2000))
