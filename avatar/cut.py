import sys, os
from PIL import Image
import numpy as np
src, outdir = sys.argv[1], sys.argv[2]
def cut(path, n, names):
    im = np.array(Image.open(path).convert('RGB')).astype(int)
    H, W, _ = im.shape
    for i, name in enumerate(names):
        if not name: continue
        r, c = divmod(i, n)
        y0, y1 = r*H//n, (r+1)*H//n; x0, x1 = c*W//n, (c+1)*W//n
        cell = im[y0:y1, x0:x1]
        R, G, B = cell[...,0], cell[...,1], cell[...,2]
        green = (G > 150) & (G > R + 60) & (G > B + 60)
        a = np.where(green, 0, 255).astype(np.uint8)
        # despill: pull green down on near-edge pixels
        G2 = np.minimum(G, np.maximum(R, B) + 20)
        rgb = np.stack([R, G2, B], -1).clip(0,255).astype(np.uint8)
        img = Image.fromarray(np.dstack([rgb, a]), 'RGBA')
        bbox = img.getbbox(); img = img.crop(bbox)
        img.thumbnail((360, 360), Image.NEAREST)
        img.save(os.path.join(outdir, name + '.webp'), 'WEBP', lossless=True, quality=100, method=6)
cut(os.path.join(src,'2.webp'), 3, ['aponta_voce','aponta_lado','ideia','duvida','bracos_cruzados','joinha','ok','acenando','surpreso'])
cut(os.path.join(src,'1.webp'), 4, ['','','','','','','piscando','','choque','bravo','pensando','apaixonado','cansado','comemorando','chorando','oculos'])
