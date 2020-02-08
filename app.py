## Import libraries
from database import Database
from menu import Menu

## Initialize Database
Database.initialize()
menu = Menu()
menu.run_menu()