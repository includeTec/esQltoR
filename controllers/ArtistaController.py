# -*- coding: utf-8 -*-
# Controlador de la Lista de Escultores.
def index():
    artistas = db().select(db.t_artistas.ALL,orderby=db.t_artistas.id)
    titulo="Artistas"
    return dict(artistas=artistas, titulo=titulo)

def show():
    artista = db.t_artistas(request.args(0)) or redirect(URL('index'))
    titulo="Artista"
    return dict(artista=artista, titulo=titulo)

def download():
    return response.download(request, db)
