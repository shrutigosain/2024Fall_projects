class User:
    def __init__(self, age: int, height: float, weight: float, calorie_intake: float, gender: str):
        """
        Initializes a User instance with the provided attributes.

        :param age: age of the user in years.
        :param height: height of the user in inches.
        :param weight: initial weight of the user in lbs.
        :param calorie_intake: daily caloric intake of the user in kcal.
        :param gender: gender of the user ('male' or 'female').

        Raises:
            ValueError: If the gender is not 'male' or 'female'.

        >>> user = User(30, 180, 75, 2500, 'female')
        >>> user.gender
        'female'
        """

        self.age = age
        self.height = height
        self.weight = weight
        self.calorie_intake = calorie_intake
        self.gender = gender.lower()