import flet as ft 
from requests import get
  
moedaescolhida='twastwt'
def main(page: ft.Page):
    global apre
    texto ='preecha os campos para obter a cotaçao em reais'
    apre=ft.Text(texto)


    def on_changa(e: ft.ControlEvent):
        global valor_dropdown
        valor_dropdown = e.control.value
        print(f"moeda selecionado: {valor_dropdown}")
    
    def on_change(e: ft.ControlEvent):
        global valor_moeda
        valor_moeda = e.control.value
        print(f"Valor selecionado: {valor_moeda}")
    
    def caucula(e: ft.ControlEvent):
        resu= get( 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        tte=resu.json()
        if valor_dropdown=='Dolar':
            moeda=tte['USDBRL']['bid']
            resutado=float(moeda)*float(valor_moeda)
            resultado=format(resutado, ".2f")
            texto2={'moeda':'Dólar Americano','valor em doler':valor_moeda, 'Valor em Reais': str(resultado)  }
            texto=valor_moeda+' dolar vale: R$ '+ str(resultado)
            apre.value=texto
            
            page.update()
            print(resutado)
        elif valor_dropdown=='Euro':
            moeda=tte['EURBRL']['bid']
            resutado=float(moeda)*float(valor_moeda)
            resultado=format(resutado, ".2f")
            texto=valor_moeda+' Euro vale: R$ '+ str(resultado)
            apre.value=texto
            page.update()
            print(resutado)
        else:
            moeda=tte['BTCBRL']['bid']
            resutado=float(moeda)*float(valor_moeda)
            resultado=format(resutado, ".2f")
            texto=valor_moeda+' Bitcoin vale: R$ '+ str(resultado)
            apre.value=texto
            page.update()
            print(resutado)  
            print
    
    moeda=ft.Dropdown(
                label="Moeda",
                hint_text="qual?",
                options=[
                    ft.dropdown.Option("Dolar"),
                    ft.dropdown.Option("Euro"),
                    ft.dropdown.Option("Bitcoin"),
                ],
               
                on_change=on_changa
                    
                    
            )
        
    insere=ft.TextField(label='valor o desejado',on_change=on_change)
    envia=ft.OutlinedButton('enviar',on_click=caucula)
   
    page.title='Conversor de Moedas'
    page.favicon = ft.Icon(name="favicon.ico")
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    txt1 = ft.Text("O primeiro controle seleciona o número de colunas:")
    txt2 = ft.Text("O segundo controle seleciona espaçamento entre colunas:")
    page.add(moeda,insere,envia,apre )

ft.app(target=main)
