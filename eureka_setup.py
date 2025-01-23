import py_eureka_client.eureka_client as eureka_client
import logging
import random
 
def init_eureka():
    logging.info("Inicializando o cliente Eureka...")
 
    try:
        # Gera uma porta aleatória entre 1024 e 65535
        random_port = random.randint(1024, 65535)
        logging.info(f"Porta aleatória gerada: {random_port}")
 
        # Inicialize o cliente Eureka com as configurações especificadas
        eureka_client.init(
            eureka_server="http://eureka2.octopustax.com.br/eureka",
            app_name="apresentacao-ia-service",
            instance_id=f"apresentacao-ia-service:{random_port}",
            instance_host="127.0.0.1",
            instance_port=random_port,
            renewal_interval_in_secs=10,
            duration_in_secs=30,
            should_register=True
        )
 
        logging.info("Cliente Eureka inicializado com sucesso.")
        return random_port
 
    except Exception as e:
        logging.error(f"Erro ao inicializar o cliente Eureka: {e}")
        raise