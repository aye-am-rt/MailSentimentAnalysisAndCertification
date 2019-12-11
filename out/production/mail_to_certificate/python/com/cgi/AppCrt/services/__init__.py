from Sentiment_analysis import read_and_analyze
from GetSenderReceiver import get_sender_and_receiver
from CertificateGenerator import generate_certificate

value = read_and_analyze()
final_dictionary = {}
if value == 1:
    final_dictionary = get_sender_and_receiver()
else:
    print("no certificate generated")

if len(final_dictionary) != 0:
    generate_certificate(final_dictionary)
