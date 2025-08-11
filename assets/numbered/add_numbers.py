# ex. uv run --with pillow add_numbers.py objects.bmp 64 5 10

from PIL import Image, ImageDraw, ImageFont
import os
import sys
import argparse

def add_numbers_to_textures(input_path, output_path, texture_size, textures_per_row, total_rows):
    """
    Add numbers to each texture in a grid within an image file.
    
    Args:
        input_path: Path to the input image file
        output_path: Path for the output PNG file
        texture_size: Size of each square texture in pixels
        textures_per_row: Number of textures in each row
        total_rows: Total number of rows
    """
    # Load the image
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return False
    
    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Verify image dimensions match expected grid
    expected_width = textures_per_row * texture_size
    expected_height = total_rows * texture_size
    
    if img.width != expected_width or img.height != expected_height:
        print(f"Warning: Image size ({img.width}x{img.height}) doesn't match expected size ({expected_width}x{expected_height})")
        print(f"Expected: {textures_per_row} columns x {total_rows} rows of {texture_size}x{texture_size} textures")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return False
    
    # Create a drawing object
    draw = ImageDraw.Draw(img)
    
    # Calculate appropriate font size based on texture size
    font_size = max(12, texture_size // 4)
    
    # Try to use a built-in font, with fallback to default
    try:
        # Try to use a TrueType font if available
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            # Fallback to DejaVu (common on Linux)
            font = ImageFont.truetype("DejaVuSans.ttf", font_size)
        except:
            try:
                # Another fallback for Linux/Mac
                font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", font_size)
            except:
                # Use default font if no TrueType fonts are available
                font = ImageFont.load_default()
                print("Using default font (may be small)")
    
    # Counter for texture numbers
    texture_number = 1
    
    # Iterate through each texture position
    for row in range(total_rows):
        for col in range(textures_per_row):
            # Calculate position for this texture
            x = col * texture_size
            y = row * texture_size
            
            # Get the number as string
            number_text = str(texture_number)
            
            # Get text bounding box to center it
            bbox = draw.textbbox((0, 0), number_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Calculate centered position within the texture
            text_x = x + (texture_size - text_width) // 2
            text_y = y + texture_size // 20  # Proportional offset from top
            
            # Draw white background for better visibility
            padding = max(2, texture_size // 32)
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
    
    # Save the result as PNG
    try:
        img.save(output_path, 'PNG')
        print(f"\nSuccess! Numbered texture grid saved to: {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")
        return False
    
    # Print summary
    total_textures = textures_per_row * total_rows
    print(f"\nSummary:")
    print(f"  - Added numbers 1-{total_textures} to {total_textures} textures")
    print(f"  - Grid: {textures_per_row} columns x {total_rows} rows")
    print(f"  - Each texture: {texture_size}x{texture_size} pixels")
    print(f"  - Total image size: {img.width}x{img.height} pixels")
    print(f"  - Output format: PNG")
    
    return True

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Add numbers to textures in a grid image',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python %(prog)s wall_textures.bmp 64 6 19
  python %(prog)s /path/to/textures.bmp 32 8 10 -o numbered_textures.png
  python %(prog)s sprites.png 16 16 16 --output sprites_numbered.png
        """
    )
    
    # Positional arguments
    parser.add_argument('input_file', 
                        help='Path to the input image file (BMP, PNG, etc.)')
    parser.add_argument('texture_size', 
                        type=int,
                        help='Size of each square texture in pixels (e.g., 64 for 64x64)')
    parser.add_argument('textures_per_row', 
                        type=int,
                        help='Number of textures in each row')
    parser.add_argument('total_rows', 
                        type=int,
                        help='Total number of rows')
    
    # Optional arguments
    parser.add_argument('-o', '--output', 
                        dest='output_file',
                        help='Output PNG file path (default: input_numbered.png)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found!")
        sys.exit(1)
    
    # Generate output filename if not specified
    if args.output_file:
        output_file = args.output_file
    else:
        # Get input filename without extension and add _numbered.png
        base_name = os.path.splitext(args.input_file)[0]
        output_file = f"{base_name}_numbered.png"
    
    # Validate arguments
    if args.texture_size <= 0:
        print("Error: Texture size must be positive")
        sys.exit(1)
    if args.textures_per_row <= 0:
        print("Error: Number of textures per row must be positive")
        sys.exit(1)
    if args.total_rows <= 0:
        print("Error: Number of rows must be positive")
        sys.exit(1)
    
    # Print configuration
    print(f"Configuration:")
    print(f"  - Input file: {args.input_file}")
    print(f"  - Output file: {output_file}")
    print(f"  - Texture size: {args.texture_size}x{args.texture_size} pixels")
    print(f"  - Grid: {args.textures_per_row} columns x {args.total_rows} rows")
    print(f"  - Total textures: {args.textures_per_row * args.total_rows}")
    print()
    
    # Process the image
    success = add_numbers_to_textures(
        args.input_file,
        output_file,
        args.texture_size,
        args.textures_per_row,
        args.total_rows
    )
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()