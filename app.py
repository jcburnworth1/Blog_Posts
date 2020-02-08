## Import libraries
from database import Database
from menu import Menu

## Initialize Database
Database.initialize()

## Bring up the menu
menu = Menu()
menu.run_menu()