__author__ = 'rogeriolabat'
# -*- codging: utf-8 -*-
#from  __future__ import  absolute_import,unicode_literals
from zen import router

#def index(_resp):
#   _resp.write ("Hello Zenwarch")

def index(_handler):
#    _handler.redirect("/usuario/form/umNome")
    path=router.to_path(salvar,'Rogerio','Labat')
    _handler.redirect(path)

def salvar(_resp,nome,sobrenome):
    _resp.write("Ola %s %s" % (nome, sobrenome))


