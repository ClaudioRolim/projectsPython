from time import sleep

from kivy.app import App
from kivy.lang import Builder

import requests

GUI = Builder.load_file("tela.kv")

class MyApp(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["coin1"].text = f"Dollar R${self.get_quotation('USD')}"
        self.root.ids["coin2"].text = f"Euro R$ {self.get_quotation('EUR')}"
        self.root.ids["coin3"].text = f"Bitcoin R$ {self.get_quotation('BTC')}"
        self.root.ids["coin4"].text = f"Ethereum R${self.get_quotation('ETH')}"

    def get_quotation(self, coin):
        link = f"https://economia.awesomeapi.com.br/last/{coin}-BRL"
        requisition = requests.get(link)
        dict_requisition = requisition.json()
        quotation = dict_requisition[f"{coin}BRL"]['bid']
        return quotation
        
MyApp().run()

exit(0)
