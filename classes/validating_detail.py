
class Validation:

    def validate_birthday_month(self,b_month):

        while True:
            if b_month.lower() in ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']:
                break
            else:
                b_month = input("Enter month (ex:jan): ")
                continue
        return b_month

    def validate_rating(self,rating):
        while True:
            try:
                if 0 <= float(rating) <=10:
                    break
                else:
                    rating = input("Enter valid rating: ")
                    continue
            except TypeError:
                rating = input("Enter numbers as rating: ")
                continue

        return rating
