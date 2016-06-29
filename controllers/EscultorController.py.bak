# -*- coding: utf-8 -*-
# Controlador de la Lista de Escultores.
def index():
    escultores = db().select(db.t_escultores.ALL,orderby=db.t_escultores.id)
    titulo="Escultores"
    return dict(escultores=escultores, titulo=titulo)

def show():
    escultor = db.t_escultores(request.args(0)) or redirect(URL('index'))
    premios = db(db.t_premios.f_premios_escultor==escultor.id).select()
    titulo="Escultor"
    
    return dict(escultor=escultor, premios=premios, titulo=titulo)

def download():
    return response.download(request, db)

def escultura():
    titulo="Escultura"
    escultor = db.t_escultores(request.args(0)) or redirect(URL('index'))
    escultura = db(db.t_esculturas.f_escultura_id==escultor.f_escultor_id).select().first()
   
    return dict(escultor=escultor, escultura=escultura, titulo=titulo)
