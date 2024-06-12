from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, text, output_path):
    img = Image.open(image_path).convert("RGBA")
    watermark = Image.new("RGBA", img.size)
    draw = ImageDraw.Draw(watermark)
    
    font = ImageFont.truetype("arial.ttf", 50)
    
    width, height = img.size
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    spacing = 50
    
    for y in range(0, height, text_height + spacing):
        for x in range(0, width, text_width + spacing):
            draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    
    watermarked = Image.alpha_composite(img, watermark)
    watermarked.save(output_path)

add_watermark("input.png", "Watermark", "output.png")
