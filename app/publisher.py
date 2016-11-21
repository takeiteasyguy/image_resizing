from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage


def publish_message_2_user(text, facility, *to):
    """
    Publish
    :param facility:
    :param text:
    :param to:
    :return:
    """
    if not (to and text and facility):
        return

    RedisPublisher(facility=facility, users=to).publish_message(RedisMessage(text))