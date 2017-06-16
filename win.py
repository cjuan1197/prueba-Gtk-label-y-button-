# coding=utf8

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ventana = Gtk.Window()
ventana.set_title("la concha")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show()

caja = Gtk.Box (orientation=Gtk.Orientation.VERTICAL)
caja.show()
ventana.add(caja)

etiqueta = Gtk.Label("Puto")
etiqueta.show()
caja.pack_start(etiqueta, True, True, 0)

boton = Gtk.Button("el que lo lea")
boton.show()
caja.pack_start(boton, False, False, 0)

Gtk.main()
