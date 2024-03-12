from domain.car import Car
from repository.repository import Repository
from service.cars_ervice import CarService
from UI.ui import UI
from domain.driver import Driver
from service.driver_service import DriverService
from service.statistics import StatisticsService

car_repository = Repository([Car('audi', 'SB12TNH', 331, 2), Car('audi', 'SB31CAI', 666, 2)])
car_service = CarService(car_repository)

driver_repository = Repository([Driver('Raul', 55, 'audi')])
driver_service = DriverService(driver_repository)
statistics_service = StatisticsService(car_repository, driver_repository)

ui = UI(car_service, driver_service, statistics_service)
ui.run()
