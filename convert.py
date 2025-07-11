import gzip, base64

with open("userbot.session", "rb") as f_in:
    compressed = gzip.compress(f_in.read())

with open("compressed_b64.txt", "w") as f_out:
    f_out.write(base64.b64encode(compressed).decode())