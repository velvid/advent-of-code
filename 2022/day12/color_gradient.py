colors = [
    # all combinations of 0, 128, 255
    # (  0,   0,   0),
    (  0,   0, 128),
    (  0,   0, 255),
    (  0, 128,   0),
    (  0, 128, 128),
    (  0, 128, 255),
    (  0, 255,   0),
    (  0, 255, 128),
    (  0, 255, 255),
    (128,   0,   0),
    (128,   0, 128),
    (128,   0, 255),
    (128, 128,   0),
    (128, 128, 128),
    (128, 128, 255),
    (128, 255,   0),
    (128, 255, 128),
    (128, 255, 255),
    (255,   0,   0),
    (255,   0, 128),
    (255,   0, 255),
    (255, 128,   0),
    (255, 128, 128),
    (255, 128, 255),
    (255, 255,   0),
    (255, 255, 128),
    (255, 255, 255)
]

def fg_gradient(char: str) -> str:
    if char < "a" or char > "z":
        return "\x1b[38;2;255;255;255m"
    i = ord(char) - ord("a")
    r, g, b = colors[i % len(colors)]
    return f"\x1b[38;2;{r};{g};{b}m"

def bg_gradient(char: str) -> str:
    if char < "a" or char > "z":
        return "\x1b[48;2;255;255;255m"
    i = ord(char) - ord("a")
    r, g, b = colors[i % len(colors)]
    return f"\x1b[48;2;{r};{g};{b}m"

def fg_bg_gradient(char: str) -> str:
    if char < "a" or char > "z":
        return "\x1b[38;2;255;255;255m\x1b[48;2;0;0;0m"
    i = ord(char) - ord("a")

    r, g, b = colors[i % len(colors)]
    ri, gi, bi = 255 - r, 255 - g, 255 - b

    return f"\x1b[48;2;{r};{g};{b}m" \
           f"\x1b[38;2;{ri};{gi};{bi}m" \
           f"\x1b[1m"