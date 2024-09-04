from actions import add_new_contact, display_contacts, edit_contact, toggle_favorite, view_favorites, delete_contact

options = (
    "1. Adicionar um novo contato",
    "2. Visualizar contatos cadastrados",
    "3. Editar um contato existente",
    "4. Marcar/desmarcar um contato como favorito",
    "5. Visualizar contatos favoritos",
    "6. Apagar um contato",
    "7. Sair"
)

contacts = []

while True:
    print("\nMenu da Lista de Contatos:\n")
    for option in options:
        print(option)

    choice = input("\nDigite o número da ação desejada: ")

    if choice == "1":
        add_new_contact(contacts)
    elif choice == "2":
        display_contacts(contacts)
    elif choice == "3":
        edit_contact(contacts)
    elif choice == "4":
        toggle_favorite(contacts)
    elif choice == "5":
        view_favorites(contacts)
    elif choice == "6":
        delete_contact(contacts)
    elif choice == "7":
        break
    else:
        print(">>> Opção inválida. Tente novamente.\n")
