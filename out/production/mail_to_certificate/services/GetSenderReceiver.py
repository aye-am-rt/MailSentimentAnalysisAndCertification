import os
import sys


def get_sender_and_receiver():
    dictionary = {'sender': "undefined", 'receiver': "undefined"}
    regardList = ["regards", "yours sincerely", "thanking you,"]
    addressList = ["to,", "dear,", "the,"]
    os.chdir('../../../../../resources')
    try:
        f = open('appreciate.txt')
        line = f.readline()
        while line:
            line = line.strip('\n')
            if str(line).lower() in regardList:
                sender = f.readline()
                print(sender)
                dictionary['sender'] = sender
                break
            line = f.readline()
        f.close()
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    try:
        f = open('appreciate.txt')
        line = f.readline()
        while line:
            line = line.strip('\n')
            print(line)
            if str(line).lower() in addressList:
                receiver = f.readline()
                print(receiver)
                dictionary['receiver'] = receiver
                break
            line = f.readline()
        f.close()
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    dictionary['receiver']=dictionary['receiver'].strip('\n').strip(' ')
    dictionary['sender']=dictionary['sender'].strip('\n').strip(' ')
    return dictionary
