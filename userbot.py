import os
import gzip
import base64
import asyncio
from telethon import TelegramClient

# Nome base da sessão
SESSION_NAME = os.environ.get("SESSION_NAME", "userbot")

# Restaura o arquivo .session se ainda não existir
if not os.path.exists(f"{SESSION_NAME}.session"):
    session_b64 = os.environ.get("SESSION_B64_GZ")
    if not session_b64:
        raise ValueError("❌ Variável SESSION_B64_GZ não definida.")
    
    # Descomprime e grava
    with open(f"{SESSION_NAME}.session", "wb") as f:
        f.write(gzip.decompress(base64.b64decode(session_b64)))
    
    print("✅ Arquivo .session restaurado com sucesso!")

# Credenciais da API Telegram
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]

# Cria o cliente
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Main loop
async def main():
    await client.start()
    print("✅ Userbot conectado com sucesso!")
    await client.run_until_disconnected()

# Executa
if __name__ == "__main__":
    asyncio.run(main())
