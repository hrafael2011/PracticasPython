from casa import apartamento

apartamento1 = apartamento()

apartamento1.setHabitaciones(2)

info = f'El apartamento tiene un total de {apartamento1.getHabitaciones()} habitaciones'

print(info)