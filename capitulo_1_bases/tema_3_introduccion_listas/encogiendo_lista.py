invitados = ['Don Ramón', 'Homero Simpson', 'Peter Griffin']

print(f'{invitados[0]} estas invitado a mi fiesta')
print(f'{invitados[1]} estas invitado a mi fiesta')
print(f'{invitados[2]} estas invitado a mi fiesta')

print(invitados[2])
invitados[2] = 'Pinocho'

print(f'{invitados[0]} estas invitado a mi fiesta')
print(f'{invitados[1]} estas invitado a mi fiesta')
print(f'{invitados[2]} estas invitado a mi fiesta')

print("Encontre una mesa mas grande puedo invitar a 3 personas mas")
invitados.insert(0, 'Señor Barriga')
invitados.insert(2, 'Pedro Picapiedra')
invitados.append('Brian Griffin')
print(f'{invitados[0]} estas invitado a mi fiesta')
print(f'{invitados[1]} estas invitado a mi fiesta')
print(f'{invitados[2]} estas invitado a mi fiesta')
print(f'{invitados[3]} estas invitado a mi fiesta')
print(f'{invitados[4]} estas invitado a mi fiesta')
print(f'{invitados[5]} estas invitado a mi fiesta')

print("Lo siento solo podre invitar a dos personas a la fiesta")
desinvitado = invitados.pop(0)
print(f'{desinvitado} lo siento no estas invitado a mi fiesta')
desinvitado = invitados.pop(1)
print(f'{desinvitado} lo siento no estas invitado a mi fiesta')
desinvitado = invitados.pop(2)
print(f'{desinvitado} lo siento no estas invitado a mi fiesta')
desinvitado = invitados.pop(2)
print(f'{desinvitado} lo siento no estas invitado a mi fiesta')
print(f'{invitados[0]} estas invitado a mi fiesta')
print(f'{invitados[1]} estas invitado a mi fiesta')
del invitados[0]
del invitados[0]
print(invitados)
