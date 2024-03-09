from TaxiApp.service import Service
from TaxiApp.ui import UI

service = Service()
ui = UI(service)
ui.run()