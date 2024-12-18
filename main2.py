class Personazh(ABC):
    def __init__(self, imya: str, zdorove: int, sila: int):
        """
        Initialization of the character.

        :param imya: name of the character
        :param zdorove: health points
        :param sila: strength points
        """
        if zdorove <= 0:
            raise ValueError("Health must be greater than 0.")
        if sila <= 0:
            raise ValueError("Strength must be greater than 0.")

        self.imya = imya
        self.zdorove = zdorove
        self.sila = sila

    @abstractmethod
    def atakovat(self, target: 'Personazh') -> None:
        """
        Attacks a target character.

        :param target: the target character to attack

        :Example:
        >>> character = Personazh("Hero", 100, 20)
        >>> character.atakovat(target_character)
        ...
        """
        ...

    @abstractmethod
    def poluchit_ushkod(self, damage: int) -> None:
        """
        Receives damage.

        :param damage: the amount of damage received

        :Example:
        >>> character.poluchit_ushkod(10)
        ...
        """
        ...