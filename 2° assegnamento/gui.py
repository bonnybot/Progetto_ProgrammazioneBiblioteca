import tkinter as tk
from tkinter import messagebox as mb
from babs import *

cat = Catalogo()


def handler_inserisci():
    def event_inserisci():
        try:
            # collezioniamo i parametri creando l'oggetto libro
            libro = Libro(cognome.get(), nome.get(), titolo.get(), int(anno.get()), (collocazione_str.get(), int(collocazione_int.get())), iban.get(), note.get())
            inserimento = cat.inserisci(libro)

            if inserimento:
                mb.showinfo("Fatto!", "Libro inserito nel catalogo!")
            else:
                mb.showwarning("Attenzione!", "Errore nell'inserimento")
        except Exception as e:
            mb.showwarning("Attenzione!", "Impossibile aggiungere il libro. Errore: {}".format(e))

    # creiamo la finestra aggiungi libro da aggiungere nel master
    root = tk.Toplevel(finestra)
    root.geometry("550x450+475+150")

    # creiamo le label dei parametri, le posizioniamo e inseriamo le entry per i valori da tastiera
    inserisci_label = tk.Label(root, text="Aggiungi libro")
    inserisci_label.grid(row=0, column=1, pady=(5, 5))

    cognome_label = tk.Label(root, text="Cognome autore", anchor="w")
    cognome_label.grid(row=1, column=0, pady=(1, 5))

    cognome = tk.Entry(root, width=25)
    cognome.grid(row=1, column=1, pady=(1, 5))

    nome_label = tk.Label(root, text="Nome autore", anchor="w")
    nome_label.grid(row=2, column=0, pady=(1, 5))

    nome = tk.Entry(root, width=25)
    nome.grid(row=2, column=1, pady=(1, 5))

    titolo_label = tk.Label(root, text="Titolo libro", anchor="w")
    titolo_label.grid(row=3, column=0, pady=(1, 5))

    titolo = tk.Entry(root, width=25)
    titolo.grid(row=3, column=1, pady=(1, 5))

    anno_label = tk.Label(root, text="Anno pubblicazione", anchor="w")
    anno_label.grid(row=4, column=0, pady=(1, 5))

    anno = tk.Entry(root, width=25)
    anno.grid(row=4, column=1, pady=(1, 5))

    collocazione_label = tk.Label(root, text="Collocazione libro", anchor="w")
    collocazione_label.grid(row=5, column=0, pady=(1, 5))

    collocazione_str = tk.Entry(root, width=10)
    collocazione_str.grid(row=5, column=1, pady=(1, 5))

    collocazione_int = tk.Entry(root, width=10)
    collocazione_int.grid(row=5, column=2, pady=(1, 5))

    iban_label = tk.Label(root, text="IBAN", anchor="w")
    iban_label.grid(row=6, column=0, pady=(1, 5))

    iban = tk.Entry(root, width=25)
    iban.grid(row=6, column=1, pady=(1, 5))

    note_label = tk.Label(root, text="Note", anchor="w")
    note_label.grid(row=7, column=0, pady=(1, 5))

    note = tk.Entry(root, width=20)
    note.grid(row=7, column=1, pady=(1, 5))

    # creiamo il bottone finale per l'evento di inserimento libro
    button = tk.Button(root, text="Aggiungi libro", width=15, height=2, pady=10, command=event_inserisci)
    button.grid(row=8, column=1, pady=(1, 5))

def handler_visualizza():
    # se sono presenti libri in catalogo creiamo la finestra
    if cat.n_books() > 0:
        root = tk.Toplevel(finestra)
        root.geometry("550x700")
        # usiamo listbox per la visualizzazione
        list_box = tk.Listbox(root)
        # iteriamo il catalogo e inseriamo i libri nella lista
        for book in cat.cat.items():
            list_box.insert(0, book)
        # inseriamo listbox e la espandiamo in tutta la finestra
        list_box.pack(expand=True, fill=tk.BOTH)
    else:
        mb.showwarning("Attenzione!", "Catalogo vuoto.")

def handler_catstore():
    # creiamo la finestra per la store
    root = tk.Toplevel(finestra)
    root.geometry("400x150+520+300")

    def event_store():
        # verifichiamo se non ci sono libri nel catalogo e stampiamo l'errore
        if cat.n_books() < 1:
            mb.showwarning("Attenzione!", "Catalogo vuoto")
            return

        # richiamiamo la store e chiudiamo la finestra a operazione completata
        cat.store(nomefile.get())
        mb.showinfo("Fatto!", "Catalogo salvato in {}".format(nomefile.get()))
        root.destroy()

    # creiamo le label, le posizioniamo e inseriamo la entry per la scrittura da tastiera
    catstore_label = tk.Label(root, text="Scrivi catalogo su file")
    catstore_label.grid(row=0, column=1, pady=(5, 5))

    nomefile_label = tk.Label(root, text="Nome file", anchor="w")
    nomefile_label.grid(row=1, column=0, pady=(1, 5))

    nomefile = tk.Entry(root, width=25)
    nomefile.grid(row=1, column=1, pady=(1, 5))

    # creiamo il bottone per eseguire l'evento di scrittura su file
    button = tk.Button(root, text="Scrivi catalogo su file", width=15, height=2, command=event_store)
    button.grid(row=2, column=1, pady=(1, 5))

def handler_catload():
    # creiamo la finestra per il caricamento del catalogo e ne definiamo le dimensioni
    root = tk.Toplevel(finestra)
    root.geometry("400x150+520+300")

    def event_load():
        try:
            # richiamiamo la funzione load e chiudiamo la finestra al termine dell'operazione
            catfile = cat.load(nomefile.get())
            mb.showinfo("Fatto!", "Catalogo caricato da {}".format(nomefile.get()))
            root.destroy()
        except Exception as e:
            mb.showwarning("Attenzione!", "Errore nel caricamento: {}".format(e))

    # creiamo le label, le posizioniamo e inseriamo la entry per la scrittura da tastiera
    catload_label = tk.Label(root, text="Carica catalogo da file")
    catload_label.grid(row=0, column=1, pady=(5, 5))

    nomefile_label = tk.Label(root, text="Nome file", anchor="w")
    nomefile_label.grid(row=1, column=0, pady=(1, 5))

    nomefile = tk.Entry(root, width=25)
    nomefile.grid(row=1, column=1, pady=(1, 5))

    # creiamo il bottone per eseguire l'evento di caricamento catalogo
    button = tk.Button(root, text="Carica catalogo", width=15, height=2, command=event_load)
    button.grid(row=2, column=1, pady=(1, 5))

def handler_esci():
    # chiudiamo la finestra master
    finestra.quit()

# creiamo la finestra master, impostiamo colore e dimensioni
finestra = tk.Tk(className=" GUI CATALOGO")
finestra['background']="beige"
finestra.geometry("500x500+475+150")

# creiamo le label e i bottini associati ai vari eventi
nome_finestra = tk.Label(text="CATALOGO", anchor="e", font=("Times New Roman", 30), bg="beige")
nome_finestra.place(relx=0.25, rely=0.1, relwidth=0.43, relheight=0.1)

visualizza_cat = tk.Button(finestra, text="Visualizza catalogo", height=2, pady=5, command=handler_visualizza)
visualizza_cat.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

inserisci_libro = tk.Button(finestra, text="Aggiungi libro", height=2, pady=5, command=handler_inserisci)
inserisci_libro.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

carica_cat = tk.Button(finestra, text="Carica catalogo da file", height=2, pady=5, command=handler_catload)
carica_cat.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

scrivi_cat = tk.Button(finestra, text="Scrivi catalogo su file", height=2, pady=5, command=handler_catstore)
scrivi_cat.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

esci = tk.Button(finestra, text="ESCI", height=2, pady=5, command=handler_esci)
esci.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

# la finestra è sempre aperta ed è l'utente a gestirne gli eventi
finestra.mainloop()
