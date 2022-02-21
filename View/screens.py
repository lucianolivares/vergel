# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Model.plagas_screen import PlagasScreenModel

from Controller.main_screen import MainScreenController
from Controller.plagas_screen import PlagasScreenController

screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "plagas screen": {
        "model": PlagasScreenModel,
        "controller": PlagasScreenController,
    },
}
