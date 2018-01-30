import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="UNMSM")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)
        holi = Gtk.Label("Seleccione de las listas abajo")
        box_outer.add(holi)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Alumno", xalign=0)
        entry = Gtk.Entry()
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(entry, False, True, 0)
        listbox.add(row)
       
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)

        row.add(hbox)
        label = Gtk.Label("Facultad", xalign=0)
        combo = Gtk.ComboBoxText()
        combo.insert(0, "0", "Facultad Ciencias Matematicas")
        combo.insert(1, "1", "Facultad de Sistemas")
        combo.insert(0, "2", "Facultas de Ciencias Biologicas")
        combo.insert(1, "3", "Facultad de Ciencias Fisicas")
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(combo, False, True, 0) 
        listbox.add(row)

        

win = ListBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()