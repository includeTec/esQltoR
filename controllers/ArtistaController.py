# -*- coding: utf-8 -*-
# Controlador de la Lista de Escultores.
def index():
    artistas = db().select(db.t_artistas.ALL,orderby=db.t_artistas.id)
    return dict(artistas=artistas)

def show():
    artista = db.t_artistas(request.args(0)) or redirect(URL('index'))
    return dict(artista=artista)

def download():
    return response.download(request, db)
