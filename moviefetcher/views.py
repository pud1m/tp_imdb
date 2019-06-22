from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template import loader
from .utils import *
from datetime import datetime


def teste(request):
    x = get_delta('Thriller')
    print(x)
    return HttpResponse(str(x))


def requester(request):
    contexto = {
        '0': 0,
    }
    template = loader.get_template('moviefetcher/requester.html')
    return HttpResponse(template.render(contexto, request))


def pedido(request):
    # Recebe o formulário com os parâmetros para a busca
    periodo_start = str(request.POST.get('periodo_start'))
    periodo_end = str(request.POST.get('periodo_end'))
    avalia_min = str(request.POST.get('avalia_min'))

    url1 = 'https://www.imdb.com/search/title/?title_type=feature&release_date='
    url2 = '&count=250&ref_=adv_prv'

    # Converte o período do formulário para formato que será recebido pela busca do IMDb
    periodo = ','.join((periodo_start, periodo_end))

    # Converte o número mínimo de votos para formato que será recebido pela busca do IMDb
    avalia = ''.join(('&num_votes=', avalia_min, ','))

    # Cria a URL final a ser enviada para o crawler
    url_final = ''.join((url1, periodo, avalia, url2))

    # Envia para o crawler
    run_crawler(url_final)

    # Cria lista de generos
    lista_generos = get_generos()

    # Converte a data enviada para texto amigável
    inicio = datetime.strptime(periodo_start, '%Y-%m-%d').strftime('%d de %B de %Y')
    fim = datetime.strptime(periodo_end, '%Y-%m-%d').strftime('%d de %B de %Y')

    # Loop pela lista de gêneros, atribuindo delta para cada gênero
    deltas = []
    for genero in lista_generos:
        delta = get_delta(str(genero))
        deltas.append(delta)

    # Cria o dict de retorno
    contexto = {
        'total': len(Filme.objects.all()),
        'inicio': inicio,
        'fim': fim,
        'deltas': deltas
    }

    # Retorno com os dados
    template = loader.get_template('moviefetcher/resultado.html')
    return HttpResponse(template.render(contexto, request))
