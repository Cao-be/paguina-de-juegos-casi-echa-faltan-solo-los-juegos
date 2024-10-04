Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template, request
... 
... app = Flask(__x.x.x__)
... 
... # Lista de juegos de ejemplo
... games = [
...     {"name": "Juego 1", "category": "de dos", "platform": "pc y mac"},
...     {"name": "Juego 2", "category": "de mause", "platform": "pc y mac"},
...     {"name": "Juego 3", "category": "de carros", "platform": "pc y mac"},
...     {"name": "Juego 4", "category": "de tanques", "platform": "pc y mac"},
...     {"name": "Juego 5", "category": "de aviones", "platform": "pc y mac"},
... ]
... 
... @app.route('/')
... def home():
...     search_query = request.args.get('search')
...     if search_query:
...         filtered_games = [game for game in games if search_query.lower() in game['name'].lower()]
...     else:
...         filtered_games = games
...     return render_template('index.html', games=filtered_games)
... 
... if __name__ == '__main__':
...     app.run(debug=True)
