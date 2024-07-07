from telethon import TelegramClient, sync, events
from credentials import api_hash, api_id
from time import sleep
import requests

sessao = 'Repassar Mensagem'


def obter_charts():
    client = TelegramClient(sessao, api_id, api_hash)
    client.start()
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        print('---------------------------')
        if dialog.id < 0:
            print(f'Grupo: {dialog.title}')
            print(f'id: {dialog.id}')
        else:
            print(f'Nome: {dialog.title}')
            print(f'id: {dialog.id}')
        print('---------------------------\n')
    client.disconnect()


def main():
    print('Monitoramento iniciado...')
    client = TelegramClient(sessao, api_id, api_hash)

    @client.on(events.NewMessage(chats=[1001820464652, 4129742860]))
    async def enviar_mensagem(event):
        await client.send_message(1002166484639, event.raw_text)
    client.start()
    client.run_until_disconnected()


main()
