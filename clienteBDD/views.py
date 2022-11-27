from django.http import HttpResponse
from django import forms

def saludo(request):
    
    documento = ''' 
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lista de productos</title>
  <meta name="robots" content="index, follow">
</head>
<body>
<div>
<input type = "text" name="prd">
<input type = "button" value="Enviar">
</body>
</html>
    '''
    return HttpResponse(documento)
