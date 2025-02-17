from typing import Optional

class ElectronicDevice:
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price
        self._is_on = False

    def turn_on(self) -> None:
        self._is_on = True
        print(f"{self} turned on.")

    def turn_off(self) -> None:
        self._is_on = False
        print(f"{self} turned off.")

    def get_status(self) -> str:
        return f"{self} is {'on' if self._is_on else 'off'}."

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"ElectronicDevice(brand={self.brand}, model={self.model}, price={self.price})"


class Smartphone(ElectronicDevice):
    def __init__(self, brand: str, model: str, price: float, screen_size: float, camera_mp: int):
        super().__init__(brand, model, price)
        self.screen_size = screen_size
        self.camera_mp = camera_mp

    def make_call(self, number: str) -> None:
        print(f"Calling {number} from {self}...")

    def take_photo(self) -> None:
        print(f"Taking a photo with {self.camera_mp} MP camera.")

    def get_status(self) -> str:
        base_status = super().get_status()
        return f"{base_status} Screen size: {self.screen_size} inches."

    def __str__(self) -> str:
        return f"{self.brand} {self.model} (Smartphone)"


class Laptop(ElectronicDevice):
    def __init__(self, brand: str, model: str, price: float, screen_diagonal: float, ram_gb: int):
        super().__init__(brand, model, price)
        self.screen_diagonal = screen_diagonal
        self.ram_gb = ram_gb

    def run_program(self, program: str) -> None:
        print(f"Running {program} on {self}.")

    def get_status(self) -> str:
        base_status = super().get_status()
        return f"{base_status} Screen diagonal: {self.screen_diagonal} inches, RAM: {self.ram_gb} GB."

    def __str__(self) -> str:
        return f"{self.brand} {self.model} (Laptop)"