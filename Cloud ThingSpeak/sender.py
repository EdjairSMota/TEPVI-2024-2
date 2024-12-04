"""
Processo python para envio de dados do gateway para o thingspeak

Author:
    Name: Diogo Soares @diogosm 
"""

import random
import string
import time
import logging
from datetime import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import psutil

'''
    Configura o logging para debug ao invés de print
'''
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('op_log.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

## dados do thingspeak
CHANNEL_ID = "2771764"
WRITE_API_KEY = "OX45FWGR9HB1A6K2"
MQTT_HOST = "mqtt3.thingspeak.com"
#MQTT_USERNAME = "mwa0000021483824" # versão antiga
#MQTT_API_KEY = "MVALKEH208WOKAHE"  # versão antiga
CLIENT_ID = "AA07IAsxBzY6KCATGyMABRE"
MQTT_USERNAME = "AA07IAsxBzY6KCATGyMABRE"
MQTT_PASSWORD = "colocar uma senha"

# trocar pela função de coletar dados dos sensores
def gera_dados():
    return {
        'turbidez': round(random.uniform(0, 100), 2)
    }

def build_payload(data):
    return (
        f"field1={data['turbidez']}"
    )

def envia_thingspeak(payload):
    """
        Envia dados para thingespeak usando mqtt com websockets
        Para mais formas de configuração, consulte:
            1. https://www.mathworks.com/help/thingspeak/mqtt-basics.html#mw_4ce42c87-9abe-40a6-bab0-134b01cb9305
            2. https://www.mathworks.com/help/thingspeak/use-raspberry-pi-board-that-runs-python-websockets-to-publish-to-a-channel.html
        
        :param payload: json payload com o dado para enviar
            se precisar mandar mais campos, adicione o &field2={data['nomedonovocampo']} na função build_payload
    """
    topic = f"channels/{CHANNEL_ID}/publish"
    
    try:
        # Configura o cliente mqtt
        mqtt_client = mqtt.Client(
            client_id=CLIENT_ID, 
            transport="websockets", ## configura o cliente mqtt para transporte com websockets. Pode ser 'tcp' também
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2
        )
        
        # Autentica o cliente MQTT com os dados do thingspeak
        mqtt_client.username_pw_set(
            username=MQTT_USERNAME, 
            password=MQTT_PASSWORD
        )
        
        # Conecta com o broker do thingspeak
        mqtt_client.connect(
            host=MQTT_HOST, 
            port=80,  # ou 1883 para tcp. Lembre-se de considerar 1883 para não encriptado ou 8883 para SSL/TLS encriptação
            keepalive=60
        )

        # ativa o logger do mqtt antes de tentar enviar
        mqtt_client.enable_logger(logger)
        
        # Faz o publish e espera pelo resultado
        result, msg = mqtt_client.publish(topic, payload, qos=1)
        
        # Checa se ocorreu tudo bem ou se aumenta o timeout
        if result == mqtt.MQTT_ERR_SUCCESS:
            mqtt_client.loop(timeout=5.0)
        else:
            logger.error("Falha no envio! Código de erro: {result}")
            return False
        
        logger.info("Dado " + payload + " enviado com sucesso!")
        return True
    
    except Exception as e:
        logger.error(f"MQTT Error: {e}")
        return False
    finally:
        # force o disconnect
        if 'mqtt_client' in locals():
            mqtt_client.disconnect()
            aux = 1

def main():
    logger.info("Inicializando o serviço de envio para o MQTT broker do thingspeak")
    
    try:
        for tentativa in range(5): # Generate 5 dados e para
            sensor_data = gera_dados()
            logger.info(f"Dado gerado: {sensor_data}")
            
            # Constrói o o payload e envia
            payload = build_payload(sensor_data)
            sucesso_envio = envia_thingspeak(payload)
            
            if not sucesso_envio:
                logger.warning(f"Falha na tentativa de envio {tentativa + 1}")
            
            time.sleep(5)
    
    except KeyboardInterrupt:
        logger.info("Finishing script de envio")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
