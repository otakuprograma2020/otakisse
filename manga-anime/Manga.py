import re, requests, random, os, shutil, subprocess, platform, operator, sys, webbrowser, zipfile, getpass, time, base64, rarfile, datetime
from Common import Common
from numpy import arange
from playsound import playsound
import pyexcel_ods3 as pods
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located, alert_is_present,element_to_be_clickable,visibility_of_element_located
import selenium.webdriver.firefox.options as firefoxOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
class Manga:
    
    def __init__(self, feature=None):
        self.initURLBH = 'http://baixarhentai.net'
        self.initURLHC = 'https://hiper.cool'
        self.initURLHS = 'https://hentaiseason.com'
        self.initURLUnion = 'https://unionleitor.top/'
        self.initURLmangadex = 'https://mangadex.org'
        self.initURLTsukiMangas = 'https://tsukimangas.com'
        self.initURLLeitorDotNet = 'https://leitor.net'
        self.initURLMangaLivre = 'https://mangalivre.net/'
        self.initURLSearchAniList = 'https://anilist.co/search/manga?search='
        self.url_search_manga = 'https://myanimelist.net/manga.php?q='
        self.names_mangas = {
            "Iinchou, Sakki Toile de Onatteta desho ~Itta Kaisuu ga Barechau Sekai~": "Committee Chairman, Didn't You Just",
            "Uma História Sobre Tratar Uma Cavaleira Mulher Que Nunca foi Tratada como uma Mulher": "Ima made Ichido mo Onna Atsukaisareta Koto ga nai Jokishi wo Onna Atsukai Suru",
            "We May Be An Inexperienced Couple But": "Mijuku na Futari de Gozaimasu ga",
            "Rabuyu!": "Love You",
            "Adamas no Majo-tachi": "Adamasu no Majotachi",
            "Boushoku no Berserk: Ore dake Level to Iu Gainen wo Toppa suru the Comic": "Berserk of Gluttony",
            "Dosanko Gal wa Namara Menkoi": "Dosanko Gyaru wa Namaramenkoi",
            "Junk the Black Shadow":"Kokuei no Junk",
            "Yotsuba and!": "Yotsubato!",
            "Haitekudasai Takamine-san": "Haite Kudasai, Takamine-san",
            "Uzaki-chan Wants to Hang Out!": "Uzaki-chan wa Asobitai!",
            "Monster Musume no Oishasan": "Monster Musume no Oisha-san",
            "Tensei shitara Dragon no Tamago datta- Saikyou Igai Mezasanee":"Tensei shitara Dragon no Tamago datta - Ibara no Dragon Road",
            "Maou desu Onna Yuusha no Hahaoya to Saikon Shita no de": "Maou desu. Onna Yuusha no Hahaoya to Saikon Shitanode, Onna Yuusha ga Giri no Musume ni Narimashita @comic",
            "Maou desu. Onna Yuusha no Hahaoya to Saikon shita node, Onna Yuusha ga Giri no Musume ni Narimashita. @comic":"Maou desu. Onna Yuusha no Hahaoya to Saikon Shitanode, Onna Yuusha ga Giri no Musume ni Narimashita @comic",
            "Ashigei Shoujo Komura-san (Pt-Br)":"Ashigei Shoujo Komura-san",
            "Perfect Half (pt-br)":"Perfect Half",
            "Megan to Dangan o Tsukatte Isekai o Buchinuku!":"Magan to Dangan wo Tsukatte Isekai wo Buchinuku!"
        }
        self.manga18 = {
            'A Perverts Daily Life': r'D:\Imagens\Mangás\A Perverts Daily Life',
            'Adamasu no Majotachi': r'D:\Imagens\Mangás\Adamasu no Majotachi',
            'Alcafus': r'D:\Imagens\Mangás\Alcafus',
            'Black Gakkou ni Tsutomete Shimatta Sensei': r'D:\Imagens\Mangás\Black Gakkou ni Tsutomete Shimatta Sensei',
            'Chichi Chichi':r'D:\Imagens\Mangás\Chichi Chichi',
            'Close as Neighbors':r'D:\Imagens\Mangás\Close as Neighbors',
            'Committee Chairman':r'D:\Imagens\Mangás\Committee Chairman',
            'Crime and Punishment':r'D:\Imagens\Mangás\Crime and Punishment',
            'Dating Contract':r'D:\Imagens\Mangás\Dating Contract',
            'Deceptions':r'D:\Imagens\Mangás\Deceptions',
            'Delivery Cinderella':r'D:\Imagens\Mangás\Delivery Cinderella',
            'Domesticate the Housekeeper':r'D:\Imagens\Mangás\Domesticate the Housekeeper',
            'Fitness':r'D:\Imagens\Mangás\Fitness',
            'Good Night':r'D:\Imagens\Mangás\Good Night',
            'His Place':r'D:\Imagens\Mangás\His Place',
            'Ishuzoku Reviewers':r'D:\Imagens\Mangás\Ishuzoku Reviewers',
            'Jag-eun Jeonjaeng - My Kingdom':r'D:\Imagens\Mangás\Jag-eun Jeonjaeng - My Kingdom',
            'Jeopardy':r'D:\Imagens\Mangás\Jeopardy',
            'Koakuma Setsuko no Himitsu':r'D:\Imagens\Mangás\Koakuma Setsuko no Himitsu',
            'Lucky Guy':r'D:\Imagens\Mangás\Lucky Guy',
            'Lust Awakening': r'D:\Imagens\Mangás\Lust Awakening',
            'Lust Geass':r'D:\Imagens\Mangás\Lust Geass',
            'Megami no Sprinter':r'D:\Imagens\Mangás\Megami no Sprinter',
            'Mind Reader':r'D:\Imagens\Mangás\Mind Reader',
            'Minimum':r'D:\Imagens\Mangás\Minimum',
            'Monster Musume no Iru Nichijou':r'D:\Imagens\Mangás\Monster Musume no Iru Nichijou',
            'Mousou Megane':r'D:\Imagens\Mangás\Mousou Megane',
            'My Friends Dad':r'D:\Imagens\Mangás\My Friends Dad',
            'Nande Koko ni Sensei ga':r'D:\Imagens\Mangás\Nande Koko ni Sensei ga',
            'Office Ladies':r'D:\Imagens\Mangás\Office Ladies',
            'Our Complications':r'D:\Imagens\Mangás\Our Complications',
            'Parallel Paradise':r'D:\Imagens\Mangás\Parallel Paradise',
            'Perfect Half (pt-br)':r'D:\Imagens\Mangás\Perfect Half (pt-br)',
            'Peter Grill to Kenja no Jikan':r'D:\Imagens\Mangás\Peter Grill to Kenja no Jikan',
            'Pheromone Holic':r'D:\Imagens\Mangás\Pheromone Holic',
            'Ren Arisugawa Is Actually A Girl':r'D:\Imagens\Mangás\Ren Arisugawa Is Actually A Girl',
            'Rental Girls':r'D:\Imagens\Mangás\Rental Girls',
            'Saikyou no Shuzoku ga Ningen Datta Ken':r'D:\Imagens\Mangás\Saikyou no Shuzoku ga Ningen Datta Ken',
            'Secret Class':r'D:\Imagens\Mangás\Secret Class',
            'Sekkaku Cheat wo Moratte Isekai ni Teni shita n dakara, Suki na you ni Ikitemitai':r'D:\Imagens\Mangás\Sekkaku Cheat wo Moratte Isekai ni Teni shita n dakara, Suki na you ni Ikitemitai',
            'Sexercice':r'D:\Imagens\Mangás\Sexercice',
            'Shuumatsu No Harem':r'D:\Imagens\Mangás\Shuumatsu No Harem',
            'Shuumatsu no Harem- Fantasia':r'D:\Imagens\Mangás\Shuumatsu no Harem- Fantasia',
            'Solmis Channel':r'D:\Imagens\Mangás\Solmis Channel',
            'Sundome!! Milky Way':r'D:\Imagens\Mangás\Sundome!! Milky Way',
            'Taking a Hot Tanned Chicks Virginity':r'D:\Imagens\Mangás\Taking a Hot Tanned Chicks Virginity',
            'Teach Me How to Please You':r'D:\Imagens\Mangás\Teach Me How to Please You',
            'The Girl Next Door':r'D:\Imagens\Mangás\The Girl Next Door',
            'Tsugumomo':r'D:\Imagens\Mangás\Tsugumomo',
            'Wakamono no Kuro Mahou Hanare ga Shinkoku desu ga':r'D:\Imagens\Mangás\Wakamono no Kuro Mahou Hanare ga Shinkoku desu ga',
        }
        self.exclude_url_hc = ['https://hiper.cool/tags/shota-gay', 'https://hiper.cool/tags/yaoi', 'https://hiper.cool/tags/travesti', 'https://hiper.cool/tags/futanari', 'https://hiper.cool/tags/futanari-on-futanari', 'https://hiper.cool/tags/enema', 'https://hiper.cool/tags/scat', 'https://hiper.cool/tags/zoofilia', 'https://hiper.cool/tags/coprofilia']
        self.exclude_generos_bh = [360, 5048, 5670, 4426, 4232, 8123, 4993, 1067, 1658, 9, 1150, 2233, 8]
        self.categoriasHC = ['H-Mangá', 'H-Manga', 'Oneshot', 'Doujinshi', 'Paródia', 'HQs', 'Mangá', 'Manga', 'Manhwa', 'Manhua', 'Artist CG', 'H-Mnagá','HQs 3D']
        self.categoriasDicHC = {'oneshot': [], 'doujinshi': [], 'paródia': [], 'h-manga': [], 'hqs': [], 'manga': [], 'manhwa': [], 'manhua': [], 'artist cg': [], 'hqs 3d':[], 'uncategorized': []}
        self.categoriasHS = ['One-Shot', 'Doujin', 'h-manga', 'Uncategorized', 'Pack-de-Imagens']
        self.categoriasDicHS = {'one-shot': [], 'doujin': [], 'h-manga': [], 'uncategorized': [], 'pack-de-imagens': []}
        self.categoriaDicBH = {'one-shots': [], 'doujinshis': [], 'h-mangá': []}
        self.exclude_urls_hs = ['https://hentaiseason.com/tag/futanari/', 'https://hentaiseason.com/tag/scat/', 'https://hentaiseason.com/tag/shemale/', 'https://hentaiseason.com/tag/yaoi/', 'https://hentaiseason.com/tag/zoofilia/', 'https://hentaiseason.com/category/tia-primas-e-cia/', 'https://hentaiseason.com/category/familia-sacana/']
        self.feature = feature
        self.cwd = os.getcwd()
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.arquivos_sounds = os.path.join(self.dir_path, 'sounds')
        self.arquivo_entrada = os.path.join(self.dir_path, 'entrada')
        self.saida_path = self.criarPastaManga('saida', self.dir_path)[0]
        self.common = Common(feature, self.saida_path)
        self.mangaPasta = self.criarPastaManga('mangas', self.dir_path)[0]
        self.path_H_manga = os.path.join(self.mangaPasta, 'H')
        self.path_H_manga_hs = os.path.join(self.path_H_manga, 'h-mangas links HS')
        self.path_H_manga_hc = os.path.join(self.path_H_manga, 'h-mangas links HC')
        self.path_H_manga_bh = os.path.join(self.path_H_manga, 'h-mangas links BH')
        self.mangasDeletados = {}
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        self.login_data = {
            'email':'', 
            'password':'',
            'logar' : '1'
        }
        self.url_login = 'https://unionleitor.top/login'
        self.regex_urlWEB = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", re.IGNORECASE)
        self.regexPath = re.compile(r'^(~?/|[a-zA-Z]:[\\/]).+')
        self.regexDataUri = re.compile(r'data:([a-zA-Z0-9]+\/[a-zA-Z0-9-.+]+).*')
        self.firefox_options = firefoxOptions.Options()
        self.firefox_options.headless = True
        self.common.clearTerminal()
        self.verificaMangasLogDelete()
        # self.verificaLogBaixados()
        self.verificaLogDelete()
        self.verificaLogNotificacoes()
        self.completados = self.verificaCompletados()
        self.baixados = self.getBaixados()
        print("-"*15)
        print("| MENU MANGÁS |")
        print("-"*15)

    def verificaLogDelete(self):
        try:
            nomeArquivo = os.path.join(self.saida_path, "logDeleteCaps.txt")
            arquivo = open(nomeArquivo, 'r', encoding='utf-8')
            texto = arquivo.readlines()
            arquivo.close()
            i = 0
            newData = []
            for t in texto:
                texto[texto.index(t)] = re.sub('[ ]{2}',' ',texto[texto.index(t)])
                texto[-1] = re.sub('[ ]{2}',' ',texto[-1])
                busca = re.search("(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{1,2}) (([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]) [0-9]{4}", t)
                if(busca):
                    if(i == 0):
                        i += 1
                        buscaUltimo = re.search("(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{1,2}) (([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]) [0-9]{4}", texto[-1])
                        if(buscaUltimo):
                            ultimo = buscaUltimo.group()
                    atual = busca.group()
                    resultDateTime =  datetime.datetime.strptime(ultimo, '%a %b %d %H:%M:%S %Y') - datetime.datetime.strptime(atual, '%a %b %d %H:%M:%S %Y')
                    if(resultDateTime.days <= 30):
                        newData.append(t)
            arquivo = open(nomeArquivo, 'w', encoding='utf-8')
            arquivo.truncate(0)
            arquivo.writelines(newData)
            arquivo.close()
        except Exception as err:
            print("ERRO (verificaLogDelete): {}".format(err))
            os.system('pause')
    
    def verificaLogBaixados(self):
        try:
            nomeArquivo = os.path.join(self.saida_path, "logMangasBaixados.txt")
            arquivo = open(nomeArquivo, 'r', encoding='utf-8')
            texto = arquivo.readlines()
            arquivo.close()
            i = 0
            newData = []
            for t in texto:
                texto[texto.index(t)] = re.sub('[ ]{2}',' ',texto[texto.index(t)])
            for t in texto:
                texto[texto.index(t)] = re.sub('[ ]{2}',' ',texto[texto.index(t)])
                busca = re.search("(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{1,2}) (([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]) [0-9]{4}", t)
                if(texto.index(t) == 23):
                    print()
                if(busca):
                    if(i == 0):
                        i += 1
                        texto[-1] = re.sub('[ ]{2}',' ',texto[-1])
                        buscaUltimo = re.search("(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{1,2}) (([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]) [0-9]{4}", texto[-1])
                        if(buscaUltimo):
                            ultimo = buscaUltimo.group()
                    atual = busca.group()
                    resultDateTime =  datetime.datetime.strptime(ultimo, '%a %b %d %H:%M:%S %Y') - datetime.datetime.strptime(atual, '%a %b %d %H:%M:%S %Y')
                    if(resultDateTime.days <= 30):
                        newData.append(t)
            arquivo = open(nomeArquivo, 'w', encoding='utf-8')
            arquivo.truncate(0)
            arquivo.writelines(newData)
            arquivo.close()
        except Exception as err:
            print("ERRO (verificaLogBaixados): {}".format(err))
            os.system('pause')

    def verificaLogNotificacoes(self):
        try:
            nomeArquivo = os.path.join(self.saida_path, "logNotificacoes.txt")
            arquivo = open(nomeArquivo, 'r', encoding='utf-8')
            texto = arquivo.readlines()
            arquivo.close()
            i = 0
            newData = []
            for t in texto:
                texto[texto.index(t)] = re.sub('[ ]{2}',' ',texto[texto.index(t)])
                texto[-1] = re.sub('[ ]{2}',' ',texto[-1])
                busca = re.search("(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{1,2}) (([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]) [0-9]{4}", t)
                if(busca):
                    if(i == 0):
                        i += 1
                        buscaUltimo = re.search("(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]{1,2}) (([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]) [0-9]{4}", texto[-1])
                        if(buscaUltimo):
                            ultimo = buscaUltimo.group()
                    atual = busca.group()
                    resultDateTime =  datetime.datetime.strptime(ultimo, '%a %b %d %H:%M:%S %Y') - datetime.datetime.strptime(atual, '%a %b %d %H:%M:%S %Y')
                    if(resultDateTime.days <= 30):
                        newData.append(t)
            arquivo = open(nomeArquivo, 'w', encoding='utf-8')
            arquivo.truncate(0)
            arquivo.writelines(newData)
            arquivo.close()
        except Exception as err:
            print("ERRO (verificaLogNotificacoes): {}".format(err))
            os.system('pause')

    def verificaMangasLogDelete(self):
        try:
            nomeArquivo = os.path.join(self.saida_path, "logDeleteCaps.txt")
            arquivo = open(nomeArquivo, 'r', encoding='utf-8')
            texto = arquivo.readlines()
            arquivo.close()
            mangas = {}
            for t in texto:
                texto[texto.index(t)] = re.sub('[ ]{2}',' ',texto[texto.index(t)])
                texto[-1] = re.sub('[ ]{2}',' ',texto[-1])
                buscaUltimoLido = re.search('\[[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\']*\]', t) #pylint: disable=anomalous-backslash-in-string
                buscaManga  = re.search('<[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\']*>', t)  #pylint: disable=anomalous-backslash-in-string
                buscaCaps = re.search('\{[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\']*\}', t) #pylint: disable=anomalous-backslash-in-string
                if(buscaCaps):
                    listaCaps = re.findall('([0-9]+\.?[0-9]*)',buscaCaps.group(0)) #pylint: disable=anomalous-backslash-in-string
                    if(buscaUltimoLido):
                        ultimoLido = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?',buscaUltimoLido.group()) #pylint: disable=anomalous-backslash-in-string
                        if(ultimoLido):
                            listaCaps.append(ultimoLido.group())
                    if(buscaManga):
                        if(mangas.get(buscaManga.group()[1:-1])):
                            mangas[buscaManga.group()[1:-1]].extend(listaCaps)
                            mangas[buscaManga.group()[1:-1]] = sorted(set(mangas[buscaManga.group()[1:-1]]), key=lambda v: self.common.ordenateStringNum(v))
                        else:
                            mangas.update({buscaManga.group()[1:-1]:listaCaps})
            self.mangasDeletados = mangas
        except Exception as err:
            print('ERRO (verificaMangasLogDelete): {}'.format(err))
            os.system('pause')

    def verificaCompletados(self):
        try:
            arquivo_entrada = (os.path.join(self.arquivo_entrada, 'completados.txt'))
            if(os.path.isfile(arquivo_entrada)):
                arquivo = open(arquivo_entrada, 'r')
                completados = [x.replace('\n', '') for x in arquivo.readlines()]
            arquivo.close()
            return completados
        except Exception as err:
            print('ERRO (verificaCompletados): {}'.format(err))

    def getBaixados(self):
        try:
            baixados = []
            nomeArquivo = os.path.join(self.saida_path, "logMangasBaixados.txt")
            arquivo = open(nomeArquivo, 'r', encoding='utf-8')
            texto = arquivo.readlines()
            arquivo.close()
            for t in texto:
                busca = re.search(r'\[[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\']*\]', t)
                if(busca):
                    manga = busca.group()
                    manga = manga.replace('[', '')
                    manga = manga.replace(']', '')
                    baixados.append(manga)
            return baixados
        except Exception as err:
            print('ERRO (getBaixados): {}'.format(err))
            os.system('pause')

    def verifyGenero(self, generos):
        try:
            for g in generos:   
                param = g.get('href').split('=')[-1]
                if(self.common.isNumber(param)):
                    param = int(param)
                else:
                    return False
                if(param in self.exclude_generos_bh):
                    return False
            return True
        except Exception as err:
            print('ERROR: {0}'.format(err))
            os.system('pause')

    def getLinkBH(self, div, filter_links=False):
        try:
            links = []
            for d in div:
                # autor = d.find('span', 'views-label views-label-field-autor')
                # if(len(autor.nextSibling.contents)>1):
                #     for a in autor.nextSibling.contents:
                #         artistas.update({a: [autor.nextSibling.get('href')]})
                # else:
                #     artistas.update({autor.nextSibling.string: [autor.nextSibling.get('href')]})
                try:
                    generos = [x for x in d.find('div', class_='views-field views-field-term-node-tid').find('span', 'field-content').find_all('a') if('/categoria/' not in x.get('href'))]
                except Exception:
                    generos = [x for x in d.find('div', class_='views-field views-field-term-node-tid-1').find('span', 'field-content').find_all('a') if('/categoria/' not in x.get('href'))]
                    # generos = [x.get('href') for x in generos]
                if filter_links:
                    if(generos):
                        if(self.verifyGenero(generos)):
                            content = d.find('div', class_='views-field views-field-title')
                            postedBy = d.find('div', class_='views-field views-field-field-traduzido-porv2-doujinshis')
                            if(postedBy):
                                if(postedBy.a):
                                    if(postedBy.a.string != 'FAKKU'):
                                        links.append(content.span.a.get('href'))
                            else:
                                links.append(self.initURLBH + content.span.a.get('href'))
                    else:
                        links.append(self.initURLBH + content.span.a.get('href'))
                else:
                    links.append(self.initURLBH + content.span.a.get('href'))
            return links
        except Exception as err:
            print('ERRO (getLinkBH): {}'.format(err))
            os.system('pause')

    def getLinksToTxtBH(self, url):
        try:
            # artistas = {}
            site = self.common.soup(url=url)
            """ driver = webdriver.Chrome(options=self.common.optionsChrome(headless=True))
            driver.get(url)
            elements = driver.find_elements_by_tag_name('select')
            for s in elements:
                select = Select(elements[0])
                selected_option = select.first_selected_option
                if selected_option.text != '- Qualquer -':
                    break
            driver.close() """
            selects = site.find_all('select')
            for select in selects:
                option = select.find('option', selected='selected')
                if option.text  != '- Qualquer -':
                    break
            div = site.find_all('div', class_='views-row')
            pager = site.find('ul', class_ = 'pager')
            tipo = site.find(class_='active')
            if(tipo):
                tipo = tipo.string
            else:
                busca = re.search(r'\/(\w)+\?', url)
                if(busca):
                    tipo = busca.group()
                    tipo = tipo.replace('?', '')
                    tipo = tipo.replace('/', '')
            links = []
            complete_path = os.path.join(self.dir_path, 'saida\\BH-links-{}-{}.txt'.format(tipo.lower(), option.text))
            if(pager):
                nextPage = pager.find('li', class_ = 'pager-next')
                currentPage = pager.find('li', class_ = 'pager-current')
                while currentPage.string:
                    links.extend(self.getLinkBH(div))
                    if nextPage:
                        site = self.common.soup(url= self.initURLBH + nextPage.a.get('href'))
                        div = site.find_all('div', class_ = 'views-row')
                        pager = site.find('ul', class_ = 'pager')
                        nextPage = pager.find('li', class_ = 'pager-next')
                        currentPage = pager.find('li', class_ = 'pager-current')
                    else:
                        break
            else:
                links.extend(self.getLinkBH(div))
            if(links):
                with open(complete_path, 'w', encoding='utf-8') as archive:
                    for l in links:
                        if(self.initURLBH not in l):
                            archive.writelines('{}\n'.format(self.initURLBH+l))
                        else:
                            archive.writelines('{}\n'.format(l))
                print('Arquivo salvo em: {}'.format(complete_path))
            else:
                print('SEM LINKS')
        except Exception as err:
            print('ERROR (getLinksToTxtBH): {0}'.format(err))
            os.system('pause')

    def getLinkCodigoBH(self, codigo):
        try:
            links = [
                [
                'http://baixarhentai.net/one-shots?autor='+codigo,
                'http://baixarhentai.net/one-shots?autor='+codigo,
                'http://baixarhentai.net/one-shots?circulo='+codigo,
                'http://baixarhentai.net/one-shots?genero='+codigo,
                'http://baixarhentai.net/one-shots?tradutor='+codigo
                ],
                [
                    'http://baixarhentai.net/doujinshis?autor='+codigo,
                    'http://baixarhentai.net/doujinshis?autor='+codigo,
                    'http://baixarhentai.net/doujinshis?circulo='+codigo,
                    'http://baixarhentai.net/doujinshis?genero='+codigo,
                    'http://baixarhentai.net/doujinshis?tradutor='+codigo
                ],
                [
                    'http://baixarhentai.net/h-mangas?autor='+codigo,
                    'http://baixarhentai.net/h-mangas?circulo='+codigo,
                    'http://baixarhentai.net/h-mangas?genero='+codigo,
                    'http://baixarhentai.net/h-mangas?tradutor='+codigo
                ]
            ]
            tipo = None
            link = None
            while tipo != 0:
                print('1 - One-Shots\n2 - Doujinshis\n3 - H-Mangás\n0 - Voltar')
                tipo = self.common.whileDataTypeReadString(int)
                if tipo == 3:
                    print('1 - Autor\n2 - Circulo\n3 - Genero\n4 - Tradutor\n0 - Voltar')
                elif tipo == 0:
                    return 
                else:
                    print('1 - Serie\n2 - Autor\n3 - Circulo\n4 - Genero\n5 - Tradutor\n0 - Voltar')
                link = self.common.whileDataTypeReadString(int)
                if link == 0:
                    continue
                self.getLinksToTxtBH(links[tipo-1][link-1])
        except Exception as err:
            print('ERRO (getLinkCodigoBH): {}'.format(err))

    def getLinksHC(self, url, feature):
        try:
            # categorias = {'oneshot': [], 'doujinshi': [], 'h-mangá': [], 'hqs': [], 'mangá': [], 'manga': [], 'manhwa': [], 'manhua': [], 'artist cg': []}
            artistas = {}
            site = self.common.soup(feature, url)
            divP = site.find_all('div', class_='buttons')
            pages = []
            for p in divP[0].contents:
                pages.append(p.get('href'))
            nextPage = pages[0]
            fim = divP[0].find_all('a')[-1]
            i = 0
            while len(fim.get('class')) < 3:
                divP = site.find_all('div', class_='buttons')
                conteudo = site.find_all('a', class_='news-thumb')
                for c in conteudo:
                    categoria, artista = self.getCategoriaTagsHC(self.initURLHC + c.get('href'), feature, 1)
                    if(categoria):
                        self.categoriasDicHC.get(categoria).append(self.initURLHC + c.get('href'))
                        self.categoriasDicHC[categoria] = list(set(self.categoriasDicHC[categoria]))
                        if(type(artista) == list):
                            for a in artista: #pylint: disable=not-an-iterable
                                if(not artistas.get(a)):
                                    artistas.update(a)
                                else:
                                    continue
                        else:
                            artistas.update(artista)
                        
                i += 1
                if pages != divP[0].contents:
                    for p in divP[0].contents:
                        if p.get('href') not in pages:
                            pages.append(p.get('href'))
                if i < len(pages):
                    nextPage = pages[i]
                fim = divP[0].find_all('a')[-1]
                site = self.common.soup(feature, self.initURLHC + nextPage)
            # self.salvarArquivoArtistas(artistas, url.split('/')[-1], 'HC')
            choice = self.common.readString('Deseja gerar arquivo dos artistas?\n=> ')
            if(choice == 'sim' or choice == '1' or choice == 's' or choice == 'SIM' or choice == 'S'):
                self.getLinksHCArtista(artistas, 'link-'+url.split('/')[-1])
            self.salvarArquivoCategorias(self.categoriasDicHC,'HC', 'link-'+url.split('/')[-1])
            for c in self.categoriasDicHC:
                self.categoriasDicHC[c] = []
        except Exception as err:
            print('ERROR (getLinksHC): {0}'.format(err))
            os.system('pause')

    def getLinksHS(self, url):
        try:
            url.endswith
            # links = []
            artistas = {}
            site = self.common.soup(self.feature, url)
            ulsP = site.find_all('ul', class_='paginacao')
            try:
                nextPage = ulsP[0].find_all('a')[-1]
                while nextPage.text == 'Próxima página »':
                    ulsP = site.find_all('ul', class_='paginacao')
                    conteudo = site.find_all('div', class_='thumb-conteudo')
                    for c in conteudo:
                        if c.a:
                            categoria, artista = self.getCategoriaTagsHS(c.a.get('href'), 1)
                            if categoria:
                                self.categoriasDicHS[categoria].append(c.a.get('href'))
                            else:
                                continue
                            if(artista):
                                artistas.update(artista)
                                # links.append(c.a.get('href'))
                    nextPage = ulsP[0].find_all('a')[-1]
                    site = self.common.soup(self.feature, nextPage.get('href'))
            except Exception as err:
                print('ERRO (getLinksHS): {}'.format(err))
                os.system('pause')
                # ulsP = site.find_all('ul')
                # conteudo = site.find_all('div', class_='thumb-conteudo')
                # for c in conteudo:
                #     if c.a:
                #         links.append(c.a.get('href'))
            choice = self.common.readString('Deseja gerar arquivo dos artistas?\n=> ')
            if(choice == 'sim' or choice == '1' or choice == 's' or choice == 'SIM' or choice == 'S'):
                self.getLinksHCArtista(artistas, 'link-'+url[:-1].split('/')[-1])
            self.salvarArquivoCategorias(self.categoriasDicHS, 'HS', url[:-1].split('/')[-1])
            for c in self.categoriasDicHS:
                self.categoriasDicHS[c] = []
        except Exception as err:
            print('ERRO (getLinksHS): {}'.format(err))

    def getCategoriaTagsHC(self, url, feature, op):
        try:
            categoria = None
            site = self.common.soup(feature, url)
            div = site.find_all('div', class_='tag')
            categoria = 'uncategorized'
            artistas = {}
            namesArtistas = []
            categorias = {'oneshot': [], 'doujinshi': [], 'paródia':[], 'h-mangá': [], 'h-manga': [], 'hqs': [], 'mangá': [], 'manga': [], 'manhwa': [], 'manhua': [], 'artist cg': [], 'uncategorized': []}
            for d in div:
                if(d.a):
                    if(d.span):
                        if(d.span.string == 'Artista:'):
                            linksA = d.find_all('a', class_='value')
                            if(len(linksA) > 1):
                                for l in linksA:
                                    nameArtist = l.string.replace(' ', '_')
                                    namesArtistas.append(nameArtist)
                                    artista = {l.string.replace(' ', '_'): {self.initURLHC+l.get('href'): categorias}}
                                    artistas.update(artista)
                            else:
                                nameArtist = linksA[0].string.replace(' ', '_')
                                artista = {linksA[0].string.replace(' ', '_'): {self.initURLHC+linksA[0].get('href'): categorias}}
                        elif('Artista:' not in [x.span.string for x in div]):
                            artista = {'sem_artista': None}
                    if(d.span.string == 'Categoria:'):
                        if(d.a.string in self.categoriasHC):
                            if(d.a.string == 'H-Mangá' or d.a.string == 'H-Mnagá'):
                                categoria = 'H-Manga'
                            elif(d.a.string == 'Mangá'):
                                categoria = 'Manga'
                            else:
                                categoria = d.a.string
                        else:
                            categoria = 'uncategorized'
                    if(d.span.string == 'Tags:'):
                        links = d.find_all('a')
                        links = [self.initURLHC + x.get('href') for x in links if x.get('href')]
                        intersection = list(set(links).intersection(self.exclude_url_hc))
                        newExclude = ['https://hiper.cool/tags/shota-gay', 'https://hiper.cool/tags/yaoi', 'https://hiper.cool/tags/travesti']
                        if(intersection):
                            newIntersection = list(set(links).intersection(newExclude))
                            if(newIntersection):
                                if(len(links) < 10):
                                    if(op == 1):
                                        return False, False
                                    if(op == 0):
                                        return False
                                else:
                                    if(op == 1):
                                        return False, False
                                    if(op == 2):
                                        return False, False
                                    if(op == 0):
                                        return False

                else:
                    categoria = 'uncategorized'
            if(op == 1):
                if(isinstance(categoria, str)):
                    if(len(artistas) > 1):
                        return categoria.lower(), artistas
                    else:
                        return categoria.lower(), artista
            if(op == 2):
                if isinstance(categoria, str):
                    if(len(namesArtistas) > 1):
                        return categoria.lower(), namesArtistas
                    else:
                        return categoria.lower(), nameArtist
            if(op == 0):
                if isinstance(categoria, str):
                    return categoria.lower()
        except Exception as err:
            print('ERROR (getCategoriaTags): {0}'.format(err))
            os.system('pause')

    def verifyHomeHManga(self, op):
        choice = -1
        self.common.clearTerminal()
        while True:
            try:
                t_0 = self.common.initCountTime()
                pages = int(self.common.readString('Digite a quantidade de página ser verificada: '))
                if(pages == -1):
                    self.common.shutDown()
                elif(pages == 0):
                    break
                print('1 - para HiperCool\n2 - para Hentai Season\n3 - para BH')
                choice = int(self.common.readString())
                if(choice == 0):
                    continue
                elif(choice == -1):
                    self.common.shutDown()
                elif(choice == 1):
                    choice2 = self.common.readString('Deseja gerar arquivo de artista?\n=>')
                    url = self.initURLHC + '/home'
                    self.verifyHomeHC(pages, url, op, choice2)
                    self.finishinMusic()
                elif(choice == 2):
                    url = self.initURLHS + '/page'
                    choice2 = self.common.readString('Deseja gerar arquivo de artista?\n=>')
                    self.verifyHomeHS(pages, url, op, choice2)
                    self.finishinMusic()
                elif(choice == 3):
                    url = self.initURLBH + '/inicio'
                    self.verifyHomeBH(pages, url)
                    self.finishinMusic()
                t_f = self.common.finishCountTime(t_0)
                segundos = t_f % 60
                minutos  = int(t_f / 60)
                print('Executado em: {} minutos e {} segundos'.format(minutos, segundos))
            except Exception as err:
                print('Error (verifyHomeHManga): {0}'.format(err))
                os.system('pause')
    
    def verifyHomeHS(self, pages, url, op, op2):
        try:
            artistas = {}
            for i in range(1, pages+1):
                site = self.common.soup(feature='html.parser',url=url+str(i))
                print('Visitando página {}'.format(i))
                conteudo = site.find_all('div', class_='thumb-conteudo')
                for c in conteudo:
                    novo = c.find('span', class_='selo-novo')
                    if(op == 1):
                        if(not novo):
                            break
                    tag_a = c.find('a')
                    categoria, artista = self.getCategoriaTagsHS(tag_a.get('href'), 1)
                    if(categoria):
                        self.categoriasDicHS.get(categoria).append(tag_a.get('href'))
                    if(artista):
                        artistas.update(artista)
                    else:
                        continue
            if(op == 1):
                self.salvarArquivoCategorias(self.categoriasDicHS, 'HS', 'NewLinks-pages={}'.format(pages))
                if(op2 == '1'):
                    self.getLinksHSArtista(artistas, 'NewLinks')
            if(op == 2):
                self.salvarArquivoCategorias(self.categoriasDicHS, 'HS', 'Links-pages={}'.format(pages))
                if(op2 == '1'):
                    self.getLinksHSArtista(artistas, 'Links')
        except Exception as err:
            print('ERROR (verifyHomeHS): {0}'.format(err))
            os.system('pause')
    
    def verifyHomeBH(self, pages, url):
        try:
            hentais = {'H-Mangás':[],'One-Shots':[],'Doujinshis':[], 'Hentais':[],'None':[]}
            links = []
            list_divs = []
            driver = webdriver.Chrome(options=self.common.optionsChrome(headless=True))
            driver.get(url)
            for i in range(1, pages+1): 
                print('Visitando página {}'.format(i))
                proximo = driver.find_elements_by_class_name('pager-next')
                html = driver.page_source
                if(proximo):
                    proximo[0].click()
                    time.sleep(3)
                    site = self.common.soup(markup=html)
                    divs = site.find_all('div', class_='englobadora')
                    if(divs):
                        list_divs.extend(divs)
                else:
                    print('Pager next não encontrado nº {}'.format(i))
            links.extend([x.a.get('href') for x in list_divs if(x.a) if('episodio-online' not in x.a.get('href'))]) #extrai todos links
            links = list(set(links)) # retirando elementos repetidos
            driver.close()
            # visitando cada link verificando o tipo e traduzido por
            for l in links:
                site = self.common.soup(url=l)
                span = site.find('span', class_='inline even')
                divs_bhd = site.find_all('div', class_='campo-bhd7')
                traduzidoPor = [x for x in divs_bhd if(re.search('Traduzido por:', x.text))]
                generos = [x for x in divs_bhd if(re.search('Gêneros:', x.text))]
                if(span):
                    l = l.replace('https','http')
                    if(generos):
                        if(self.verifyGenero(generos[0].find_all('a'))):
                            if(traduzidoPor):
                                if(traduzidoPor[0].a.text != 'FAKKU'):
                                    hentais[span.text].append(l)
                            else:
                                hentais[span.text].append(l)
                    else:
                        hentais[span.text].append(l)
                else:
                    hentais['None'].append(l)
            self.salvarArquivoBH(hentais, 'BH', 'inicio-pages={}'.format(pages))
        except Exception as err:
            print('ERRO (verifyHomeBH): {}'.format(err))
            os.system('pause')

    def salvarArquivoBH(self, hentais, primeiro_nome, segundo_nome):
        try:
            data = OrderedDict()
            for h in hentais:
                coluna = [[x] for x in hentais[h]]
                data.update({h:coluna})
            complete_path = os.path.join(self.saida_path, '{}-{}.ods'.format(primeiro_nome, segundo_nome))
            pods.save_data(complete_path, data)
            print('Arquivo salvo em: {}'.format(complete_path))
        except Exception as err:
            print('ERRO (salvarArquivoBH): {}'.format(err))
            os.system('pause')

    def getCategoriaTagsHS(self, url, op):
        try:
            artista = None
            categoriasA = {'one-shot': [], 'doujin': [], 'h-manga': [], 'uncategorized': [], 'pack-de-imagens': [], 'familia-sacana':[]}
            site = self.common.soup(feature='html.parser', url=url)
            # site = self.common.soup(feature='html.parser', url='https://hentaiseason.com/2019/11/27/ur-poison/')
            ul = [x for x in site.find('ul', class_='post-itens').contents if x != '\n' if x != ' ' if x != ''] 
            eita = False
            for u in ul:
                if('Tags' in u.text):
                    textos = u.text.split(' ')
                    tags_a = u.find_all('a')
                    for a in tags_a:
                        if a.get('href') in self.exclude_urls_hs:
                            eita = True
                            break
                if('Categorias' in u.text):
                    if u.a.get('href') in self.exclude_urls_hs:
                        eita = True
                        break
                    textos = u.text.split(' ')
                    if(len(textos) > 2):
                        categoria = '-'.join(map(str, textos[1:])).lower()
                    else:
                        categoria = textos[1].lower()
                # agora pegar links do artista
                if('Artista' in u.text):
                    textos = [x for x in u.text.split(' ') if x != '' if x != ' ']
                    if(len(textos) > 2):
                        art = '-'.join(map(str, textos[1:])).lower()
                    else:
                        art = textos[1].lower()
                    link_art = [x for x in u.contents if x != '\n' if x != ' ' if x != ''] 
                    artista = {art: {link_art[-1].get('href'): categoriasA}}
                    # if(not eita):
                    #     artistas.update(artista)
                    #     self.categoriasDicHS.get(categoria).append(link_categoria)
            if(not artista):
                artista = {'Sem-autor':{'sem-autor': categoriasA}}
            if(not eita):
                if(op == 1):
                    return categoria, artista
                elif(op == 0):
                    return categoria
            else:
                if(op == 1):
                    return None, None
                elif(op == 0):
                    return None
        except Exception as err:
            print('ERROR (getCategoriaTagsHS): {0}'.format(err))
            os.system('pause')

    def getLinksHSArtista(self, artistas, nome):
        try:
            
            links = []
            for a in artistas:
                for url in artistas[a]:
                    if(re.match(self.regex_urlWEB, url) is None):
                        continue
                    site = self.common.soup(feature=self.feature, url=url)
                    ulsP = site.find_all('ul', class_='paginacao')
                    try:
                        nextPage = ulsP[0].find_all('a')[-1]
                        while nextPage.text == 'Próxima página »':
                            ulsP = site.find_all('ul', class_='paginacao')
                            conteudo = site.find_all('div', class_='thumb-conteudo')
                            for c in conteudo:
                                if c.a:
                                    search = re.search('hentaiseason', c.a.get('href'))
                                    if(search):
                                        links.append(c.a.get('href'))
                            
                            nextPage = ulsP[0].find_all('a')[-1]
                            site = self.common.soup(self.feature, nextPage.get('href'))
                    except Exception:
                        ulsP = site.find_all('ul')
                        conteudo = site.find_all('div', class_='thumb-conteudo')
                        for c in conteudo:
                            if c.a:
                                search = re.search('hentaiseason', c.a.get('href'))
                                if(search):
                                    links.append(c.a.get('href'))
                    for l in links:
                        categoria = self.getCategoriaTagsHS(l, 0)
                        if(categoria):
                            artistas[a][url][categoria].append(l)
                    links = []
            self.salvaNewArquivoArtistas(artistas, 'HS', nome)
        except Exception as err:
            print('ERROR (getLinksHSArtista): {0}'.format(err))
            os.system('pause')
    
    def salvaNewArquivoArtistas(self, artistas, primeiro_nome,segundo_nome):
        try:
            for art in artistas:
                data = OrderedDict()
                for a in artistas[art]:
                    for c in artistas[art][a]:
                        if(artistas[art][a][c]):
                            if(c != 'manhua' and c != 'manhwa' and c != 'mangá' and c != 'manga'):
                                links = list(set(artistas[art][a][c]))
                                coluna = [[x] for x in links]
                                data.update({c:coluna})
                if(data):
                    path = self.criarPastaManga('saida', self.dir_path)[0]
                    complete_path = os.path.join(path, '{}_artista_{}_{}.ods'.format(primeiro_nome,segundo_nome, art))
                    pods.save_data(complete_path, data)
                    print('Arquivo salvo em: {}'.format(complete_path))
                        # complete_path = os.path.join(self.dir_path, 'saida\\links{}_{}_{}.txt'.format(nome, art, c))
                        # if(links):
                        #     with open(complete_path, 'w', encoding='utf-8') as archive:
                        #         for l in links:
                        #             archive.writelines(l+'\n')
                        #     print('Arquivo salvo em: {}'.format(complete_path))
        except Exception as err:
            print('ERROR (salvaTxtArtistas): {0}'.format(err))
            os.system('pause')
    
    def salvarArquivoArtistas(self, artistas, primeiro_nome,segundo_nome):
        try:
            data = OrderedDict()
            for a in artistas:
                coluna = [[x] for x in artistas[a]]
                data.update({a: coluna})
            complete_path = os.path.join(self.saida_path, 'links-{}-artistas-{}.ods'.format(primeiro_nome,segundo_nome))
            pods.save_data(complete_path, data)
            print('Arquivo salvo em: {}'.format(complete_path))
        except Exception as err:
            print('ERRO (salvarArquivoArtistas): {}'.format(err))
    
    def salvarArquivoCategorias(self, categorias, primeiro_nome,segundo_nome):
        try:
            data = OrderedDict()
            for c in categorias:
                if categorias.get(c):
                    categorias[c] = list(set(categorias.get(c)))
                    coluna = [[x] for x in categorias[c]]
                    data.update({c:coluna})
                    # complete_path = os.path.join(self.dir_path, 'saida\\NewLinks{}_{}.txt'.format(nome,c))
                    # with open(complete_path, 'w', encoding='utf-8') as archive:
                    #     for l in categorias.get(c):
                    #         archive.writelines(l+'\n')
                    # print('Arquivo salvo em: {}'.format(complete_path))
            
            complete_path = os.path.join(self.saida_path, '{}-{}.ods'.format(primeiro_nome, segundo_nome))
            pods.save_data(complete_path, data)
            print('Arquivo salvo em: {}'.format(complete_path))
            # os.system('pause')
        except Exception as err:
            print('ERROR (salvarTxtCategorias): {0}'.format(err))
            os.system('pause')
    
    def verifyHomeHC(self, pages, url, op, op2):
        try:
            artistas = {}
            t_o = self.common.initCountTime()
            for i in range(1, pages + 1):
                site = self.common.soup(self.feature, '{}/{}'.format(url,i))
                print('Visitando página {}'.format(i))
                conteudo = site.find_all('li')
                for c in conteudo:
                    today = c.find('div', class_='today')
                    if(op == 1):
                        if(not today):
                            break
                    if(c.a):
                        categoria, artista = self.getCategoriaTagsHC('{}{}'.format(self.initURLHC, c.a.get('href')), self.feature, 1)
                        if(artista):
                            artistas.update(artista)
                        if(categoria):
                            self.categoriasDicHC.get(categoria).append(self.initURLHC + c.a.get('href'))
                    else:
                        break
            if(op == 1):
                self.salvarArquivoCategorias(self.categoriasDicHC, 'HC', 'NewLinks-pages={}'.format(pages))
                if(op == '1'):
                    self.getLinksHCArtista(artistas, 'NewLinks')
            else:
                self.salvarArquivoCategorias(self.categoriasDicHC, 'HC', 'Links-pages={}'.format(pages))
                if(op == '1'):
                    self.getLinksHCArtista(artistas, 'Links')
            t_f = self.common.finishCountTime(t_o)
            segundos = t_f % 60
            minutos  = int(t_f / 60)
            print('Executado em {} minutos e {} segundos'.format(minutos, segundos))
        except Exception as err:
            print('ERROR (verifyHomeHC): {0}'.format(err))
            os.system('pause')
    
    def getLinksHCArtista(self, artistas, nome):
            categoria = None
            for art in artistas:
                for a in artistas[art]:
                    if(a):
                        try:
                            site = self.common.soup(self.feature, a)
                            divP = site.find_all('div', class_='buttons')
                            pages = []
                            for p in divP[0].contents:
                                pages.append(p.get('href'))
                            nextPage = pages[0]
                            fim = divP[0].find_all('a')[-1]
                            i = 0
                            while len(fim.get('class')) < 3:
                                divP = site.find_all('div', class_='buttons')
                                conteudo = site.find_all('a', class_='news-thumb')
                                for c in conteudo:
                                    categoria = self.getCategoriaTagsHC(self.initURLHC+c.get('href'), self.feature, 0)
                                    if(categoria):
                                        artistas[art][a][categoria].append(self.initURLHC+c.get('href'))
                                i += 1
                                if pages != divP[0].contents:
                                    for p in divP[0].contents:
                                        if p.get('href') not in pages:
                                            pages.append(p.get('href'))
                                if i < len(pages):
                                    nextPage = pages[i]
                                fim = divP[0].find_all('a')[-1]
                                site = self.common.soup(self.feature, self.initURLHC + nextPage)
                        
                        except Exception as err:
                            print("error (getLinksHCArtista): {0}".format(err))
                            os.system('pause')
                    
            self.salvaNewArquivoArtistas(artistas, 'HC', nome)

    """ def pesquisaMangaInMAL(self, nome):
        try:
            site = self.common.soup(url=self.url_search_manga+nome)
            mangas = site.find_all('a', class_='hoverinfo_trigger fw-b')
            for m in mangas:
                site = self.common.soup(url=m.get('href'))
                td = site.find('td', class_='borderClass')
                spaceit_pad = td.find_all('div', class_='spaceit_pad')
                print()
                parent_manga = m.parent.find('a', class_='Lightbox_AddEdit button_edit reading')
                if(parent_manga):
                    print('ok')
                else:
                    print('not ok')
            return mangas[0].string
        except Exception as err:
            print('ERRO (pesquisaMangaInMAL): {}'.format(err)) """

    def criarPastaManga(self, name, path):
        try:
            name = name.replace(':', '-')
            directory = os.listdir(path)
            complete = os.path.join(path, name)
            # print(complete)
            if(name not in directory):
                if not os.path.isdir(complete):
                    os.mkdir(complete)
                    return complete, False
                return complete, False
            else:
                print('Diretório {} existente'.format(complete))
                return complete, True
        except Exception as err:
            print('ERROR (criarPastaManga): {0}'.format(err))
            os.system('pause')

    def criarPastaCap(self, path, id):
        try:
            name = 'cap_{}'.format(id)
            directory = os.listdir(path)
            if name not in directory:
                complete = os.path.join(path, name)
                if not os.path.isdir(complete):
                    os.mkdir(complete)
                    return complete
                else:
                    print('Diretório {} existente'.format(complete))
                    return None
        except Exception as err:
            print('ERROR (criarPastaCap): {0}'.format(err))
            os.system('pause')

    def criarPastaCapCompLen(self, path, id, lenght, initCap=None):
        try:
            try:
                id = int(id)
            except:
                try:
                    id = float(id)
                except:
                    if(re.search(r'Oneshot|Oneeshot|Oneshoot|Onneshot', id, flags=re.IGNORECASE)):
                        id = 0
            if(not initCap):
                name = 'cap_{}'.format(id)
            else:
                name = str(id)
            directory = os.listdir(path)
            if name not in directory:
                complete = os.path.join(path, name)
                if not os.path.isdir(complete):
                    os.mkdir(complete)
                    return complete
                else:
                    print('Diretório {} existente'.format(complete))
                    return None
            else:
                path_existent = os.path.join(path, name)
                dir_path_ex = os.listdir(path_existent)
                if(len(dir_path_ex) < lenght):
                    shutil.rmtree(path_existent)
                    os.mkdir(path_existent)
                    return path_existent
                else:
                    print('Diretório {} existente'.format(path_existent))
                    return None
        except Exception as err:
            print('ERROR (criarPastaCapCompLen): {0}'.format(err))
            os.system('pause')

    def logInUnion(self):
        alertLogin = None
        while True:
            print('É necessário informar suas credenciais para se comunicar com o site')
            # email = input('Email: ')
            email = 'bros_mario_rv@hotmail.com'
            password = '8Qk3LmcP'
            # password = getpass.getpass('Senha: ')
            self.login_data['email'] = email
            self.login_data['password'] = password
            s = requests.Session()
            r = s.get(self.url_login, headers=self.headers)
            site = self.common.soup('html.parser',request=r, headers=self.headers)
            if(site.title.text == 'Just a moment...'):
                print('Site indisponível')
                continue
            elif(site.title.text == 'unionleitor.top | 521: Web server is down'):
                while site.title.text == 'unionleitor.top | 521: Web server is down':
                    site = self.common.soup('html.parser',request=r, headers=self.headers)
            self.login_data['logar'] = site.find('input', attrs={'name': 'logar'})['value']
            r = s.post(self.url_login, data=self.login_data, headers=self.headers)
            alertLogin = self.common.soup(feature=self.feature, request=r).find('div', class_='alert alert-danger')
            successLogin = self.common.soup(feature=self.feature, request=r).find('div', class_='alert alert-success alert-dismissible')
            if(successLogin):
                print(successLogin.text.replace('\n×', ''))
                break
            elif(alertLogin):
                if (alertLogin.text == '\xa0Usuário ou senha inválidos'):
                    print(alertLogin.text)
        s.close()
        cookies = r.cookies
        return cookies, r

    def getMangaNewCapUnion(self):
        with webdriver.Chrome(options=self.common.optionsChrome(headless=False)) as driver:
            driver.get(self.url_login)
            email = 'bros_mario_rv@hotmail.com'
            password = '8Qk3LmcP'
            time.sleep(10)
            element =  driver.find_element_by_id('email')
            element.send_keys(email)
            time.sleep(10)
            element = driver.find_element_by_id('password')
            element.send_keys(password)
            time.sleep(10)
            element = driver.find_element_by_id('btn-enviar')
            element.click()
            time.sleep(10)
    
    def verificaNotificacoesUnion(self):
        t_o = self.common.initCountTime()
        try:
            x = 0
            y = 0
            limparNotificacoes = None
            cookies, r = self.logInUnion()
            site = self.common.soup('html.parser',request=r, headers=self.headers)
            while site.title.text == 'unionleitor.top | 521: Web server is down':
                site = self.common.soup('html.parser',request=r, headers=self.headers)
            dropdown = site.find('li', class_='dropdown').contents
            dropdown_clean = [x for x in dropdown if x != '\n' if x != ' ' if x != '']
            menus = [x for x in dropdown_clean[-1].contents if x != '\n' if x != ' ' if x != '']
            mangas = {}
            for li in menus:
                if(li.a):
                    if(li.a.get('href') == 'https://unionleitor.top/notificacoes'):
                        site = self.common.soup(feature='html.parser',url=li.a.get('href'), headers=self.headers, cookies=cookies)
                        while site.title.text == 'unionleitor.top | 521: Web server is down':
                            site = self.common.soup(feature='html.parser',url=li.a.get('href'), headers=self.headers, cookies=cookies)
                        alert = site.find('div', class_='alert alert-danger text-center')
                        if(alert):
                            print(alert.text)
                            arquivo = open(os.path.join(self.saida_path, "logNotificacoes.txt"), "a", encoding='utf-8')
                            arquivo.writelines(self.common.timestamp() + " " + alert.text + "\n")
                            arquivo.close()
                            break
                        else:
                            mangas, notificacoes, limparNotificacoes = self.getNotificacoes(site) #pylint: disable=unused-variable
                            x, y = self.salvarMangasNotificacoes(site,mangas)
                            newManga = []
                            while True:
                                site = self.common.soup(feature='html.parser',url=li.a.get('href'), headers=self.headers, cookies=cookies)
                                while site.title.text == 'unionleitor.top | 521: Web server is down':
                                    site = self.common.soup(feature='html.parser',url=li.a.get('href'), headers=self.headers, cookies=cookies)
                                newManga, notificacoes, limparNotificacoes = self.getNotificacoes(site)
                                if(len(newManga) == len(mangas)):
                                    break
                                else:
                                    x, y= self.salvarMangasNotificacoes(site,newManga)
                                    mangas, notificacoes, limparNotificacoes = self.getNotificacoes(site)
                            break
            t_f = self.common.finishCountTime(t_o)
            segundos = t_f % 60
            minutos  = int(t_f / 60)
            print('{} capitulos baixados de {} mangás em {} minutos e {} segundos'.format(x, y, minutos, segundos))
            if(limparNotificacoes):
                rq = requests.get(self.initURLUnion+limparNotificacoes, headers=self.headers,cookies=cookies)
                rq.close()
        except:
            print("Unexpected error (verificaNotificacoesUnion):", sys.exc_info()[0])
            os.system('pause')
            raise

    def getNotificacoes(self, site):
        try:
            notificacoes = site.find_all('div', class_='col-md-12 text-left')
            while site.title.text == 'unionleitor.top | 521: Web server is down':
                    site.find_all('div', class_='col-md-12 text-left')
            limparNotificacoes = site.find('a', class_='btn btn-primary pull-right').get('href')
            mangas = {}
            for i in notificacoes:
                item = i.find('div', class_='col-md-9')
                tags_b = item.find_all('b')
                link = item.find('a').get('href')
                # cap = tags_b[0].string.replace(' ', '_')
                cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tags_b[0].string).group(0) #pylint: disable=anomalous-backslash-in-string
                nome = re.sub('[\\/*?<>|]+', '',tags_b[1].string).replace(':', '-')
                nome = self.normalizeNameManga(nome)
                if(self.checkNameManga(nome)):
                    nome = self.checkNameManga(nome)
                # nome = ' '.join(re.findall('[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\']*', nome)) #pylint: disable=anomalous-backslash-in-string
                # nome = nome.strip()
                # if(nome == 'Iinchou, Sakki Toile de Onatteta desho ~Itta Kaisuu ga Barechau Sekai~'):
                #     nome = 'Committee Chairman'
                # if(nome == 'Rabuyu!'):
                #     nome = 'Love You'
                if(mangas.get(nome)):
                    mangas[nome].append(cap)
                    mangas[nome] = sorted(mangas[nome], key=lambda v: self.common.ordenateStringNum(v))
                    # mangas[nome] = list(set(lista + mangas[nome]))
                else: 
                    mangas.update({nome:sorted([link, cap])})
            return mangas, notificacoes, limparNotificacoes
        except Exception as err:
            print('ERRO (getNotificacoes): {0}'.format(err))
            os.system('pause')

    def salvarMangasNotificacoes(self, site, mangas):
        try:
            x = 0
            y = 0
            check = 0
            unionPasta = self.criarPastaManga('Union', self.mangaPasta)
            with open(os.path.join(self.saida_path, "logNotificacoes.txt"), "a", encoding='utf-8') as arquivo:
                arquivo.writelines(self.common.timestamp() + ' ')
                ultimaChave = list(mangas.keys())[-1]
                for k in mangas:
                    check = 0
                    # manga_path = self.criarPastaManga(k, self.mangaPasta)
                    site = self.common.soup('html.parser', url=mangas[k][-1])
                    caps = site.find_all('div', class_='col-xs-6 col-md-6')
                    if(ultimaChave == k):
                        arquivo.writelines('Mangá: <{}> - Capitulos: [{}]'.format(k, ', '.join(mangas[k][:-1])))
                    else:
                        arquivo.writelines('Mangá: <{}> - Capitulos: [{}], '.format(k, ', '.join(mangas[k][:-1])))
                    text = "-1"
                    i = 0
                    while text != mangas[k][0]:
                        text = re.sub('Cap. ', '', caps[i].find('a', class_='').string)
                        text = text.replace(' ', '_')
                        text = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', text).group(0) #pylint: disable=anomalous-backslash-in-string
                        if(text != mangas[k][0]):
                            mangas[k].append(text)
                            mangas[k] = sorted(set(mangas[k]), key=lambda v: self.common.ordenateStringNum(v))
                            total_caps = len(mangas[k][:-1])
                        i += 1
                    """ for c in caps:
                        # index = caps.index(c)
                        text = re.sub('Cap. ', '', c.find('a', class_='').string)
                        text = text.replace(' ', '_')
                        if(text in mangas[k]):
                            total_caps = 1 + len(mangas[k][:-1])
                            pega_ultimo_lido = len(mangas[k][:-1])
                            id_ultimo_lido = caps[pega_ultimo_lido].find('a', class_='').string.replace('Cap. ', '')
                            mangas[k].append(id_ultimo_lido)
                            mangas[k] = sorted(mangas[k], key=lambda v: self.common.ordenateStringNum(v))
                            # cap_path = self.criarPastaCap(manga_path, )
                            # link_ultimo_lido = caps[pega_ultimo_lido].find('a', class_='').get('href') """
                    total_caps = 1 + len(mangas[k][:-1])
                    mangasLog = []
                    for c in caps[:total_caps]:
                        id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', c.find('a', class_='').string) #pylint: disable=anomalous-backslash-in-string
                        if(id_cap):
                            mangaPath= self.criarPastaManga(k, unionPasta)[0]
                        # id_capitulo = c.find('a', class_='').string.replace('Cap. ', '').replace(' ', '_')
                        url_capitulo = c.find('a', class_='').get('href')
                        site = self.common.soup(feature=self.feature, url=url_capitulo)
                        while site.title.text == 'unionleitor.top | 521: Web server is down':
                            site = self.common.soup(feature=self.feature, url=url_capitulo)
                        imgs = site.find_all('img',class_='img-manga')[2:]
                        if(self.mangasDeletados.get(k)):
                            if(id_cap.group() not in self.mangasDeletados.get(k)):
                                complete_path = self.criarPastaCapCompLen(mangaPath,id_cap.group(), len(imgs))
                                if(complete_path):
                                    if(len(imgs) > 0):
                                        self.downloadsImgs(imgs, complete_path)
                                        # print(k + ':' + id_capitulo)
                                        x += 1
                                        check += 1
                                        mangasLog.append(id_cap.group())
                                    else:
                                        site = self.common.soup(feature=self.feature, url=url_capitulo)
                                        while site.title.text == 'unionleitor.top | 521: Web server is down':
                                            site = self.common.soup(feature=self.feature, url=url_capitulo)
                                        imgs = site.find_all('img',class_='img-manga')[2:]
                                        self.downloadsImgs(imgs, complete_path)
                                        # print(k + ':' + id_capitulo)
                                        x += 1
                                        check += 1
                                        mangasLog.append(id_cap.group())
                                else:
                                    continue
                                print()
                            else:
                                print('O capitulo {} consta no logDelete'.format(id_cap.group()))
                        else:
                            complete_path = self.criarPastaCapCompLen(mangaPath,id_cap.group(), len(imgs))
                            if(complete_path):
                                self.downloadsImgs(imgs, complete_path)
                                # print(k + ':' + id_capitulo)
                                x += 1
                                check += 1
                                mangasLog.append(id_cap.group())
                            else:
                                continue
                            print()
                    if(check > 0):
                        y += 1
                    self.logMangasBaixados('Union', k, mangasLog)
                arquivo.writelines('\n')
            return x, y
        except Exception as err:
            print('ERRO (salvarMangasNotificacoes): {0}'.format(err))
            os.system('pause')

    def enable_download_headless(self, browser,download_dir):
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        browser.execute("send_command", params)

    def logMangasBaixados(self, fonte, nome, caps):
        try:
            arquivo = open(os.path.join(self.saida_path, 'logMangasBaixados.txt'), 'a', encoding='utf-8')
            if(len(caps) >= 1):
                arquivo.writelines('{} - FONTE: <{}> - MANGÁ: [{}] - CAPÍTULOS ({}) - TOTAL = {}\n'.format(self.common.timestamp(),fonte, nome, ', '.join(caps), len(caps)))
            arquivo.close()
        except Exception as err:
            print("ERRO (logMangasBaixados): {}".format(err))

    def getImgsHS(self, url, driver, flag=None):
        try:
            imgs = []
            site = self.common.soup(self.feature, url=url)
            categoria = self.getCategoriaTagsHS(url, 0)
            post_texto =site.find('div', class_='post-texto')
            if(post_texto):
                busca = re.search(r'parte do[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\|\']*', post_texto.text)
                if(busca):
                    return None, None, None
            if(not categoria):
                return None, None, None
            post_fotos = site.find('ul', class_='post-fotos')
            nomeManga = site.find('title').string.split('Hentai Season')[0].replace('-','').strip()
            sinopse = site.find('div', class_='post-texto')
            if(sinopse):
                busca = re.search(r'parte do mangá [\w\sà-ú\(\)\[\]\{\}\-\+\=!/\\@#$%:ªº´`¨&\*_§¬¢£~^\?°;,.<>\|\'\"]*', sinopse.text)
                if(busca):
                    if(sinopse.a):
                        nomeManga = sinopse.a.string
            nomeManga = self.normalizeNameManga(nomeManga)
            if(self.checkNameManga(nomeManga)):
                nomeManga = self.checkNameManga(nomeManga)
            if('(Completo)' in site.find('title').string or '(Incompleto)' in site.find('title').string):
                nomeManga = nomeManga.replace('(Completo)', '')
                divs = site.find_all('div',  class_='galeria-conteudo')
                caps = {}
                caps_imgs = {}
                for d in divs:
                    id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', d.find('span', class_='galeria-nome').text) #pylint: disable=anomalous-backslash-in-string
                    if(id_cap):
                        id_cap = id_cap.group()
                        caps.update({id_cap: d.a.get('href')})
                for c, v in caps.items():
                    site = self.common.soup(self.feature, v)
                    imgs = site.find_all('img')
                    wait = WebDriverWait(driver, 10)
                    driver.get(v)
                    elmnt = wait.until(element_to_be_clickable((By.ID, 'mudar-leitura')))
                    time.sleep(5)
                    elmnt.click()
                    elmnt.click()
                    title = driver.title
                    while 'Hentai Season' not in title:
                        driver.get(v)
                        wait.until(element_to_be_clickable((By.ID, 'mudar-leitura'))).click()
                        time.sleep(5)
                        title = driver.title
                    time.sleep(5)
                    html = driver.page_source
                    site = self.common.soup(self.feature, markup=html)
                    galeria = site.find('div', class_='galeria-foto')
                    imgs = [x for x in galeria.contents if x != '\n' if x != '\t' if x != '\r' if x != ' ' if x != '']
                    caps_imgs.update({c: imgs})
                return nomeManga, caps_imgs, None
            else:
                primeiro_pag = post_fotos.find('li')
                post_itens = site.find('ul', class_='post-itens')
                post_itens = [x for x in post_itens.contents if x != ' ' if x != '\n' if x != '\t' if x != '\r']
                cap = [x.text for x in post_itens if x.strong.string == 'Episódio']
                if(cap):
                    search = re.search('[0-9]+/', cap[0])
                    if (search):
                        cap = search.group(0).replace('/', '')
                else:
                    cap = nomeManga
                if(flag):
                    cap = nomeManga
                if(primeiro_pag.a):
                    while(len(imgs) <= 1):
                        site = self.common.soup(self.feature, primeiro_pag.a.get('href'))
                        imgs = site.find_all('img')
                        wait = WebDriverWait(driver, 10)
                        driver.get(primeiro_pag.a.get('href'))
                        wait.until(element_to_be_clickable((By.ID, 'mudar-leitura'))).click()
                        time.sleep(5)
                        title = driver.title
                        while 'Hentai Season' not in title:
                            driver.get(primeiro_pag.a.get('href'))
                            wait.until(element_to_be_clickable((By.ID, 'mudar-leitura'))).click()
                            time.sleep(5)
                            title = driver.title
                        time.sleep(5)
                        html = driver.page_source
                        site = self.common.soup(self.feature, markup=html)
                        galeria = site.find('div', class_='galeria-foto')
                        imgs = [x for x in galeria.contents if x != '\n' if x != '\t' if x != '\r' if x != ' ' if x != '']
                return nomeManga, cap, imgs
        except Exception as err:
            print('ERRO (getImgsHS): {0}'.format(err))
            driver.close()
            os.system('pause')

    def baixarUmCapHS(self, manga, cap, imgs, artista=None):
        try:
            self.baixados = self.getBaixados()
            if(manga not in self.baixados):
                if(not artista):
                    mangaPath = self.criarPastaManga(manga, self.path_H_manga_hs)[0]
                else:
                    artistaPath = self.criarPastaManga(artista, self.path_H_manga_hs)[0]
                    mangaPath = self.criarPastaCapCompLen(artistaPath, cap, len(imgs), initCap=True)
                print('\n')
                if(mangaPath):
                    self.logMangasBaixados('Hentai Season', manga, [manga])
                    self.downloadsImgs(imgs, mangaPath)
            else:
                print()
                print('{} consta logMangaBaixados.txt'.format(manga))
                print()
        except Exception as err:
            print('ERRO (baixarUmCapHS): {}'.format(err))

    def baixarMangaInteiroHS(self, manga, cap, imgs, driver, artista):
        try:
            self.baixados = self.getBaixados()
            if(manga not in self.baixados):
                lists_imgs = {}
                lists_imgs.update({cap: imgs})
                if(artista):
                    artistaPath = self.criarPastaManga(artista, self.path_H_manga_hs)[0]
                    mangaPath = self.criarPastaManga(manga, artistaPath)[0]
                else:    
                    mangaPath = self.criarPastaManga(manga, self.path_H_manga_hs)[0]
                while True:
                    proximo_cap = driver.find_elements_by_link_text('Próximo capítulo >')
                    if(not proximo_cap):
                        break
                    proximo_cap[0].click()
                    time.sleep(5)
                    title = driver.title
                    while 'Hentai Season' not in title:
                        driver.switch_to_window(title)
                        self.getImgsHS(driver.current_url, driver)
                    time.sleep(5)
                    manga, cap, imgs = self.getImgsHS(driver.current_url, driver)
                    lists_imgs.update({cap: imgs})
                self.logMangasBaixados('Hentai Season', manga, lists_imgs.keys())
                for l in lists_imgs:
                    capPath = self.criarPastaCapCompLen(mangaPath, l, len(lists_imgs[l]))
                    self.downloadsImgs(lists_imgs[l], capPath)
            else:
                print()
                print('{} consta logMangaBaixados.txt'.format(manga))
                print()
        except Exception as err:
            print('ERRO (baixarMangaInteiroHS): {}'.format(err))

    def getMangaCapImgs(self, url, driver,flag=None):
        try:
            manga, cap, imgs = None, None, None
            if(url not in self.completados):
                manga, cap, imgs = self.getImgsHS(url, driver, flag)
                if(manga):
                    manga = re.sub('[\\/*?<>|]+', '',manga)
                    manga = self.normalizeNameManga(manga)
                    if(self.checkNameManga(manga)):
                        manga = self.checkNameManga(manga)
            else:
                print('{} está em completados.txt'.format(manga))
            return manga, cap, imgs
        except Exception as err:
            print('ERRO (getMangaCapImgs): {}'.format(err))
            driver.close()
    
    def baixarImgsHS(self, url, op, artista):
        try:
            exclude_links = []
            while True:
                exclude = self.common.readString('URL => ')
                if(not exclude):
                    break
                exclude_links.append(exclude)
            self.baixados = self.getBaixados()
            driver = webdriver.Chrome(chrome_options=self.common.optionsChrome(headless=True,id_extension='gighmmpiobklfepjocnamgkkbiglidom'))
            if(op == 1):
                if(url not in self.completados):
                    manga, cap, imgs = self.getMangaCapImgs(url, driver)
                    self.baixarUmCapHS(manga, cap, imgs, artista)
                else:
                    print('{} está em completados.txt'.format(manga))
            elif(op == 2):
                if(url not in self.completados):
                    manga, cap, imgs = self.getMangaCapImgs(url, driver)
                    if(imgs):
                        self.baixarMangaInteiroHS(manga,cap, imgs, driver, artista)
                else:
                    print('{} está em completados.txt'.format(manga))
            elif(op == 3):
                site = self.common.soup(url=url)
                ul = site.find('ul', class_='paginacao')
                if(ul):
                    if(ul.contents[-2].a):
                        ultimo = int(ul.contents[-2].a.text)
                    else:
                        return
                else:
                    ultimo = 1
                for i in range(1,ultimo+1):
                    site = self.common.soup(url=os.path.join(url, 'page/' + str(i)))
                    # titulo = site.find('h1', class_='pagina-titulo')
                    titulo = site.find('h1', class_='pagina-titulo')
                    if(titulo):
                        if(titulo.string):
                            busca = re.search(r':[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\|\']*|[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\|\']*-', titulo.string)
                            nome = busca.group()
                            nome = nome.replace(':', '')
                            nome = nome.replace('-', '')
                            nome = nome.replace('Arquivos', '').strip()
                            nome = self.normalizeNameManga(nome)
                    conteudos = site.find_all('div', class_='thumb-conteudo')
                    pasta = self.criarPastaManga(nome, os.path.join(self.path_H_manga, 'h-mangas links HS'))[0]
                    for c in conteudos:
                        if(c.a.get('href') not in exclude_links):
                            manga, cap, imgs = self.getMangaCapImgs(c.a.get('href'), driver, True)
                            if(manga):
                                manga = re.sub('[0-9]+', '', manga)
                                manga = manga.replace('[Final]', '')
                                manga = manga.strip()
                            if(imgs):
                                if(manga not in self.baixados):
                                    self.baixarUmCapHS(manga, cap, imgs, artista)
                                else:
                                    print('{} já baixado'.format(manga))
                            elif(isinstance(cap, dict)):
                                if(manga not in self.baixados):
                                    mangaPath = self.criarPastaManga(manga,pasta)[0]
                                    for c, v in cap.items():
                                        capPath = self.criarPastaCapCompLen(mangaPath, c, len(v))
                                        if(capPath):
                                            self.logMangasBaixados('Hentai Season', manga, v)
                                            self.downloadsImgs(v, capPath)
                                else:
                                    print()
                                    print('{} consta logMangaBaixados.txt'.format(manga))
                                    print()
            elif(op == 0):
                return
            elif(op == -1):
                self.common.shutDown()
            driver.close()
                
        except Exception as err:
            print('ERRO (baixarImgsHS): {0}'.format(err))
            os.system('pause')
            driver.close()
    
    def baixarZipadoHS(self, url):
        try:
            login = 'mdac.mario@gmail.com',
            senha = '59Md0060'
            url_loginHS = 'https://hentaiseason.com/entrar/'
            driver =  webdriver.Chrome(chrome_options=self.common.optionsChrome(True))
            self.enable_download_headless(driver,self.path_H_manga)
            wait = WebDriverWait(driver, 10)
            driver.get(url_loginHS)
            elmnt = driver.find_element_by_name('login')
            elmnt.send_keys(login)
            elmnt = driver.find_element_by_name('senha')
            elmnt.send_keys(senha)
            elmnt = wait.until(presence_of_element_located((By.CSS_SELECTOR, 'button.btn:nth-child(3)')))
            elmnt.click()
            time.sleep(2)
            driver.get(url)
            html = driver.page_source
            site = self.common.soup(feature=self.feature, markup=html)
            download = site.find('a', class_='btn btn-success')
            driver.get(download.get('href'))
        except Exception as err:
            print('ERRO (salvarMangaInteiroHS): {0}'.format(err))
            os.system('pause')

    def normalizeNameManga(self, mangaNome):
        try:
            mangaNome = mangaNome.replace(':', '-')
            mangaNome = mangaNome.replace('’', '\'')
            mangaNome = re.sub(r'[\\\/\:\*\?\"\<\>\|]+', '', mangaNome)
            mangaNome = re.sub(r'[.]{2,}', '', mangaNome)
            mangaNome = re.sub(r'\(?COMIC[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%:ªº´`¨&\_§¬¢£~^°;,.\']*|\([\w\sà-ú\(\)\[\]\{\}\-\+\=\!@#$%ªº´`&\_§¬¢£~^°;,.\']*\)', '', mangaNome, flags=re.IGNORECASE)
            # mangaNome = ' '.join(re.findall('[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.]*', mangaNome)) #pylint: disable=anomalous-backslash-in-string
            mangaNome = mangaNome.strip()
            return mangaNome
        except Exception as err:
            print('ERRO (normalizeNameManga): {}'.format(err))

    def checkNameManga(self, mangaNome):
        try:
            if(mangaNome in list(self.names_mangas.keys())):
                mangaNome = self.names_mangas[mangaNome]
                return mangaNome
            else:
                return
        except Exception as err:
            print('ERRO (checkNameManga): {0}'.format(err))
    
    def baixarMangaScan(self):
        try:
            choice = -2
            while choice != 0:
                print('1 - Markscan\n2 - Gekkouscans\n3 - Taosect\n4 - Mundo Mangá-kun\n5 - Aura Scan\n6 - Drope Scan (SITE MODIFICADO)\n7 - Lima Scan\n8 - REMANGAS\n9 - DarkYue Realm\n10 - NekoBreaker\n11 - AnimaRegia\n12 - Neox\n13 - AMA Scan')
                choice = int(self.common.readString())
                if(choice == -1):
                    self.common.shutDown()
                elif(choice == 0):
                    return
                url = self.common.readString('Digite a url: ')
                if(url == '-1'):
                    self.common.shutDown()
                elif(url == '0'):
                    return
                t_o = self.common.initCountTime()
                if(choice == 1):
                    self.baixarMangaMarkScan(url)
                elif(choice == 2):
                    self.baixarMangaGekkou(url)
                elif(choice == 3):
                    self.baixarMangaTaosect(url)
                elif(choice == 4):
                    self.baixarMangaMundoManga(url)
                elif(choice == 5):
                    self.baixarMangaAuraMangas(url)
                elif(choice == 6):
                    self.baixarMangaDrope(url)
                elif(choice == 7):
                    self.baixarMangaLima(url)
                elif(choice == 8):
                    self.baixarMangaRemangas(url)
                elif(choice == 9):
                    self.baixarMangaDarkYue(url)
                elif(choice == 10):
                    self.baixarMangaNekoBreaker(url)
                elif(choice == 11):
                    self.baixarMangaAnimaRegia(url)
                elif(choice == 12):
                    self.baixarMangaNeox(url)
                elif(choice == 13):
                    self.baixarMangaAma(url)
                t_f = self.common.finishCountTime(t_o)
                segundos = t_f % 60
                minutos  = int(t_f / 60)
                print('Executado em: {} minutos e {} segundos'.format(minutos, segundos))
                self.finishinMusic()
        except Exception as err:
            print('ERRO (baixarMangaScan): {0}'.format(err))
            os.system('pause')

    def baixarMangaGolden(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome()) as driver:
                self.common.clearTerminal()
                print('='*8+'Golden Mangas'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                time.sleep(10)
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = site.find('h2', class_='cg_color').text
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            capsH5 = site.find_all('ul', id='capitulos')
            caps_dic = {}
            cap = {}
            for c in capsH5:
                tag_a = c.find('a')
                if(tag_a):
                    id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.text) #pylint: disable=anomalous-backslash-in-string
                    if(id_cap):
                        id_cap = id_cap.group()
                        id_cap = re.sub('^[0]+','', id_cap)
                        cap = {id_cap: tag_a.get('href')}
                        caps_dic = {**caps_dic,  **cap}

            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            cap_i, cap_f = None, None
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapAma(caps_values[-1], caps_keys[-1], mangaNome)
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                self.logMangasBaixados('Golden Mangas', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
                return
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Golden Mangas', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaGolden): {}'.format(err))

    def baixarCapGolden(self, url, id_cap, mangaNome):
        try:
            goldenPasta = self.criarPastaManga('Golden', self.mangaPasta)
            site = self.common.soup(url=os.path.join(url))
            imgs = site.find_all('img', class_='img-responsive')
            print()
            mangaPath = self.criarPastaManga(mangaNome, goldenPasta)[0]
            if(self.mangasDeletados.get(mangaNome)):
                if(id_cap not in self.mangasDeletados.get(mangaNome)):
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap
                else:
                    print("Capítulo {} consta no logDelete".format(id_cap))
            else:
                capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                if(capPath):
                    self.downloadsImgs(imgs, capPath)
                    print()
                    return id_cap
        except Exception as err:
            print('ERRO (baixarCapGolden): {}'.format(err))

    def baixarMangaAma(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(url=url)
            mangaNome = site.find('h2', class_='widget-title').text
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            capsH5 = site.find_all('h5', class_='chapter-title-rtl')
            caps_dic = {}
            cap = {}
            for c in capsH5:
                tag_a = c.find('a')
                if(tag_a):
                    id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.text) #pylint: disable=anomalous-backslash-in-string
                    if(id_cap):
                        id_cap = id_cap.group()
                        id_cap = re.sub('^[0]+','', id_cap)
                        cap = {id_cap: tag_a.get('href')}
                        caps_dic = {**caps_dic,  **cap}

            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            cap_i, cap_f = None, None
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapAma(caps_values[-1], caps_keys[-1], mangaNome)
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                self.logMangasBaixados('Ama Scan', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
                return
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapAma(c, caps_keys[caps_values.index(c)], mangaNome)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Ama Scan', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaAma): {}'.format(err))

    def baixarCapAma(self, url, id_cap, mangaNome):
        try:
            amaPasta = self.criarPastaManga('Ama Scan', self.mangaPasta)
            site = self.common.soup(url=os.path.join(url))
            imgs = site.find_all('img', class_='img-responsive')
            mangaPath = self.criarPastaManga(mangaNome, amaPasta)[0]
            if(self.mangasDeletados.get(mangaNome)):
                if(id_cap not in self.mangasDeletados.get(mangaNome)):
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap
                else:
                    print("Capítulo {} consta no logDelete".format(id_cap))
            else:
                capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                if(capPath):
                    self.downloadsImgs(imgs, capPath)
                    print()
                    return id_cap
        except Exception as err:
            print('ERRO (baixarCapAma): {}'.format(err))

    def baixarMangaMHost(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(url=url)
            mangaNome = site.find('h3', class_='subtitle').text
            mangaNome = mangaNome.replace('Ativo', '')
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            caps = site.find_all('a', class_='btn-green w-button pull-left')
            caps_dic = {}
            cap = {}
            for c in caps:
                id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', c.get('title')) #pylint: disable=anomalous-backslash-in-string
                if(id_cap):
                    id_cap = id_cap.group()
                    id_cap = re.sub('^[0]+','', id_cap)
                    cap = {id_cap: c.get('href')}
                    caps_dic = {**caps_dic,  **cap}

            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            cap_i, cap_f = None, None
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapMangaHost(caps_values[-1], caps_keys[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                self.logMangasBaixados('Neox', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
                return
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMangaHost(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapMangaHost(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMangaHost(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapMangaHost(c, caps_values.index(c)+1)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Manga Host', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaMHost): {}'.format(err))

    def baixarCapMangaHost(self, url, id_cap):
        try:
            manga_host_manga = self.criarPastaManga('Manga Host', self.mangaPasta)
            with webdriver.Chrome(options=self.common.optionsChrome()) as driver:
                self.common.clearTerminal()
                print('='*8+'Manga Host'+'='*8)
                print('Obtendo informações do capitulo ...')
                driver.get(url)
                time.sleep(2)
                html = driver.page_source
            site = self.common.soup(markup=html)
            a_imgs = site.find_all('a', class_='read-slide')
            imgs = [x.find('img') for x in a_imgs]
            a_title = site.find('a', class_='bold-text-2')
            mangaNome = a_title.text
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            print()
            mangaPath = self.criarPastaManga(mangaNome, manga_host_manga)[0]
            if(self.mangasDeletados.get(mangaNome)):
                if(id_cap not in self.mangasDeletados.get(mangaNome)):
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath, name_less=True)
                        print()
                        return id_cap
                else:
                    print("Capítulo {} consta no logDelete".format(id_cap))
            else:
                capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                if(capPath):
                    self.downloadsImgs(imgs, capPath)
                    print()
                    return id_cap
        except Exception as err:
            print('ERRO (baixarCapMangaHost): {}'.format(err))

    def baixarMangaNeox(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(url=url)
            mangaNome = site.find('h1').text
            mangaNome = mangaNome.replace('NOVO\n', '')
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            caps = site.find_all('li', class_='wp-manga-chapter')
            caps_dic = {}
            cap = {}
            for c in caps:
                tag_a = c.find('a')
                if(tag_a):
                    id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.text) #pylint: disable=anomalous-backslash-in-string
                    if(id_cap):
                        id_cap = id_cap.group()
                        id_cap = re.sub('^[0]+','', id_cap)
                        cap = {id_cap: tag_a.get('href')}
                        caps_dic = {**caps_dic,  **cap}

            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            cap_i, cap_f = None, None
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapNeox(caps_values[-1], caps_keys[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                self.logMangasBaixados('Neox', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
                return
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapNeox(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapNeox(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapNeox(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapNeox(c, caps_values.index(c)+1)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Neox', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaNeox): {}'.format(err))

    def baixarCapNeox(self, url, id_cap):
        try:
            neox_pasta = self.criarPastaManga('Neox Scan', self.mangaPasta)
            site = self.common.soup(url=os.path.join(url,'?style=list'))
            imgs = site.find_all('img', class_='wp-manga-chapter-img')
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[2].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            print()
            mangaPath = self.criarPastaManga(mangaNome, neox_pasta)[0]
            if(self.mangasDeletados.get(mangaNome)):
                if(id_cap not in self.mangasDeletados.get(mangaNome)):
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap
                else:
                    print("Capítulo {} consta no logDelete".format(id_cap))
            else:
                capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                if(capPath):
                    self.downloadsImgs(imgs, capPath)
                    print()
                    return id_cap
        except Exception as err:
            print('ERRO (baixarCapNeox): {}'.format(err))

    def baixarMangaAnimaRegia(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(url=url)
            mangaNome = site.find('h1', class_='widget-title').text
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            capsH5 = site.find_all('h5', class_='chapter-title-rtl')
            caps_dic = {}
            cap = {}
            for c in capsH5:
                tag_a = c.find('a')
                if(tag_a):
                    id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.text) #pylint: disable=anomalous-backslash-in-string
                    if(id_cap):
                        id_cap = id_cap.group()
                        id_cap = re.sub('^[0]+','', id_cap)
                        cap = {id_cap: tag_a.get('href')}
                        caps_dic = {**caps_dic,  **cap}

            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            cap_i, cap_f = None, None
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapAnimaRegia(caps_values[-1], caps_keys[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                self.logMangasBaixados('AnimaRegia', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
                return
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAnimaRegia(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapAnimaRegia(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAnimaRegia(c, caps_values.index(c)+1)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapAnimaRegia(c, caps_values.index(c)+1)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('AnimaRegia', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaAnimaRegia): {}'.format(err))

    def baixarCapAnimaRegia(self, url, id):
        try:
            anima_regia_pasta = self.criarPastaManga('Anima Regia Scan', self.mangaPasta)
            site = self.common.soup(url=url)
            imgs = site.find_all('img', class_='img-responsive')[:-1]
            linkName = site.find('ul', class_='nav navbar-nav').find('a')
            if(linkName):
                mangaNome = linkName.string
                mangaNome = self.normalizeNameManga(mangaNome)
                if(self.checkNameManga(mangaNome)):
                    mangaNome = self.checkNameManga(mangaNome)
            else:
                print('Nome de mangá não encontrado')
                return
            print()
            mangaPath = self.criarPastaManga(mangaNome, anima_regia_pasta)[0]
            if(self.mangasDeletados.get(mangaNome)):
                if(id not in self.mangasDeletados.get(mangaNome)):
                    capPath = self.criarPastaCapCompLen(mangaPath, id, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath, name_less=True)
                        print()
                        return id
                else:
                    print("Capítulo {} consta no logDelete".format(id))
            else:
                capPath = self.criarPastaCapCompLen(mangaPath, id, len(imgs))
                if(capPath):
                    self.downloadsImgs(imgs, capPath, name_less=True)
                    print()
                    return id
        except Exception as err:
            print('ERRO (baixarCapAnimaRegia): {}'.format(err))

    def baixarMangaNekoBreaker(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Neko Breaker'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                time.sleep(2)
                html = driver.page_source
            site = self.common.soup(markup=html)
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[-1].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            lista_li = site.find_all('li', class_='wp-manga-chapter')
            caps_dic = {}
            cap = {}
            for li in lista_li:
                tag_a = li.find('a')
                cap = {re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.string).group():tag_a.get('href')} #pylint: disable=anomalous-backslash-in-string
                caps_dic = {**caps_dic,  **cap}
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            i = 0
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapNekoBreaker(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    print('{} capítulo(s) baixado(s)'.format(i))
                    self.logMangasBaixados('NekoBreaker', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapNekoBreaker(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapNekoBreaker(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapNekoBreaker(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapNekoBreaker(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
            self.logMangasBaixados('NekoBreaker', mangaNome, capsBaixados)
        except Exception as err:
            print('ERRO (baixarMangaNekoBreaker): {}'.format(err))

    def baixarCapNekoBreaker(self,url):
        try:
            neko_breaker_pasta =self.criarPastaManga('Neko Breaker Scab', self.mangaPasta)
            site = self.common.soup(url=url+'?style=list')
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[2].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', ol[-1]) #pylint: disable=anomalous-backslash-in-string
            mangaPath = self.criarPastaManga(mangaNome, neko_breaker_pasta)[0]
            imgs = site.find_all('img', class_='wp-manga-chapter-img')
            if(id_cap):
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap.group() not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap.group()
                    else:
                        print("Capítulo {} consta no logDelete".format(id_cap.group()))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap.group()
        except Exception as err:
            print('ERRO (baixarNekoBreaker): {}'.format(err))

    def baixarMangaDarkYue(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Dark Yue Scan'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                time.sleep(2)
                html = driver.page_source
            site = self.common.soup(markup=html)
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[-1].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            lista_li = site.find_all('li', class_='wp-manga-chapter')
            caps_dic = {}
            cap = {}
            for li in lista_li:
                tag_a = li.find('a')
                cap = {re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.string).group():tag_a.get('href')} #pylint: disable=anomalous-backslash-in-string
                caps_dic = {**caps_dic,  **cap}
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                try:
                    if(int(cap_i)<10):
                        cap_i = '0' + cap_i
                except:
                    pass
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
                try:
                    if(int(cap_f)<10):
                        cap_f = '0' + cap_f
                except:
                    pass
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
                try:
                    if(int(cap_f)<10):
                        cap_f = '0' + cap_f
                    if(int(cap_i)<10):
                        cap_i = '0' + cap_i
                except:
                    pass
            elif(choice == '5'):
                capBaixado = self.baixarCapDarkYue(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('DarkYue Realm', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapDarkYue(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapDarkYue(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapDarkYue(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapDarkYue(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Lima Scan', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaDarkYue): {}'.format(err))

    def baixarCapDarkYue(self, url):
        try:
            dark_yue_pasta = self.criarPastaManga('Dark Yue Scan', self.mangaPasta)
            site = self.common.soup(url=url+'?style=list')
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[1].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', ol[-1]) #pylint: disable=anomalous-backslash-in-string
            mangaPath = self.criarPastaManga(mangaNome, dark_yue_pasta)[0]
            imgs = site.find_all('img', class_='wp-manga-chapter-img')
            if(id_cap):
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap.group() not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap.group()
                    else:
                        print("O capítulo {} consta no logDelete".format(id_cap.group()))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap.group()
        except Exception as err:
            print('ERRO (baixarCapDarkYue): {}'.format(err))

    def baixarMangaRemangas(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(url=url)
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'ReMangas Scan'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                print()
            caps_a = [x.a for x in site.find_all('h5', class_='chapter-title-rtl') if(x.a)]
            caps_dic = {}
            mangaNome = site.find('h2', class_="widget-title").string
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            for c in caps_a:
                id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', c.string) #pylint: disable=anomalous-backslash-in-string
                if(id_cap):
                    caps_dic.update({id_cap.group():c.get('href')})
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = list(caps_dic.values())
            caps_values.reverse()
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapRemangas(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('Remangas', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapRemangas(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapRemangas(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapRemangas(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapRemangas(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Remangas', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaRemangas): {}'.format(err))

    def baixarCapRemangas(self, url):
        try:
            remangas_pasta = self.criarPastaManga('ReMangas Scan', self.mangaPasta)
            site = self.common.soup(url=url)
            # pode dar problema com titulo de mangá com dois pontos
            active = site.find('li', class_='active').string.split(':')[1]
            nameLink = site.select_one('#navbar-collapse-1 > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)')
            mangaNome = self.normalizeNameManga(nameLink.string)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', active) #pylint: disable=anomalous-backslash-in-string
            mangaPath = self.criarPastaManga(mangaNome, remangas_pasta)[0]
            imgs = site.find('div', id='all').find_all('img')
            if(id_cap):
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap.group() not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap.group()
                    else:
                        print("O capítulo {} consta no logDelete".format(id_cap.group))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap.group()
        except Exception as err:
            print('ERRO (baixarCapRemangas): {}'.format(err))

    def baixarMangaLima(self,url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Lima Scan'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                html = driver.page_source
            site = self.common.soup(markup=html)
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[-1].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            lista_li = site.find_all('li', class_='wp-manga-chapter')
            caps_dic = {}
            cap = {}
            for li in lista_li:
                tag_a = li.find('a')
                cap = {re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.string).group():tag_a.get('href')} #pylint: disable=anomalous-backslash-in-string
                caps_dic = {**caps_dic,  **cap}
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapLima(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('Lima Scan', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapLima(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapLima(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapLima(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapLima(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Lima Scan', mangaNome, capsBaixados)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaLima): {}'.format(err))

    def baixarCapLima(self, url):
        try:
            lima_pasta = self.criarPastaManga('Lima Scan', self.mangaPasta)
            site = self.common.soup(url=url+'?style=list')
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[1].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', ol[-1]) #pylint: disable=anomalous-backslash-in-string
            mangaPath = self.criarPastaManga(mangaNome, lima_pasta)[0]
            imgs = site.find_all('img', class_='wp-manga-chapter-img')
            if(id_cap):
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap.group() not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap.group()
                    else:
                        print('Capítulo {} consta no logDelete'.format(id_cap.group()))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap.group()
        except Exception as err:
            print('ERRO (baixarCapLima): {}'.format(err))
        
    def baixarMangaDrope(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Drope Scans'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                time.sleep(5)
                # element = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[2]/div/div/span')
                element = driver.find_elements_by_css_selector('.btn.btn-link.chapter-readmore.less-chap')
                if(element):
                    element[0].click()
                elements = driver.find_elements_by_css_selector('.parent.has-child')
                for e in elements:
                    e.click()
                    time.sleep(10)
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = site.find('h1').string
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            lista_caps = site.find_all('li', class_='wp-manga-chapter')
            caps_dic = {}
            for ul in lista_caps:
                caps_dic = {**caps_dic,  **{ re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', x.string).group():x.get('href') for x in ul.find_all('a') if x.get('href')}} #pylint: disable=anomalous-backslash-in-string
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapDrope(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('Drope Scan', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i):
                if(len(cap_i) < 2):
                    cap_i = '0' + cap_i
            if(cap_f):
                if(len(cap_f) < 2):
                    cap_f = '0' + cap_f
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapDrope(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapDrope(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapDrope(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapDrope(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
                self.logMangasBaixados('Drope Scan', mangaNome, capsBaixados)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarMangaDrope): {}'.format(err))
    
    def baixarCapDrope(self, url):
        try:
            drope_pasta = self.criarPastaManga('Drope Scan', self.mangaPasta)
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Drope Scan'+'='*8)
                print('Obtendo informações do capitulo ...')
                driver.get(url)
                html = driver.page_source
            site = self.common.soup(markup=html)
            ol = site.find('ol', class_='breadcrumb')
            ol = [x for x in ol.text.replace('\t', '').split('\n') if x != '']
            mangaNome = ol[1].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', ol[-1]) #pylint: disable=anomalous-backslash-in-string
            mangaPath = self.criarPastaManga(mangaNome, drope_pasta)[0]
            imgs = site.find_all('img', class_='wp-manga-chapter-img')
            if(id_cap):
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap.group() not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap.group()
                    else:
                        print("Capítulo {} consta no logDelete".format(id_cap.group()))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap.group()
        except Exception as err:
            print('ERRO (baixarCapDrope): {}'.format(err))

    def baixarCapMundoManga(self, url):
        try:
            mundo_manga_pasta = self.criarPastaManga('Mundo Manga-kun Scan', self.mangaPasta)
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Mundo Manga-kun Scan'+'='*8)
                print('Obtendo informações do capitulo ...')
                wait = WebDriverWait(driver, 10)
                driver.get(url)
                elmnt = wait.until(presence_of_element_located((By.ID, 'label_leitor_paginacao_completo')))
                elmnt.click()
                html = driver.page_source
            site = self.common.soup(markup=html)
            title = site.find('h1').string.split('-')
            mangaNome = title[0]
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', title[1]) #pylint: disable=anomalous-backslash-in-string
            mangaPath = self.criarPastaManga(mangaNome, mundo_manga_pasta)[0]
            imgs = site.find_all('img', class_='pagina_capitulo')
            if(id_cap):
                id_cap = id_cap.group()
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap
                    else:
                        print('O Capítulo {} consta no logDelete'.format(id_cap))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap
        except Exception as err:
            print( 'ERRO (baixarCapMundoManga): {}'.format(err))

    def baixarMangaMundoManga(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(url=url)
            mangaNome = site.find('h1').contents[0]
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            caps_a = site.find_all('a', class_='link_capitulo')
            caps_dic = {re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', x.string).group():x.get('href') for x in caps_a}
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapMundoManga(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('Mundo Mangá-kun', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMundoManga(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapMundoManga(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMundoManga(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapMundoManga(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Mundo Mangá-kun', mangaNome, caps_keys)
            print('{} capítulo(s) baixado(s)'.format(len(caps_values)))
        except Exception as err:
            print('ERRO (baixarMangaMundoManga) : {}'.format(err))
    
    def baixarMangaMarkScan(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Mark Scan'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                time.sleep(2)
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = site.find('title').string.split('-')[0].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            mangaNome = mangaNome.replace('Mark Scan', '').strip()
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            lista_li = site.find_all('li', class_='wp-manga-chapter')
            caps_dic = {}
            cap = {}
            for li in lista_li:
                tag_a = li.find('a')
                cap = {re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', tag_a.string).group():tag_a.get('href')} #pylint: disable=anomalous-backslash-in-string
                caps_dic = {**caps_dic,  **cap}
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            site = self.common.soup(url=url)
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapMarkScan(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('Mark Scan', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMarkScan(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapMarkScan(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys[:caps_keys.index(cap_f)+1]):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMarkScan(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapMarkScan(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Mark Scan', mangaNome, caps_keys)
            print('{} capítulo(s) baixado(s)'.format(len(caps_values)))
            print()
        except Exception as err:
            print('ERRO (baixarMangaMarkScan): {}'.format(err))

    def baixarCapMarkScan(self, url):
        try:
            mark_pasta = self.criarPastaManga('Mark Scan', self.mangaPasta)
            site = self.common.soup(feature=self.feature, url=url, headers=self.common.headers)
            title = site.find('title').string.split('-')
            mangaNome = title[0].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            mangaPath = self.criarPastaManga(mangaNome, mark_pasta)[0]
            search = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', title[1]) #pylint: disable=anomalous-backslash-in-string
            imgs = site.find_all('img', class_='wp-manga-chapter-img')
            if(search):
                cap = search.group(0)   
                if(self.mangasDeletados.get(mangaNome)):
                    if(cap not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, cap, len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return cap
                    else:
                        print('O Capítulo {} consta no logDelete'.format(cap))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return cap
        except Exception as err:
            print('ERRO (baixarCapMarkScan): {}'.format(err))

    def baixarMangaGekkou(self, url):
        try:
            self.verificaMangasLogDelete()
            site = self.common.soup(url=url)
            mangaNome = site.find('title').string.split('-')[0].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            capsBaixados = []
            caps = site.find_all('li', class_='li')
            caps = [x.find('a') for x in caps if x.find('a')]
            capitulos = {}
            for c in caps:
                search = re.search('([0-9]+)(\W.[0-9]+)?', c.string.split(' ')[-1]) #pylint: disable=anomalous-backslash-in-string
                if(search):
                    capitulos.update({search.group():c.get('href')})
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            site = self.common.soup(url=url)
            capitulos_keys = sorted(list(capitulos.keys()), key=lambda v: self.common.ordenateStringNum(v))
            # capitulos_values = sorted(list(capitulos.values()), key=lambda v: self.common.ordenateStringNum(v))
            capitulos_values = list(capitulos.values())
            capitulos_values.reverse()
            i = 0
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapGekkou(capitulos_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    i += 1
                print('{} capítulo(s) baixado(s)'.format(i))
                
                self.logMangasBaixados('Gekkou Scan', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in capitulos_keys and cap_f in capitulos_keys):
                    for c in capitulos_values[capitulos_keys.index(cap_i):capitulos_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapGekkou(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                            i += 1
                    print('{} capítulo(s) baixado(s)'.format(i))
            elif(cap_i and not cap_f):
                if(cap_i in capitulos_keys):
                    for c in capitulos_values[capitulos_keys.index(cap_i):]:
                        capBaixado = self.baixarCapGekkou(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                            i += 1
                    print('{} capítulo(s) baixado(s)'.format(i))
            elif(not cap_i and cap_f):
                if(cap_f in capitulos_keys):
                    for c in capitulos_values[:capitulos_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapGekkou(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                            i += 1
                    print('{} capítulo(s) baixado(s)'.format(i))
            elif(not cap_i and not cap_f):
                for c in capitulos_values:
                    capBaixado = self.baixarCapGekkou(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
                        i += 1
                print('{} capítulo(s) baixado(s)'.format(i))
            self.logMangasBaixados('Gekkou Scan', mangaNome, capsBaixados)
        except Exception as err:
            print('ERRO (baixarMangaGekkou): {}'.format(err))

    def baixarCapGekkou(self,url):
        try:
            gekkou_pasta = self.criarPastaManga('Gekkou Scans', self.mangaPasta)
            site = self.common.soup(feature=self.feature, url=url, headers=self.common.headers)
            title = site.find('title').string.split('Capítulo')
            mangaNome = title[0].strip()
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            mangaPath = self.criarPastaManga(mangaNome, gekkou_pasta)[0]
            search = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', title[1]) #pylint: disable=anomalous-backslash-in-string
            if(search):
                cap = search.group(0)
            if(self.mangasDeletados.get(mangaNome)):
                if(cap not in self.mangasDeletados.get(mangaNome)):
                    imgs = site.find_all('img', class_='img-responsive')
                    capPath = self.criarPastaCapCompLen(mangaPath, cap, len(imgs[:-1]))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return cap
                else:
                    print("Capítulo {} consta no logDelete".format(cap))
            else:
                imgs = site.find_all('img', class_='img-responsive')
                capPath = self.criarPastaCapCompLen(mangaPath, cap, len(imgs[:-1]))
                if(capPath):
                    self.downloadsImgs(imgs, capPath)
                    print()
                    return cap
        except Exception as err:
            print('ERRO (baixarCapGekkou): {}'.format(err))
    
    def baixarMangaAuraMangas(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(url=url)
            caps = site.find_all('a', class_='')
            caps_a = []
            for c in caps:
                if(c.string):
                    busca = re.search('(Capítulo)|(Capitulo)', c.string, flags=re.IGNORECASE)
                    if(busca):
                        caps_a.append(c)
            mangaNome = site.find('h1', class_='article__title font').string
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            caps_dic = {re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', x.string).group():x.get('href') for x in caps_a}
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = list(caps_dic.values())
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapAuraMangas(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('Aura Scan', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAuraMangas(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapAuraMangas(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapAuraMangas(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapAuraMangas(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Aura Scan', mangaNome, caps_keys)
            print('{} capítulo(s) baixado(s)'.format(len(caps_values)))
        except Exception as err:
            print("ERRO (baixarMangaAuraMangas): {}".format(err))

    def baixarCapAuraMangas(self,url):
        try:
            aura_pasta = self.criarPastaManga('Aura Mangas', self.mangaPasta)
            site = self.common.soup(url=url)
            title = site.find('title').string.split('|')
            mangaName = title[0].strip()
            mangaName = self.normalizeNameManga(mangaName)
            if(self.checkNameManga(mangaName)):
                mangaName = self.checkNameManga(mangaName)
            id_cap = re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', title[1])
            imgs = site.find_all('img')
            imgs = [x for x in imgs if x.get('border')]
            mangaPath = self.criarPastaManga(mangaName,aura_pasta)[0]
            if(id_cap):
                id_cap = id_cap.group()
                if(self.mangasDeletados.get(mangaName)):
                    if(id_cap not in self.mangasDeletados.get(mangaName)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap
                    else:
                        print('O Capítulo {} consta no logDelete'.format(id_cap))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap
        except Exception as err:
            print('ERRO (baixarCapAuraMangas): {}'.format(err))

    def baixarMangaTaosect(self,url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            capitulo = re.search('cap-tulo-', url)
            projeto = re.search('projeto', url)
            if(capitulo):
                self.baixarCapTaosect(url)
            if(projeto):
                print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
                choice = self.common.readString()
                cap_i, cap_f = None, None
                site = self.common.soup(url=url)
                mangaNome = site.find('h1', class_='titulo-projeto').text.strip()
                mangaNome = self.normalizeNameManga(mangaNome)
                if(self.checkNameManga(mangaNome)):
                    mangaNome = self.checkNameManga(mangaNome)
                capitulos_td = site.find_all('td')
                capitulos_td = [x for x in capitulos_td if x.a if x.get('align') == 'left']
                capitulos_dic = {}
                for c in capitulos_td:
                    search = re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?',c.text)
                    if(search):
                        capitulos_dic.update({search.group(): c.a.get('href')})
                capitulos_keys = sorted(list(capitulos_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
                capitulos_values = list(capitulos_dic.values())
                if(choice == '1'):
                    cap_i, cap_f = None, None
                elif(choice == '2'):
                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                elif(choice == '3'):
                    cap_f = self.common.readString('Baixar até o capítulo => ')
                elif(choice == '4'):
                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                    cap_f = self.common.readString('Baixar até o capítulo => ')
                elif(choice == '5'):
                    capBaixado = self.baixarCapTaosect(capitulos_values[-1])
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
                        self.logMangasBaixados('Tao Sect Scan', mangaNome, capsBaixados)
                        print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                    return
                else:
                    print('OPÇÃO INVÁLIDA')
                if(cap_i):
                    if(len(cap_i) == 1):
                        cap_i = '0' + cap_i
                if(cap_f):
                    if(len(cap_f) == 1):
                        cap_f = '0' + cap_f
                if(cap_i and cap_f):
                    if(cap_i in capitulos_keys and cap_f in capitulos_keys):
                        for c in capitulos_values[capitulos_keys.index(cap_i):capitulos_keys.index(cap_f)]:
                            capBaixado = self.baixarCapTaosect(c)
                            if(capBaixado):
                                capsBaixados.append(capBaixado)
                    else:
                        print('Capítulo não encontrado')
                elif(cap_i and not cap_f):
                    if(cap_i in capitulos_keys):
                        for c in capitulos_values[capitulos_keys.index(cap_i)+1:]:
                            capBaixado = self.baixarCapTaosect(c)
                            if(capBaixado):
                                capsBaixados.append(capBaixado)
                    else:
                        print('Capítulo não encontrado')
                elif(not cap_i and cap_f):
                    if(cap_f in capitulos_keys):
                        for c in capitulos_values[:capitulos_keys.index(cap_f)+1]:
                            capBaixado = self.baixarCapTaosect(c)
                            if(capBaixado):
                                capsBaixados.append(capBaixado)
                    else:
                        print('Capítulo não encontrado')
                elif(not cap_i and not cap_f):
                    for c in capitulos_values:
                        capBaixado = self.baixarCapTaosect(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                self.logMangasBaixados('Tao Sect Scan', mangaNome, capitulos_keys)
                print('{} capítulos baixados'.format(len(capitulos_values)))
            else:
                print('URL INVÁLIDA')
        except Exception as err:
            print('ERRO (baixarMangaTaosect): {}'.format(err))            

    def baixarCapTaosect(self,url):
        try:
            tao_sect_pasta = self.criarPastaManga('Tao Sect Manga', self.mangaPasta)
            # muda visualização para página completa
            with webdriver.Chrome(chrome_options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Tao Sect Scan'+'='*8)
                print('Obtendo informações do capitulo ...')
                driver.get(url)
                wait = WebDriverWait(driver, 10)
                try:
                    modal = wait.until(element_to_be_clickable((By.ID, 'btn_ok_mais_18')))
                    modal.click()
                except:
                    pass
                page_complete = wait.until(presence_of_element_located((By.ID, 'label_leitor_paginacao_completo')))
                page_complete.click()
                time.sleep(3)
                html = driver.page_source
            site = self.common.soup(markup=html)
            # tag h1 contendo nome do mangá e id do capitulo
            h1 = site.find('h1')
            if(h1.a):
                h1 = h1.a.string.split('- ')
            mangaName = h1[0].strip()
            mangaName = self.normalizeNameManga(mangaName)
            if(self.checkNameManga(mangaName)):
                mangaName = self.checkNameManga(mangaName)
            id_cap = re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', h1[-1])
            mangaPath = self.criarPastaManga(mangaName, tao_sect_pasta)[0]
            imgs = site.find_all('img', class_='pagina_capitulo')
            if(id_cap):
                id_cap = id_cap.group()
                if(self.mangasDeletados.get(mangaName)):
                    if(id_cap not in self.mangasDeletados.get(mangaName)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath, True)
                            print()
                            return id_cap
                    else:
                        print('O Capítulo {} consta no logDelete'.format(id_cap))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath, True)
                        print()
                        return id_cap
        except Exception as err:
            print('ERRO (baixarCapTaosect): {}'.format(err))
       
    def getIdCapAndMangaNameMangadex(self, url):
        try:
            site = self.common.soup(url=url)
            title = site.find('title')
            id_capitulo = re.search('Ch. ([0-9]+\-?)(\s){0,0}([\.0-9]+)?', title.string) #pylint: disable=anomalous-backslash-in-string
            if(id_capitulo):
                id_capitulo = id_capitulo.group(0).replace('Ch. ', '')
            else:
                id_capitulo = re.search('(Ch. ([0-9]+\-?)(\s){0,0}([\.0-9]+)?)|(\w)+ ', title.string).group(0).strip() #pylint: disable=anomalous-backslash-in-string
            mangaName = re.search("\([\w\sà-ú\(\)\[\]\{\}\-\+\=!/\\@#$%:ªº´`¨&\*_§¬¢£~^\?°;,.<>\|\'\"]*\)", title.string).group(0) #pylint: disable=anomalous-backslash-in-string
            mangaName = re.sub('[\(\):/\\\*\?\"\|<>]*', '', mangaName) #pylint: disable=anomalous-backslash-in-string
            mangaName = self.normalizeNameManga(mangaName)
            if(self.checkNameManga(mangaName)):
                mangaName = self.checkNameManga(mangaName)
            return id_capitulo, mangaName
        except Exception as err:
            print('ERRO (getIdCapAndMangaNameMangadex): {0}'.format(err))

    def baixarMangaDex(self,url):
        try:
            self.verificaMangasLogDelete()
            if(re.match(self.regex_urlWEB, url) is not None):
                capsBaixados = []
                search = re.search('title|chapter', url)
                if(search.group(0) == 'chapter'):
                    site = self.common.soup(url=url)
                    mangaNome = site.find('a', class_='manga-link').get('title')
                    mangaNome = self.normalizeNameManga(mangaNome)
                    if(self.checkNameManga(mangaNome)):
                        mangaNome = self.checkNameManga(mangaNome)
                    capBaixado = self.baixarCapMangaDex(url)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
                        self.logMangasBaixados('MangaDex', mangaNome, capsBaixados)
                        print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))

                elif(search.group(0) == 'title'):
                    print('1 - baixar todos capitulos BR\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar ultimo capítulo')
                    choice = self.common.readString()
                    cap_i, cap_f = None, None
                    if(choice == '1'):
                        cap_i, cap_f = None, None
                    elif(choice == '2'):
                        cap_i = self.common.readString('Baixar a partir de capítulo => ')
                    elif(choice == '3'):
                        cap_f = self.common.readString('Baixar até o capítulo => ')
                    elif(choice == '4'):
                        cap_i = self.common.readString('Baixar a partir de capítulo => ')
                        cap_f = self.common.readString('Baixar até o capítulo => ')
                    elif(choice == '5'):
                        cap_i, cap_f = 'None', 'None'
                    else:
                        print('OPÇÃO INVÁLIDA')
                        return
                    print('Buscando capítulos ...\nAGUARDE!')
                    capitulos = {}
                    site = self.common.soup(url=url)
                    mangaNome = site.find('span', class_='mx-1').string
                    mangaNome = self.normalizeNameManga(mangaNome)
                    if(self.checkNameManga(mangaNome)):
                        mangaNome = self.checkNameManga(mangaNome)
                    nav = site.find('ul', class_='pagination justify-content-center')
                    if(nav):
                        lastCapPage = nav.find('span', class_='fa-angle-double-right')
                        if(lastCapPage):
                            lastCapPage = [x for x in lastCapPage.parent.get('href').split('/') if x != '']
                            numLastCapPage = int(lastCapPage[-1])
                        linkManga = '/'.join(lastCapPage[:-1])
                    else:
                        linkManga = url
                        numLastCapPage = 1
                    for i in range(1,numLastCapPage+1):
                        if(nav):
                            site = self.common.soup(url='{}/{}/{}'.format(self.initURLmangadex,linkManga, i))
                        else:
                            site = self.common.soup(url='{}/{}'.format(linkManga, i))
                        caps = site.find_all('div', class_='chapter-row')[1:]
                        for c in caps:
                            bandeira = c.find('span', class_='rounded flag flag-br')
                            if(bandeira):
                                link = c.find('a', class_='text-truncate')
                                id_capitulo = re.search('Ch. ([0-9]+\-?)(\s){0,0}([\.0-9]+)?', link.string) #pylint: disable=anomalous-backslash-in-string
                                if(id_capitulo):
                                    id_capitulo = id_capitulo.group(0).replace('Ch. ', '')
                                else:
                                    id_capitulo = link.string
                                capitulos.update({id_capitulo:'{}{}'.format(self.initURLmangadex,link.get('href'))})
                    listCapitulos = list(capitulos.keys())
                    if(cap_i == 'None' and cap_f == 'None'):
                        capBaixado = self.baixarCapMangaDex(list(capitulos.values())[0])
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                    elif(not cap_i and not cap_f):
                        for c,l in capitulos.items():
                            capBaixado = self.baixarCapMangaDex(l)
                            if(capBaixado):
                                capsBaixados.append(capBaixado)
                            # print(c + ':' +l)
                    elif(not cap_f and cap_i):
                        if(cap_i in listCapitulos):
                            for x in listCapitulos[:listCapitulos.index(cap_i)+1]:
                                # print(x + ':'+capitulos[x])
                                capBaixado = self.baixarCapMangaDex(capitulos[x])
                                if(capBaixado):
                                    capsBaixados.append(capBaixado)
                        else:
                            print('Capítulo não encontrado')
                    elif(not cap_i and cap_f):
                        if(cap_f in listCapitulos):
                            for x in listCapitulos[listCapitulos.index(cap_f):]:
                                # print(x + ':'+capitulos[x])
                                capBaixado = self.baixarCapMangaDex(capitulos[x])
                                if(capBaixado):
                                    capsBaixados.append(capBaixado)
                        else:
                            print('Capítulo não encontrado')
                    elif(cap_i and cap_f):
                        if(cap_i in listCapitulos and cap_f in listCapitulos):
                            for x in listCapitulos[listCapitulos.index(cap_f):listCapitulos.index(cap_i)+1]:
                                # print(x + ':'+capitulos[x])
                                capBaixado = self.baixarCapMangaDex(capitulos[x])
                                if(capBaixado):
                                    capsBaixados.append(capBaixado)
                        else:
                            print('Capítulo não encontrado')
                    self.logMangasBaixados('MangaDex', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
            else:
                print('URL inválida')
        except Exception as err:
            print('ERRO (baixarMangaDex): {0}'.format(err))
            os.system('pause')

    def baixarCapMangaDex(self,url):
        try:
            mangadex_pasta = self.criarPastaManga('MangaDex', self.mangaPasta)
            imgs = []
            with webdriver.Chrome(chrome_options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'MangaDex'+'='*8)
                print('Obtendo informações do capitulo ...')
                wait = WebDriverWait(driver, 10)
                driver.get(url)
                time.sleep(3)
                native = driver.find_element_by_class_name('show-long-strip')
                # native = wait.until(presence_of_element_located((By.CLASS_NAME, 'show-native-long-strip')))
                if(native.text):
                    SCROLL_PAUSE_TIME = 0.5

                    # Get scroll height
                    last_height = driver.execute_script("return document.body.scrollHeight")

                    while True:
                        # Scroll down to bottom
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                        # Wait to load page
                        time.sleep(SCROLL_PAUSE_TIME)

                        # Calculate new scroll height and compare with last scroll height
                        new_height = driver.execute_script("return document.body.scrollHeight")
                        if new_height == last_height:
                            break
                        last_height = new_height
                    html = driver.page_source
                    site = self.common.soup(markup=html)
                    imgs = site.find_all('img', class_="noselect nodrag cursor-pointer")
                else:
                    element = wait.until(presence_of_element_located((By.CLASS_NAME, "page-link-right")))
                    currentPage = wait.until(presence_of_element_located((By.CLASS_NAME, 'current-page'))).text
                    totalPages = wait.until(presence_of_element_located((By.CLASS_NAME, 'total-pages'))).text
                    html = driver.page_source
                    site = self.common.soup(markup=html)
                    img = site.find('img', class_="noselect nodrag cursor-pointer")
                    imgs.append(img)
                    while currentPage != totalPages:
                        element = wait.until(presence_of_element_located((By.CLASS_NAME, "page-link-right")))
                        currentPage = wait.until(presence_of_element_located((By.CLASS_NAME, 'current-page'))).text
                        html = driver.page_source
                        site = self.common.soup(markup=html)
                        img = site.find('img', class_="noselect nodrag cursor-pointer")
                        imgs.append(img)
                        if(currentPage != totalPages):
                            element.click()
                            time.sleep(3)
            imgs = list(set(imgs))
            id_capitulo, mangaName = self.getIdCapAndMangaNameMangadex(url)
            mangaPath = self.criarPastaManga(mangaName, mangadex_pasta)[0]
            if(self.mangasDeletados.get(mangaName)):
                if(id_capitulo not in self.mangasDeletados.get(mangaName)):
                    capPath = self.criarPastaCapCompLen(mangaPath, id_capitulo, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_capitulo
                else:
                    print('O Capítulo {} consta no logDelete'.format(id_capitulo))
            else:
                capPath = self.criarPastaCapCompLen(mangaPath, id_capitulo, len(imgs))
                if(capPath):
                    self.downloadsImgs(imgs, capPath)
                    print()
                    return id_capitulo
        except Exception as err:
            print('ERRO (baixarCapMangaDex): {0}'.format(err))
            os.system('pause')

    def baixarMangaTsukiMangas(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Tsuki Mangas'+'='*8)
                print("Obtendo informação do manga ...")
                driver.get(url)
                time.sleep(2)
                SCROLL_PAUSE_TIME = 0.5

                # Get scroll height
                last_height = driver.execute_script("return document.body.scrollHeight")

                while True:
                    # Scroll down to bottom
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = site.find('h2').text
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            caps_a = site.find_all('a', class_='')
            caps_dic = {}
            if(caps_a):
                for x in caps_a:
                    if(x.get('href')):
                        if re.search('/leitor', x.get('href')):
                            caps_dic.update({x.get('href').split('/')[-1]:self.initURLTsukiMangas+x.get('href')})
                print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
                choice = self.common.readString()
                cap_i, cap_f = None, None
                site = self.common.soup(url=url)
                caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
                caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
                if(choice == '1'):
                    cap_i, cap_f = None, None
                elif(choice == '2'):
                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                    # adicionando um zero a esquerda
                    cap_i =  "{num:0>2}".format(num=cap_i)
                elif(choice == '3'):
                    cap_f = self.common.readString('Baixar até o capítulo => ')
                    # adicionando um zero a esquerda
                    cap_f =  "{num:0>2}".format(num=cap_f)
                elif(choice == '4'):
                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                    # adicionando um zero a esquerda
                    cap_i =  "{num:0>2}".format(num=cap_i)
                    cap_f = self.common.readString('Baixar até o capítulo => ')
                    # adicionando um zero a esquerda
                    cap_f =  "{num:0>2}".format(num=cap_f)
                elif(choice == '5'):
                    capBaixado = self.baixarCapTsukiMangas(caps_values[-1])
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
                        self.logMangasBaixados('Tsuki Mangás', mangaNome, capsBaixados)
                        print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                    return
                else:
                    print('OPÇÃO INVÁLIDA')
                
                if(cap_i and cap_f):
                    if(cap_i in caps_keys and cap_f in caps_keys):
                        for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                            capBaixado = self.baixarCapTsukiMangas(c)
                            if(capBaixado):
                                capsBaixados.append(capBaixado)
                    else:
                        print('Capítulo não encontrado')
                elif(cap_i and not cap_f):
                    if(cap_i in caps_keys):
                        for c in caps_values[caps_keys.index(cap_i):]:
                            capBaixado = self.baixarCapTsukiMangas(c)
                            if(capBaixado):
                                capsBaixados.append(capBaixado)
                    else:
                        print('Capítulo não encontrado')
                elif(not cap_i and cap_f):
                    if(cap_f in caps_keys):
                        for c in caps_values[:caps_keys.index(cap_f)+1]:
                            capBaixado = self.baixarCapTsukiMangas(c)
                            if(capBaixado):
                                capsBaixados.append(capBaixado)
                    else:
                        print('Capítulo não encontrado')
                elif(not cap_i and not cap_f):
                    for c in caps_values:
                        capBaixado = self.baixarCapTsukiMangas(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                self.logMangasBaixados('Tsuki Mangás', mangaNome, capsBaixados)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
            print()
        except Exception as err:
            print('ERRO (baixarMangaTsukiMangas): {}'.format(err))

    def baixarCapTsukiMangas(self, url):
        try:
            tsuki_pasta = self.criarPastaManga('Tsuki Mangas', self.mangaPasta)
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Tsuki Mangas'+'='*8)
                print('Obtendo informações do capítulo ...')
                wait = WebDriverWait(driver, 10)
                driver.get(url)
                elmnt = wait.until(presence_of_element_located((By.CLASS_NAME, 'bblc')))
                select = elmnt.find_element_by_tag_name('select')
                all_options = select.find_elements_by_tag_name('option')
                for option in all_options:
                    if(re.search('Páginas abertas', option.text)):
                        option.click()
                        time.sleep(3)
                        html = driver.page_source
                        break
                html = driver.page_source
            site = self.common.soup(markup=html)
            id_cap = re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', site.find('b', class_='f14c').text)
            mangaName = site.find('b', class_='f20').text
            mangaName = self.normalizeNameManga(mangaName)
            if(self.checkNameManga(mangaName)):
                mangaName = self.checkNameManga(mangaName)
            imgs = site.find_all('img', class_='leitorimg imgleitorbrabao')
            mangaPath = self.criarPastaManga(mangaName, tsuki_pasta)[0]
            if(id_cap):
                id_cap = id_cap.group()
                if(self.mangasDeletados.get(mangaName)):
                    if(id_cap not in self.mangasDeletados.get(mangaName)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap
                    else:
                        print('O Capítulo {} consta no logDelete'.format(id_cap))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap
        except Exception as err:
            print('ERRO(baixarCapTsukiMangas): {}'.format(err))

    def baixarMangaLeitorDotNet(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome()) as driver:
                self.common.clearTerminal()
                print('='*8+'Leitor.net'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                SCROLL_PAUSE_TIME = 2

                # Get scroll height
                last_height = driver.execute_script("return document.body.scrollHeight")

                while True:
                    # Scroll down to bottom
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = [x.text for x in site.find_all('span', 'series-title') if x.h1][0]
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            caps_a = site.find_all('a', 'link-dark')
            caps_dic = {}
            caps_dic = {re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', x.find('span', class_='cap-text').text).group() :self.initURLLeitorDotNet+x.get('href') for x in caps_a} #pylint: disable=anomalous-backslash-in-string
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = sorted(list(caps_dic.values()), key=lambda v: self.common.ordenateStringNum(v))
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapLeitorDotnet(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    self.logMangasBaixados('Leitor.net', mangaNome, capsBaixados)
                    print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapLeitorDotnet(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapLeitorDotnet(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapLeitorDotnet(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                for c in caps_values:
                    capBaixado = self.baixarCapLeitorDotnet(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Leitor.net', mangaNome, caps_keys)
            print('{} capítulo(s) baixado(s)'.format(len(caps_values)))
            print()
        except Exception as err:
            print('ERRO (baixarMangaLeitorDotNet): {}'.format(err))

    def baixarCapLeitorDotnet(self, url):
        try:
            leitor_pasta = self.criarPastaManga('Leitor.net', self.mangaPasta)
            check = False
            with webdriver.Chrome(options=self.common.optionsChrome()) as driver:
                self.common.clearTerminal()
                print('='*8+'Leitor.net'+'='*8)
                print('Obtendo informações do capitulo ...')
                driver.set_window_size(1366,768)
                wait = WebDriverWait(driver, 10)
                driver.get(url)
                try:
                    wait.until(presence_of_element_located((By.CLASS_NAME, 'eighteen-but'))).click()
                    check = True
                    imgs = driver.find_elements_by_tag_name('img')
                    new_imgs = []
                    while len(imgs) != len(new_imgs):
                        imgs = driver.find_elements_by_tag_name('img')
                        driver.execute_script("return arguments[0].scrollIntoView();", imgs[-1])
                        time.sleep(2)
                        new_imgs = driver.find_elements_by_tag_name('img')
                except:
                    html = driver.page_source
                    site = self.common.soup(markup=html)
                    pages = re.findall('([0-9]+)',site.find('div', class_='page-navigation').text)
                    imgs = site.find('div', class_='manga-page').find_all('img')
                    if(len(imgs) > 1):
                        imgs = driver.find_elements_by_tag_name('img')
                        new_imgs = []
                        while len(imgs) != len(new_imgs):
                            imgs = driver.find_elements_by_tag_name('img')
                            driver.execute_script("return arguments[0].scrollIntoView();", imgs[-1])
                            time.sleep(2)
                            new_imgs = driver.find_elements_by_tag_name('img')
                    else:
                        atual_pag  = pages[0]
                        final_pag = pages[1]
                        while atual_pag != final_pag:
                            imgs.append(site.find('div', class_='manga-page').find('img'))
                            wait.until(presence_of_element_located((By.CLASS_NAME, 'page-next'))).click()
                            html = driver.page_source
                            site = self.common.soup(markup=html)
                            atual_pag = re.search('([0-9]+)', site.find('div', class_='page-navigation').text).group()
                    print()
                
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = site.find('span', class_='title').string
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?',site.find('span', class_='current-chapter').text) #pylint: disable=anomalous-backslash-in-string
            mangaPath = self.criarPastaManga(mangaNome, leitor_pasta)[0]
            # mangaPath = self.criarPastaManga(mangaNome, self.mangaPasta)
            if(check):
                imgs = site.find('div', class_='manga-page').find_all('img')
            if(id_cap):
                id_cap = id_cap.group()
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap
                    else:
                        print('O Capítulo {} consta no logDelete'.format(id_cap))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap
        except Exception as err:
            print('ERRO (baixarCapLeitorDotnet): {}'.format(err))

    def baixarMangaLivre(self, url):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Manga Livre'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                SCROLL_PAUSE_TIME = 2

                # Get scroll height
                last_height = driver.execute_script("return document.body.scrollHeight")

                while True:
                    # Scroll down to bottom
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
                time.sleep(3)
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = [x.text for x in site.find_all('span', 'series-title') if x.h1][-1]
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            caps_a = site.find_all('a', 'link-dark')
            caps_dic = {}
            caps_dic = {re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', x.find('span', class_='cap-text').text).group() :self.initURLMangaLivre+x.get('href') for x in caps_a} #pylint: disable=anomalous-backslash-in-string
            print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
            choice = self.common.readString()
            cap_i, cap_f = None, None
            caps_keys = sorted(list(caps_dic.keys()), key=lambda v: self.common.ordenateStringNum(v))
            caps_values = list(caps_dic.values())
            caps_values.reverse()
            if(choice == '1'):
                cap_i, cap_f = None, None
            elif(choice == '2'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
            elif(choice == '3'):
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '4'):
                cap_i = self.common.readString('Baixar a partir de capítulo => ')
                cap_f = self.common.readString('Baixar até o capítulo => ')
            elif(choice == '5'):
                capBaixado = self.baixarCapMangaLivre(caps_values[-1])
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
                self.logMangasBaixados('MangaLivre', mangaNome, capsBaixados)
                return
            else:
                print('OPÇÃO INVÁLIDA')
            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMangaLivre(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    for c in caps_values[caps_keys.index(cap_i):]:
                        capBaixado = self.baixarCapMangaLivre(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    for c in caps_values[:caps_keys.index(cap_f)+1]:
                        capBaixado = self.baixarCapMangaLivre(c)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                self.logMangasBaixados('MangaLivre', mangaNome, caps_keys)
                for c in caps_values:
                    capBaixado = self.baixarCapMangaLivre(c)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
            self.logMangasBaixados('MangaLivre', mangaNome, capsBaixados)
        except Exception as err:
            print('ERRO (baixarMangaLivre): {}'.format(err))

    def baixarCapMangaLivre(self, url):
        try:
            manga_livre_pasta = self.criarPastaManga('Manga Livre', self.mangaPasta)
            with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Manga Livre'+'='*8)
                print('Obtendo informações do manga ...')
                driver.set_window_size(1366,768)
                wait = WebDriverWait(driver, 10)
                driver.get(url)
                try:
                    wait.until(presence_of_element_located((By.CLASS_NAME, 'eighteen-but'))).click()
                except:
                    pass
                html = driver.page_source
                site = self.common.soup(markup=html)
                pages = re.findall('([0-9]+)',site.find('div', class_='page-navigation').text)
                imgs = []
                atual_pag  = pages[0]
                final_pag = pages[1]
                imgs.append(site.find('div', class_='manga-image').find('img'))
                while atual_pag != final_pag:
                    time.sleep(2)
                    try:
                        nextPage = wait.until(element_to_be_clickable((By.CLASS_NAME, 'page-next')))
                    except:
                        nextPage = wait.until(element_to_be_clickable((By.CLASS_NAME, 'manga-image')))
                    time.sleep(2)
                    nextPage.click()
                    html = driver.page_source
                    site = self.common.soup(markup=html)
                    atual_pag = re.search('([0-9]+)', site.find('div', class_='page-navigation').text).group()
                    imgs.append(site.find('div', class_='manga-image').find('img'))
                html = driver.page_source
            site = self.common.soup(markup=html)
            mangaNome = site.find('span', class_='title').string
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            id_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?',site.find('span', class_='current-chapter').text) #pylint: disable=anomalous-backslash-in-string
            if(id_cap):
                mangaPath = self.criarPastaManga(mangaNome, manga_livre_pasta)[0]
                if(self.mangasDeletados.get(mangaNome)):
                    if(id_cap.group() not in self.mangasDeletados.get(mangaNome)):
                        capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            print()
                            return id_cap.group()
                    else:
                        print("Capítulo {} consta no logDelete".format(id_cap.group()))
                else:
                    capPath = self.criarPastaCapCompLen(mangaPath, id_cap.group(), len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_cap.group()
        except Exception as err:
            print('ERRO (baixarCapMangaLivre): {}'.format(err))

    def baixarPartindoCapUnion(self, url, cap_i = None, cap_f=None):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            if(cap_i):
                cap_i = "{num:0>2}".format(num=cap_i)
            if(cap_f):
                cap_f = "{num:0>2}".format(num=cap_f)
            site = self.common.soup(url=url)
            nomeManga = re.sub('[\\/*?<>|]+', '',site.find('h2').string).replace(':', '-')
            nomeManga = self.normalizeNameManga(nomeManga)
            caps = site.find_all('div', class_='col-xs-6 col-md-6')
            caps = [x.a for x in caps if(x.a)]
            caps.reverse()
            caps_dic = {}
            for c in caps:
                id_cap = re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', c.string)
                if(id_cap):
                    caps_dic.update({id_cap.group():c.get('href')})
            caps_keys = list(caps_dic.keys())
            caps_values = list(caps_dic.values())

            if(cap_i and cap_f):
                if(cap_i in caps_keys and cap_f in caps_keys):
                    caps = caps_values[caps_keys.index(cap_i):caps_keys.index(cap_f)+1]
                    for c in caps:
                        capBaixado = self.baixarCapUnion(c, caps_keys[caps_values.index(c)], nomeManga)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(cap_i and not cap_f):
                if(cap_i in caps_keys):
                    caps = caps_values[caps_keys.index(cap_i):]
                    for c in caps:
                        capBaixado = self.baixarCapUnion(c, caps_keys[caps_values.index(c)], nomeManga)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and cap_f):
                if(cap_f in caps_keys):
                    caps = caps_values[:caps_keys.index(cap_f)+1]
                    for c in caps:
                        capBaixado = self.baixarCapUnion(c, caps_keys[caps_values.index(c)], nomeManga)
                        if(capBaixado):
                            capsBaixados.append(capBaixado)
                else:
                    print('Capítulo não encontrado')
            elif(not cap_i and not cap_f):
                capBaixado = self.baixarCapUnion(caps_values[-1], caps_keys[-1], nomeManga)
                if(capBaixado):
                    capsBaixados.append(capBaixado)
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
            self.logMangasBaixados('Union', nomeManga, capsBaixados)
        except Exception as err:
            print('ERRO (baixarPartindoCap): {0}'.format(err))
            os.system('pause')
    
    def baixarCapUnion(self, url, id_cap, nomeManga):
        try:
            union_pasta = self.criarPastaManga('Union Mangas', self.mangaPasta)
            if(self.checkNameManga(nomeManga)):
                nomeManga = self.checkNameManga(nomeManga)
            mangaPath = self.criarPastaManga(nomeManga, union_pasta)[0]
            site = self.common.soup(url=url)
            imgs = site.find_all('img',class_='img-manga')[2:]
            if(self.mangasDeletados.get(nomeManga)):
                if(id_cap not in self.mangasDeletados.get(nomeManga)):
                    cap_path = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                    if(cap_path):
                        self.downloadsImgs(imgs, cap_path)
                        print()
                        return id_cap
                else:
                    print('O Capítulo {} consta no logDelete'.format(id_cap))
            else:
                cap_path = self.criarPastaCapCompLen(mangaPath, id_cap, len(imgs))
                if(cap_path):
                    self.downloadsImgs(imgs, cap_path)
                    print()
                    return id_cap
        except Exception as err:
            print('ERRO(baixarCapUnion): {}'.format(err))
    
    def baixarAteCapUnion(self, url, cap):
        try:
            union_pasta = self.criarPastaManga('Union Mangas', self.mangaPasta)
            i = 0
            cap = float(cap)
            site = self.common.soup(url=url)
            nomeManga = re.sub('[\\/*?<>|]+', '',site.find('h2').string).replace(':', '-')
            nomeManga = self.normalizeNameManga(nomeManga)
            if(self.checkNameManga(nomeManga)):
                nomeManga = self.checkNameManga(nomeManga)
            mangaPath = self.criarPastaManga(nomeManga, union_pasta)[0]
            caps = site.find_all('div', class_='col-xs-6 col-md-6')
            for c in caps:
                num_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', c.find('a', class_='').string).group(0) #pylint: disable=anomalous-backslash-in-string
                # num_cap = re.sub('Cap. ', '', c.find('a', class_='').string)
                f_cap = float(num_cap)
                if(cap >= f_cap):
                    url_capitulo = c.find('a', class_='').get('href')
                    site = self.common.soup(feature=self.feature, url=url_capitulo)
                    imgs = site.find_all('img',class_='img-manga')[2:]
                    complete_path = self.criarPastaCapCompLen(mangaPath, num_cap, len(imgs))
                    if(complete_path):
                        i += 1
                        self.downloadsImgs(imgs, complete_path)
                    else:
                        continue
                else:
                    print('{} capítulos baixados'.format(i))
                    break
        except Exception as err:
            print('ERRO (baixarPartindoDeUmCap): {0}'.format(err))
            os.system('pause')

    def salvarMangaInteiroUnion(self, url):
        try:
            union_pasta = self.criarPastaManga('Union Mangas', self.mangaPasta)
            self.verificaMangasLogDelete()
            capsBaixados = []
            site = self.common.soup(feature=self.feature, url=url)
            # nomeManga = site.find('h2').string.replace('\\/*?<>|', '').replace(':', '-')
            nomeManga = re.sub('[\\/*?<>|]+', '',site.find('h2').string).replace(':', '-')
            nomeManga = self.normalizeNameManga(nomeManga)
            if(self.checkNameManga(nomeManga)):
                nomeManga = self.checkNameManga(nomeManga)
            mangaPath = self.criarPastaManga(nomeManga, union_pasta)[0]
            caps = site.find_all('div', class_='col-xs-6 col-md-6')
            for c in caps:
                num_cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', c.find('a', class_='').string).group(0) #pylint: disable=anomalous-backslash-in-string
                # num_cap = re.sub('Cap. ', '', c.find('a', class_='').string)
                url_capitulo = c.find('a', class_='').get('href')
                site = self.common.soup(feature=self.feature, url=url_capitulo)
                imgs = site.find_all('img',class_='img-manga')[2:]
                if(self.mangasDeletados.get(nomeManga)):
                    if(num_cap not in self.mangasDeletados.get(nomeManga)):
                        complete_path = self.criarPastaCapCompLen(mangaPath, num_cap, len(imgs))
                        if(complete_path):
                            self.downloadsImgs(imgs, complete_path)
                            capsBaixados.append(num_cap)
                    else:
                        print('O Capítulo {} consta no logDelete'.format(num_cap))
                else:
                    complete_path = self.criarPastaCapCompLen(mangaPath, num_cap, len(imgs))
                    if(complete_path):
                        self.downloadsImgs(imgs, complete_path)
                        capsBaixados.append(num_cap)
                print()
            print('{} capítulo(s) baixado(s)'.format(len(capsBaixados)))
            self.logMangasBaixados('Union', nomeManga, capsBaixados)

        except Exception as err:
            print('ERROR (salvarMangaInteiroUnion): {0}'.format(err))
            os.system('pause')

    def salvarMangaInteiroHC(self, url, path=None):
        try:
            hipercool_pasta_manga = self.criarPastaManga('Hipercool', self.mangaPasta)
            self.baixados = self.getBaixados()
            site = self.common.soup(feature=self.feature, url=url)
            categoria = self.getCategoriaTagsHC(url, self.feature, 0)
            categorias = [x.lower() for x in self.categoriasHC if(x != 'Mangá' and x != 'Manga' and x != 'Manhwa' and x != 'Manhua')]
            if(site.find('span', class_='title').string):
                manga_nome = re.sub('[\\/*?<>|]+', '',site.find('span', class_='title').string).replace(':', '-')
            else:
                manga_nome = re.sub('[\\/*?<>|]+', '',site.find('span', class_='title').text).replace(':', '-')
            manga_nome = self.normalizeNameManga(manga_nome)
            if(manga_nome not in self.baixados):
                if(url not in self.completados):
                    pasta = self.criarPastaManga('h-mangas links HC', self.path_H_manga)[0]
                    if(self.checkNameManga(manga_nome)):
                        manga_nome = self.checkNameManga(manga_nome)
                    if(path):
                        if(manga_nome in self.baixados):
                            print('{} consta logMangaBaixados.txt'.format(manga_nome))
                            return None
                        else:
                            manga_path = self.criarPastaManga(manga_nome, path)[0]
                    elif(categoria in categorias):
                        if(manga_nome in self.baixados):
                            print('{} consta logMangaBaixados.txt'.format(manga_nome))
                            return None
                        manga_path = self.criarPastaManga(manga_nome, pasta)[0]
                    else:
                        manga_path = self.criarPastaManga(manga_nome, hipercool_pasta_manga)[0]
                    caps = site.find_all('a', class_='title')[1:]
                    caps_dic = {x.string : self.initURLHC+x.get('href') for x in caps}
                    caps_keys = list(caps_dic.keys())
                    self.logMangasBaixados('Hipercool', manga_nome, caps_keys)
                    for c in caps:
                        id_cap = c.string
                        url_cap = self.initURLHC+c.get('href')
                        site = self.common.soup(feature=self.feature, url=url_cap)
                        imgs = site.find_all('img',class_='page')
                        if(categoria in categorias):
                            if(len(caps) > 1):
                                complete_path = self.criarPastaCapCompLen(manga_path, id_cap, len(imgs))
                            else:
                                complete_path = manga_path
                        else:
                            complete_path = self.criarPastaCapCompLen(manga_path, id_cap, len(imgs))
                        if(complete_path):
                            self.downloadsImgs(imgs, complete_path)
                else:
                    print('{} está em completados.txt'.format(manga_nome))
            else:
                print('{} consta logMangaBaixados.txt'.format(manga_nome))
        except Exception as err:
            print('ERROR (salvarMangaInteiroHC): {0}'.format(err))
            os.system('pause')

    def baixarTodosMangasLinkHC(self, url):
        try:
            exclude_links = []
            while True:
                exclude = self.common.readString('URL => ')
                if(not exclude):
                    break
                exclude_links.append(exclude)
            site = self.common.soup(url=url)
            divP = site.find_all('div', class_='buttons')
            h2 = site.find('h2')
            if(h2):
                busca = re.search(r':[\w\sà-ú\(\)\[\]\{\}\-\+\=!/\\@#$%:ªº´`¨&\*_§¬¢£~^\?°;,.<>\|\'\"]*\(', h2.string)
                if(busca):
                    nomeLink = busca.group()
                    nomeLink = nomeLink.replace(':', '')
                    nomeLink = nomeLink.replace('(', '')
                    nomeLink = nomeLink.strip()
            pages = []
            for p in divP[0].contents:
                pages.append(p.get('href'))
            nextPage = pages[0]
            fim = divP[0].find_all('a')[-1]
            i = 0
            mangas = {}
            while len(fim.get('class')) < 3:
                divP = site.find_all('div', class_='buttons')
                conteudo = site.find_all('a', class_='news-thumb')
                for c in conteudo:
                    nome = re.sub(r'[0-9]+$|[0-9]+ Final$|[0-9]+ Extra$', '', c.text)
                    nome = re.sub(r'\\/:\*\"<>\|', '', nome)
                    nome = nome.strip()
                    nome = self.normalizeNameManga(nome)
                    link = self.initURLHC+c.get('href')
                    categoria = self.getCategoriaTagsHC(link, self.feature, 0)
                    if(categoria):
                        if(link not in exclude_links):
                            mangas.update({nome:link})
                i += 1
                if pages != divP[0].contents:
                    for p in divP[0].contents:
                        if p.get('href') not in pages:
                            pages.append(p.get('href'))
                if i < len(pages):
                    nextPage = pages[i]
                fim = divP[0].find_all('a')[-1]
                site = self.common.soup(url= self.initURLHC + nextPage)
            pasta = self.criarPastaManga('h-mangas links HC', self.path_H_manga)[0]
            pastaLink = self.criarPastaManga(nomeLink, pasta)[0]
            for link in mangas.values():
                self.salvarMangaInteiroHC(link, pastaLink)
            print('{} mangás baixados'.format(len(mangas)))
        except Exception as err:
            print(time.ctime())
            print('ERRO (baixarTodosMangasLinkHC): {}'.format(err))
            print(link)
            os.system('pause')

    def baixarLeitorBH(self, url, artista):
        try:
            self.baixados = self.getBaixados()
            with webdriver.Chrome(options=self.common.optionsChrome(headless=True)) as driver:
                self.common.clearTerminal()
                print('='*8+'Baixar Hentai'+'='*8)
                print('Obtendo informações do manga ...')
                driver.get(url)
                time.sleep(3)
                html = driver.page_source
            initUrl = re.search(r'((?:https?:\/\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}))+', url).group()
            site = self.common.soup(markup=html)
            titulos = [x for x in site.title.string.split(':') if(x != '') if(x != 'Página 1 ')]
            nome = titulos[0].strip()
            nome = self.normalizeNameManga(nome)
            nome = re.sub(r'[\- ]*Capítulo[0-9 ]+[\- ]*Página[0-9 ]+', '', nome)
            nome = re.sub(r'Leitura Online[\- ]*', '', nome)
            if(url not in self.completados):
                if(nome not in self.baixados):
                    options = site.find_all('option')
                    if(not options):
                        options = site.find('ul', class_='dropdown').find_all('li')
                    caps_dic = {}
                    pasta = self.criarPastaManga('h-mangas links BH', self.path_H_manga)[0]
                    if(len(options) > 1):
                        for op in options:
                            if(op.get('value')):
                                if(re.match(self.regex_urlWEB, op.get('value')) is not None):
                                    if(op.get('value')):
                                        buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.string)
                                        if(buscaCap):
                                            caps_dic.update({buscaCap.group():op.get('value')})
                                    else:
                                        buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.a.text)
                                        if(buscaCap):
                                            caps_dic.update({buscaCap.group():op.a.get('href')})
                                else:
                                    buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.string)
                                    if(buscaCap):
                                        caps_dic.update({buscaCap.group():url+'/'+buscaCap.group()})
                            elif(op.get('href')):
                                if(re.match(self.regex_urlWEB, op.get('href')) is not None):
                                    if(op.get('href')):
                                        buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.string)
                                        if(buscaCap):
                                            caps_dic.update({buscaCap.group():op.get('href')})
                                    else:
                                        buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.a.text)
                                        if(buscaCap):
                                            caps_dic.update({buscaCap.group():op.a.get('href')})
                                else:
                                    buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.string)
                                    if(buscaCap):
                                        caps_dic.update({buscaCap.group():url+'/'+buscaCap.group()})
                            elif(op.a):
                                if(re.match(self.regex_urlWEB, op.a.get('href')) is not None):
                                    if(op.a.get('href')):
                                        buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.string)
                                        if(buscaCap):
                                            caps_dic.update({buscaCap.group():op.a.get('href')})
                                else:
                                    buscaCap =  re.search(r'([0-9]+\-?)(\s){0,0}([\.0-9]+)?', op.string)
                                    if(buscaCap):
                                        caps_dic.update({buscaCap.group():url+'/'+buscaCap.group()})
                        for c, v in caps_dic.items():
                            with webdriver.Chrome(options=self.common.optionsChrome(headless=True)) as driver:
                                driver.get(v)
                                time.sleep(3)
                                html = driver.page_source
                            site = self.common.soup(markup=html)
                            imgs = site.find_all('img', class_='')[1:]
                            if(len(imgs) <= 1):
                                imgs = site.find_all('img')[1:]
                            for x in imgs:
                                if(initUrl not in x.get('src')):
                                    x['src'] = initUrl + '/' + x.get('src')
                            if(artista):
                                artistaPath = self.criarPastaManga(artista, pasta)[0]
                                mangaPath = self.criarPastaManga(nome, artistaPath)[0]
                                capPath = self.criarPastaCapCompLen(mangaPath, c, len(imgs))
                                if(capPath):
                                    self.downloadsImgs(imgs, capPath)
                            else:
                                mangaPath = self.criarPastaManga(nome, pasta)[0]
                                capPath = self.criarPastaCapCompLen(mangaPath, c, len(imgs))
                                if(capPath):
                                    self.downloadsImgs(imgs, capPath)
                        self.logMangasBaixados('BH', nome, list(caps_dic.keys()))

                    else:
                        imgs = site.find_all('img', class_='')[1:]
                        if(len(imgs) <= 1):
                            imgs = site.find_all('img')[1:]
                        if(artista):
                            pasta = self.criarPastaManga(artista, pasta)[0]
                        capPath = self.criarPastaCapCompLen(pasta, nome, len(imgs), True)
                        if(capPath):
                            self.downloadsImgs(imgs, capPath)
                            self.logMangasBaixados('BH', nome, [nome])
                else:
                    print()
                    print('{} consta logMangaBaixados.txt'.format(nome))
                    print()
            else:
                print('{} está em completados.txt'.format(nome))  
                print()
        except Exception as err:
            print('ERRO (baixarLeitorBH): {}'.format(err))
            os.system('pause')

    def baixarCapHC(self, url, url_main):
        try:
            hipercool_pasta_manga = self.criarPastaManga('Hipercool', self.mangaPasta)
            self.baixados = self.getBaixados()
            site = self.common.soup(feature=self.feature, url=url_main)
            categoria = self.getCategoriaTagsHC(url_main, self.feature, 0)
            categorias = [x.lower() for x in self.categoriasHC if(x != 'Mangá' and x != 'Manga' and x != 'Manhwa' and x != 'Manhua')]
            manga_nome = re.sub('[\\/*?<>|]+', '',site.find('span', class_='title').string).replace(':', '-')
            manga_nome = self.normalizeNameManga(manga_nome)
            pasta = self.criarPastaManga('h-mangas links HC', self.path_H_manga)[0]
            if(self.checkNameManga(manga_nome)):
                manga_nome = self.checkNameManga(manga_nome)
            if(categoria in categorias):
                if(manga_nome in self.baixados):
                    print('{} consta logMangaBaixados.txt'.format(manga_nome))
                    return None
                manga_path = self.criarPastaManga(manga_nome, pasta)[0]
            else:
                manga_path = self.criarPastaManga(manga_nome, hipercool_pasta_manga)[0]
            site = self.common.soup(url=url)
            title = site.find('title').string
            id_capitulo = re.search('Capítulo ([0-9]+\-?)(\s){0,0}([\.0-9]+)?', title.string) #pylint: disable=anomalous-backslash-in-string
            if(id_capitulo):
                id_capitulo = id_capitulo.group(0).replace('Capítulo ', '')
            else:
                id_capitulo = re.search('(Ch. ([0-9]+\-?)(\s){0,0}([\.0-9]+)?)|(\w)+ ', title.string).group(0).strip() #pylint: disable=anomalous-backslash-in-string
            imgs = site.find_all('img',class_='page')
            if(self.mangasDeletados.get(manga_nome)):
                if(id_capitulo not in self.mangasDeletados.get(manga_nome)):
                    capPath = self.criarPastaCapCompLen(manga_path, id_capitulo, len(imgs))
                    if(capPath):
                        self.downloadsImgs(imgs, capPath)
                        print()
                        return id_capitulo
                else:
                    print('O Capítulo {} consta no logDelete'.format(id_capitulo))
            else:
                capPath = self.criarPastaCapCompLen(manga_path, id_capitulo, len(imgs))
                if(capPath):
                    self.downloadsImgs(imgs, capPath)
                    print()
                    return id_capitulo
            # self.downloadsImgs(imgs)
        except Exception as err:
            print('ERRO (baixarCapHC): {0}'.format(err))
            os.system('pause')

    def baixarPartindoCapHC(self, url, cap_i = None, cap_f = None):
        try:
            self.verificaMangasLogDelete()
            capsBaixados = []
            if(cap_i):
                if(len(cap_i) < 2):
                    cap_i = '0' + cap_i
            if(cap_f):
                if(len(cap_f) < 2):
                    cap_f = '0' + cap_f
            site = self.common.soup(url=url)
            mangaNome = site.find('span', class_='title').string
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            all_caps = site.find_all('a', class_='title')
            all_caps = {x.string: self.initURLHC+x.get('href') for x in all_caps if(x.get('href') != '/')}
            listAll_caps = list(all_caps.keys())
            if(cap_i == 'None' and cap_f == 'None'):
                capBaixado = self.baixarCapHC(list(all_caps.values())[-1], url)
                if(capBaixado):
                    capsBaixados.append(capBaixado)
                    print()
            elif(cap_i and not cap_f):
                self.logMangasBaixados('Hipercool', mangaNome, listAll_caps[listAll_caps.index(cap_i):])
                for x in listAll_caps[listAll_caps.index(cap_i):]:
                    # print(x + ':' + all_caps[x])
                    capBaixado = None
                    capBaixado = self.baixarCapHC(all_caps[x], url)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            elif(not cap_i and cap_f):
                self.logMangasBaixados('Hipercool', mangaNome, listAll_caps[:listAll_caps.index(cap_f)+1])
                for x in listAll_caps[:listAll_caps.index(cap_f)+1]:
                    # print(x + ':' + all_caps[x])
                    capBaixado = self.baixarCapHC(all_caps[x], url)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            elif(cap_i and cap_f):
                self.logMangasBaixados('Hipercool', mangaNome, listAll_caps[listAll_caps.index(cap_i):listAll_caps.index(cap_f)+1])
                for x in listAll_caps[listAll_caps.index(cap_i):listAll_caps.index(cap_f)+1]:
                    # print(x + ':' + all_caps[x])
                    capBaixado = self.baixarCapHC(all_caps[x], url)
                    if(capBaixado):
                        capsBaixados.append(capBaixado)
            self.logMangasBaixados('Hipercool', mangaNome, capsBaixados)
            print('{} capítulos baixados'.format(len(capsBaixados)))
        except Exception as err:
            print('ERRO (baixarPartindoCapHC): {0}'.format(err))

    def baixarProximosCapsHC_Hmanga(self, url):
        try:
            list_caps = {}
            site = self.common.soup(url=url, headers=self.headers)
            mangaNome = site.find('title').string.split('-')
            mangaNome = self.normalizeNameManga(mangaNome)
            if(self.checkNameManga(mangaNome)):
                mangaNome = self.checkNameManga(mangaNome)
            cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', site.find('title').string).group(0) #pylint: disable=anomalous-backslash-in-string
            # cap = cap.replace('Capítulo ', '')
            proximo_cap = site.find('a', class_='next')
            pasta = self.criarPastaManga('h-mangas links HC', self.path_H_manga)[0]
            mangaPath = self.criarPastaManga(mangaNome, pasta)[0]
            imgs = site.find_all('img',class_='page')
            list_caps.update({cap: imgs})
            while proximo_cap:
                site = self.common.soup(url=self.initURLHC+proximo_cap.get('href'))
                cap = re.search('Capítulo [0-9]+', site.find('title').string).group(0)
                cap = cap.replace('Capítulo ', '')
                imgs = site.find_all('img',class_='page')
                list_caps.update({cap: imgs})
                proximo_cap = site.find('a', class_='next')
            for c in list_caps:
                capPath = self.criarPastaCapCompLen(mangaPath, c, len(list_caps[c]))
                self.downloadsImgs(list_caps[c], capPath)
                print()
        except Exception as err:
            print('ERRO (baixarProximosCapsHC): {0}'.format(err))
            os.system('pause')
    
    def downloadManga(self, urlsPaths):        
        try:
            for chave in urlsPaths:
                directory = chave
                if(re.match(self.regexPath, directory) is not None):
                    for url in urlsPaths.get(chave):
                        if(re.match(self.regex_urlWEB, url) is not None):
                            site = self.common.soup(self.feature, url)
                            cap = re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', url.split('/')[-1]).group(0) #pylint: disable=anomalous-backslash-in-string
                            # name = url.split('/')[-1]
                            if re.findall('union', url):
                                imgs = site.find_all('img',class_='img-manga')[2:]
                            if re.findall('hiper', url):
                                imgs = site.find_all('img',class_='page')
                            if(directory == 'D:\\Imagens\\Mangás\\H'):
                                mangaName = re.sub('[\\/*?<>|]+', '',site.find('title').string.split('-')[0].strip()).replace(':', '-')
                                mangaPath = self.criarPastaManga(mangaName,directory)[0]
                                directory_complete = self.criarPastaCapCompLen(mangaPath, cap, len(imgs))
                            else:
                                directory_complete = self.criarPastaCapCompLen(directory, cap, len(imgs))
                            if(directory_complete is None):
                                print('Pasta de capítulo já existente')
                                continue
                                
                            self.downloadsImgs(imgs, directory_complete)
                        else:
                            print('A url {} é inválida'.format(url))
                else:
                    print('O caminho da pasta {} é inválido'.format(directory))
        except requests.exceptions.ConnectionError:
            print('Erro de conexão (downloadManga). Tente novamente mais tarde')
            os.system('pause')
        except:
            print('Erro desconhecido (downloadManga): ', sys.exc_info()[0])
            os.system('pause')

    def downloadsImgs(self, imgs, directory_complete, name_less=False):
        directory_argument = directory_complete
        try:
            for i in imgs:
                if(name_less):
                    directory_complete = os.path.join(directory_argument, str(imgs.index(i)))
                # buscaDataUri = re.search(self.regexDataUri, i.get('src'))
                # if(buscaDataUri):
                #     data_uri = buscaDataUri.group()
                #     header, encoded = data_uri.split(",", 1)
                #     buscaMime = re.search(r'([a-zA-Z0-9]+\/[a-zA-Z0-9-.+]+)', header)
                #     if(buscaMime):
                #         data = base64.b64decode(encoded)
                #         arquivo = os.path.join(self.saida_path,"image{}.{}".format(x, buscaMime.group().split('/')[-1]))
                #         with open(arquivo, "wb") as f:
                #             f.write(data)
                #         x += 1
                if(i.get('data-src')):
                    src = re.sub('[\n\t]', '',i.get('data-src'))
                    self.common.downloadArchive(src.strip(), directory_complete)
                elif(i.get('src')):
                    src = re.sub('[\n\t]', '',i.get('src'))
                    if(re.match(self.regex_urlWEB, src) is not None):
                        print()
                        self.common.downloadArchive(src, directory_complete)
                    else:
                        print('URL {} INVÁLIDA'.format(src))
                else:
                    print('URL INVÁLIDA')
        except Exception as err:
            if('520 Server Error' in str(err) or '522 Server Error' in str(err) or '404 Client Error' in str(err)):
                print(time.ctime())
                print('ERROR (downloadsImgs): {0}'.format(err))
                pass
            else:
                print(time.ctime())
                print('ERROR (downloadsImgs): {0}'.format(err))
                os.system('pause')

    def getURLsUnion(self, lists):
        try:
            i = 0
            lists_list = []
            texts_itens = []
            for c in lists:
                if(c.string != '\n'):
                    i += 1
                    if(c.string != None):
                        print(('{} - {}'.format(i, c.string)).upper())
                        lists_list.append(c.a.get('href'))
                        texts_itens.append(c.string.upper())
                    if(c.get('class')):
                        if('dropdown' in c.get('class')):
                            texts = list(filter(None,c.text.split('\n')))
                            texts.remove('\r')
                            texts[0] = texts[0].strip(' ')
                            print(('{} - {}'.format(i, texts[0])).upper())
                            texts_itens.append(texts[0].upper())
            return lists_list,texts_itens
        except Exception as err:
            print('ERROR (getURLsUnion): {0}'.format(err))
            os.system('pause')

    def getMax(self, conteudo):
        try:
            maxLen = -1
            index = 0
            for c in conteudo:
                if len(c.contents) > maxLen:
                    maxLen = (len(c.contents))
                    index = conteudo.index(c)
            conteudo = [x for x in conteudo[index].contents if x != '\n' if x != ' ' if x != '']
            return conteudo
        except Exception as err:
            print('ERROR (getMax): {0}'.format(err))
            os.system('pause')

    def updateContent(self, site):
        try:
            conteudo = site.find_all('div', class_='row')
            pager = site.find('ul', class_='pagination')
            pager = [x for x in pager.contents if x != '\n' if x != ' ' if x != '']
            return conteudo, pager
        except Exception as err:
            print('ERROR (updateContent): {0}'.format(err))
            os.system('pause')

    def getContent(self, url):
        try:
            links = []
            site = self.common.soup(self.feature, url)
            self.common.clearTerminal()
            print('PROCESSANDO ...')
            conteudo, pager = self.updateContent(site)
            conteudo = self.getMax(conteudo)
            i = 0
            fim = 0
            text = [x for x in pager[-1].a.get('href').split('/') if x != '\n' if x != ' ' if x != '' if x != '*']
            if(self.common.isNumber(text[-1])):
                fim = int(text[-1])
            elif(self.common.isNumber(text[-2])):
                fim = int(text[-2])
            for i in range(1, fim+1):
                site = self.common.soup(self.feature, url+'/{}'.format(i),)
                self.common.clearTerminal()
                print('PROCESSANDO ... PÁGINA {}'.format(i))
                conteudo, pager = self.updateContent(site)
                conteudo = self.getMax(conteudo)
                for c in conteudo:
                    if(c.a):
                        site = self.common.soup(self.feature, c.a.get('href'))
                        manga_perfil = site.find_all('h4', class_='media-heading manga-perfil')
                        for m in manga_perfil:
                            if(m.a):
                                links_m = m.find_all('a')
                                generos = [x.string for x in links_m if x.string]
                                del links_m
                                break
                        if('Yaoi' not in generos):
                            links.append(c.a.get('href'))
            return random.choice(links)
        except Exception as err:
            print('ERROR (getContent): {0}'.format(err))
            os.system('pause')

    def getURLsUnionGeneros(self,generos):
        try:
            i = 0
            generos_list = []
            itens = []
            for g in generos:
                if(g.string != '\n'):
                    i += 1
                    print(('{} - {}'.format(i, g.string)).upper())
                    itens.append(g.string.upper())
                    generos_list.append(g.a.get('href'))
            return generos_list, itens
        except Exception as err:
            print('ERROR (getURLsUnion): {0}'.format(err))
            os.system('pause')

    def getURLsUnionA_Z(self, a_z):
        try:
            i = 0
            a_z_list = []
            itens = []
            for item in a_z:
                if(item.string != '\n'):
                    i += 1
                    print(('{} - {}'.format(i, item.string)).upper())
                    itens.append(item.string.upper())
                    a_z_list.append(item.a.get('href'))
            return a_z_list, itens
        except Exception as err:
            print('ERROR (getURLsUnion): {0}'.format(err))
            os.system('pause')
            
    def randomItemList(self):
        try:
            url = 'https://unionleitor.top/lista-mangas'
            t_0 = self.common.initCountTime()
            site = self.common.soup(self.feature, url)
            self.common.clearTerminal()
            print('PROCESSANDO ...')
            lists = site.find('ul', class_='nav nav-tabs')
            generos = lists.find('ul', class_='dropdown-menu')
            a_z = site.find('ul', class_='nav nav-pills nav-justified')
            choice = -2
            while choice != 0:
                lists_list, texts_itens = self.getURLsUnion(lists)
                try:
                    choice = int(self.common.readString())
                    if(choice == -2):
                        choice = random.randint(1, 4)
                    if(choice == 1):
                        a_z_list, itens = self.getURLsUnionA_Z(a_z)
                        try:
                            choice = int(self.common.readString())
                            if (choice == -2):
                                choice = random.randint(0, len(a_z_list))
                            url_list = (a_z_list[choice - 1])
                            print('Escolhido => {}'.format(itens[choice - 1]))
                            url_choice = self.getContent(url_list)
                            webbrowser.open(url_choice, new=0, autoraise=True)
                        except Exception as err:
                            pass
                    if(choice == 2):
                        print('Escolhido => {}'.format(texts_itens[choice - 1]))
                        url_list = lists_list[choice - 1]
                        url_choice = self.getContent(url_list)
                        webbrowser.open(url_choice, new=0, autoraise=True)
                    if(choice == 3):
                        print('Escolhido => {}'.format(texts_itens[choice - 1]))
                        url_list = lists_list[choice - 1]
                        url_choice = self.getContent(url_list)
                        webbrowser.open(url_choice, new=0, autoraise=True)
                    if(choice == 4):    
                        generos_list, itens = self.getURLsUnionGeneros(generos)
                        try:
                            choice = int(self.common.readString())
                            if (choice == -2):
                                choice = random.randint(0, len(generos_list))
                            print('Escolhido => {}'.format(itens[choice - 1]))
                            url_list = (generos_list[choice - 1])
                            url_choice = self.getContent(url_list)
                            webbrowser.open(url_choice, new=0, autoraise=True)
                        except Exception as err:
                            print('Error with choice (randomItemList): {0}'.format(err))
                            os.system('pause')
                    if(choice == -1):
                        exit(0)
                except Exception as err:
                    print('Error (randomItemList): {0}'.format(err))
                    os.system('pause')
                t_f = self.common.finishCountTime(t_0)
                segundos = t_f % 60
                minutos  = int(t_f / 60)
                print('Executado em {} minutos e {} segundos'.format(minutos, segundos))
        except Exception as err:
            print('ERROR (randomItemList): {0}'.format(err))
            os.system('pause')

    def buscaSubPastaNaoVazia(self, pasta):
        try:
            subpastas = dict()
            diretorio = os.listdir(pasta)
            for item in diretorio:
                if(item != 'H'):
                    novo_item = os.path.join(pasta, item)
                    if os.path.isdir(novo_item):
                        novo_diretorio = [x for x in os.listdir(novo_item) if x != 'desktop.ini' if x != 'cover.jpg']
                        if len(novo_diretorio) >= 2:
                            subpastas.update({item : novo_item})
            return subpastas
        except Exception as err:
            print('ERROR (buscaSubPastaNaoVazia): {0}'.format(err))
            os.system('pause')

    def openExplorerAleatorioCaps(self, pasta, op):
        try:
            mangas, caps = self.menuCountCaps(pasta, 0)
            if op == 0 or op == 1:
                if op == 0:
                    escolha = (min(list(caps.values())))
                elif op == 1:
                    escolha = (max(list(caps.values())))
                get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
                minimos = (get_indexes(escolha, list(caps.values())))
                aleatorio = random.choice(minimos)
            else:
                aleatorio = list(mangas.values()).index(random.choice(list(mangas.values())))
            print("Selecionado -> {}".format(list(mangas.keys())[aleatorio]))
            # subprocess.run(['explorer', os.path.realpath(list(ordered.values())[aleatorio][1])])
            os.system("pause")
            if platform.system() == "Windows":
                os.startfile(list(mangas.values())[aleatorio][1])
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", list(mangas.values())[aleatorio][1]])
            else:
                subprocess.Popen(["xdg-open", list(mangas.values())[aleatorio][1]])
        except Exception as err:
            print('ERROR (openExplorerAleatorioCaps): {0}'.format(err))
            os.system('pause')

    def escolhaDiretorio(self, subpastas, chaves, nomes, escolha):
        try:
            diretorioEscolhido = subpastas[chaves[escolha-1]]
            self.common.clearTerminal()
            print("Sua escolha: {}".format(nomes[escolha-1]))
            diretorio = os.listdir(diretorioEscolhido)
            return diretorioEscolhido, diretorio
        except Exception as err:
            print('ERROR (escolhaDiretorio): {0}'.format(err))
            os.system('pause')

    def deleteCapHManga(self):
        try:
            choiceH = -1
            pasta = 'D:\\Imagens\\Mangás\\H'
            while choiceH != 0:
                subpastas = self.buscaSubPastaNaoVazia(pasta)
                chaves, nomes = self.menuDeletarMangas(pasta)
                try:
                    escolha = int(self.common.readString())
                    if escolha == 0:
                        break
                    elif escolha == -1:
                        self.common.clearTerminal()
                        self.common.shutDown()
                    diretorioEscolhido, diretorio = self.escolhaDiretorio(subpastas, chaves, nomes, escolha)
                    escolha_e = self.menuExcluir()
                    if escolha_e  == '1' or escolha_e == '2':
                        self.deletar(escolha_e, diretorio, diretorioEscolhido, chaves, nomes, escolha)
                    elif escolha_e == '3':
                        continue
                    elif escolha_e == '-1':
                        self.common.clearTerminal()
                        print("Xau!")
                        sys.exit(0)
                except Exception as err:
                    print('Error com escolha_e (deleteCapHManga): {0}'.format(err))
                    os.system('pause')
        except Exception as err:
            print('ERROR (deleteCapHManga): {0}'.format(err))
            os.system('pause')
    
    def ordenateStringNum(self,value):
        parts = re.split(r'(\d+)', value)
        return [int(part) if part.isdigit() else part for part in parts]

    def deleteCap(self, pasta):
        escolha_e = -2
        while escolha_e != "0":
            subpastas = self.buscaSubPastaNaoVazia(pasta)
            chaves, nomes = self.menuDeletarMangas(pasta)
            try:
                escolha = int(self.common.readString())
                if escolha == 0:
                    break
                elif escolha == -1:
                    self.common.clearTerminal()
                    self.common.shutDown()
                diretorioEscolhido, diretorio = self.escolhaDiretorio(subpastas, chaves, nomes, escolha)
                escolha_e = self.menuExcluir()
                if escolha_e  == '1' or escolha_e == '2':
                    self.deletar(escolha_e, diretorio, diretorioEscolhido, chaves, nomes, escolha)
                elif escolha_e == '3':
                    continue
                elif escolha_e == '-1':
                    self.common.clearTerminal()
                    print("Xau!")
                    sys.exit(0)
            except Exception as err:
                print('Error (deleteCap): {0}'.format(err))
                os.system('pause')

    def deletar(self, escolha_e, diretorio, diretorioEscolhido, chaves, nomes, escolha):    
        try:
            itens = []
            if escolha_e == '1':
                e = 0
                complete_path = os.path.join(self.saida_path, 'logDeleteCaps.txt')
                arquivo = open(complete_path, 'a', encoding='utf-8')
                arquivo.writelines(self.common.timestamp() + '-')
                arquivo.writelines('Mangá: <' + diretorioEscolhido.split('\\')[-1] + '> - ')
                itens = [x for x in diretorio if x != 'desktop.ini' if x != 'cover.jpg']
                itens = sorted(itens, key=lambda v: self.common.ordenateStringNum(v))
                arquivo.writelines('Capítulos apagados: {' + ', '.join(itens[:-1]) + '} - ')
                arquivo.writelines("[Último lido {}]".format(itens[-1]) + '\n')
                arquivo.close()
                for item in itens[:-1]:
                    item_e = os.path.join(diretorioEscolhido, item)
                    if os.path.isfile(item_e):
                        os.chmod(item_e, 0o0777)
                        os.remove(item_e)
                        e += 1
                    else:
                        shutil.rmtree(item_e)
                        e += 1
                    print("{} foi removido".format(item))
                print("Último lido {}".format(itens[-1]))
                print("{} itens excluídos!".format(e))
                if(os.path.split(diretorioEscolhido)[-1] in os.listdir(self.path_H_manga)):
                    shutil.rmtree(diretorioEscolhido)
                    print('Diretório {} removido'.format(diretorioEscolhido))
            elif escolha_e == '2':
                cap_i = float(self.common.readString("Digite o capítulo inicial => "))
                cap_f = float(self.common.readString("Digite o capítulo final => "))
                caps = [round(x,1) for x in arange(cap_i, cap_f+0.1, 0.1)]
                i = 0
                for num in caps[:-2]:
                    busca = re.search(r"\.[0]", str(num)) 
                    if(busca):
                        item = "cap_" + str(int(num))
                    else:
                        item = "cap_" + str(num)
                    item_e = os.path.join(diretorioEscolhido, item)
                    if(os.path.isdir(item_e)):
                        # shutil.rmtree(item_e)
                        i += 1
                        itens.append(item)
                        print("{} foi removido".format(item))
                    else:
                        busca = re.search(r"\.[0]", str(num)) 
                        if(busca):
                            if(num > 9):
                                item = "cap_" + str(int(num))
                            else:
                                item = "cap_0" + str(int(num))
                        else:
                            if(num > 9):
                                item = "cap_" + str(num)
                            else:
                                item = "cap_0" + str(num)
                        item_e = os.path.join(diretorioEscolhido, item)
                        if(os.path.isdir(item_e)):
                            # shutil.rmtree(item_e)
                            i += 1
                            itens.append(item)
                            print("{} foi removido".format(item))
                itens = list(set(itens))
                print("Último lido {}".format(cap_f))
                print("{} itens excluídos!".format(len(itens)))
                complete_path = os.path.join(self.saida_path, 'logDeleteCaps.txt')
                arquivo = open(complete_path, 'a', encoding='utf-8')
                arquivo.writelines(self.common.timestamp() + '-')
                arquivo.writelines('Mangá: <' + diretorioEscolhido.split('\\')[-1] + '> - ')
                arquivo.writelines('Capítulos apagados: {' + ', '.join(itens) + '} - ')
                arquivo.writelines("[Último lido cap_{}]".format(cap_f) + '\n')
                arquivo.close()
            nome = chaves[escolha-1].lower()
            # nomeCompleto = chaves[escolha-1].lower()
            nome = nome.replace("_", ":")
            nome = nome.split(" ")
            if len(nome) > 1:
                novo_nome = nome[0] + " " + nome[1] # pylint: disable=unused-variable
                if len(nome) > 2:
                    novo_nome = " ".join(nome[0:3])
            else:
                novo_nome = nome[0]
            if (" ".join(nome)).startswith("isekai"):
                novo_nome = " ".join(nome)
            print("Lembre-se de ATUALIZAR o(s) capítulo(s) de => [{}] <= na sua lista!!".format(nomes[escolha-1]))
            os.system('PAUSE')
            # print('Abrir AniList?s/n')
            # choice = self.common.readString()
            # if(choice == 's' or choice == 'sim' or choice == 'S' or choice == 'SIM' or choice == '1'):
            #     webbrowser.open(self.initURLSearchAniList+nomeCompleto, new=0, autoraise=True)
            # print('Atualizar [{}] no Myanimelist?s/n'.format(nomes[escolha-1]))
            # choice = self.common.readString()
            # url = 'https://myanimelist.net/login.php'
            # user_name = str(base64.b64decode(b'TWFyaW9vYnJvcw=='), 'utf-8')
            # password = str(base64.b64decode(b'NTlNZDAwNjAh'), 'utf-8')
            # check = False
            # if(choice == 's' or choice == 'sim' or choice == 'S' or choice == 'SIM' or choice == '1'):
            #     while True:
            #         # print('É necessário informar suas credenciais para se comunicar com o site')
            #         # user_name = self.common.readString('Usuário: ')
            #         # password= getpass.getpass('Senha: ')
            #         with webdriver.Chrome(chrome_options=self.common.optionsChrome(True)) as driver:
            #             wait = WebDriverWait(driver, 10)
            #             driver.get(url)
            #             elmnt = driver.find_element(By.ID, 'loginUserName')
            #             elmnt.send_keys(user_name)
            #             elmnt = driver.find_element(By.ID, 'login-password')
            #             elmnt.send_keys(password)
            #             wait.until(presence_of_element_located((By.NAME, 'sublogin'))).send_keys(Keys.ENTER)
            #             time.sleep(2)
            #             site = self.common.soup(feature=self.feature, markup=driver.page_source)
            #             badresult = site.find('div', class_='badresult')
            #             if(badresult):
            #                 message = badresult.string.replace('\n      ', '').replace('\n        ', '')
            #                 print(message)
            #                 continue
            #             if(escolha_e == '1'):
            #                 cap = re.sub('^([a-z_])*|(\.[0-9])$', '', itens[-1]) #pylint: disable=anomalous-backslash-in-string
            #                 lido_cap_i = re.sub('^([a-z_])*|(\.[0-9])$', '', itens[0]) #pylint: disable=anomalous-backslash-in-string
            #             else:
            #                 cap = str(int(caps[-1]+1))
            #                 lido_cap_i = str(cap_i)
            #             driver.get(self.url_search_manga+nomeCompleto)
            #             site = self.common.soup(feature=self.feature, markup=driver.page_source)
            #             mangaResults = site.find_all('a', class_='hoverinfo_trigger fw-b')
            #             mangasCR = [x for x in mangaResults if x.parent.find('a', class_='Lightbox_AddEdit button_edit reading')]
            #             dataSets = [x.string for x in mangasCR]
            #             query = nomeCompleto
            #             v = Vectorial_Model(dataSets)
            #             results = v.cosine_similarity(1, query)
            #             resultV = v.get_doc(results[0])
            #             self.common.clearTerminal()
            #             index = dataSets.index(resultV)
            #             driver.get(mangasCR[index].get('href'))
            #             in_cap = wait.until(presence_of_element_located((By.ID, 'myinfo_chapters')))
            #             mal_cap_atual = in_cap.get_attribute("value")
            #             print('ATUALIZANDO {} EM MYANIMELIST'.format(resultV))
            #             if(len(mal_cap_atual) == 1):
            #                 if(lido_cap_i[0] == '0' and len(lido_cap_i) == 2):
            #                     mal_cap_atual = '0' + mal_cap_atual
            #             if(mal_cap_atual == lido_cap_i):
            #                 check = True
            #                 in_cap.clear()
            #                 in_cap.send_keys(cap)
            #                 button_submit =wait.until(presence_of_element_located((By.NAME, 'myinfo_submit')))
            #                 button_submit.click()
            #                 time.sleep(3)
            #                 break
            #             elif(int(mal_cap_atual) > int(lido_cap_i)):
            #                 check = False
            #             if(not check):
            #                 print("Nada encontrado em MyAnimeList")
            #                 print('Abrir Planilha?s/n')
            #                 choice = self.common.readString()
            #                 if(choice == 's' or choice == 'sim' or choice == 'S' or choice == 'SIM' or choice == '1'):
            #                     webbrowser.open('https://docs.google.com/spreadsheets/d/1rUN-DWuv9PphSXin4C-U2hYKhCur4PTgu9OzJD3nZnc/edit#gid=0', new=0, autoraise=True)
            #                     break
            #                 else:
            #                     webbrowser.open(self.url_search_manga+nomeCompleto)
            #                     break
            #             else:
            #                 break
            # else:
            #     print('Abrir Planilha?s/n')
            #     choice = self.common.readString()
            #     if(choice == 's' or choice == 'sim' or choice == 'S' or choice == 'SIM' or choice ==  '1'):
            #         webbrowser.open('https://docs.google.com/spreadsheets/d/1rUN-DWuv9PphSXin4C-U2hYKhCur4PTgu9OzJD3nZnc/edit#gid=0', new=0, autoraise=True)
            # if(os.path.split(diretorioEscolhido)[-1] in os.listdir(self.path_H_manga)):
            #     webbrowser.open('https://docs.google.com/spreadsheets/d/1Anq_7VqWSLSZ0qXbz4zLCgExoiq7x8sdxjb-VBADVA8/edit#gid=828388584', new=0, autoraise=True)
                

        except Exception as err:
            print('ERROR (deletar): {0}'.format(err))
            os.system('pause')
    
    def getFiles(self, file_path):
        try:
            directory = os.listdir(file_path)
            i = 0
            for d in directory:
                if(d == 'completados.txt'):
                    continue
                index = directory.index(d)
                i = index + 1 
                new_name = re.sub('.txt','',d)
                print('{} - {}'.format(i, new_name))
            choice = int(input('Sua escolha => '))
            if choice == 0:
                return None,  0
            if choice == -1:
                sys.exit(0)
            if choice == -2:
                randomInt = random.randint(0, index - 1)
                file = open(os.path.join(file_path, directory[randomInt]), 'r', encoding='utf-8')
                text = file.read()
                print('Escolhido => {}'.format(re.sub('.txt','',directory[randomInt])))
                return text, randomInt
            print('Escolhido => {}'.format(re.sub('.txt','',directory[choice - 1])))
            file_c = open(os.path.join(file_path, directory[choice - 1]), 'r', encoding='utf-8')
            text = file_c.read()
            file_c.close()
            return text, choice
        except Exception as err:
            print('ERROR (getFiles): {0}'.format(err))
            os.system('pause')
    
    def getURLsBH(self, text):
        try:
            texts = list(filter(None, text.split('\n')))
            i = 0
            texts[0]
            site = self.common.soup(self.feature, texts[0])
            select = site.select('select#edit-genero')
            names = []
            for t in texts:
                index = texts.index(t)
                i = index + 1
                generos = select[0].contents
                names.append(generos[index].string.strip('- '))
                print('{} - {}'.format(i, generos[index].string.strip('- ')))
            choice = int(input('Sua escolha=> '))
            if choice == -1:
                sys.exit(0)
            if choice == 0:
                return None
            if choice == -2:
                randomInt = random.randint(0, len(texts))
                print('Escolhido => {}'.format(names[randomInt]))
                # os.system('PAUSE')
                return texts[randomInt]
            print('Escolhido => {}'.format(names[choice - 1]))
            # os.system('PAUSE')
            return (texts[choice - 1])
        except Exception as err:
            print('ERROR (getURLsBH): {0}'.format(err))
            os.system('pause')

    def getURLs(self, text, choice, bhs):
        try:
            if choice in bhs:
                return self.getURLsBH(text)
            else:
                texts = sorted(text.split('\n'))
                i = 0
                for t in texts:
                    index = texts.index(t)
                    i = index + 1 
                    new_texts = list(filter(None, t.split('/')))
                    print('{} - {}'.format(i, new_texts[-1].upper()))
                choice = int(input('Sua escolha=> '))
                if choice == -1:
                    sys.exit(0)    
                if choice == 0:
                    return
                if choice == -2:
                    randomInt = random.randint(0, len(texts))
                    print('Escolhido => {}'.format(list(filter(None, texts[randomInt].split('/')))[-1].upper()))
                    # os.system('PAUSE')
                    return texts[randomInt]
                print('Escolhido => {}'.format(list(filter(None, texts[choice - 1].split('/')))[-1].upper()))
                # os.system('PAUSE')
                return (texts[choice - 1])
        except Exception as err:
            print('ERROR (getURLs): {0}'.format(err))
            os.system('pause')

    def getContentSiteHS(self, url):
        try:
            links = []
            site = self.common.soup(self.feature, url)
            ulsP = site.find_all('ul', class_='paginacao')
            try:
                nextPage = ulsP[0].find_all('a')[-1]
                while nextPage.text == 'Próxima página »':
                    ulsP = site.find_all('ul', class_='paginacao')
                    conteudo = site.find_all('div', class_='thumb-conteudo')
                    for c in conteudo:
                        if c.a:
                            categoria = self.getCategoriaTagsHS(c.a.get('href'), 0)
                            if(categoria in self.exclude_urls_hs):
                                continue
                            else:
                                links.append(c.a.get('href'))
                    nextPage = ulsP[0].find_all('a')[-1]
                    site = self.common.soup(self.feature, nextPage.get('href'))
            except Exception:
                ulsP = site.find_all('ul')
                conteudo = site.find_all('div', class_='thumb-conteudo')
                for c in conteudo:
                    if c.a:
                        links.append(c.a.get('href'))
            print(random.choice(links))
            webbrowser.open(random.choice(links), new=0, autoraise=True)
        except Exception as err:
            print('ERROR (getContentSiteHS): {0}'.format(err))     
            os.system('pause')

    def getContentSiteHC(self, url):
        try:
            links = []
            initURL = 'https://hiper.cool'
            site = self.common.soup(self.feature, url)
            divP = site.find_all('div', class_='buttons')
            pages = []
            for p in divP[0].contents:
                pages.append(p.get('href'))
            nextPage = pages[0]
            fim = divP[0].find_all('a')[-1]
            i = 0
            while len(fim.get('class')) < 3:
                divP = site.find_all('div', class_='buttons')
                conteudo = site.find_all('a', class_='news-thumb')
                for c in conteudo:
                    links.append(initURL + c.get('href'))
                i += 1
                if pages != divP[0].contents:
                    for p in divP[0].contents:
                        if p.get('href') not in pages:
                            pages.append(p.get('href'))
                if i < len(pages):
                    nextPage = pages[i]
                fim = divP[0].find_all('a')[-1]
                site = self.common.soup(self.feature, initURL + nextPage,)
                links = list(set(links))
            print(nextPage)
            print(random.choice(links))
            webbrowser.open(random.choice(links), new=0, autoraise=True)
        except Exception as err:
            print('ERROR (getContentSiteHC): {0}'.format(err))
            os.system('pause')

    def getContentSiteBH(self, url):
        try:
            links = []
            initURL = 'http://baixarhentai.net'
            site = self.common.soup(self.feature, url)
            conteudo = site.find_all('div', class_ = 'views-field views-field-title')
            pager = site.find('ul', class_ = 'pager')
            nextPage = pager.find('li', class_ = 'pager-next')
            currentPage = pager.find('li', class_ = 'pager-current')
            while currentPage.string:
                for c in conteudo:
                    # print(c.a.get('href'))
                    links.append(initURL + c.a.get('href'))
                if nextPage:
                    site = self.common.soup(self.feature, initURL + nextPage.a.get('href'))
                    conteudo = site.find_all('div', class_ = 'views-field views-field-title')
                    pager = site.find('ul', class_ = 'pager')
                    nextPage = pager.find('li', class_ = 'pager-next')
                    currentPage = pager.find('li', class_ = 'pager-current')
                else:
                    break
            print(random.choice(links))
            webbrowser.open(random.choice(links), new=0, autoraise=True)
        except Exception:
            print("Opção escolhida está vazia")
            os.system('pause')

    def menuCountCaps(self, pasta, op, subpastas=None):
        try:
            if(not subpastas):
                subpastas = self.buscaSubPastaNaoVazia(pasta)
            else:
                exclude = []
                for s in subpastas:
                    directory = os.listdir(subpastas[s])
                    if(len(directory) < 3):
                        exclude.append(s)
                for e in exclude:
                    subpastas.pop(e)
            mangas = dict()
            caps = dict()
            for itens in subpastas.items():
                nome = itens[0]
                nome = nome.replace("_", ":")
                if('desktop.ini' in os.listdir(itens[1])):
                    caps.update({nome : len(os.listdir(itens[1])) - 1})
                    mangas.update({nome : [len(os.listdir(itens[1])) - 1, itens[1]]})
                else:
                    mangas.update({nome : [len(os.listdir(itens[1])), itens[1]]})
                    caps.update({nome : len(os.listdir(itens[1]))})
            alphaKeysOrdenedList = list(sorted(mangas.keys(), key=operator.itemgetter(0))) 
            mangasOrdered = dict(sorted(mangas.items(), key=operator.itemgetter(1)))
            caps = dict(sorted(caps.items(), key=operator.itemgetter(1)))
            if op == 1:
                for k, v in mangasOrdered.items():
                    novo_nome = k
                    # nome = itens[0]
                    # nome = nome.replace("_", ":")
                    # nome = nome.split(" ")
                    # if len(nome) > 1:
                    #     novo_nome = nome[0] + " " + nome[1]
                    #     if len(nome) > 2:
                    #         novo_nome = " ".join(nome[0:3])
                    # else:
                    #     novo_nome = nome[0]
                    if(novo_nome != 'H'):
                        if(v[0] >= 2):
                            print('({}) CAPS = {} \t {}'.format(alphaKeysOrdenedList.index(novo_nome)+1, v[0], novo_nome))
                os.system('pause')
                return mangasOrdered, caps
            if op == 0:
                return mangasOrdered, caps
        except Exception as err:
            print('ERROR (menuCountCaps): {0}'.format(err))
            os.system('pause')

    def mangaMinMax10(self, caps, mangas, op):
        try:
            lista = list(caps.items())
            minimos = []
            maximos =  []
            aleatorio = None
            ordenedList = list(sorted(mangas.items(), key=operator.itemgetter(0)))
            alphaKeysOrdenedList = list(sorted(mangas.keys()))    
            for item in lista:
                indice = (lista.index(item))
                if item[1] < 10:
                    minimos.append(indice)
                else:
                    maximos.append(indice)
            if op == 4:
                print('\t\t   ||')
                print('\tRANDOM MAX \\/')
                aleatorio = (random.choice(maximos))
            if op == 5:
                print('\t\t   ||')
                print('\tRANDOM MIN \\/')
                aleatorio = (random.choice(minimos))
            if op == 6:
                aleatorioMax = (random.choice(maximos))
                aleatorioMin = (random.choice(minimos))
                chaveMax = ordenedList[aleatorioMax][0]
                chaveMin = ordenedList[aleatorioMin][0]
                print('\t\t   ||')
                print('\tRANDOM MIN \\/')
                print("Selecionado->({}) {} \tCAPS {}".format(alphaKeysOrdenedList.index(chaveMin)+1, chaveMin,(mangas[chaveMin][0])))
                print('\t\t   ||')
                print('\tRANDOM MAX \\/')
                print("Selecionado MAX ->({}) {} \tCAPS {}".format(alphaKeysOrdenedList.index(chaveMax)+1, chaveMax,(mangas[chaveMax][0])))
                os.system('pause')
                
            if aleatorio:
                chave = ordenedList[aleatorio][0]
                print("Selecionado ->({}) {} \tCAPS {}".format(alphaKeysOrdenedList.index(chave)+1, chave,(mangas[chave][0])))
                os.system('pause')
        except Exception as err:
            print('ERROR (mangaMinMax10): {0}'.format(err))       
            os.system('pause')

    def mangaMinMaxNone(self, op, caps, mangas):
        try:
            aleatorio = None
            alphaKeysOrdenedList = (sorted(mangas.keys()))
            alphaItemsOrdenedList = list(sorted(mangas.items(), key=operator.itemgetter(0)))
            if op == 0 or op == 1:
                if op == 0:
                    escolha = (min(list(caps.values())))
                    print('\t\t   ||')
                    print('\tRANDOM MIN \\/')
                elif op == 1:
                    escolha = (max(list(caps.values())))
                    print('\t\t   ||')
                    print('\tRANDOM MAX \\/')

                get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
                selecionados = (get_indexes(escolha, list(caps.values())))
                aleatorio = random.choice(selecionados)
                CapsOrdenedList = list(sorted(mangas.items(), key=operator.itemgetter(1)))
                chave = CapsOrdenedList[aleatorio][0]
            elif op == -1:
                aleatorio = list(mangas.values()).index(random.choice(list(mangas.values())))
                chave = alphaItemsOrdenedList[aleatorio][0]
                print('\t\t    ||')
                print('\tRANDOM NONE \\/')
            print("Selecionado ->({}) {} \tCAPS {}".format(alphaKeysOrdenedList.index(chave) + 1, chave,(mangas[chave][0])))
            os.system('pause')
        except Exception as err:
            print('ERROR (mangaMinMaxNone): {0}'.format(err))
            os.system('pause')

    def mangaAleatorio(self, pasta, op, subpastas=None):
        try:
            mangas, caps = self.menuCountCaps(pasta, 0,subpastas)
            
            if op in range(4, 7):
                self.mangaMinMax10(caps, mangas, op)
            else:
                self.mangaMinMaxNone(op, caps, mangas)
        except Exception as err:
            print('ERROR (mangaAleatorio): {0}'.format(err))
            os.system('pause')
    
    def unzipRename(self, pasta):
        try:
            contadorUnzips = 0
            contadorCapsMangas = 0
            pathName = "content"
            mangas = []
            subpastas = self.buscaSubPasta(pasta)
            for pasta in subpastas.items():
                diretorio = os.listdir(pasta[1])
                for arquivo in diretorio:
                    item = os.path.join(pasta[1], arquivo)
                    if os.path.isfile(item):
                        busca = re.findall('.zip', arquivo)
                        
                        if len(busca) >= 1:
                            # completo = "{}/{}".format(pasta, arquivo)
                            with zipfile.ZipFile("{}/{}".format(pasta[1], arquivo), 'r') as zip_ref:
                                zip_ref.extractall("{}".format(pasta[1]))
                            try:
                                newName = "cap" + re.sub("-", ".", re.findall("[0-9]+-[0-9]+",arquivo)[0])
                            except Exception:
                                newName = "cap" + re.sub("_", "", re.findall("_[0-9]+_", arquivo)[0])
                            shutil.move("{}/{}".format(pasta[1], pathName), "{}/{}".format(pasta[1], newName))
                            nome = "{}/{}".format(pasta[1], arquivo)
                            os.chmod(nome, 0o0777)
                            os.remove(nome)
                            contadorCapsMangas += 1
                            contadorUnzips += 1
                            if pasta[0] not in mangas:
                                print("Mangá: {}".format(pasta[0]))
                                mangas.append(pasta[0])
                            print("{} foi descompactado!".format(newName))
                            # shutil.move("{}/{}".format(pasta, arquivo), lixeira)
                            # shutil.rmtree("{}/{}".format(pasta, arquivo))
                if contadorCapsMangas > 0:
                    print("{} capítulo(s) descompactado(s) e renomeado(s)!".format(contadorCapsMangas))
                    contadorCapsMangas = 0

            print("PROCESSO FINALIZADO")
            print("{} capítulo(s) descompactado(s) e renomeado(s) de {} mangá(s)!".format(contadorUnzips, len(mangas)))
        except Exception as err:
            print('ERROR (unzipRename): {0}'.format(err))
            os.system('pause')

    def buscaSubPasta(self, pasta):
        try:
            subpastas = dict()
            diretorio = os.listdir(pasta)
            for item in diretorio:
                novo_item = os.path.join(pasta, item)
                if os.path.isdir(novo_item):
                    subpastas.update({item : novo_item})
            return subpastas
        except Exception as err:
            print('ERROR (buscaSubPasta): {0}'.format(err))
            os.system('pause')
    
    def unzipManga(self):
        subpastas = self.buscaSubPasta(self.mangaPasta)
        for pasta in subpastas.items():
            diretorio = os.listdir(pasta[1])
            for arquivo in diretorio:
                item = os.path.join(pasta[1], arquivo)
                if os.path.isfile(item):
                    if item.endswith('zip'):
                        if arquivo.startswith('drive'):
                            self.extractZipDrive(item)
                            os.chmod(item, 0o0777)
                            os.remove(item)
                    elif item.endswith('rar'):
                        print("Precisa revisão")
                        # self.extractRar(item)
                    else:
                        print("Nenhum arquivo encontrado em " + pasta[1])

    def extractZipDrive(self, file):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            out_dir = os.path.dirname(os.path.realpath(file))
            for item in zip_ref.infolist():
                new_item = zip_ref.extract(item, out_dir)
                if(os.path.isfile(new_item)):
                    if(new_item.endswith('rar')):
                        self.extractRar(new_item, out_dir)
                    elif(new_item.endswith('zip')):
                        pass
                        # self.extractZip(new_item)          

    def extractRar(self, file, out_dir):
        with rarfile.RarFile(file, 'r') as rar_ref:
            last_item = rar_ref.namelist()[-1]
            # new_path = os.path.dirname(os.path.realpath(file))
            new_path = os.path.join(out_dir, last_item)
            for item in rar_ref.infolist():
                rar_ref.extract(item, out_dir)
        if(os.path.isdir(new_path)):
            name_file = os.path.basename(new_path)
            id_cap = "cap_" + re.search('([0-9]+\-?)(\s){0,0}([\.0-9]+)?', name_file).group(0) #pylint: disable=anomalous-backslash-in-string
            shutil.move(new_path, os.path.join(out_dir, id_cap))
            os.chmod(file, 0o0777)
            os.remove(file)

    """ def extractZip(self, file):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            print("Precisa revisão")
            # for item in zip_ref.infolist(): """

    def unzipHs(self, pasta):
        try:
            diretorio = os.listdir(pasta)
            for arquivo in diretorio:
                busca = re.findall('.zip', arquivo)

                if len(busca) >= 1:
                    with zipfile.ZipFile("{}/{}".format(pasta, arquivo), 'r') as zip_ref:
                        zip_ref.extractall("{}".format(pasta))
        except Exception as err:
            print('ERROR (unzipInPath): {0}'.format(err))        
            os.system('pause')
                
    def unzipInPath(self,pasta):
        try:
            diretorio = os.listdir(pasta)
            contador = 0
            pathName = "content"
            for arquivo in diretorio:
                busca = re.findall('.zip', arquivo)

                if len(busca) >= 1:
                    with zipfile.ZipFile("{}/{}".format(pasta, arquivo), 'r') as zip_ref:
                        zip_ref.extractall("{}".format(pasta))
                    try:
                        newName = "cap" + re.sub("-", ".", re.findall("[0-9]+-[0-9]+",arquivo)[0])
                    except Exception:
                        newName = "cap" + re.sub("_", "", re.findall("_[0-9]+_", arquivo)[0])
                    shutil.move("{}/{}".format(pasta, pathName), "{}/{}".format(pasta, newName))
                    nome = "{}/{}".format(pasta, arquivo)
                    os.chmod(nome, 0o0777)
                    os.remove(nome)
                    contador += 1
            print("{} mangá(s) descompactado(s) e renomeado(s)!".format(contador))
            os.system('PAUSE')
        except Exception as err:
            print('ERROR (unzipInPath): {0}'.format(err))
            os.system('pause')
      
    def menuMangaAleatorio(self, path, subpastas=None):
        try:
            escolha = -2
            while escolha != 0:
                self.common.clearTerminal()
                print("-"*32)
                print("| SELECIONANDO MANGÁ ALEATÓRIO |")
                print("-"*32)
                print("1 - selecionar mangá com menos capítulos\n2 - selecionar mangá com mais capítulos\n3 - selecionar mangás aleatório com nenhum critério\n4 - para > 10\n5 - para < 10\n6 - para ambos\n0 - para sair")
                try:
                    escolha = int(self.common.readString())
                except Exception:
                    escolha = -2
                if escolha == 0:
                    self.common.clearTerminal()
                    return 0
                    
                elif escolha == 1:
                    self.common.clearTerminal()
                    self.mangaAleatorio(path, 0, subpastas)
                elif escolha == 2:
                    self.common.clearTerminal()
                    self.mangaAleatorio(path, 1, subpastas)
                elif escolha == 3:
                    self.common.clearTerminal()
                    self.mangaAleatorio(path, -1, subpastas)
                elif escolha == 4:
                    self.common.clearTerminal()
                    self.mangaAleatorio(path, escolha, subpastas)
                elif escolha == 5:
                    self.common.clearTerminal()
                    self.mangaAleatorio(path, escolha, subpastas)
                elif escolha == 6:
                    self.common.clearTerminal()
                    self.mangaAleatorio(path, escolha, subpastas)
                else: 
                    self.common.clearTerminal()
                    print("Opção inválida")
        except Exception as err:
            print('ERROR (menuMangaAleatorio): {0}'.format(err))
            os.system('pause')
    
    def menuOpenExplorerAleatorioCaps(self, pasta):
        try:
            escolha = -1
            while escolha != 0:
                self.common.clearTerminal()
                try:
                    escolha = self.menuExplorarManga()
                except Exception:
                    escolha = -1
                if escolha == 0:
                    self.common.clearTerminal()
                    print("Xau!")
                elif escolha == 1:
                    self.common.clearTerminal()
                    self.menuCountCaps(pasta, 1)
                elif escolha == 2:
                    self.common.clearTerminal()
                    self.openExplorerAleatorioCaps(pasta, 0)
                elif escolha == 3:
                    self.common.clearTerminal()
                    self.openExplorerAleatorioCaps(pasta, 1)
                elif escolha == 4:
                    self.common.clearTerminal()
                    self.openExplorerAleatorioCaps(pasta, 2)
                else: 
                    self.common.clearTerminal()
                    print("Opção inválida")
                    os.system("pause")
                return escolha
        except Exception as err:
            print('ERROR (menuOpenExplorerAleatorioCaps): {0}'.format(err))
            os.system('pause')
        
    def menuExplorarManga(self):
        try:
            print("-"*20)
            print("| EXPLORANDO MANGÁ |")
            print("-"*20)
            print("0 - para sair\n1 - ver quantidade de capítulos dos mangas\n2 - abrir mangá com menos capítulos\n3 - abrir mangá com mais capítulos\n4 - abrir mangás aleatório")
            escolha = int(input("Digite a opção -> "))
            return escolha
        except Exception as err:
            print('ERROR (menuExplorarManga): {0}'.format(err))
            os.system('pause')

    def menuExcluir(self):
        print("Deseja?\n1 - Excluir todos capitulos\n2 - Selecionar capitulos a excluir\n3 - para selecionar novamente\n0 - para sair")
        try:
            escolha_e = input("Digite sua escolha -> ")
            return escolha_e
        except Exception as err:
            print('Error (menuExcluir): {0}'.format(err))
            return '3'

    def menuDeletarMangas(self, pasta):
        try:
            subpastas = self.buscaSubPastaNaoVazia(pasta)
            i = 1
            nomes = []
            chaves = list(sorted(subpastas.keys(), key=operator.itemgetter(0)))
            for chave in chaves:
                novo_nome = chave
                # nome = chave.split(" ") 
                # if len(nome) > 1:
                #     if len(nome) > 10:
                #         novo_nome = nome[0] + " " + nome[1]
                #     else:
                #         novo_nome = " ".join(nome)
                # else:
                #     novo_nome = nome[0]
                # novo_nome = novo_nome.replace("_", ":")
                clean_dir = [x for x in os.listdir(subpastas[chave]) if x != 'desktop.ini']
                if(novo_nome != 'H'):
                    if(len(clean_dir) >= 2):
                        nomes.append(novo_nome)
                        print("{} - {}".format(i, novo_nome))
                        i += 1
            return chaves, nomes
        except Exception as err:
            print('ERROR (menuDeletarMangas): {0}'.format(err))
            os.system('pause')

    def menuPrincipalDeletarMangas(self):
        try:
            pasta = self.mangaPasta
            escolha = 1
            while escolha != 0:
                self.common.clearTerminal()
                print("-"*27)
                print("| EXCLUI CAPÍTULOS MANGÁS |")
                print("-"*27)
                print("0 - para sair\n1 - para deletar capitulos mangás\n2 - para deletar capitulos h-mangás")
                try:
                    escolha = int(self.common.readString())
                except Exception:
                    escolha = -1
                if escolha == 0:
                    self.common.clearTerminal()
                    print("XAU!")
                    # os.system("pause")
                elif escolha == 1:
                    self.common.clearTerminal()
                    self.deleteCap(pasta)
                elif escolha == 2:
                    self.common.clearTerminal()
                    self.deleteCapHManga()
                elif escolha == -1:
                    self.common.clearTerminal()
                    self.common.shutDown()
                else: 
                    self.common.clearTerminal()
                    print("Opção inválida")
                    os.system("pause")
        except Exception as err:
            print('ERROR (menuPrincipalDeletarMangas): {0}'.format(err))
            os.system('pause')

    def menuH_mangaAleatorioWeb(self):
        try:
            bh = [1,2,3]
            hc = [5,6]
            hs = [7,8,9,10]
            choice = -2
            while choice  != 0:
                text, choice = self.getFiles(self.arquivo_entrada)
                if(text and choice):
                    t_o = self.common.initCountTime()
                    url= self.getURLs(text,choice,bh)
                    if(url):
                        if choice in hs:
                            self.getContentSiteHS(url)
                            t_f = self.common.finishCountTime(t_o)
                            segundos = t_f % 60
                            minutos  = int(t_f / 60)
                            print('Tempo total: {} minutos e {} segundos'.format(minutos, segundos))
                        if choice in hc:
                            self.getContentSiteHC(url)
                            t_f = self.common.finishCountTime(t_o)
                            segundos = t_f % 60
                            minutos  = int(t_f / 60)
                            print('Tempo total: {} minutos e {} segundos'.format(minutos, segundos))
                        if choice in bh:
                            self.getContentSiteBH(url)
                            t_f = self.common.finishCountTime(t_o)
                            segundos = t_f % 60
                            minutos  = int(t_f / 60)
                            print('Tempo total: {} minutos e {} segundos'.format(minutos, segundos))
        except Exception as err:
            print('ERROR (menuPrincipalDeletarMangas): {0}'.format(err))
            os.system('pause')

    def finishinMusic(self):
        try:
            sound = self.arquivos_sounds+'\\gta-v-mission-passed-sound.mp3'
            playsound(sound)
        except Exception as err:
            print('Error (music): {0}'.format(err))
            # os.system('pause')
    
    def menu(self):
        choice = -2
        while choice:
            print('''1 - selecionar site para baixar mangá\n2 - para baixar mangá de site de uma scan\n3 - verificar notificações union\n4 - para baixar capítulo mangá em pasta especifica\n5 - para mangá aleatório na web\n6 - para explorar mangás\n7 - para deletar capítulos\n8 - para manga aleatório\n9 - para descompactar todos mangas baixados da manga livre/mangaProject\n10 - para descompactar de um manga baixado da manga livre/mangaProject\n11 - para extrair capitulos de arquivos compactados baixados do drive\n12 - para verificar home H-manga\n13 - Gerar arquivo com links H\n14 - para H-Manga aleatório na web\n0 - voltar''')
            try:
                choice = int(self.common.readString())
                if(choice == -1):
                    self.common.shutDown()
                elif(choice == 0):
                    self.common.clearTerminal()
                    break
                elif(choice == 13):
                    choice1 = -2
                    while choice1 != -1:
                        print('1 - gerar links HC\n2 - gerar links de HS\n3 - gerar links de BH')
                        choice1 = int(self.common.readString())
                        if(choice1 == -1):
                            self.common.shutDown()
                        elif(choice1 == 0):
                            break
                        if(choice1 == 1):
                            url = input('Digite a url: ')
                            self.getLinksHC(url, self.feature)
                            self.finishinMusic()
                        elif(choice1 == 2):
                            url = input('Digite a url: ')
                            self.getLinksHS(url)
                            self.finishinMusic()
                        elif(choice1 == 3):
                            print('1 - via url\n2 - via codigo')
                            newChoice = self.common.readString()
                            if(newChoice == '1'):
                                url = input('Digite a url: ')
                                self.getLinksToTxtBH(url)
                                self.finishinMusic()
                            elif(newChoice == '2'):
                                codigo = self.common.readString('Codigo => ')
                                self.getLinkCodigoBH(codigo)
                                self.finishinMusic()
                            elif(newChoice == '-1'):
                                self.common.shutDown()         
                elif(choice == 4):
                    choice = -1
                    urlsPath = dict()
                    url = ''
                    path = ''
                    while True:
                        try:
                            url = input('URL do capítulo => ')
                            if(url == '0'):
                                break
                            path = input('Onde salvar => ')
                            if(path == '0'):
                                break
                            elif(path == '-1'):
                                self.common.shutDown()
                            else:
                                if(urlsPath.get(path)):
                                    update = urlsPath.get(path)
                                    update.append(url)
                                    urlsPath.update({path: update})
                                else:
                                    urlsPath.update({path : [url]})
                        except Exception as err:
                            print('Error with url choice 3: {0}'.format(err))
                            os.system('pause')
                        
                    self.downloadManga(urlsPath)
                    self.finishinMusic()
                elif(choice == 5):
                    self.randomItemList()
                elif(choice == 6):
                    choice5 = -2
                    while choice5 != 0:
                        print('1 - para mangás\n2 - para h-mangás')
                        choice5 = int(self.common.readString())
                        if(choice5 == 1):
                            self.menuOpenExplorerAleatorioCaps(self.mangaPasta)
                        elif(choice5 == 2):
                            self.menuOpenExplorerAleatorioCaps(self.path_H_manga)
                        elif(choice5 == -1):
                                self.common.shutDown()
                elif(choice == 7):
                    self.menuPrincipalDeletarMangas()
                elif(choice == 14):
                    self.menuH_mangaAleatorioWeb()
                elif(choice == 8):
                    choice8 = -2
                    while choice8 != 0:
                        print('1 - para mangás\n2 - para h-mangás\n3- para mangás +18\n4 - para aleatório de uma pasta')
                        choice8 = int(self.common.readString())
                        result = -1
                        if(choice8 == 0):
                            break
                        while result != 0:
                            if(choice8 == 1):
                                result = self.menuMangaAleatorio(self.mangaPasta)
                            elif choice8 == 2:
                                result = self.menuMangaAleatorio(self.path_H_manga)
                            elif choice8 == 3:
                                result = self.menuMangaAleatorio(self.mangaPasta, self.manga18)
                            elif choice8 == 4:
                                self.common.clearTerminal()
                                path = 'a'
                                while path != '':
                                    path = self.common.readString('Diretório => ')
                                    if(path == '0'):
                                        break
                                    elif(path == '-1'):
                                        self.common.shutDown()
                                    diretorio = os.listdir(path)
                                    aleatorio = random.choice(diretorio)
                                    print(aleatorio)
                                    os.system('pause')
                elif(choice in range(9, 11)):
                    print("-"*22)
                    print("| DESCOMPACTA MANGÁS |")
                    print("-"*22)
                    if(choice == 9):
                        self.unzipRename(self.mangaPasta)
                    if(choice == 10):
                        pasta = input("Digite o diretorio a ser analisado -> ")
                        if(pasta == '-1'):
                            self.common.shutDown()
                        elif(pasta == '0'):
                            continue
                        self.unzipInPath(pasta)
                elif(choice == 12):
                    try:
                        print('1 - para novos\n2 - para todos\n0 para voltar')
                        choice_ = int(self.common.readString())
                        if(choice_ == -1):
                            self.common.shutDown()
                        elif(choice_ == 0):
                            continue
                        self.verifyHomeHManga(choice_) 
                    except Exception as err:
                        print('Error choice 11: {0}'.format(err))
                        os.system('pause')
                elif(choice == 3):
                    self.verificaNotificacoesUnion()
                    self.finishinMusic()   
                elif(choice == 1):
                    try:
                        choice13 = -2
                        while choice != 0:
                            t_o = self.common.initCountTime()
                            print('1 - Union\n2 - Mangadex\n3 - Tsuki Mangás\n4 - Leitor.net\n5 - MangaLivre\n6 - MangaHost\n7 - Golden Mangás\n-3 - hipercool\n-4 - HSeason\n-5 - BH')
                            choice13 = int(self.common.readString())
                            if(choice13 != -1 and choice13 != 0):
                                url = self.common.readString('Digite a url: ')
                            if(choice13 == 1):
                                print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo')
                                choice13 = int(self.common.readString())
                                if(choice13 == 1):
                                    self.salvarMangaInteiroUnion(url)
                                elif(choice13 == 2):
                                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                                    self.baixarPartindoCapUnion(url=url, cap_i=cap_i )
                                elif(choice13 == 3):
                                    cap_f = self.common.readString('Baixar até o capítulo => ')
                                    self.baixarPartindoCapUnion(url=url, cap_f=cap_f)
                                elif(choice13 == 4):
                                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                                    cap_f = self.common.readString('Baixar até o capítulo => ')
                                    self.baixarPartindoCapUnion(url=url, cap_i=cap_i, cap_f=cap_f)
                                elif(choice13 == 5):
                                    self.baixarPartindoCapUnion(url=url)
                            elif(choice13 == 2):
                                self.baixarMangaDex(url=url)
                            elif(choice13 == 3):
                                print('='*8+'Tsuki Mangas'+'='*8)
                                self.baixarMangaTsukiMangas(url=url)
                            elif(choice13 == 4):
                                self.baixarMangaLeitorDotNet(url=url)
                            elif(choice13 == 5):
                                self.baixarMangaLivre(url=url)
                            elif(choice13 == 6):
                                self.baixarMangaMHost(url)
                            elif(choice13 == 7):
                                self.baixarMangaGolden(url)
                            elif(choice13 == -3):
                                print('1 - baixar todos capitulos\n2 - baixar a partir de um capítulo até final\n3 - baixar do inicio até um capítulo\n4 - baixar a partir de um capítulo até um capítulo\n5 - baixar último capitulo\n6 - baixar todos mangas do link')
                                choice13 = int(self.common.readString())
                                if(choice13 == 1):
                                    self.salvarMangaInteiroHC(url)
                                elif(choice13 == 2):
                                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                                    self.baixarPartindoCapHC(url=url,cap_i=cap_i)
                                elif(choice13 == 3):
                                    cap_f = self.common.readString('Baixar até o capítulo => ')
                                    self.baixarPartindoCapHC(url=url,cap_f=cap_f)
                                elif(choice13 == 4):
                                    cap_i = self.common.readString('Baixar a partir de capítulo => ')
                                    cap_f = self.common.readString('Baixar até o capítulo => ')
                                    self.baixarPartindoCapHC(url=url,cap_f=cap_f, cap_i=cap_i)
                                elif(choice13 == 5):
                                    cap_i, cap_f = 'None', 'None'
                                    self.baixarPartindoCapHC(url=url,cap_f=cap_f, cap_i=cap_i)
                                elif(choice13 == 6):
                                    self.baixarTodosMangasLinkHC(url)
                            elif(choice13 == -4):
                                print('1 - para somente um capitulo\n2 - para baixar todos capítulos\n3 - para baixar todos os mangás do link')
                                choice13 = int(self.common.readString())
                                artista = self.common.readString('Artista => ')
                                artista = artista.strip()
                                self.baixarImgsHS(url, choice13, artista)
                                # self.baixarZipadoHS(url)
                                # self.common.unzipCommon(self.path_H_manga)
                            elif(choice13 == -5):
                                artista = self.common.readString('Artista => ')
                                artista = artista.strip()
                                self.baixarLeitorBH(url, artista)
                            elif(choice13 == -1):
                                self.common.shutDown()
                            elif(choice13 == 0):
                                break
                            t_f = self.common.finishCountTime(t_o)
                            segundos = t_f % 60
                            minutos  = int(t_f / 60)
                            print('Executado em: {} minutos e {} segundos'.format(minutos, segundos))
                            self.finishinMusic()
                    except Exception as err:
                        print('Error choice 13: {0}'.format(err))
                        os.system('pause')
                elif(choice == 2):
                    self.baixarMangaScan()
                elif(choice == 11):
                    self.unzipManga()
                elif(choice == -2):
                    # self.baixarCapLeitorDotnet('https://leitor.net/manga/saenai-riiman-to-yankee-joshikousei/217913/capitulo-13')
                    self.baixarCapNeox('https://neoxscans.com/manga/fff-class-trashero/', 52)
                else:
                    self.common.clearTerminal()
                    print('Opção Inválida!')
            except Exception as err:
                print('Error (menu): {0}'.format(err))
                os.system('pause')

if __name__ == "__main__":
    manga = Manga()
    manga.getMangaNewCapUnion()