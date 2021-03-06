# Copyright (C) 2015, Carlo de Franchis <carlo.de-franchis@cmla.ens-cachan.fr>
# Copyright (C) 2015, Gabriele Facciolo <facciolo@cmla.ens-cachan.fr>
# Copyright (C) 2015, Enric Meinhardt <enric.meinhardt@cmla.ens-cachan.fr>
# Copyright (C) 2015, Julien Michel <julien.michel@cnes.fr>


import os 
import numpy as np

from config import cfg
from python import pointing_accuracy


def pointing_correction(tiles):
    """
    Compute the global pointing corrections for each pair of images.

    Args:
        tiles: list of tile_info dictionaries
    """
    nb_pairs = tiles[0]['number_of_pairs']
    for i in range(1, nb_pairs + 1):
        list_of_tiles = [os.path.join(t['directory'], 'pair_%d' % i) for t in
                         tiles]
        np.savetxt(os.path.join(cfg['out_dir'], 'global_pointing_pair_%d.txt' % i),
                   pointing_accuracy.global_from_local(list_of_tiles))


def minmax_intensities(tiles_full_info):
    """
    Compute the min and max intensities from the tiles that will be processed.

    This will allow to re-code colors by using 8-bits instead of 12-bits or
    more, and to better vizualise the ply files.

    Args:
         tiles_full_info: list of tile_info dictionaries
    """
    minlist = []
    maxlist = []
    for tile_info in tiles_full_info:
        minmax = np.loadtxt(os.path.join(tile_info['directory'],
                                         'local_minmax.txt'))
        minlist.append(minmax[0])
        maxlist.append(minmax[1])

    global_minmax = [min(minlist), max(maxlist)]

    np.savetxt(os.path.join(cfg['out_dir'], 'global_minmax.txt'), global_minmax)
