class BoulangerieQuantiteException(Exception):
    def __init__(self, message="Quantité incorrecte !"):
        self.message = message

    def __str__(self):
        return self.message
