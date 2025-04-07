import flet as ft

def main(page: ft.Page):
    pass

    text1 = ft.Text("Shut up Calcium")
    text2 = ft.Text("I don't know my name")
    text3 = ft.Text("Its all the same water")

    image1 = ft.Image(src="/Users/laurarosello/Desktop/Image 7-4-25 at 8.14 AM (1).jpg")
    image2 = ft.Image(src="/Users/laurarosello/Desktop/Image 7-4-25 at 8.14 AM.jpg")
    image3 = ft.Image(src="/Users/laurarosello/Desktop/Image 7-4-25 at 8.13 AM.jpg")

    drop = ft.Dropdown(label= "languages",
                       options=[
                           ft.dropdown.Option("Chinese"),
                           ft.dropdown.Option("Japanese"),
                           ft.dropdown.Option("French"),
                           ft.dropdown.Option("Decrypt")
        ])

    page.add()
ft.app(target=main)