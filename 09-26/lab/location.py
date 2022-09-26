from dataclasses import dataclass


@dataclass(order=True)
class Location:
    longitude: str
    latitude: str

    def update_location(self, new_location: tuple) -> None:
        self.longitude, self.latitude = new_location
