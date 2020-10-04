import requests, base64,os, getpass, sys
import selenium.webdriver.chrome.options as chromeOptions
from time import sleep, time, ctime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located, alert_is_present,element_to_be_clickable

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS #pylint:disable=no-member
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def timestamp ():    
    """ Retorna tempo  atual """       
    t = time ( )
    # print (ctime ( t ) )
    return ctime ( t )

def initCountTime():
    """ Inicia contagem de tempo """
    print(timestamp())
    t_o = time() 
    return t_o

def finishCountTime(t_o):
    """ Finaliza contagem de tempo """
    print(timestamp())
    t_f = int(time () - t_o)
    return t_f

def soup(feature=None, url=None, cookies =None, markup=None, headers=None, request=None, pause=None):
    """ retorna objeto BeautifulSoup """
    if(not feature):
        feature = 'html.parser'
    if(not headers):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
    try:
        if(not request):
            if(url):
                if(pause):
                    sleep(pause)
                if(headers):
                    request = requests.get(url, headers=headers, cookies=cookies)
                else:
                    request = requests.get(url, headers=headers, cookies=cookies)
        
        if(markup):
            if(feature):
                soup = BeautifulSoup(markup, feature)
            else:
                soup = BeautifulSoup(markup, feature)
        else:
            if(feature):
                soup = BeautifulSoup(request.content, feature,from_encoding="utf-8")
            else:
                soup = BeautifulSoup(request.content, feature,from_encoding="utf-8")
        return soup
    except requests.exceptions.ConnectionError as err:
        print('Erro de conexão: {0}'.format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def optionsChrome(headless=False):
    chrome_options = chromeOptions.Options()
    if(headless):
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "D:\\Downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    return chrome_options

if __name__ == "__main__":
    t_i = initCountTime()
    scans = {}
    mangas_scans = {}
    mangasNomes = []
    mangas_links = []
    caminho = os.path.dirname(os.path.realpath(__file__))
    print(caminho)
    os.system('pause')
    try:
        # criando pasta para salvar arquivos gerados
        saida = os.mkdir(os.path.join(caminho, 'saida'))
    except:
        # se a pasta já tiver criada somente salva o caminho para usar depois
        saida = os.path.join(caminho, 'saida')
        print('Já existe pasta saida')
    caminhoArquivo_mangas_assinados = os.path.join(saida, 'mangas-assinados.txt')
    caminhoArquivo_mangas_scans = os.path.join(saida, 'mangas-scans.txt')
    url_inicial = 'https://unionleitor.top'
    url_login = 'https://unionleitor.top/login'
    url_ass = 'https://unionleitor.top/minhas-assinaturas'
    resposta = input('Deseja salvar nome das scans? (s/n)')
    dir = os.path.dirname(__file__)
    rel_chrome_path = os.path.join(dir,'chromedriver.exe')
    chrome_path = resource_path(rel_chrome_path)
    print(chrome_path)
    
    try:
        with webdriver.Chrome(executable_path=chrome_path,options=optionsChrome()) as driver:
            # abre página inicial
            driver.get(url_inicial)
            wait = WebDriverWait(driver, 10)
            # print('É necessário informar suas credenciais para se comunicar com o site')
            driver.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[6]/a').click()
            sleep(3)
            # driver.get(url_login)
            # pede o login enquanto não for válido o login
            while True:
                email = 'bros_mario_rv@hotmail.com'
                # leitura de dados de email ou usuário
                # email = input('Email ou usuário: ')
                password = "yW#8%DY4Am&A"
                # leitura de senha
                # password = getpass.getpass('Senha: ')
                # envia email para navegador
                wait.until(presence_of_element_located((By.ID, 'email'))).send_keys(email)
                # envia senha para navegador
                wait.until(presence_of_element_located((By.ID, 'password'))).send_keys(password)
                # realiza login no navegador
                wait.until(presence_of_element_located((By.ID, 'btn-enviar'))).click()
                sleep(3)
                alertLogin = driver.find_elements_by_css_selector('.alert.alert-danger')
                resultA = [x.text for x in alertLogin if x.text == ' Usuário ou senha inválidos']
                # verificação se falhou o login e continua o loop
                if(resultA):
                    print(resultA[0])
                    continue
                successLogin = driver.find_elements_by_css_selector('.alert.alert-success.alert-dismissible')
                resultS = [x.text for x in successLogin if x.text == '×\nLogin efetuado com sucesso!']
                # verificação se sucesso no login e sai do loop
                if(resultS):
                    print(resultS[0])
                    break
            # abre páginas de mangás assinados
            driver.get('https://unionmangas.top/minhas-assinaturas') 
            sleep(3)
            while True:
                try:
                    # pega o numero atual da página
                    e = driver.find_element_by_class_name('pagination').find_element_by_class_name('active').find_element_by_tag_name('a')
                    print('Visitando página {}'.format(e.text))
                except Exception as err:
                    print(err)
                html = driver.page_source
                site = soup(markup=html)
                # encontra todos os mangas da página
                mangas = site.find_all('div', class_='col-md-2 col-xs-6 text-center')
                for m in mangas:
                    if(m.b):
                        # adiciona nome para ser salvo depois
                        mangasNomes.append(m.b.text)
                    if(m.a):
                        # adiciona link para ser acessado depois
                        mangas_links.append(m.a.get('href'))
                # pega elemento para próxima página
                try:
                    # encontra o elemento para próxima página
                    nextPage = driver.find_element_by_class_name('pagination').find_elements_by_tag_name('a')[-2]
                    if(nextPage.text == '›\nNext'):
                        sleep(2)
                        # clica no elemento para próxima página
                        nextPage.click()
                    else:
                        break
                except Exception as err:
                    print(err)
            if(resposta == 's' or resposta == 'S'):
                for lm in mangas_links:
                    mangaNome = 'Web server is down'
                    # abre página do mangá enquanto estiver com problema para abrir
                    while mangaNome == 'Web server is down':
                        driver.get(lm)
                        html = driver.page_source
                        site = soup(markup=html)
                        mangaNome = site.find('h2').text
                    # verifica se existe o elemento com nome da scan
                    if(site.find('div', class_='text-right')):
                        elmnt = site.find('div', class_='text-right')
                        scans = {x.string:x.get('href') for x in elmnt.find_all('a')}
                        mangas_scans.update({mangaNome: scans})
            print()
    except Exception as err:
        print(err)
        os.system('pause')
    # salva arquivo de com os mangás e suas scans
    with open(caminhoArquivo_mangas_assinados, 'w', encoding='utf-8') as arquivo:
        for m in mangasNomes:
            arquivo.writelines('{}\n'.format(m))
    print('Seu arquivo foi salvo em: {}'.format(caminhoArquivo_mangas_assinados))
    with open(caminhoArquivo_mangas_scans, 'w', encoding='utf-8') as arquivo:
        for c, v in mangas_scans.items():
            arquivo.writelines('Mangá: {} | Scans: {} link => {}\n'.format(c, ' '.join(v)))
    print('Seu arquivo foi salvo em: {}'.format(caminhoArquivo_mangas_scans))
    t_f = finishCountTime(t_i)
    millis = int(t_f * 1000)
    hours = int(millis / 3.6e+6)
    x = millis % 3.6e+6
    minutes = int(x / 60000)
    y = x % 60000
    seconds = int(y / 1000)
    k = y % 1000
    milliseconds = k
    print('Terminado em {} horas {} minutos {} segundos {} milisegundos. '.format(hours, minutes, seconds, milliseconds))
