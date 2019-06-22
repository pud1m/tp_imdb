from .models import Filme
from django.db.models import Q


def get_delta(genero):

    lista_filmes = Filme.objects.filter(
        Q(gen1=genero) | Q(gen2=genero) | Q(gen3=genero)
    ).exclude(nota_usu=0, nota_meta=0)

    usu_total = 0
    meta_total = 0

    leng = len(lista_filmes)

    for movie in lista_filmes:
        # Adiciona as notas nos montantes totais
        usu_total = usu_total + int(movie.nota_usu)
        meta_total = meta_total + int(movie.nota_meta)

    # Tira a média das notas do gênero
    avg_usu = float(usu_total/leng)
    avg_meta = float(meta_total/leng)

    # Calcula o delta subtraindo as médias. Se a nota dos críticos for mais alta, o delta será negativo
    delta = avg_usu - avg_meta

    retorno = {
        'genero': genero,
        'total': leng,
        'avg_usu': avg_usu,
        'avg_meta': avg_meta,
        'delta': delta
    }

    return retorno


def get_generos():
    print('criando lista de generos')
    lista_generos = []

    todos_filmes = Filme.objects.all()

    for movie in todos_filmes:
        if movie.gen1 != '!' and movie.gen1 not in lista_generos:
            lista_generos.append(movie.gen1)
        if movie.gen2 != '!' and movie.gen2 not in lista_generos:
            lista_generos.append(movie.gen2)
        if movie.gen3 != '!' and movie.gen3 not in lista_generos:
            lista_generos.append(movie.gen3)
    print('criada lista de generos')
    return lista_generos