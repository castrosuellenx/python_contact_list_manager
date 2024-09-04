def add_new_contact(contacts):
    contact_name = input("Digite o nome do contato: ")
    contact_phone = input("Digite o telefone do contato: ")
    contact_email = input("Digite o e-mail do contato: ")

    contact = {"name": contact_name, "phone": contact_phone, "email": contact_email, "is_favorite": False}

    contacts.append(contact)

    print(">>> Contato adicionado com sucesso!\n")
    return

def display_contacts(contacts):
    if len(contacts) == 0:
        print(">>> Não há contatos cadastrados.\n")
        return False

    print("\nLista de contatos:")
    for index, contact in enumerate(contacts, start=1):
        is_favorite = "⭐" if contact["is_favorite"] else ""
        print(f"{index}. [{is_favorite}] {contact['name']} - {contact['phone']} - {contact['email']}")
    return True

def edit_contact(contacts):
    if not display_contacts(contacts):
        return  # Sai da função se não houver contatos

    contact_index_ajustado = int(input("\nDigite o número do contato que deseja editar: ")) - 1

    if contact_index_ajustado < 0 or contact_index_ajustado >= len(contacts):
        print(">>> Número inválido. Contato não encontrado.\n")
        return

    contact_new_name = input("Digite o novo nome do contato: ")
    contact_new_phone = input("Digite o novo telefone do contato: ")
    contact_new_email = input("Digite o novo e-mail do contato: ")

    new_contact = {"name": contact_new_name, "phone": contact_new_phone, "email": contact_new_email, "is_favorite": False}

    contacts[contact_index_ajustado] = new_contact
    print(">>> Contato editado com sucesso!\n")
    return

def toggle_favorite(contacts):
    if not display_contacts(contacts):
        return  # Sai da função se não houver contatos

    contact_index_ajustado = int(input("\nDigite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1

    if contact_index_ajustado < 0 or contact_index_ajustado >= len(contacts):
        print(">>> Número inválido. Contato não encontrado.\n")
        return

    contacts[contact_index_ajustado]["is_favorite"] = not contacts[contact_index_ajustado]["is_favorite"]
    print(">>> Contato marcado/desmarcado como favorito com sucesso!\n")
    return

def view_favorites(contacts):
    favorites_contacts = [contact for contact in contacts if contact['is_favorite']]

    if len(favorites_contacts) == 0:
        print(">>> Não há contatos favoritos cadastrados.\n")
        return

    print("\nLista de contatos favoritos:")
    for contact in favorites_contacts:
        print(f"{contact['name']} - {contact['phone']} - {contact['email']}")
    return

def delete_contact(contacts):
    if not display_contacts(contacts):
        return  # Sai da função se não houver contatos

    contact_index_ajustado = int(input("\nDigite o número do contato que deseja excluir: ")) - 1

    if contact_index_ajustado < 0 or contact_index_ajustado >= len(contacts):
        print(">>> Número inválido. Contato não encontrado.\n")
        return

    del contacts[contact_index_ajustado]
    print(">>> Contato excluído com sucesso!\n")
    return
