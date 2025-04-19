#El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.




unstructuredInformationOfPeople= "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

def _sort_information(unstructuredInformationOfPeople:str):
    
    informationOfPeople = unstructuredInformationOfPeople.split("\n")

    headers = informationOfPeople[0].split(";")

    people = {}

    for person in informationOfPeople[1:]:
        informationOfPerson = person.split(";")
        nif = informationOfPerson[0]
        information = {}
        for i in range(1, len(informationOfPerson)):
            information[headers[i]] = informationOfPerson[i]
        
        people[nif] = information

    return people

estructuredInformation = _sort_information(unstructuredInformationOfPeople)
print(estructuredInformation)