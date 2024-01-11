from car_class_logging import Car
from car_class_logging import ElektricalCar
import pytest

@pytest.fixture
def get_car():
    return Car("Toyota","Yaris",2023)

@pytest.fixture
def get_electric_car():
    return ElektricalCar("Tesla","Model 3",2024,75)

def test_car(get_car):
    expected_output="Marka: Toyota\nModel: Yaris\nRocznik: 2023\nProdukcja: nie"
    assert get_car.display_info()==expected_output

def test_car_start_production(get_car):
    get_car.start_production()
    assert get_car.is_production ==True