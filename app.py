def processar_content(entrada, saidaContent):
    with open(entrada, 'r') as arq_entrada, open(saidaContent, 'w') as arq_saida:
        documento = ""
        banco = ""
        forma = ""
        valor = ""
        
        for linha in arq_entrada:
            if not linha.strip():
                continue
            
            partes = linha.split()
            if linha.startswith('Vencimento'):
                continue
            elif any(palavra in linha for palavra in ["Glosa/Desc.", "Deb.Autom.", "Dinheiro", "CHQ:", "C.Credito", "C.Debito", "Deposito"]):
                banco = linha.split()[2]
                forma = linha.split()[3]
                valor = linha.split()[4]
                print(banco, forma, valor)
                arq_saida.write(f"{banco};{forma};{valor}\n")
            else:
                documento = linha.split()[3]
                arq_saida.write(f"{documento}\n")


entrada = 'input.txt'
saidaContent = 'saidamos_content.txt'

processar_content(entrada, saidaContent)
print("Arquivo processado com sucesso!")
