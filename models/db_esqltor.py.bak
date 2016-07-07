### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_escultores',
    Field('f_escultor_id', type='string',
          label=T('Escultor Id')),
    Field('f_escultor_nombre', type='string',
          label=T('Escultor Nombre')),
    Field('f_escultor_nacimiento', type='string',
          label=T('Escultor Nacimiento')),
    Field('f_escultor_origen', type='string',
          label=T('Escultor origen')),
    Field('f_escultor_descripcion', type='text',
          label=T('Escultor Descripcion')),
    Field('f_escultor_contacto', type='string',
          label=T('Escultor Contacto')),
    Field('f_escultor_imagen', type='upload',
          label=T('Escultor Imagen')),
    Field('f_escultor_mini', type='upload',
          label=T('Escultor miniatura')),
    Field('f_escultor_audio', type='upload',
          label=T('Escultor Audio')),
    
    format='%(f_escultor_id)s',
    migrate=settings.migrate)

db.define_table('t_escultores_archive',db.t_escultores,Field('current_record','reference t_escultores',readable=False,writable=False))

########################################
db.define_table('t_premios',
    Field('f_premios_escultor', db.t_escultores ,
          label=T('Escultor ID')),
    Field('f_premios_anio', type='string',
          label=T('Año de Premio')),
    Field('f_premios_descripcion', type='string',
          label=T('Descripción de Premio')),
    format='%(f_premios_id)s',
    migrate=settings.migrate)


########################################
db.define_table('t_esculturas',
    Field('f_escultura_id', type='string',
          label=T('Escultura Id')),
    Field('f_escultura_nombre', type='string',
          label=T('Escultura Nombre')),
    Field('f_escultura_descripcion', type='text',
          label=T('Escultura Descripcion')),
    Field('f_escultura_imagen', type='upload',
          label=T('Escultura Imagen')),
    format='%(f_escultura_id)s',
    migrate=settings.migrate)

db.define_table('t_esculturas_archive',db.t_esculturas,Field('current_record','reference t_esculturas',readable=False,writable=False))



##################################################

db.define_table('t_artistas',
    Field('f_artista_id', type='string',
          label=T('Artista Id')),
    Field('f_artista_nombre', type='string',
          label=T('Artista Nombre')),
    Field('f_artista_pais', type='string',
          label=T('Artista Pais')),
    Field('f_artista_tematica', type='text',
        label=T('Artista Tematica')),
    Field('f_artista_tecnica', type='text',
           label=T('Artista Tecnica')),
    Field('f_artista_materiales', type='text',
           label=T('Artista Materiales')),
    Field('f_artista_descripcion', type='text',
          label=T('Artista Descripcion')),
    Field('f_artista_premio', type='text',
          label=T('Artista Contacto')),
    Field('f_artista_imagen', type='upload',
          label=T('Artista Imagen')),
    Field('f_artista_mini', type='upload',
          label=T('Artista Mini')),
    format='%(f_artista_id)s',
    migrate=settings.migrate)

db.define_table('t_artistas_archive',db.t_artistas,Field('current_record','reference t_artistas',readable=False,writable=False))

##################################################
