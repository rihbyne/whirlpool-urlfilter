# sys imports
import pickle

# local imports
import publisher

# whirlpool-urlfilter consume
def consume_from_parser_queue(channel):
    print('invoked {0}'.format(consume_from_parser_queue.__name__))
    channel.basic_consume('urlfilter.q', on_msg_callback)
    print('consumer listening for messages on urlfilter.q')

def on_msg_callback(channel, method_frame, header_frame, body):
     print('delivery tag {}'.format(method_frame.delivery_tag))
     print('header_frame {}'.format(header_frame))
     print('msg body {}'.format(body))

     # do some processing
     #
     #

     # finally send message by call publisher
     msg = {
         'urls': ['http://a1.com', 'http://a2.com', 'http://a3.com']
     }

     bmsg = pickle.dumps(msg)
     pub_confirm = publisher.publish_to_due_queue(channel, bmsg)
     if pub_confirm:
         channel.basic_ack(delivery_tag=method_frame.delivery_tag)
         print('message from urlfilter.q acknowledged')
     else:
         channel.basic_nack(delivery_tag=method_frame.delivery_tag)
         print('message from urlfilter.q acknowledgement failed')
