from bs4 import BeautifulSoup
import requests, sys, rarfile, zipfile, re, json, shutil, base64
from os import system, name, listdir, path, chmod, remove, mkdir, environ
from time import time, ctime, sleep
import selenium.webdriver.chrome.options as chromeOptions
from progress.bar import ChargingBar
class Common:
    def __init__(self, feature = None, saida_path=None):
        if(feature):
            self.feature = feature
        else:
            self.feature = 'html.parser'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        self.chrome_options = chromeOptions.Options()
        if saida_path:
            self.saida_path = saida_path
        else:
            self.saida_path = self.criarPasta('saida', path.dirname(path.realpath(__file__)))
        self.chrome_extension = self.chromeAppData()

    def chromeAppData(self):
        try:
            chrome_extension = path.join(environ['USERPROFILE'], 'AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions')
            if(path.isdir(chrome_extension)):
                return chrome_extension
            else:
                print('Instale o google chrome')
                return
        except Exception as err:
            print('ERRO (chromeAppData): {}'.format(err))

    def checkExtensionChrome(self, id_extension,):
        try:
            if(self.chrome_extension):
                directory = listdir(self.chrome_extension)
                extension_path = None
                for d in directory:
                    if(d == id_extension):
                        path_dir = path.join(self.chrome_extension, d)
                        if(path.isdir(path_dir)):
                            new_directory = listdir(path_dir)
                            for i in new_directory:
                                extension_path = path.join(path_dir, i)
                                if(path.isdir(extension_path)):
                                    return extension_path
                    else:
                        extension_path = None
                return extension_path
            else:
                print('Impossível continuar sem o google chrome')
                return
        except Exception as err:
            print('ERRO (checkExtensionChrome): {}'.format(err))

    def makeExtension(self, unpack_extension, version, version_path):
        try:
            directory = listdir(unpack_extension)
            new_extension_path = path.join(unpack_extension, version_path)
            for d in directory:
                if(d != version):
                    item = path.join(unpack_extension, d)
                    checkPath = path.join(new_extension_path, d)
                    if(d in listdir(new_extension_path)):
                        if(path.isdir(checkPath)):
                            shutil.rmtree(checkPath)
                        elif(path.isfile(checkPath)):
                            chmod(checkPath, 0o0777)
                            remove(checkPath)
                    shutil.move(item, new_extension_path)
            return new_extension_path
        except Exception as err:
            print('ERRO (makeExtension): {}'.format(err))

    def installExtensionCRX(self, id_extension):
        try:
            extension = self.checkExtensionChrome(id_extension)
            if(self.chrome_extension):
                if(not extension):
                    extension_crx = self.downloadArchive("https://clients2.google.com/service/update2/crx?response=redirect&os=win&arch=x86-64&os_arch=x86-64&nacl_arch=x86-64&prod=chromiumcrx&prodchannel=unknown&prodversion=9999.0.9999.0&acceptformat=crx2,crx3&x=id%3D{}%26uc".format(id_extension), op=1)        
                    return extension_crx
                else:
                    return extension
            else:
                print('Voce insiste em continuar sem o google chrome')
                return 
                
        except Exception as err:
            print('ERRO (installExtensionCRX): {}'.format(err))

    def installExtensionUnpacked(self, id_extension):
        try:
            extension = self.checkExtensionChrome(id_extension)
            if(extension):
                new_chrome_extension = ''
                if(not extension):
                    extension_down = self.downloadArchive("https://clients2.google.com/service/update2/crx?response=redirect&os=win&arch=x86-64&os_arch=x86-64&nacl_arch=x86-64&prod=chromiumcrx&prodchannel=unknown&prodversion=9999.0.9999.0&acceptformat=crx2,crx3&x=id%3Dclddifkhlkcojbojppdojfeeikdkgiae%26uc", path.join(self.saida_path, id_extension+'.zip'), op=1)
                    unpack_extension = re.sub('.zip', '', extension_down)
                    if(not path.isdir(unpack_extension)):
                        mkdir(unpack_extension)
                        with zipfile.ZipFile(extension_down, 'r') as zip_ref:
                            for item in zip_ref.infolist():
                                zip_ref.extract(item,path=unpack_extension)
                    manifest = path.join(unpack_extension, 'manifest.json')
                    if(path.isfile(manifest)):
                        json_f = open(manifest, 'r')
                        data = json.load(json_f)
                        json_f.close()
                        for i in data:
                            if(i == 'version'):
                                version = data[i] + '_0'
                                version_path = path.join(unpack_extension, version)
                                if(path.isdir(version_path)):
                                    directory = listdir(version_path)
                                    directory_ue = listdir(unpack_extension)
                                    if(len(directory) != len(directory_ue) - 1):
                                        new_extension_path = self.makeExtension(unpack_extension, version, version_path)
                                else:
                                    mkdir(version_path)
                                    new_extension_path = self.makeExtension(unpack_extension, version, version_path)
                                break
                    new_chrome_extension = path.join(self.chrome_extension, id_extension)
                    try:
                        shutil.copytree(unpack_extension, new_chrome_extension)
                    except FileExistsError:
                        pass
                else:
                    new_extension_path = extension
            else:
                print('Voce insiste em continuar sem o google chrome')
                return 
            return new_extension_path
        except Exception as err:
            print('ERRO (installExtensionUnpacked): {}'.format(err))
    
    def optionsChrome(self, headless=False, id_extension=None):
        if(headless):
            self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.chrome_options.add_argument("--disable-notifications")
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--verbose')
        self.chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "D:\\Downloads",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-software-rasterizer')
        if(id_extension):
            extension_crx = self.installExtensionCRX(id_extension)
            if(extension_crx.endswith('.crx')):
                self.chrome_options.add_extension(extension_crx)
            else:
                self.chrome_options.add_argument('load-extension='+extension_crx)
        return self.chrome_options

    def ordenateStringNum(self,value):
        parts = re.split(r'(\d+)', value)
        return [int(part) if part.isdigit() else part for part in parts]

    def soup(self, feature=None, url=None, cookies =None, markup=None, headers=None, request=None, pause=None):
        """ retorna objeto BeautifulSoup """
        try:
            if(not request):
                if(url):
                    if(pause):
                        sleep(pause)
                    if(headers):
                        request = requests.get(url, headers=headers, cookies=cookies)
                    else:
                        request = requests.get(url, headers=self.headers, cookies=cookies)
            
            if(markup):
                if(feature):
                    soup = BeautifulSoup(markup, feature)
                else:
                    soup = BeautifulSoup(markup, self.feature)
            else:
                if(feature):
                    soup = BeautifulSoup(request.content, feature,from_encoding="utf-8")
                else:
                    soup = BeautifulSoup(request.content, self.feature,from_encoding="utf-8")
            return soup
        except requests.exceptions.ConnectionError as err:
            print('Erro de conexão: {0}'.format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def downloadArchive(self, url, total_files=1, file_atual=0,path_archiveName=None, op=None):  
        try:
            archiveName = path.basename(url.split("?")[0])
            response = requests.get(url, headers=self.headers, stream=True)
            # rContent = response.content
            content_type = response.headers['content-type']
            # data = base64.b64decode(rContent)
            # archiveName = path.join(self.saida_path,"image{}.{}".format(x, content_type.split('/')[-1]))
            # with open(archiveName, "wb") as f:
            #     for chunk in response:
            #         f.write(chunk)
            searchUrl = re.search('\.[a-zA-Z0-9]+$', url) #pylint: disable=anomalous-backslash-in-string
            if(not path_archiveName):
                path_archiveName = path.join(self.saida_path, path.basename(response.url.split("/")[-1]))
            searchArchiveName = re.search('\.[a-zA-Z0-9]+$', path_archiveName) #pylint: disable=anomalous-backslash-in-string
            if(searchUrl):
                path_archiveName = path.join(path_archiveName, archiveName)
            elif(re.search('\.', archiveName)): #pylint: disable=anomalous-backslash-in-string
                path_archiveName = path.join(path_archiveName, archiveName)
            elif(searchArchiveName):
                pass
            else:
                path_archiveName = path_archiveName + '.' + content_type.split('/')[-1]
            if(re.search(r'(\.webp)$', path_archiveName)):
                path_archiveName = re.sub(r'\.[a-zA-Z0-9]+$', '.jpg',path_archiveName)
            if response.status_code == requests.codes.OK: #pylint: disable=no-member
                response.raw.decode_content = True
                chunks = [x for x in response]
                bar = ChargingBar('Baixando',  suffix='%(percent).1f%% - %(eta)ds', max=len(chunks))
                with open(path_archiveName, 'wb') as new_archive:
                    for chunk in chunks:
                        new_archive.write(chunk)
                        bar.next()
                        bar.write('\t\t\t\t\t\t[{}/{}]'.format(file_atual+1,total_files))
                    bar.finish()
                print("Download finalizado. Arquivo salvo em: {}".format(path_archiveName))
                if op:
                    return path_archiveName
            else:
                response.raise_for_status()
        except Exception as err:
            if('520 Server Error' in str(err) or '522 Server Error' in str(err) or '404 Client Error' in str(err)):
                print(ctime())
                print('ERROR (downloadArchive): {0}'.format(err))
                pass
            else:
                print(ctime())
                print('ERROR (downloadArchive): {0}'.format(err))
                system('pause')
            raise

    def criarPasta(self, name, pasta):
        try:
            name = name.replace(':', '-')
            directory = listdir(pasta)
            complete = path.join(pasta, name)
            # print(complete)
            if(name not in directory):
                if not path.isdir(complete):
                    mkdir(complete)
                    return complete, False
                return complete, False
            else:
                # print('Diretório {} existente'.format(complete))
                return complete
        except Exception as err:
            print('ERROR (criarPasta): {0}'.format(err))
            system('pause')

    def unzipCommon(self, directory):
        diretorio =  listdir(directory)
        for d in diretorio:
            item = path.join(directory, d)
            if path.isfile(item):
                if item.endswith('.rar') or item.endswith('.zip'):
                    if item.endswith('.rar'):
                        with rarfile.RarFile(item, 'r') as rar_ref:
                            rar_ref.extractall(directory)
                    if item.endswith('.zip'):
                        with zipfile.ZipFile(item, 'r') as zip_ref:
                            zip_ref.extractall()
                    chmod(item, 0o0777)
                    remove(item)    
    
    def clearTerminal(self):
        """ limpar terminal multiplataforma """
        system('cls' if name == 'nt' else 'clear')  
    
    def timestamp (self):           
        t = time ()
        # print (ctime ( t ) )
        return ctime (t)

    def initCountTime(self):
        print(self.timestamp())
        t_o = time() 
        return t_o

    def finishCountTime(self, t_o):
        print(self.timestamp())
        t_f = int(time () - t_o)
        return t_f
    
    def isNumber(self, string):
        try:
            int(string)
        except ValueError:
            return False
        return True
    
    def readString(self, string=None):
        try:
            if(string):
                choice = input(string)
            else:
                choice = input('Sua escolha => ')
            return choice
        except Exception as err:
            print('Error: {0}'.format(err))
            return None

    def whileDataTypeReadString(self, data_type):
        entrada = None
        try:
            entrada = int(self.readString())
        except Exception:
            while type(entrada) != data_type:
                entrada = self.readString()
                try:
                    entrada = data_type(entrada)
                except ValueError:
                    continue
        return entrada
    
    def shutDown(self):
        sys.exit(0)
        



