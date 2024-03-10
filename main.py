from service.service import Service
from UI.ui import UI

service = Service()
ui = UI(service)
ui.run()