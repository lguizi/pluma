import requests
from bs4 import BeautifulSoup
from colorama import *

class spider:
    def __init__(self,url):
        print (f"\n {Fore.YELLOW}> SPIDER")
        self.url_master = url
        self.links_extraidos = self.links_internos = self.links_externos = []

        def extrair(self,url):
            print (' '*6 + f'|-[{url}]' + ' '*48)
            conteudo = BeautifulSoup(requests.get(url).content,'lxml')
            links = conteudo.findAll(href=True)

            for link in links:
                self.links_extraidos.append(str(link['href']))
                for link in self.links_extraidos:
                    if 'http' not in link and link[:1] != '/':
                        link = self.url_master+'/'+link
                    elif 'http' not in link and link[:1] == '/':
                        link = self.url_master+link
                    if self.url_master in link and link not in self.links_internos:
                        self.links_internos.append(link)
                        print (f'          |-{link}')
                    elif self.url_master not in link and link not in self.links_externos:
                        self.links_externos.append(link)
        def resumo(self):
            print (' '*8 + f'|------ {len(self.links_internos)} INTERNAL LINK(S)')
            print (' '*8 + f'|------ {len(self.links_externos)} EXTERNAL LINK(S)')
