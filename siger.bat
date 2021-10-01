@echo Deletando SIGER
RD /S /Q C:\RECH
@echo Copiando novo atalho do SIGER
copy \\SERVERBRASIL\RECH\RTS\SIGER.lnk
@echo Executando o atalho SIGER na sua area de trabalho
cd desktop
start siger.lnk
exit
