from abc import ABC, abstractmethod


class TransportnoeSredstvo(ABC):
    def __init__(self, marka: str, maksimalnaya_skoroct: float, kolichestvo_koles: int):
        """
        Initialization of the transport vehicle.

        :param marka: brand of the transport vehicle
        :param maksimalnaya_skoroct: maximum speed in km/h (must be greater than 0)
        :param kolichestvo_koles: number of wheels (must be greater than or equal to 2)

        :raises ValueError: if maximum speed is less than or equal to 0,
                            or number of wheels is less than 2
        """
        if maksimalnaya_skoroct <= 0:
            raise ValueError("Maximum speed must be greater than 0.")
        if kolichestvo_koles < 2:
            raise ValueError("Number of wheels must be greater than or equal to 2.")

        self.marka = marka
        self.maksimalnaya_skoroct = maksimalnaya_skoroct
        self.kolichestvo_koles = kolichestvo_koles

    @abstractmethod
    def razognat_sya(self, do_skorosti: float) -> bool:
        """
        Accelerates the transport vehicle to a given speed.

        :param do_skorosti: target speed in km/h
        :return: True if acceleration is successful, False if unable to accelerate

        :Example:
        >>> transport = TransportnoeSredstvo("Toyota", 200, 4)  # Create an implementation and test
        >>> transport.razognat_sya(150)
        True
        """
        ...

    @abstractmethod
    def ostanovitsya(self) -> None:
        """
        Stops the transport vehicle.

        :return: None

        :Example:
        >>> transport.ostanovitsya()
        ...
        """
        ...