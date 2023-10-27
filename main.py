from obj import Extractor

extractor = Extractor("donnees.txt")

mails = extractor.extract_mail()
phone_numbers = extractor.extract_phone_number()
names = extractor.extract_name()


print(extractor.print_data())