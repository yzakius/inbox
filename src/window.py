# window.py
#
# Copyright 2024 Isaac Ferreira Filho
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk, Gio
import os

@Gtk.Template(resource_path='/me/yzakius/Inbox/window.ui')
class InboxWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'InboxWindow'

    label = Gtk.Template.Child()
    button_save = Gtk.Template.Child()
    entry = Gtk.Template.Child()



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button_save.connect("clicked", self.on_save_button)

    def on_save_button(self, *args):
        entry_text = self.entry.get_text()
        if entry_text:
            filepath = os.path.exists("inbox.txt")
            if filepath:
                with open("inbox.txt", "a") as file_:
                    file_.write(entry_text + "\n")
            self.destroy()





