### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_escultores',
    Field('f_escultor_id', type='string',
          label=T('Escultor Id')),
    Field('f_escultor_nombre', type='string',
          label=T('Escultor Nombre')),
    Field('f_escultor_descripcion', type='text',
          label=T('Escultor Descripcion')),
    Field('f_escultor_contacto', type='string',
          label=T('Escultor Contacto')),
    Field('f_escultor_imagen', type='upload',
          label=T('Escultor Imagen')),
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

########################################
db.define_table('t_sesion',
    Field('f_user_email', type='string',
          label=T('User Email')),
    Field('f_user_contrasenia', type='string',
          label=T('User Contrasenia')),
    Field('f_user_nombre', type='string',
          label=T('User Nombre')),
    Field('f_user_fechanacimiento', type='string',
          label=T('User Fechanacimiento')),
    format='%(f_user_email)s',
    migrate=settings.migrate)

db.define_table('t_sesion_archive',db.t_sesion,Field('current_record','reference t_sesion',readable=False,writable=False))

##################################################

db.define_table('t_artistas',
    Field('f_artista_id', type='string',
          label=T('Artista Id')),
    Field('f_artista_nombre', type='string',
          label=T('Artista Nombre')),
    Field('f_artista_descripcion', type='text',
          label=T('Artista Descripcion')),
    Field('f_artista_premio', type='text',
          label=T('Artista Premio')),
    Field('f_artista_contacto', type='string',
          label=T('Artista Contacto')),
    Field('f_artista_imagen', type='upload',
          label=T('Artista Imagen')),
    format='%(f_artista_id)s',
    migrate=settings.migrate)

db.define_table('t_artistas_archive',db.t_artistas,Field('current_record','reference t_artistas',readable=False,writable=False))

##################################################
