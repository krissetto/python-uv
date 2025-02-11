from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import pyfiglet

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root(
    text: str = Query(default="Hey!", description="Text to convert to ASCII art"),
    font: str = Query(default="standard", description="Font style for ASCII art")
):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except pyfiglet.FontNotFound:
        return f"Font '{font}' not found. Using default font.\n" + pyfiglet.figlet_format(text)
