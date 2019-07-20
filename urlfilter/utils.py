# import sys libs
import os

# import third-party libs
from pika import PlainCredentials, ConnectionParameters
from pika import BlockingConnection


def auth_rmq():
    from settings import RMQ
    print('importing rabbitmq settings ok...')

    creds = PlainCredentials(RMQ['username'], RMQ['password'])
    params = ConnectionParameters(host=RMQ['hostname'],
                                  port=RMQ['port'],
                                  virtual_host=RMQ['vhost'],
                                  credentials=creds)

    conn = BlockingConnection(params)
    print('authenticated to rabbitmq as user: {u}, node: {h}, vhost: {v}'.format(u=RMQ['username'],
                                                                                 h=RMQ['hostname'],
                                                                                 v=RMQ['vhost']))
    channel = conn.channel()
    channel.confirm_delivery()
    channel.basic_qos(prefetch_count=1)
    print('publish message confirmation delivery enabled. prefetch count set to {}'.format(1))
    return (conn, channel)

def auth_db():
    from settings import DATABASES

    if os.getenv('PY_ENV') == 'development':
        print('connecting to {0} database'.format(os.getenv('PY_ENV')))
    elif os.getenv('PY_ENV') == 'production':
        print('connection to {1} database'.format(os.getenv('PY_ENV')))
    else:
        raise LookupError('database environment not defined')
