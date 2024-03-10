from TaxiApp.domain.animal import Car
from TaxiApp.repository.repository import Repository
from TaxiApp.service.carservice import CarService
from UI.ui import UI

car_repository = Repository([Car('audi', 'SB12TNH', 331, 2), Car('audi', 'SB31CAI', 666, 2)])
car_service = CarService(car_repository)
ui = UI(car_service)
ui.run()