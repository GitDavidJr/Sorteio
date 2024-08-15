import random
import flet as ft

lista = []  
tamahoCaixa = 200
indice = 0
first = True


def main(page: ft.Page):

    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    numeroSorteado = ft.TextField(label="Numeros que vão ser sorteados \n(Coloque tudo junto separado apenas com virgula)", width=500)
    entradaNomes = ft.TextField(label="Lista de nomes separado por virgula \n(Coloque tudo junto separado apenas com virgula)", width=500)

    sorteio_img = ft.Image(src="sorteio.png", width=600, height=140)

    numeroInicio = ft.TextField(label="Primeiro numero", width=tamahoCaixa)
    numeroFim = ft.TextField(label="Ultimo numero", width=tamahoCaixa)

    text_sorteado = ft.Text(
            size=40,
            color=ft.colors.BLUE,
            weight=ft.FontWeight.BOLD,
            italic=True
            )

    #tela inicial
    def telaInicial():

        page.clean()
        page.add(
            ft.ElevatedButton(text="Sorteio A", on_click=aleatorioTela),
            ft.ElevatedButton(text="Sorteio P", on_click=insNumTela),
            ft.ElevatedButton(text="Sorteio N", on_click=insListNomTela),
            ft.ElevatedButton(text="Sorteio NP", on_click=insNomTelaProgramado)
        )

    #tela de sorteio aleatorio
    def aleatorioTela(e):
        
        page.clean()
        page.add(
            ft.Column(
            [
                sorteio_img,
                numeroInicio,
                numeroFim,
                ft.ElevatedButton(text="Sortear", on_click=sortearNumAleatorio)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )   
        )

    #sorteio de numeros aleatorio
    def sortearNumAleatorio(e):
        global first

        if first:
            text_sorteado.value = f"NUMERO SORTEADO: {random.randint(int(numeroInicio.value),int(numeroFim.value))}"
            page.add(text_sorteado)
            first = False
        else:
            text_sorteado.value = f"NUMERO SORTEADO: {random.randint(int(numeroInicio.value),int(numeroFim.value))}"
            page.update()

    #Tela inserir numeros para serem sorteados
    def insNumTela(e):
        page.clean()
        page.add(
            ft.Column(
                [
                    numeroSorteado,
                    ft.ElevatedButton(text="Começar", on_click=sorteioNumInseridosTela)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    #Tela de sorteio de numeros iseridos anteriormente
    def sorteioNumInseridosTela(e):

        global lista
        lista = numeroSorteado.value.split(",")
        page.clean()
        page.add(
            ft.Column(
            [
                sorteio_img,
                numeroInicio,
                numeroFim,
                ft.ElevatedButton(text="Sortear", on_click=exibirNumInseridos)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )   
        )

    #Ixibição de numeros inseridos anteriormente
    def exibirNumInseridos(e):
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

    #listagem de nomes para sorteio
    def insListNomTela(e):
        page.clean()
        page.add(
            ft.Column(
                [
                    entradaNomes,
                    ft.ElevatedButton(text="Começar", on_click=sorteioNomeTela)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    #Tela de sorteio de nomes aleatorios
    def sorteioNomeTela(e):

        global lista
        lista = entradaNomes.value.split(",")
        page.clean()
        page.add(
            ft.Column(
            [
                sorteio_img,
                ft.ElevatedButton(text="SORTEAR NOME", on_click=sortearNome)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )   
        )

    def sortearNome(e):
        
        global lista
        global first

        if first:
            text_sorteado.value = f"{random.choice(lista)}"
            page.add(text_sorteado)
            first = False
        else:
            text_sorteado.value = f"{random.choice(lista)}"
            page.update()

    #Tela inserir nomes para sortear
    def insNomTelaProgramado(e):
        page.clean()
        page.add(
            ft.Column(
                [
                    entradaNomes,
                    ft.ElevatedButton(text="Começar", on_click=sorteioNumInseridosTela)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    #Tela de sorteio de nomes inseridos
    def sorteioNumInseridosTela(e):

        global lista
        lista = entradaNomes.value.split(",")
        page.clean()
        page.add(
            ft.Column(
            [
                sorteio_img,
                ft.ElevatedButton(text="Sortear Nome", on_click=exibirNomInseridos)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )   
        )

    #Ixibição de nomes inseridos
    def exibirNomInseridos(e):
        global indice
        global first

        if first:
            text_sorteado.value = f"NOME SORTEADO: {lista[indice]}"
            page.add(text_sorteado)
            first = False
        else:
            text_sorteado.value = f"NOME SORTEADO: {lista[indice]}"
            page.update()
        
        indice += 1


    telaInicial()

ft.app(target=main)
