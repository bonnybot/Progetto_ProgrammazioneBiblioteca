def inserisci(cat,cognome,nome,titolo,anno,collocazione,note=[]):
    """ Inserisce un nuovo record (libro) nel catalogo controllando che i tipi dei
    parametri attuali siano corretti -- non modifica maiuscole e minuscole dei parametri
    :param cat: il catalogo da modificare
    :param cognome: cognome dell'autore (stringa)
    :param nome: nome dell'autore (stringa)
    :param titolo: titolo del libro (stringa)
    :param anno: anno di pubblicazione (intero positivo=
    :param collocazione: tupla (stringa,intero positivo)
    :param note: stringa (opzionale)
    :return: True se l'inserimento e' stato effettuato con successo, False
    altrimenti
    :return: None se i parametri non hanno il tipo corretto
    """
    pass #istruzione che non fa niente --> da sostituire con il codice


def serializza (cat):
    """ Serializza un catalogo rappresentando la sequenza dei record in una singola stringa
    La sottostringa relativa al singolo record
    puo' usare un formato a scelta dello studente,
    i record devono essere separati dal carattere "a capo" --> "\n"

    :param cat: il catalogo da serializzare
    :return: una stringa che rappresenta il catalogo
    """
    pass #istruzione che non fa niente --> da sostituire con il codice


def crea_copia(cat):
    """ Crea una copia completa del catalogo cat (un clone) e lo restituisce
    :param cat: il catalogo da clonare
    :return: il nuovo catalogo clonato
    """
    pass #istruzione che non fa niente --> da sostituire con il codice


def sono_uguali(cat1,cat2):
    """Funzione booleana che stabilisce se due cataloghi contengono
    esattamente gli stessi record con gli stessi dati (eccetto collocazione e nota -- che possono
    essere divers)
    I record possono non essere nello stesso ordine nei due cataloghi
    :param cat1: primo catalogo da confrontare
    :param cat2: secondo catalogo da confrontare
    :return: True se sono uguali, False altrimenti
    """
    pass  # istruzione che non fa niente --> da sostituire con il codice


def concatena(cat1,cat2):
    """crea un nuovo catalogo concatenando cat1 e cat2 e lo restituisce come risultato --
    se ci sono k record uguali in tutti i campi eccetto il campo "note"
    il risultato contiene un solo record che nel campo note contiene la
    concatenazione delle note dei k record uguali in ordine lessicografico
    :param cat1: primo catalogo da unire (non viene modificato)
    :param cat2: secondo catalogo da unire (non viene modificato)
    :return: il nuovo catalogo
    """

    pass  # istruzione che non fa niente --> da sostituire con il codice


def cancella(cat,  titolo, anno=None):
    """Cancella tutti i record per i quali i campi titolo (e opzionalmente anno)
    coincidono con i parametri (titolo,anno)
    :param cat: il catalogo da modificare
    :param titolo: il titolo del libro (obbligatorio) che deve coincidere a meno di case (maiuscole/minuscole)
    :param anno: l' anno di pubblicazione (opzionale)
    :return: il numero dei record cancellati
    :return: None se i parametri non hanno il tipo corretto
    """
    pass  # istruzione che non fa niente --> da sostituire con il codice

def cerca(cat, pctitolo):
    """Verifica che esista almeno un titolo che contiene la stringa pctitolo come sottoscringa (attenzione agli spazi bianchi
     e a maiuscole e minuscole)
    :param cat: il catalogo (non viene modificato)
    :param pctitolo: la sottostringa che deve comparire nel titolo del libro
    :return: True se c'è almeno un record che contiene pctitolo, False altrimenti
    :return: None se i parametri non hanno il tipo corretto
    """
    pass  # instruzione che non fa niente --> da sostituire con il codice

def ordina(cat):
    """ Ordina il catalogo alfabeticamente per cognome e nome e
    (in caso di piu' opere dello stesso autore) per anno di pubblicazione e
    infine per Titolo all'interno dello stesso anno come in:

        Dexter Colin L'ultima corsa per Woodstock 2010 ....
        Dexter Colin Il mondo silenzioso di Nicholas Quinn  2012 ...
        Dexter Colin Niente vacanze per l'ispettore Morse 2012 ....
        Simenon Georges Gli intrusi 2015
    :param cat: il catalogo da ordinare
    :return: None (la funzione modifica il catalogo e non restituisce niente)
    """
    pass  # instruzione che non fa niente --> da sostituire con il codice

