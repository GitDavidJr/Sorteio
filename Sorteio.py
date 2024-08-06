import flet as ft

lista = []  
tamahoCaixa = 200
indice = 0
first = True


def main(page: ft.Page):

    numeroSorteado = ft.TextField(label="Numeros que vão ser sorteados \n(Coloque tudo junto separado apenas com virgula)", width=500)

    sorteio_img = ft.Image(src="sorteio.png", width=600, height=140)

    numeroInicio = ft.TextField(label="Primeiro numero", width=tamahoCaixa)
    numeroFim = ft.TextField(label="Ultimo numero", width=tamahoCaixa)

    def start(e):

        global lista
        lista = numeroSorteado.value.split(",")
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

    text_sorteado = ft.Text(
            size=40,
            color=ft.colors.BLUE,
            weight=ft.FontWeight.BOLD,
            italic=True
            )

    def sortearNum(e):
        global indice
        global first

        if first:
            text_sorteado.value = f"NUMERO SORTEADO: {lista[indice]}"
            page.add(text_sorteado)
            first = False
        else:
            text_sorteado.value = f"NUMERO SORTEADO: {lista[indice]}"
            page.update()

        indice += 1

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
