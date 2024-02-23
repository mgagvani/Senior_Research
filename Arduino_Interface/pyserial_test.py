import time
from pySerialTransfer import pySerialTransfer as txfer


if __name__ == '__main__':
    try:
        link = txfer.SerialTransfer('COM11')
        
        link.open()
        time.sleep(2) # allow some time for the Arduino to completely reset
        
        while True:
            send_size = 0
            
            ###################################################################
            # Send a list
            ###################################################################
            list_ = [[int(x) for x in input("steer throttle: ").split()]]
            list_ = list_[0]
            print(list_)

            list_ = [list_[0] + 65536 * list_[1], list_[0] + 65536 * list_[1]]

            list_size = link.tx_obj(list_[0])
            send_size += list_size
            
            ###################################################################
            # Transmit all the data to send in a single packet
            ###################################################################
            link.send(send_size)
            
            ###################################################################
            # Wait for a response and report any errors while receiving packets
            ###################################################################
            while not link.available():
                if link.status < 0:
                    if link.status == txfer.CRC_ERROR:
                        print('ERROR: CRC_ERROR')
                    elif link.status == txfer.PAYLOAD_ERROR:
                        print('ERROR: PAYLOAD_ERROR')
                    elif link.status == txfer.STOP_BYTE_ERROR:
                        print('ERROR: STOP_BYTE_ERROR')
                    else:
                        print('ERROR: {}'.format(link.status))
            
            ###################################################################
            # Parse response list
            ###################################################################
            rec_list_  = link.rx_obj(obj_type=type(list_),
                                     obj_byte_size=list_size*2,
                                     list_format='i')
                        
            # rec_list_  = link.rx_obj(obj_type=str,
            #                             obj_byte_size=list_size,
            #                             list_format='f')
        
            ###################################################################
            # Display the received data
            ###################################################################
            print('SENT: {}'.format(list_))
            print('RCVD: {}'.format(rec_list_))
            print(' ')
    
    except KeyboardInterrupt:
        try:
            link.close()
        except:
            pass
    
    except:
        import traceback
        traceback.print_exc()
        
        try:
            link.close()
        except:
            pass