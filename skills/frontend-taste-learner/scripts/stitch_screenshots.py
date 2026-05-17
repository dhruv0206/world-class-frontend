import sys
from PIL import Image

def main():
    if len(sys.argv) < 3:
        print("Usage: python stitch_screenshots.py <output_path> <img1> [img2 ...]")
        sys.exit(1)
    
    output_path = sys.argv[1]
    image_paths = sys.argv[2:]
    
    try:
        images = [Image.open(p) for p in image_paths]
        widths, heights = zip(*(i.size for i in images))
        
        total_height = sum(heights)
        max_width = max(widths)
        
        new_im = Image.new('RGB', (max_width, total_height))
        
        y_offset = 0
        for im in images:
            new_im.paste(im, (0,y_offset))
            y_offset += im.size[1]
            
        new_im.save(output_path)
        print(output_path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()