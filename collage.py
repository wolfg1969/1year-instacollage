#!/usr/bin/env python

import glob
import sys
import os
import Image


def collage(infiles, tile_width, tile_height, outfile, cols):
    
    tile_count = len(infiles)
    cols = cols
    rows = tile_count // cols + (1 if tile_count % cols else 0)
    padding = 5
    gap = 0
    imgsize = (2 * padding + tile_width * cols + gap * (cols - 1),
        2 * padding + tile_height * rows + gap * (rows - 1))
        
    img = Image.new('RGB', imgsize, '#fff')
    
    img_no = 0
    for tile_file in reversed(infiles):
    
        x = img_no % cols
        y = img_no // cols
        
        xoff = padding + x * (tile_width + gap)
        yoff = padding + y * (tile_height + gap)
        
        tile = Image.open(tile_file)
        
        img.paste(tile, (xoff, yoff))
        
        img_no += 1
    
    img.save(outfile, quality=95)   
        
if __name__ == '__main__':

    infiles = glob.glob(os.path.join(sys.argv[1], '*.jpg'))
    outfile = sys.argv[2]
    cols = sys.argv[3]
    
    collage(infiles, 150, 150, outfile, int(cols))