<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>x.x.x</title>
    <style>
        body {
            background-color: #00FFFF; /* Verde agua */
            font-family: Arial, sans-serif;
        }
        .search-bar {
            margin: 20px;
        }
        .game-list {
            list-style-type: none;
        }
        .game-item {
            margin: 10px 0;
        }
        .download-buttons {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Bienvenido a x.x.x</h1>
    <div class="search-bar">
        <form method="get" action="/">
            <input type="text" name="search" placeholder="Buscar juegos...">
            <button type="submit">Buscar</button>
        </form>
    </div>
    <ul class="game-list">
        {% for game in games %}
        <li class="game-item">
            <h2>{{ game.name }}</h2>
            <p>Categoría: {{ game.category }}</p>
            <div class="download-buttons">
                <button onclick="alert('Descargando para PC')">Descargar para PC</button>
                <button onclick="alert('Descargando para Mac')">Descargar para Mac</button>
            </div>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
