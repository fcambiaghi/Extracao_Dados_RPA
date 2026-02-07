import os
import time
 
import pandas as pd
import pyautogui as pg
 
# Para focar/jogar o foco numa janela pelo título (Windows)
# pip install pygetwindow
import pygetwindow as gw
 
# =========================
# CONFIG
# =========================
EXCEL_FILE = "dados_rpa_win_forms.xlsx"        # arquivo que você disse
EXCEL_SHEET = 0                 # ou "Inscricoes" se quiser
FORM_WINDOW_TITLE = "Bloco de Notas"     # precisa bater com o título da janela
START_DELAY = 5                 # segundos pra você preparar a tela
 
# Segurança
pg.FAILSAFE = True              # mover mouse pro canto sup-esq para parar
pg.PAUSE = 0.12
 
def focus_window_by_title(title: str, timeout=10):
    """Ativa a primeira janela que contém 'title' no título."""
    t0 = time.time()
    while time.time() - t0 < timeout:
        wins = gw.getWindowsWithTitle(title)
        if wins:
            w = wins[0]
            try:
                if w.isMinimized:
                    w.restore()
                w.activate()
                time.sleep(0.3)
                return True
            except Exception:
                pass
        time.sleep(0.3)
    return False
 
def open_excel_and_focus_a1(path: str):
    """1) Abre o Excel  2) Foca na primeira célula."""
    os.startfile(os.path.abspath(path))   # Windows
    time.sleep(3.5)
 
    # Tenta trazer o Excel pra frente (pode variar conforme idioma/versão)
    # Se isso falhar, clique manualmente no Excel uma vez antes de iniciar.
    # Atalho para ir ao começo da planilha:
    pg.hotkey("ctrl", "home")  # vai para A1 (ou primeiro dado visível)
    time.sleep(0.2)
 
def main():
    print("⚠️  Em 5s vou começar.")
    print("• Deixe o Excel e o Form abertos/visíveis.")
    print("• Se algo der errado, mova o mouse pro canto superior esquerdo (FAILSAFE).")
    time.sleep(START_DELAY)
 
    # 1) abre a planilha dados.xlsx
    open_excel_and_focus_a1(EXCEL_FILE)
 
    # (opcional) Lê a planilha via pandas (mais confiável que copiar da UI)
    df = pd.read_excel(EXCEL_FILE, sheet_name=EXCEL_SHEET)
 
    # 3) procura janela aberta "form1" e 4) foca nela
    ok = focus_window_by_title(FORM_WINDOW_TITLE, timeout=12)
    if not ok:
        raise RuntimeError(f"Não encontrei nenhuma janela com título contendo: {FORM_WINDOW_TITLE!r}")
 
    # Clique no primeiro campo do formulário (evita foco “perdido”)
    # Ajuste essas coordenadas para o seu Form1 (faça uma vez e pronto).
    # Você pode comentar o click se o foco já cai no 1º campo ao ativar.
    #pg.click(200, 200)
    #time.sleep(0.2)
 
    # Para cada linha: preencher campos usando TAB
    # Esperado no Excel: colunas com esses nomes (ou ajuste aqui)
    # Nome, E-mail, Cidade, Dia, Restricao
    # Se suas colunas forem diferentes, altere os nomes abaixo.
    for i, row in df.iterrows():
        nome_empresa = str(row.get("Nome empresa", ""))
        municipio = str(row.get("Cidade", ""))
        email = str(row.get("Email", ""))
        fat_estimado = str(row.get("Faturamento anual estimado", ""))
 
 
        # Campo 1: Nome
        pg.typewrite(nome_empresa)
        pg.press("tab")
 
       # Campo 2: Cidade
        pg.typewrite(municipio)
        pg.press("tab")
 
        # Campo 3: E-mail
        pg.typewrite(email)
        pg.press("tab")
 
 
       # Campo 4: faturamento
        pg.typewrite(fat_estimado)
        pg.press("tab")
 
 
 
       # SALVAR
        pg.press("tab")
        pg.press("enter")
 
        # Aqui você decide o que é "salvar/enviar" no seu Form1:
        # Ex: apertar ENTER num botão padrão, ou ALT+S, etc.
        # Vou deixar como exemplo:
        # pg.hotkey("alt", "s")  # se você criar um atalho Alt+S para salvar
        # time.sleep(0.3)
 
        # Prepara para próxima linha:
        # Se depois de salvar o formulário limpar e voltar pro primeiro campo, ok.
        # Se não limpar, você pode selecionar tudo antes de digitar na próxima volta.
        # pg.hotkey("shift", "tab"); ... (depende do seu form)
 
        print(f"✅ Linha {i+1}/{len(df)} preenchida")
 
        # Pequena pausa pra UI respirar
        time.sleep(0.2)
 
    print("✅ Finalizado.")
 
if __name__ == "__main__":
    main()
 