from PIL import Image, ImageDraw, ImageFont
import os

def add_numbers_to_textures(input_path, output_path):
    """
    Add numbers to each 64x64 texture in a BMP file grid.
    
    Args:
        input_path: Path to the input BMP file
        output_path: Path for the output BMP file
    """
    # Texture dimensions and grid layout
    TEXTURE_SIZE = 64
    TEXTURES_PER_ROW = 6
    TOTAL_ROWS = 19
    
    # Load the image
    img = Image.open(input_path)
    
    # Convert to RGB if necessary (BMP files might be in different modes)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Create a drawing object
    draw = ImageDraw.Draw(img)
    
    # Try to use a built-in font, with fallback to default
    font_size = 20
    try:
        # Try to use a TrueType font if available
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            # Fallback to DejaVu (common on Linux)
            font = ImageFont.truetype("DejaVuSans.ttf", font_size)
        except:
            # Use default font if no TrueType fonts are available
            font = ImageFont.load_default()
            print("Using default font (may be small)")
    
    # Counter for texture numbers
    texture_number = 1
    
    # Iterate through each texture position
    for row in range(TOTAL_ROWS):
        for col in range(TEXTURES_PER_ROW):
            # Calculate position for this texture
            x = col * TEXTURE_SIZE
            y = row * TEXTURE_SIZE
            
            # Get the number as string
            number_text = str(texture_number)
            
            # Get text bounding box to center it
            bbox = draw.textbbox((0, 0), number_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Calculate centered position within the texture
            text_x = x + (TEXTURE_SIZE - text_width) // 2
            text_y = y + 5  # Small offset from top
            
            # Draw white background for better visibility
            padding = 3
            draw.rectangle([
                text_x - padding, 
                text_y - padding,
                text_x + text_width + padding,
                text_y + text_height + padding
            ], fill='white', outline='black')
            
            # Draw the number
            draw.text((text_x, text_y), number_text, fill='black', font=font)
            
            # Increment counter
            texture_number += 1
    
    # Save the result as BMP
    img.save(output_path, 'BMP')
    print(f"Numbered texture grid saved to: {output_path}")
    
    # Verify the output
    total_textures = TEXTURES_PER_ROW * TOTAL_ROWS
    print(f"Added numbers 1-{total_textures} to {total_textures} textures")
    print(f"Grid: {TEXTURES_PER_ROW} columns x {TOTAL_ROWS} rows")
    print(f"Each texture: {TEXTURE_SIZE}x{TEXTURE_SIZE} pixels")
    print(f"Total image size: {img.width}x{img.height} pixels")

if __name__ == "__main__":
    # File paths
    input_file = "wall_textures.bmp"
    output_file = "wall_textures_numbered.bmp"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        print("Please make sure the file is in the same directory as this script.")
    else:
        # Process the image
        add_numbers_to_textures(input_file, output_file)
