import sys
from PIL import Image

image_paths = sys.argv[1:-1]
out_path = sys.argv[-1]

images = [Image.open(p) for p in image_paths]
widths, heights = zip(*(i.size for i in images))

new_im = Image.new('RGB', (max(widths), sum(heights)))
y_offset = 0
for im in images:
    new_im.paste(im, (0, y_offset))
    y_offset += im.size[1]

new_im.save(out_path)
print(out_path)
