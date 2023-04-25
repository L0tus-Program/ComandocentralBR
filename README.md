# Central Comander Brasil


-> Central de comando para toda a rede de computadores da Brasil dos Parafusos



-> Funcionalidades já aplicadas
    - Acesso ao portal interno da Brasil 
    - Teste de Whois e ping em python
        Opção direta no servidor de e-mails e em outros domínios

-> Funcionalidades que ainda devem ser desenvolvidas

    - Linha de comando para outros computadores da rede
        Invoke-Command -ComputerName DESKTOP-T5KT3B8 -FilePath c:\DESLIGA.ps1
            Aparentemente preciso de uma configuração de domínio da nossa rede windows pra conseguir esxecutar esse script , ele deve invocar um script do meu proprio computador para outra máquina.

    - Acesso a planilha de controle de pedidos do Jeferson




Caso não tenha os requirimentos instalados basta rodar "pip install -r requirements.txt"