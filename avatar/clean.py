import glob, sys
from PIL import Image
import numpy as np
def main_run(v):
    nz = v > 0; best=(0,0); s=None
    for i,x in enumerate(list(nz)+[False]):
        if x and s is None: s=i
        if not x and s is not None:
            if i-s > best[1]-best[0]: best=(s,i)
            s=None
    return best
for f in glob.glob(sys.argv[1] + '/*.webp'):
    if f.endswith('_s.webp'): continue
    a = np.array(Image.open(f).convert('RGBA'))
    c0,c1 = main_run((a[...,3]>0).sum(0)); a[:, :c0, 3]=0; a[:, c1:, 3]=0
    r0,r1 = main_run((a[...,3]>0).sum(1)); a[:r0, :, 3]=0; a[r1:, :, 3]=0
    img = Image.fromarray(a,'RGBA'); img = img.crop(img.getbbox())
    img.thumbnail((240,240), Image.NEAREST)
    img.save(f.replace('.webp','_s.webp'), 'WEBP', quality=82, method=6)
