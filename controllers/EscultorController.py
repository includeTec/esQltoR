# -*- coding: utf-8 -*-
# Controlador de la Lista de Escultores.
def index():
    escultores = db().select(db.t_escultores.ALL,orderby=db.t_escultores.id)
    return dict(escultores=escultores)

def show():
    escultor = db.t_escultores(request.args(0)) or redirect(URL('index'))
    premios = db(db.t_premios.f_premios_escultor==escultor.id).select()
    
    return dict(escultor=escultor, premios=premios)

def download():
    return response.download(request, db)
