import flet as ft

def main(page: ft.Page):
    pass

    t = ft.Text("Quote")

    text1 = ft.Text("Shut up Calcium")
    image1 = ft.Image(src="/Users/laurarosello/Desktop/Image 7-4-25 at 8.14 AM (1).jpg")

    change = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="Tais-toi Calcium", label="French"),
        ft.Radio(value="黙れカルシウム", label="Yapanese")
    ]))

    row1 = ft.Row(text1)
    row2 = ft.Row(image1)
    page.add(t, row1, row2, change)