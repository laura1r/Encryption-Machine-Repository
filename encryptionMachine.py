import flet as ft

def main(page: ft.Page):
    pass

    def images():
        pass

    text1 = ft.Text("Shut up Calcium")
    image1 = ft.Image(src="/Users/laurarosello/Desktop/Image 7-4-25 at 8.14 AM (1).jpg")

    change = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="French", label="French"),
        ft.Radio(value="Yapanese", label="Yapanese")
    ]))

    row1 = ft.Row(text1)
    row2 = ft.Row(image1)
    page.add(row1, row2, change)