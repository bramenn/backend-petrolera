from boto3 import client

from .config import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY

sns_client = client(
    "sns",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


def enviar_evento_petrolero(data: str, tema_sns: str):
    response = sns_client.publish(
        TopicArn=tema_sns,
        Message=data,
    )


def crear_tema_sns(id_activo_petrolero: str):
    topic = sns_client.create_topic(Name=f"activo-petrolero-{id_activo_petrolero}")
    print(f"El tema {topic} fue creado")
    return topic.get("TopicArn")


def suscribir_responsable(arn_sns: str, protocolo: str, endpoint: str):
    response = sns_client.subscribe(
        TopicArn=arn_sns,
        Protocol=protocolo,
        Endpoint=endpoint,
    )
