from Manga import Manga
from Anime import Anime
from Common import Common
import os
# os.system('pause')
if __name__ == "__main__":
    choice = -2
    # os.system('pause')
    common = Common()
    while choice != -1:
        # os.system('pause')
        common.clearTerminal()
        print(' 1) Mangá\n 2) Anime\n-1) para sair')
        try:
            choice = int(common.readString())
        except ValueError:
            print('Entrada inválida')
        if(choice == -1):
            common.shutDown()
        elif(choice == 1):
            manga = Manga('html.parser')
            manga.menu()
            print()
        elif(choice == 2):
            anime = Anime('html.parser')
            anime.animeMenu()
        else:
            common.clearTerminal()
            print('Opção inválida')
            

