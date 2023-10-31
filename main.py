from obj import Extractor

extractor = Extractor("donnees.txt")

mails = extractor.extract_mail()
phone_numbers = extractor.extract_phone_number()
names = extractor.extract_name()


print(extractor.print_data())

# https://discord.com/channels/396825382009044994/1165200377801617488