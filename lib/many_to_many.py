class Author:
    # Class attribute to keep track of all Author instances
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
         # Add this instance to the class-level list of all authors
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return list({contract.book for contract in self._contracts})

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
# Class attribute to keep track of all Book instances
class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        # Add this instance to the class-level list of all books
        Book.all.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return list({contract.author for contract in self._contracts})
 # Class attribute to keep track of all Contract instances
class Contract:
    all = []
 # Validation using properties/setters or direct checks in init.
        # The tests expect Exceptions to be raised for invalid types.
        
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        self.author._contracts.append(self)
        self.book._contracts.append(self)
         # Add this instance to the class-level list of all contracts
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]