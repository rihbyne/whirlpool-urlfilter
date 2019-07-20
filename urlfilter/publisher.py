# dep libs
import pika

# urlfilter publish
def publish_to_due_queue(channel, msg):
    pub_confirm = False
    print('invoked {0}'.format(publish_to_due_queue.__name__))
    try:
        channel.basic_publish(exchange='urlfilter.ex.due',
                              routing_key='urlfilter_p.to.due_c',
                              body=msg,
                              properties=pika.BasicProperties(content_type='application/json',
                                                              delivery_mode=1),
                              mandatory=True)
        pub_confirm = True
    except pika.exceptions.UnroutableError as push_fail_err:
        print('Message publish could not be confirmed {0}'.format(push_fail_err))

    return pub_confirm
