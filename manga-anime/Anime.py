import rarfile, zipfile, os, re, time, random, webbrowser, random
from Common import Common
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located, alert_is_present,element_to_be_clickable

class Anime:

    def __init__(self, feature):
        self.feature = feature
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.common = Common('html.parser')
        self.saida_path = self.common.criarPasta('saida', self.dir_path)
        self.cwd = os.getcwd()
        self.common.clearTerminal()
        self.initUrl_hAnime = 'https://hanime.tv'
        self.initur_url_animes_house = 'https://animeshouse.net/'
        self.favHanime = ['3D', 'AHEGAO', 'ANAL', 'BIG BOOBS', 'BLOW JOB', 'BOOB JOB', 'CENSORED', 'COSPLAY', 'CREAMPIE', 'DARK SKIN', 'FACIAL', 'FANTASY', 'FILMED', 'FOOT JOB', 'GANGBANG', 'GLASSES', 'HAND JOB', 'HAREM', 'HD', 'INCEST', 'LACTATION',  'LOLI', 'MAID', 'MASTURBATION', 'MILF', 'MIND BREAK', 'MIND CONTROL', 'MONSTER', 'NEKOMIMI', 'NURSE', 'ORGY', 'POV', 'PREGNANT', 'PUBLIC SEX', 'RAPE', 'REVERSE RAPE', 'RIMJOB', 'SCHOOL GIRL', 'SHOTA', 'SOFTCORE', 'SWIMSUIT', 'TEACHER', 'THREESOME', 'TOYS', 'TSUNDERE',  'UNCENSORED', 'VANILLA', 'VIRGIN', 'WATERSPORTS', 'X-RAY', 'YURI']
        self.tag_dic_Hanime = {}
        self.comCensura_h_tube = {}
        self.semCensura_h_tube = {}
        print("-"*15)
        print("| MENU ANIMES |")
        print("-"*15)

    def randomHAnimeWeb(self):
        choice = -2
        while choice:
            print('0) para voltar\n-1) para sair')
            choice = self.common.whileDataTypeReadString(int)
            if(choice == 0):
                self.common.clearTerminal()
                break
            elif(choice == -1):
                self.common.shutDown()
            elif(choice == 1):
                pass

    def random_anime_web(self):
        choice = -2
        while choice:
            print(' 0) para voltar\n-1) para sair')
            choice = self.common.whileDataTypeReadString(int)
            if(choice == 0):
                self.common.clearTerminal()
                break
            elif(choice == -1):
                self.common.shutDown()
            elif(choice == 1):
                pass
    
    def randomHtube(self):
        url = ('https://www.hentaistube.com/lista-de-hentais-legendados/')
        self.comCensura_h_tube = {}
        self.semCensura_h_tube = {}
        site = self.common.soup(url=url)
        abas = site.find_all(class_='aba')
        links = []
        if not self.comCensura_h_tube and not self.semCensura_h_tube:
            t_o = self.common.initCountTime()
            for x in abas:
                links.extend([y.get('href')for y in x.find_all('a')])
            for l in links:
                censurado, nome = self.verificaCensuraHTube(l, True)
                if(censurado):
                    self.comCensura_h_tube.update({nome:l})
                else:
                    self.semCensura_h_tube.update({nome:l})
            t_f = self.common.finishCountTime(t_o)
            segundos = t_f % 60
            minutos  = int(t_f / 60)
            print('Executado em: {} minutos e {} segundos'.format(minutos, segundos))
        choice = ''
        while choice != '0':
            print('1 -Com Censura\n2 - Sem Censura')
            choice = self.common.readString()
            
            if(choice == '1'):
                nameAleatorio = random.choice(list(self.comCensura_h_tube.keys()))
                valueAleatorio = self.comCensura_h_tube[nameAleatorio]
            elif(choice == '2'):
                nameAleatorio = random.choice(list(self.semCensura_h_tube.keys()))
                valueAleatorio = self.semCensura_h_tube[nameAleatorio]
            elif(choice == '0'):
                break
            elif(choice == '-1'):
                self.common.shutDown()
            os.system('pause')
            print("Selecionado " + nameAleatorio)
            self.openInChrome(valueAleatorio)
        # for ul in uls:
        #     ul_as = ul.find_all('a')
        #     for a in ul_as:
        #         # print(a.get('href'))
        #         if self.verificaCensuraHTube(a.get('href')):
        #             # print('com censura')
        #             # comCensura.append(a.get('href'))
        #         else: 
        #             # print('sem censura')
        #             # semCensura.append(a.get('href'))
    
    def getHAnimeTags(self):
        with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
            wait = WebDriverWait(driver, 5)
            driver.get(self.initUrl_hAnime)
            wait.until(presence_of_element_located((By.CLASS_NAME, 'nav_drawer_toggle'))).click()
            browse = wait.until(presence_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/aside/div[2]/div[1]/div[2]/div/div/div[2]/div[6]/a')))
            driver.get(browse.get_attribute('href'))
            # webdriver.ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.END).key_up(Keys.CONTROL).key_up(Keys.END).perform()
            # time.sleep(3)
            element = driver.find_element_by_xpath('//*[@id="app"]/div[4]/main/div/div/div/div[3]/h2')
            # localizando o elemento
            desired_y = (element.size['height'] / 2) + element.location['y']
            # dimensões da janela
            window_h = driver.execute_script('return window.innerHeight')
            window_y = driver.execute_script('return window.pageYOffset')
            # posição atual na janela
            current_y = (window_h / 2) + window_y
            # localização até onde será feito o scroll 
            scroll_y_by = desired_y - current_y
            i = current_y
            # rolando até a localização desejada
            print('PROCESSANDO TAGS')
            while i <= scroll_y_by:
                i += 200
                driver.execute_script("window.scrollTo(0, {})".format(i))
                time.sleep(0.1)
            # pegando tags
            tags = driver.find_elements_by_class_name('tile')
            self.tag_dic_Hanime = {x.text.split('\n')[0]:x.get_attribute('href') for x in tags }

    def openFavH_anime(self):
        t_o = self.common.initCountTime()
        self.getHAnimeTags()
        with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
            for f in self.favHanime:
                driver.get(self.tag_dic_Hanime[f])
                num_atual_page = -1
                last_page = -2
                print('COLETANDO HENTAIS DE {}'.format(f))
                links = []
                while num_atual_page != last_page:
                    elmnts = driver.find_elements_by_class_name('pb-3')
                    elmnts = [x for x in elmnts if x.tag_name == 'a']
                    links += [x.get_attribute('href') for x in elmnts]
                    links = list(set(links))
                    atual_page = driver.find_element_by_class_name('pagination__item--active')
                    num_atual_page = int(atual_page.text)
                    pagination = driver.find_element_by_class_name('pagination')
                    pages = pagination.find_elements_by_css_selector("button.pagination__item")
                    last_page = int(pages[-1].text)
                    for p in pages:
                        num_page = int(p.text)
                        if(num_page - num_atual_page == 1):
                            try:
                                if('pagination__item--active primary' not in  p.get_attribute('class')):
                                    p.click()
                                    time.sleep(2)
                                    break
                            except:
                                print()
                aleatorio = random.choice(links)
                titulo = self.common.soup(url=aleatorio).title.string
                titulo = titulo.replace('Watch', '')
                titulo = titulo.replace('Hentai Video', '')
                titulo = re.sub('(in)[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\']*', '', titulo) #pylint: disable=anomalous-backslash-in-string
                titulo = titulo.strip()
                self.openInChrome(aleatorio)
                print('Selecionado => {}'.format(titulo))
                # os.system('pause')
            t_f = self.common.finishCountTime(t_o)
            segundos = t_f % 60
            minutos  = int(t_f / 60)
            print('Executado em: {} minutos e {} segundos'.format(minutos, segundos))

    def hAnimeTV(self):
        links = []
        t_o = self.common.initCountTime()
        self.getHAnimeTags()
        with webdriver.Chrome(options=self.common.optionsChrome(True)) as driver:
            tags_keys = list(self.tag_dic_Hanime.keys())
            i = 0
            choice = ''
            while choice != -1:
                i = 0
                for t in self.tag_dic_Hanime:
                    i += 1
                    print('{} - {}'.format(i, t))
                try:
                    choice = int(self.common.readString())
                except:
                    print('TENTE NOVAMENTE!')
                    continue
                if(choice == -1):
                    self.common.shutDown()
                elif(choice == 0):
                    return
                print('Escolheu => {}'.format(tags_keys[choice-1]))
                driver.get(self.tag_dic_Hanime[tags_keys[choice-1]])
                num_atual_page = -1
                last_page = -2
                print('COLETANDO HENTAIS')
                links = []
                while num_atual_page != last_page:
                    elmnts = driver.find_elements_by_class_name('pb-3')
                    elmnts = [x for x in elmnts if x.tag_name == 'a']
                    links += [x.get_attribute('href') for x in elmnts]
                    links = list(set(links))
                    atual_page = driver.find_element_by_class_name('pagination__item--active')
                    num_atual_page = int(atual_page.text)
                    pagination = driver.find_element_by_class_name('pagination')
                    pages = pagination.find_elements_by_css_selector("button.pagination__item")
                    last_page = int(pages[-1].text)
                    for p in pages:
                        num_page = int(p.text)
                        if(num_page - num_atual_page == 1):
                            try:
                                if('pagination__item--active primary' not in  p.get_attribute('class')):
                                    p.click()
                                    time.sleep(2)
                                    break
                            except:
                                print()
                aleatorio = random.choice(links)
                titulo = self.common.soup(url=aleatorio).title.string
                titulo = titulo.replace('Watch', '')
                titulo = titulo.replace('Hentai Video', '')
                titulo = re.sub('(in)[\w\sà-ú\(\)\[\]\{\}\-\+\=!@#$%ªº´`¨&_§¬¢£~^\°;,.\']*', '', titulo) #pylint: disable=anomalous-backslash-in-string
                titulo = titulo.strip()
                print('Selecionado => {}'.format(titulo))
                self.openInChrome(aleatorio)
                os.system('pause')
                t_f = self.common.finishCountTime(t_o)
                segundos = t_f % 60
                minutos  = int(t_f / 60)
                print('Executado em: {} minutos e {} segundos'.format(minutos, segundos))

    def openInChrome(self, url):
        directory6432 = os.listdir(os.environ['PROGRAMW6432'])
        directoryX86 = os.listdir(os.environ['PROGRAMFILES(X86)'])
        if('Google' in directoryX86):
            if os.path.isdir(os.path.join(os.environ['PROGRAMFILES(X86)'], 'Google\\Chrome')):
                chrome_path = os.path.join(os.environ['PROGRAMFILES(X86)'], 'Google\\Chrome\\Application\\chrome.exe')
            else:
                chrome_path = os.path.join(os.environ['PROGRAMW6432'], 'Google\\Chrome\\Application\\chrome.exe')
        elif('Google' in directory6432):
            if os.path.isdir(os.path.join(os.environ['PROGRAMW6432'], 'Google\\Chrome')):
                chrome_path = os.path.join(os.environ['PROGRAMW6432'], 'Google\\Chrome\\Application\\chrome.exe')
            else:
                chrome_path = os.path.join(os.environ['PROGRAMFILES(X86)'], 'Google\\Chrome\\Application\\chrome.exe')
        webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('google-chrome').open(url)
    
    def openInFirefox(self, url):
        directory6432 = os.listdir(os.environ['PROGRAMFILES'])
        directoryX86 = os.listdir(os.environ['PROGRAMFILES(X86)'])
        if('Mozilla Firefox' in directoryX86):
            if os.path.isdir(os.path.join(os.environ['PROGRAMFILES(X86)'], 'Mozilla Firefox')):
                firefox_path = os.path.join(os.environ['PROGRAMFILES(X86)'], 'Mozilla Firefox\\firefox.exe')
        elif('Mozilla Firefox' in directory6432):
            if os.path.isdir(os.path.join(os.environ['PROGRAMFILES'], 'Mozilla Firefox')):
                firefox_path = os.path.join(os.environ['PROGRAMFILES'], 'Mozilla Firefox\\firefox.exe')
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
        webbrowser.get('firefox').open(url)

    def renameFilesAnime(self, directory):
        archives = os.listdir(directory)
        i = 0

        for archive in archives:
            resultSearch = re.search('[0-9]{1,2} ', archive)
            if resultSearch:
                newName = re.sub('[0-9]{1,2} ','', archive) 
            finalResult = re.findall('-[0-9]*', archive)
            finalResult = list(filter(None, finalResult))
            if finalResult:
                while '-' in finalResult:
                    finalResult.remove('-')
                print(finalResult)
                r = finalResult[0].strip('-')
                os.rename(archive, r + ' ' +newName)
                i += 1
        print('{} arquivos renomeados!'.format(i))
    
    def unzipAnime(self, directory):
        diretorio =  os.listdir(directory)
        for d in diretorio:
            item = os.path.join(directory, d)
            if os.path.isfile(item):
                if item.endswith('.rar') or item.endswith('.zip'):
                    if item.endswith('.rar'):
                        with rarfile.RarFile(item, 'r') as rar_ref:
                            rar_ref.extractall(directory)
                    if item.endswith('.zip'):
                        with zipfile.ZipFile(item, 'r') as zip_ref:
                            zip_ref.extractall()
                    os.chmod(item, 0o0777)
                    os.remove(item)

    def checkpathVariables(self):
        '''
        check path variables.
        if unrar.exe nor present then 
        install unrar and set unrar.exe in path variable.
        '''
        try:
                user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
        except KeyError:
                user_paths = []
        # iterate over paths.
        for item in user_paths:
            print("User path python variables :"+ item)
        # check rar tool exe present or not.
        for item in user_paths:
            # print(item)
            if("unrar.exe" in item):
                print("Unrar tool setup found PYTHONPATH")
                return
        print("Unrar tool setup not found in  PYTHONPATH")
        # print os path
        os_paths_list = os.environ['PATH'].split(';')
        # check rar tool exe present or not.
        for item in os_paths_list:
            # print(item)
            if("unrar.exe" in item):
                print("Unrar tool setup found in PATH")
                rarfile.UNRAR_TOOL = item 
                print("Unrar tool path set up complete ."+item)
                return
        print("Unrar tool setup not found in PATH")
        print("RAR TOOL WILL NOT WORK FOR YOU.")
        downloadlocation = "https://www.rarlab.com/rar/unrarw32.exe"
        print("install unrar form the link "+downloadlocation)

    def getLinksToTxt_hAnime_BH(self):
        initUrl = 'http://baixarhentai.net'
        censura = ['All', 88, 87]
        nomes = ['All', 'SemCensura', 'ComCensura']
        n = 0
        for c in censura:
            site = self.common.soup('http://baixarhentai.net/listona?field_censura_tid={}&field_estudio_tid=All&field_generos_tid=All&field_produzido_em_tid=All&field_audio_legenda_value=All'.format(c), self.feature)
            tbl = site.findAll('tbody')[0]
            complete_path  = os.path.join(self.dir_path, 'saida_TXT\\bhLinks{}.txt'.format(nomes[n]))
            if os.path.isfile(complete_path):
                os.remove(complete_path)
            for tr in tbl.findAll('tr'):
                for td in tr.findAll('td'):
                    if td.a:
                        href = td.a.get('href')

                        arquivo = open(complete_path, 'a')
                        arquivo.writelines(initUrl+href+"\n")
            n += 1
            print('Arquivo salvo em: {}'.format(complete_path))  
    
    def verificaCensuraHTube(self, url, op=None):
        site = self.common.soup(url=url)
        name = site.find_all('b')
        nome = ""
        censura = None
        for n in name:
            if n.string == 'Censura:':
                busca = re.findall("Sim", n.parent.text)
                if busca:
                    censura = True
                else:
                    censura = False
            elif(n.string == 'Hentai:'):
                if(n.parent):
                    if(n.parent.a):
                        nome = n.parent.a.string
        if(op):
            return censura, nome
        else:
            return censura

    def getAllLinksToTxtHTube(self):
        t_o = self.common.initCountTime()
        url = ('https://www.hentaistube.com/lista-de-hentais-legendados/')
        site = self.common.soup(url=url)
        uls = site.find_all('ul')[2:]
        comCensura = []
        semCensura = []
        for ul in uls:
            ul_as = ul.find_all('a')
            for a in ul_as:
                # print(a.get('href'))
                if self.verificaCensuraHTube(a.get('href')):
                    # print('com censura')
                    comCensura.append(a.get('href'))
                else: 
                    # print('sem censura')
                    semCensura.append(a.get('href'))
        
        complete_path  = os.path.join(self.dir_path, 'saida_TXT')
        nameArchiveC = '\\hTubeComCensura.txt'
        if os.path.isfile(complete_path):
            os.remove(complete_path)
            for c in comCensura:
                arquivo = open(complete_path + nameArchiveC, 'a')
                arquivo.writelines(c + '\n')
            arquivo.close()
        print('Arquivo salvo em: {}'.format(complete_path+nameArchiveC))
        nameArchiveS = '\\hTubeSemCensura.txt'
        if os.path.isfile(complete_path):
            os.remove(complete_path)
            for s in semCensura:
                arquivo2 = open(complete_path + nameArchiveS, 'a')
                arquivo2.writelines(s + '\n')
            arquivo2.close()
        print('Arquivo salvo em: {}'.format(complete_path+nameArchiveS))
        t_f = self.common.finishCountTime(t_o)
        segundos = t_f % 60
        minutos  = int(t_f / 60)
        print('Foram encontrados {} com censura e {} sem censura!'.format(len(comCensura), len(semCensura)))
        print('Tempo total: {} minutos e {} segundos'.format(minutos, segundos))

    def menu_gerar_arquivo(self):
        choice = -2
        while choice:
            print('0 - para voltar\n1 - para Links H-Animes BH em txt\n2 - para H-Animes H-Tube em txt\n-1 - para sair')
            choice = self.common.whileDataTypeReadString(int)
            if(choice == 0):
                self.common.clearTerminal()
                break
            elif(choice == -1):
                self.common.shutDown()
            elif(choice == 1):
                self.getLinksToTxt_hAnime_BH()
            elif(choice == 2):
                self.getAllLinksToTxtHTube()

    def animes_house_aleatorio(self):
        site = self.common.soup(url='https://animeshouse.net/anime/')
        next_pag = site.find('i', id='nextpagination')
        arrow_pag =  next_pag.parent
        dic_animes = {}
        while next_pag:
            archive_content = site.find('div', id='archive-content')
            animes = archive_content.find_all('article')
            for anime in animes:
                h3 = anime.find('h3')
                if h3:
                    if h3.a:
                        dic_animes.update({h3.text: h3.a.get('href')})
            site = self.common.soup(url=arrow_pag.get('href'))
            next_pag = site.find('i', id='nextpagination')
            if next_pag:
                arrow_pag =  next_pag.parent
        r =random.choice(list(dic_animes.keys()))
        print('Abrindo {}'.format(r))
        webbrowser.open(dic_animes[r])

    def animeMenu(self):
        choice = -2
        while choice:
            print('1 - para gerar arquivos de Links\n3 - para hanime aleatório\n4 - para abrir todos os favoritos do hanime\n5 - para htube aleatório\n0 - para voltar')
            choice = ''
            while type(choice) != int:
                try:
                    choice = int(self.common.readString())
                except:
                    print('TENTE NOVAMENTE')
            if(choice == 0):
                self.common.clearTerminal()
                break
            elif(choice == -1):
                self.common.shutDown()
            elif(choice == 3):
                self.hAnimeTV()
            elif(choice == 4):
                self.openFavH_anime()
            elif(choice == 5):
                self.randomHtube()
            else:
                self.common.clearTerminal()
                print('Opção Inválida!')
                

if __name__ == "__main__":
    c = Common()
    site = c.soup(url='https://animeshouse.net/anime/')
    next_pag = site.find('i', id='nextpagination')
    arrow_pag =  next_pag.parent
    dic_animes = {}
    while next_pag:
        archive_content = site.find('div', id='archive-content')
        animes = archive_content.find_all('article')
        for anime in animes:
            h3 = anime.find('h3')
            if h3:
                if h3.a:
                    dic_animes.update({h3.text: h3.a.get('href')})
        site = c.soup(url=arrow_pag.get('href'))
        next_pag = site.find('i', id='nextpagination')
        if next_pag:
            arrow_pag =  next_pag.parent
    r =random.choice(list(dic_animes.keys()))
    print('Abrindo {}'.format(r))
    webbrowser.open(dic_animes[r])
    print()
