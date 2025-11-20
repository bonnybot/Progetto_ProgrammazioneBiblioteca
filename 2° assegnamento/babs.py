class Libro:
    def __init__(self,cognome,nome,titolo,anno,collocazione,iban,note=""):
        """ Crea un nuovo oggetto Libro
        :param cognome: cognome dell'autore
        :param nome: nome dell'autore
        :param titolo: titolo del libro
        :param anno: anno di pubblicazione
        :param collocazione: tupla (stringa,intero positivo)
        :param iban: IBAN (stringa) unico per ogni libro
        :param note: stringa eventualmente vuota
        """
        # controlliamo il tipo dei parametri
        if type(cognome) != str:
            raise Exception("Il cognome non è una stringa")
        if type(nome) != str:
            raise Exception("Il nome non è una stringa ")
        if type(titolo) != str:
            raise Exception("Il titolo non è una stringa")
        if type(iban) != str:
            raise Exception("L'iban non è una stringa")
        if type(note) != str:
            raise Exception("Le note non sono una stringa")
        if type(anno) != int:
            raise Exception("L'anno non è un intero")
        if type(collocazione) != tuple:
            if (type(collocazione[0]) != str) or (type(collocazione[1]) != int):
                raise Exception("La collocazione non è corretta")

        # inizializziamo i parametri del libro
        self.cognome = cognome
        self.nome = nome
        self.titolo = titolo
        self.anno = anno
        self.collocazione = collocazione
        self.iban = iban
        self.note = note

    def __str__ (self):
        """ Serializza un libro rappresentandolo come una stringa. La stringa
        puo' usare un formato a scelta dello studente
        :return: una stringa che rappresenta il libro
        """
        libro = self.cognome + " " + self.nome + " " + self.titolo + " "

        return libro

    def __eq__(self,a):
        """Stabilisce se self e a sono uguali -- due libri sono considerati uguali
            se hanno esattamente gli stessi campi (eccetto le note e la collocazione)  """
        if self.cognome and self.nome and self.titolo and self.anno and self.iban == a:
            return True
        return False


class Catalogo:
    def __init__(self):
        """Crea un catalogo vuoto rappresentato come un dizionario di
           libri con chiave iban"""
        # inizializziamo un dizionario vuoto
        self.cat = {}

    def n_books(self):
        """Ritorna il numero di libri nel catalogo """
        return len(self.cat)

    def inserisci(self,li):
        """Inserisce un nuovo libro nel catalogo:
            se l'iban è già presente non modifica il catalogo
            :param: li oggetto libro da inserire
            :returns: True se il libro è stato inserito
            :returns: False altrimenti """
        # verifichiamo che la chiave del libro non sia presente per procedere all'inserimento nel catalogo
        if li.iban not in self.cat.keys():
            self.cat[li.iban] = li
            return True
        return False

    def __str__(self):
        """Serializza il catalogo in una stringa che contiene tutti i libri
        in ordine di IBAN crescente.
        Ogni libro è separato dal successivo da "\n" """
        stringa = ""

        # iteriamo il catalogo riordinato
        for iban, book in sorted(self.cat.items()):
            # separiamo i parametri del libro con il carattere -
            stringa += "{}-{}-{}-{}-{}-{}-{}-{}\n".format(book.iban, book.cognome, book.nome, book.titolo,
                                                               book.anno,
                                                               book.collocazione[0], book.collocazione[1], book.note)
        return stringa

    def store(self,nomefile):
        """Scrive il catalogo sul file "nomefile" -- > formato a scelta dello studente
         da specificare nei commenti"""
        # apriamo un nuovo file in scrittura
        with open(nomefile, 'w+') as f:
            f.write(str(self)) # scriviamo il catalogo nel file

    def load(self,nomefile):
        """Legge il catalogo dal file "nomefile" nel formato a scelta dello studente
        e lo carica nel catalogo eliminando tutto il contenuto precedente
        del catalogo """
        try:
            # apriamo il file in lettura
            with open(nomefile, 'r') as f:
                # leggiamo ogni linea del file
                catalogo = f.readlines()
            self.cat = {}
            # iteriamo il file
            for book in catalogo:
                # rimuoviamo con strip spazi e caratteri indesiderati e utilizziamo come separatore -
                info = book.strip().split('-')
                # inizializziamo l'oggetto libro nel dizionario con i relativi parametri
                self.cat[info[0]] = Libro(info[1], info[2], info[3],
                                                  int(info[4]), (info[5], int(info[6])),
                                                  info[0], info[7])
            return True
        except IOError:
            print("ERRORE: il file non è presente.")

    def __eq__(self,cat2):
        """Stabilisce se due cataloghi contengono
        esattamente gli stessi libri
        :param cat2: secondo catalogo da confrontare
        :return: True se sono uguali, False altrimenti
        """
        # verifichiamo l'uguaglianza tra i due cataloghi riordinati

        return sorted(self.cat.keys()) == sorted(cat2.cat.keys())
