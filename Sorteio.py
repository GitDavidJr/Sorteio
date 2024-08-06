import flet as ft

numero: str
tamahoCaixa = 200


def main(page: ft.Page):

    numeroSorteado = ft.TextField(label="Numero que vai ser sorteado", width=tamahoCaixa)

    sorteio_img = ft.Image(src="sorteio.png", width=600, height=140)

    numeroInicio = ft.TextField(label="Primeiro numero", width=tamahoCaixa)
    numeroFim = ft.TextField(label="Ultimo numero", width=tamahoCaixa)

    def sortearNum(e):
        page.add(ft.Text(
        f"NUMERO SORTEADO: {numero}",
        size=40,
        color=ft.colors.BLUE,
        weight=ft.FontWeight.BOLD,
        italic=True
    ))

    def start(e):

        global numero
        numero = numeroSorteado.value
        page.clean()
        page.add(
            ft.Column(
            [
                sorteio_img,
                numeroInicio,
                numeroFim,
                ft.ElevatedButton(text="Sortear", on_click=sortearNum)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )   
        )

    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Column(
            [
                numeroSorteado,
                ft.ElevatedButton(text="Começar", on_click=start)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
