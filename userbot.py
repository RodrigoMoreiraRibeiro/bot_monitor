import os
import gzip
import base64
import asyncio
from telethon import TelegramClient, events

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

# Grupo privado para onde as mensagens serão encaminhadas
GROUP_ID = os.environ.get("GROUP_ID")
if not GROUP_ID:
    raise ValueError("❌ Variável GROUP_ID não definida.")

# Cria o cliente
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Lista dos canais para monitorar — coloque os usernames ou IDs
CANAIS_MONITORADOS = [
    'ofertaskabum',
    'anrutech',
    'anrutech',
]

@client.on(events.NewMessage(chats=CANAIS_MONITORADOS))
async def monitorar_mensagens(event):
    try:
        msg = event.message.message or ""
        print(f"[MONITOR] Nova mensagem do canal {event.chat_id}: {msg[:100]}")

        # Encaminhar mensagem para o grupo privado
        await client.send_message(GROUP_ID, msg)
        print("[MONITOR] Mensagem encaminhada com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao encaminhar mensagem: {e}")

async def main():
    await client.start()
    print("✅ Userbot conectado com sucesso!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
