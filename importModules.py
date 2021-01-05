# import modules

# modules.escribeHola()
# modules.escribeHola("Monio")
# modules.escribeHola(3)
# modules.escribeAdios("Monio")

from modules import escribeHola, escribeAdios
import datetime

escribeHola()
escribeHola("Monio")
escribeHola(3)

escribeAdios("Monio")
escribeAdios("Ertika")
escribeAdios("Alejhandro")
escribeAdios()
escribeAdios("Anya")

miFechaAhora = datetime.datetime.now()

print(f"Hoy estamos a día {miFechaAhora.day} del mes {miFechaAhora.month} del año {miFechaAhora.year}")
