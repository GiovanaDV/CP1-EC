# instalar no terminal: pip install paho-mqtt==1.5.0
import paho.mqtt.client as mqtt

def ao_conectar(client, userdata, flags, rc):
    print("Conectado com código:", rc)
    client.subscribe("giovana")

def ao_receber(client, userdata, msg):
    mensagem = msg.payload.decode()
    if mensagem == "silo abastecido":
        print("✅ Silo abastecido")
    elif mensagem == "silo em consumo":
        print("⚠️  Silo em consumo")
    elif mensagem == "silo vazio":
        print("🚨 Silo vazio")
    else:
        print("Mensagem recebida:", mensagem)

cliente = mqtt.Client()
cliente.on_connect = ao_conectar
cliente.on_message = ao_receber
cliente.connect("broker.hivemq.com", 1883, 60)
cliente.loop_forever() 