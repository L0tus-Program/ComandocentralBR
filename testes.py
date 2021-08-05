import tkinter as tk
from typing import Sized, Text
import whois
import os
import pyautogui as gui # posteriormente vou trocar todas as telas do pyautogui para usar o tkinter diretamente
import webbrowser


dom = "cascadebanana.com"
w = whois.whois(dom)

print(w + "TESTE")