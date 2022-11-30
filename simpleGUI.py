import PySimpleGUI as sg

sg.theme("GrayGrayGray")

layout = [[sg.Text("Entrez votre nom")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-', text_color='red')], #zone d'affichage
          [sg.Button('Ok'), sg.Stretch(),sg.Button('Fermer la fenêtre', key='_QUIT_', border_width=4)]]

window = sg.Window('Exemple 2 : Event Loop', layout)

# Event Loop - la fenêtre reste ouverte tant qu'une condition de sortie
# n'est pas atteinte.
while True:
    event, values = window.read()
    # Appui sur le bouton QUIT ou l'icone de fermeture de la fenêtre
    if event == sg.WINDOW_CLOSED or event == '_QUIT_':
        break
    # Affichage dans la fenêtre
    window['-OUTPUT-'].update(f'Bienvenue {values["-INPUT-"]}! Merci de tester PySimpleGUI')

# Ferme la fenêtr et le programme
window.close()

print("""
Une boucle d'événements permet de garder la fenêtre ouverte tout en traitant
les différents messages. Tous les éléments possèdent une méthode update permettant
d'en modifier l'aspect : contenu, couleur, etc.
Noter dans le layout, sg.stretch() qui pousse le bouton vers le bord droit.
La commande sg.theme() qui permet de choisir un thème graphique pour l'application.
""")
