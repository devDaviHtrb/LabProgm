from flask import Flask, render_template, request, session, redirect, url_for
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# --- Lógica do Jogo Adivinhar o Número ---



def inicializar_adivinhar_numero():
    """Inicializa ou reinicia o estado do jogo Adivinhar o Número."""
   
