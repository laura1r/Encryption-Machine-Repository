import flet as ft

def main(page: ft.Page):
    def buttom(e):
        t.value = f"The quote has been translated {e.control.value}"
        page.update()

    t = ft.Text()

    text1 = ft.Text("Shut up Calcium")
    image1 = ft.Image(src="Image 7-4-25 at 8.14 AM (1).jpg")

    change = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="Tais-toi Calcium", label="French"),
        ft.Radio(value="黙れカルシウム", label="Yapanese")
    ]), on_change=buttom)

    row1 = ft.Row(controls=[text1])
    row2 = ft.Row(controls=[image1])
    page.add(t, row1, row2, change)
ft.app(target=main, assets_dir="assets")