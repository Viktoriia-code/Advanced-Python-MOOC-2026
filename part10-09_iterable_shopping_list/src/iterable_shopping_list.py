# TEE RATKAISUSI TÄHÄN:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]

    # This is the iterator initialization method
    # The iteration variable(s) should be initialized here
    def __iter__(self):
        self.n = 0
        # the method returns a reference to the object itself as 
        # the iterator is implemented within the same class definition
        return self

    # This method returns the next item within the object
    # If all items have been traversed, the StopIteration event is raised
    def __next__(self):
        if self.n < len(self.products):
            # Select the current item from the list within the object
            product = self.products[self.n]
            # increase the counter (i.e. iteration variable) by one
            self.n += 1
            # return the current item
            return product
        else:
            # All books have been traversed
            raise StopIteration