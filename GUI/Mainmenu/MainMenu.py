from GUI.Mainmenu.Ui_WIndow_Aquazul import Ui_WIndow_Aquazul
from GUI.Mainmenu.Pantallas.Animal.Animal import Animal
from GUI.Mainmenu.Pantallas.Species.Species import Species
from GUI.Mainmenu.Pantallas.Habitat.Habitat import Habitat
from GUI.Mainmenu.Pantallas.Danger.Danger import Danger
from GUI.Mainmenu.Pantallas.Material.Material import Material
from GUI.Mainmenu.Pantallas.Feeding.Feeding import Feeding
from GUI.Mainmenu.Pantallas.Employe.Employe import Employe
from GUI.Mainmenu.Pantallas.Email.Correo import Email
from GUI.Mainmenu.Pantallas.AquariumBranch.AquariumBranch import AquariumBranch
from GUI.Mainmenu.Pantallas.State.State import State
from GUI.Mainmenu.Pantallas.Address.Address import Address
from GUI.Mainmenu.Pantallas.TypeWater.TypeWater import TypeofWater
from PyQt5.QtWidgets import QMainWindow


class MainMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_WIndow_Aquazul()
        self.ui.setupUi(self)
        self.conn = None
        self.s_animal = None
        self.s_specie = None
        self.s_habitat = None
        self.s_danger = None
        self.s_material = None
        self.s_feeding = None
        self.s_employe = None
        self.s_email = None
        self.s_aquarium_branch = None
        self.s_state = None
        self.s_address = None
        self.s_type_water = None

        # Acciones a cada boton de la interfaz
        self.ui.btn_animal.clicked.connect(self.btn_animal_clicked)
        self.ui.btn_especie.clicked.connect(self.btn_specie_clicked)
        self.ui.btn_habitat.clicked.connect(self.btn_habitat_clicked)
        self.ui.btn_peligro.clicked.connect(self.btn_danger_clicked)
        self.ui.btn_material.clicked.connect(self.btn_material_clicked)
        self.ui.btn_alimentacion.clicked.connect(self.btn_feeding_clicked)
        self.ui.btn_empleado.clicked.connect(self.btn_employe_clicked)
        self.ui.btn_correo.clicked.connect(self.btn_email_clicked)
        self.ui.btn_sucursal.clicked.connect(self.btn_aquarium_branch_clicked)
        self.ui.btn_estado.clicked.connect(self.btn_state_clicked)
        self.ui.btn_direccion.clicked.connect(self.btn_address_clicked)
        self.ui.btn_tipoagua.clicked.connect(self.btn_type_water_clicked)

    def btn_animal_clicked(self):
        self.setDisabled(True)

        self.s_animal = Animal(self.conn)
        self.s_animal.closed.connect(self.enable_main_menu)
        self.s_animal.show()

    def btn_specie_clicked(self):
        self.setDisabled(True)

        self.s_specie = Species(self.conn)
        self.s_specie.closed.connect(self.enable_main_menu)
        self.s_specie.show()

    def btn_habitat_clicked(self):
        self.setDisabled(True)

        self.s_habitat = Habitat(self.conn)
        self.s_habitat.closed.connect(self.enable_main_menu)
        self.s_habitat.show()

    def btn_danger_clicked(self):
        self.setDisabled(True)

        self.s_danger = Danger(self.conn)
        self.s_danger.closed.connect(self.enable_main_menu)
        self.s_danger.show()

    def btn_material_clicked(self):
        self.setDisabled(True)

        self.s_material = Material(self.conn)
        self.s_material.closed.connect(self.enable_main_menu)
        self.s_material.show()

    def btn_feeding_clicked(self):
        self.setDisabled(True)

        self.s_feeding = Feeding(self.conn)
        self.s_feeding.closed.connect(self.enable_main_menu)
        self.s_feeding.show()

    def btn_employe_clicked(self):
        self.setDisabled(True)

        self.s_employe = Employe(self.conn)
        self.s_employe.closed.connect(self.enable_main_menu)
        self.s_employe.show()

    def btn_email_clicked(self):
        self.setDisabled(True)

        self.s_email = Email(self.conn)
        self.s_email.closed.connect(self.enable_main_menu)
        self.s_email.show()

    def btn_aquarium_branch_clicked(self):
        self.setDisabled(True)

        self.s_aquarium_branch = AquariumBranch(self.conn)
        self.s_aquarium_branch.closed.connect(self.enable_main_menu)
        self.s_aquarium_branch.show()

    def btn_state_clicked(self):
        self.setDisabled(True)

        self.s_state = State(self.conn)
        self.s_state.closed.connect(self.enable_main_menu)
        self.s_state.show()

    def btn_address_clicked(self):
        self.setDisabled(True)

        self.s_address = Address(self.conn)
        self.s_address.closed.connect(self.enable_main_menu)
        self.s_address.show()

    def btn_type_water_clicked(self):
        self.setDisabled(True)

        self.s_type_water = TypeofWater(self.conn)
        self.s_type_water.closed.connect(self.enable_main_menu)
        self.s_type_water.show()

    def enable_main_menu(self):
        self.setEnabled(True)

    def set_connection(self, conn):
        self.conn = conn
