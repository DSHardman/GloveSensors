#!/usr/bin/env python3
#

# EDITED 15/11/22 DSH46

# curve xy co-ordinate export
# Authors:
# Jean Moreno <jean.moreno.fr@gmail.com>
# John Cliff <john.cliff@gmail.com>
# Neon22 <https://github.com/Neon22?tab=repositories>
# Jens N. Lallensack <jens.lallensack@gmail.com>
#
# Copyright (C) 2011 Jean Moreno
# Copyright (C) 2011 John Cliff 
# Copyright (C) 2011 Neon22
# Copyright (C) 2019 Jens N. Lallensack
#
# Released under GNU GPL v3, see https://www.gnu.org/licenses/gpl-3.0.en.html for details.
#
import inkex
import sys
from inkex import paths
from inkex import transforms

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

class TemplateEffect(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
    def effect(self):
        for node in self.selected.items():
            output_all = output_nodes = ""
            for id, node in self.selected.items():
                if node.tag == inkex.addNS('path','svg'):
                    output_all += ""
                    output_nodes += ""
                    node.apply_transform()
                    d = node.get('d')
                    p = paths.CubicSuperPath(d)
                    for subpath in p:
                        for csp in subpath:
                            # output_nodes += str(csp[1][0]) + "\t" + str(csp[1][1]) + "\n"
                            # dsh46 15/11/22: add uniform thickness
                            output_nodes += str(csp[1][0]) + "\t" + str(csp[1][1]) + "\t" + str(1.0) + "\n"
            # sys.stderr.write(output_nodes)
            file = open("C:/Users/dshar/OneDrive - University of Cambridge/Documents/PhD/Sojiro/TestXY.xyz", 'w')
            file.write(output_nodes)
            file.close()


TemplateEffect().run()
sys.exit(0) #helps to keep the selection
