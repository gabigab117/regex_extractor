from re import compile


class Extractor:
    def __init__(self, file):
        self.data = self.__open_file(file)
    
    def __open_file(self, file):
        with open(file, "r") as f:
            return f.read()
        
    def extract_mail(self):
        regex_pattern = compile(r'[\w\.]+@\w+\.\w{2,}')
        return regex_pattern.findall(self.data)
    
    def extract_phone_number(self):
        # Commence par un digit, peut avoir des espaces et . et se termine par un digit
        regex_pattern = compile(r'\d[\d\s\.]+\d')
        number_list = [numbers.replace(" ", "").replace(".", "") for numbers in regex_pattern.findall(self.data)]

        list_formated = []
        for number in number_list:

            if len(number) == 11:
                with_indicatif_number = number[0:2] + "." + number[2:3] + "." + ".".join([number[i:i+2] for i in range(3, len(number), 2)])
                list_formated.append(with_indicatif_number)

            else:
                list_formated.append(".".join([number[i:i+2] for i in range(0, len(number), 2)]))

        return list_formated
    
    def extract_name(self):
        # 1ere parenthèse globale c'est ce qu'on récupère (2 mots) groupe et extract
        # 2eme parenthèse est un groupe mais pas une extract 2 parenthèse 2 résultats. Donc éliminer
        regex_pattern = compile(r'(?:Madame|monsieur|M.|Mlle|Dr|mademoiselle|Mme)\s((?:[A-Z]\w+\s?){2})')
        return regex_pattern.findall(self.data)
    
    def all_data(self):
        return {"name": self.extract_name(), "phone": self.extract_phone_number(), "email": self.extract_mail()}
    
    def print_data(self):
        data = self.all_data()

        # Valeur Max de chaque élément
        max_name = len(max(self.extract_name(), key=len))
        max_number = len(max(self.extract_phone_number(), key=len))
        max_mail = len(max(self.extract_mail(), key=len))
        space = " "
        tiret = "-"
        limite = f"|-{tiret*max_name}-|-{tiret*max_mail}-|-{tiret*max_number}-|"
        name_head = "Nom & Prénom"
        number_head = "Numéro"
        email_head = "Mail"

        # names = str([f"| {name}" for name in data["name"]]).replace(",", "").replace("[", "").replace("]", "").replace("'", '')
        names = [f"| {name}{space*(max_name-len(name))} |" for name in data["name"]]
        numbers = [f"{number}{space*(max_number-len(number))} |" for number in data["phone"]]
        emails = [f"{email}{space*(max_mail-len(email))} |" for email in data["email"]]

        print(f"| {name_head: ^{max_name}} | {email_head: ^{max_mail}} | {number_head: ^{max_number}} |")
        print(limite)

        for el1, el2, el3 in zip(names, emails, numbers):
            print(el1, 
                  el2, 
                  el3)
        print(limite)
        
        return ""
    