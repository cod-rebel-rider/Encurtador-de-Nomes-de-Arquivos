import os

def renomear_arquivos(diretorio):
    lista_arquivos = []
    print("Iniciando a verificação do diretório...")
    for pasta_atual, sub_pastas, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_do_arquivo = os.path.join(pasta_atual, arquivo)
            nome_atual_do_arquivo = os.path.join(arquivo)
            print (f"")
            if len(nome_atual_do_arquivo) > 200:
                novo_nome = nome_atual_do_arquivo[:200]
                lista_arquivos.append(caminho_do_arquivo)
                print(f"Arquivo identificado: {caminho_do_arquivo} -> {novo_nome}")
    print("Varredura concluída.")
    return lista_arquivos

diretorio = '/home/cod-rebel-rider/Backup_HD'

lista_arquivos = renomear_arquivos(diretorio)

with open('arquivos_longos.txt', 'w') as file:
    for arquivo in lista_arquivos:
        file.write(f'{arquivo}\n')
print("Lista de arquivos salva em arquivos_longos.txt.")