# instalar no terminal: pip install paho-mqtt==1.5.0
import paho.mqtt.client as mqtt

def ao_conectar(client, userdata, flags, rc):
    print("Nos conectamos com o seguinte código de resultado {}".format((rc)))
    client.subscribe("giovana")

def ao_receber(client, userdata, msg):
    mensagem = msg.payload.decode()
    print("Mensagem recebida:", mensagem)
        
cliente = mqtt.Client()

cliente.on_connect = ao_conectar
cliente.on_message = ao_receber
cliente.connect("broker.hivemq.com", 1883, 60)
cliente.loop_forever()

cliente.loop_start()
while True:
    cliente.publish("giovana", input("Envie uma mensagem")) # topico pra enviar
cliente.loop_finish()