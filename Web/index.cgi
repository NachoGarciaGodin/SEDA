t <!DOCTYPE html>
t  <html>
t   <head>
t     <meta http-equiv="refresh" content="20; url=http://192.168.1.120/index.cgi">
t     <title> PAGINA WEB </title>
t   </head>
t   <body>
t     <h2>Robot tracción diferencial</h2>
t       <p>Datos del robot:</p>
t        <form action="/index.cgi" method="get">
c 0   <p>Batería:%d </p>
c 1   <p>Umbral:%d </p>
t <p>Seleccion modo de funcionamiento:</p>
c 2     <input type="radio" name="modo" value="manual" OnClick="submit()" type="checked" %s >Modo manual<br>
c 3     <input type="radio" name="modo" value="auto" OnClick="submit()" type="checked" %s >Modo automatico<br>
c 4     <input type="radio" name="modo" value="debug" OnClick="submit()" type="checked" %s >Modo debug<br><br>
t     <label for="fname">Comando:</label><br>
c 5  <input name="Comando" type="test" value=%s ><br>
t  <input type="submit" value="Submit"><br><br>
t </form>
t </body>
t </html>
. 