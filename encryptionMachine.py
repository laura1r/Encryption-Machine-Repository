import flet as ft

def main(page: ft.Page):
    pass

    text = ft.Text()
    drop = ft.Dropdown(label= "languages",
                       options=[
                           ft.dropdown.Option("Morse"),
                           ft.dropdown.Option("Alien"),
                           ft.dropdown.Option("Numbers"),
                           ft.dropdown.Option("Decrypt")
        ])
    
    #bEncrypt = ft.ElevatedButton(text="Encrypt")
    #bDecrypt = ft.ElevatedButton(text="Decrypt")

    page.add()
ft.app(target=main)