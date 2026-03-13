import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Меняем рабочую директорию на текущую папку
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    print("Папка:", os.getcwd())
    print("Нажмите Ctrl+C для остановки")
    
    # Автоматически открываем браузер
    webbrowser.open(f'http://localhost:{PORT}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")