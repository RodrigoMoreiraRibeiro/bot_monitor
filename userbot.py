import os
import base64
import asyncio
from telethon import TelegramClient

# Nome da sessão (sem ".session")
SESSION_NAME = os.environ.get("SESSION_NAME", "userbot")

# Salva o .session se ainda não existir
if not os.path.exists(f"{SESSION_NAME}.session"):
    session_b64 = os.environ.get("SESSION_B64")
    if session_b64:
        with open(f"{SESSION_NAME}.session", "wb") as f:
            f.write(base64.b64decode(session_b64))
    else:
        raise ValueError("Variável de ambiente SESSION_B64 não está definida.")

# Credenciais da API do Telegram
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]

# Criação do cliente
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ Userbot iniciado com sucesso!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
