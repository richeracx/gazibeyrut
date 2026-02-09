
import colorgram

# Extract 5 colors from the image
try:
    colors = colorgram.extract('gazibeyrut.jpg', 5)
    print("Extracted Colors:")
    for color in colors:
        rgb = color.rgb
        print(f"rgb({rgb.r}, {rgb.g}, {rgb.b})")
except Exception as e:
    print(f"Error: {e}")
