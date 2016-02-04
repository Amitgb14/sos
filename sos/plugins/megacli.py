# megacli.py
# Copyright (C) 2007-2014 Red Hat, Inc., Jon Magrini <jmagrini@redhat.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
import os.path
from sos.plugins import Plugin, RedHatPlugin


class MegaCLI(Plugin, RedHatPlugin):
    """LSI MegaRAID devices
    """

    plugin_name = 'megacli'
    profiles = ('system', 'storage', 'hardware')

    megacli_bin = '/opt/MegaRAID/MegaCli/MegaCli64'

    def setup(self):
        if os.path.isfile(self.megacli_bin):
            self.add_custom_text("LSI MegaCLI is installed.<br>")
            self.get_megacli_files()

    def get_megacli_files(self):
        """ MegaCLI specific output
        """

        self.add_cmd_output([
            "{0} LDPDInfo -aALL".format(self.megacli_bin),
            "{0} -AdpAllInfo -aALL".format(self.megacli_bin),
            "{0} -AdpBbuCmd -GetBbuStatus -aALL".format(self.megacli_bin),
            "{0} -ShowSummary -aALL".format(self.megacli_bin)
        ])

# vim: set et ts=4 sw=4 :
