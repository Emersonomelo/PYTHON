'''Feito por EMERSON MELO Janeiro 2021
Script feito para separar e renomear todos os boletos gerado pelo sistema GERENCIANET
'''


import PyPDF2
#nome dos clientes
clientes = ['Cliente 1 - mensalidade mes janeiro 2022']

def separar_pdf():
    #pasta para salvar os novos boletos
    pasta_nova = r"C:\PYTHON_BOLETOS\novos_pdfs"
    #nome do arquivo com todos os boletos
    arquivo_pdf_junto = r"C:\PYTHON_BOLETOS\arquivo boletos\1-mesclado.pdf"
    #Função para separar e renomear cada boleto
    with open(arquivo_pdf_junto, 'rb') as arquivo_pdf:
        leitor = PyPDF2.PdfFileReader(arquivo_pdf)
        num_paginas = leitor.getNumPages()
        i = 0
        for num_pagina in range(1,num_paginas,2):
            escritor = PyPDF2.PdfFileWriter()
            pagina_atual = leitor.getPage(num_pagina)
            escritor.addPage(pagina_atual)
            with open(f'{pasta_nova}/{clientes[i]}.pdf', 'wb') as novo_pdf:
                escritor.write(novo_pdf)
                i+=1
        print()
        print(f'Separação feita e colocada na pasta: \n {pasta_nova}')

separar_pdf()
