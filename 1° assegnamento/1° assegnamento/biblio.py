# Alessandra Bottiglieri 648769 a.bottiglieri1@studenti.unipi.it
# Giorgia Cestaro 620023 g.cestaro@studenti.unipi.it

def inserisci(cat,cognome,nome,titolo,anno,collocazione,note=""):
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
    tupla = (cognome, nome, titolo, anno, collocazione, note)
    if (type(cognome) or type(nome) or type(titolo) or type(note)) != str:
        return None
    elif type(anno) != int:
        return None
    elif type(collocazione) != tuple:
        if (type(collocazione[0]) != str) or (type(collocazione[1]) != int):
            return None
    else:
        cat.append(tupla)
        return True


def serializza (cat):
    """ Serializza un catalogo rappresentando la sequenza dei record in una singola stringa
    La sottostringa relativa al singolo record
    puo' usare un formato a scelta dello studente,
    i record devono essere separati dal carattere "a capo" --> "\n"

    :param cat: il catalogo da serializzare
    :return: una stringa che rappresenta il catalogo
    """
    count = 1
    string = []

    for i in cat:
        string = "Libro numero " + str(count) + ": " + str(i)
        count += 1

    return string

def crea_copia(cat):
    """ Crea una copia completa del catalogo cat (un clone) e lo restituisce
    :param cat: il catalogo da clonare
    :return: il nuovo catalogo clonato
    """
    catcopy = cat[:]

    return catcopy


def sono_uguali(cat1,cat2):
    """Funzione booleana che stabilisce se due cataloghi contengono
    esattamente gli stessi record con gli stessi dati (eccetto collocazione e nota -- che possono
    essere divers)
    I record possono non essere nello stesso ordine nei due cataloghi
    :param cat1: primo catalogo da confrontare
    :param cat2: secondo catalogo da confrontare
    :return: True se sono uguali, False altrimenti
    """
    x = [x[:3] for x in cat1]  # esclude collocazione e nota
    y = [x[:3] for x in cat2]

    if set(x) == set(y):  # set crea un insieme disordinato delle liste
        return True
    else:
        return False


def concatenamento_lessicografico(x, y):

    if x < y:
        result = x + " " + y
    else:
        result = y + " " + x

    return result


def concatena(cat1,cat2):
    """crea un nuovo catalogo concatenando cat1 e cat2 e lo restituisce come risultato --
    se ci sono k record uguali in tutti i campi eccetto il campo "note"
    il risultato contiene un solo record che nel campo note contiene la
    concatenazione delle note dei k record uguali in ordine lessicografico
    :param cat1: primo catalogo da unire (non viene modificato)
    :param cat2: secondo catalogo da unire (non viene modificato)
    :return: il nuovo catalogo
    """
    cat = cat1 + cat2
    cat_without_note = [x[:5] for x in cat]

    cat_finale = []
    tupla_letta = []

    for i in range(len(cat_without_note)):
        book = cat_without_note[i]
        # se il record non è stato ancora letto
        if book not in tupla_letta:
            # controlliamo se c'è un duplicato
            if cat_without_note.count(book) > 1:
                # ripeschiamo l'indice del duplicato partendo dalla posizione seguente
                j = cat_without_note[i + 1:].index(book) + i + 1
                # concateniamo le note richiamando la funzione
                nota_unita = concatenamento_lessicografico(cat[i][5], cat[j][5])
                # aggiungiamo il libro con le note concatenate
                cat_finale.append((book[0], book[1], book[2], book[3], book[4], nota_unita))
            else:
                cat_finale.append(cat[i])

            tupla_letta.append(book)
    return cat_finale


def cancella(cat,  titolo, anno=None):
    """Cancella tutti i record per i quali i campi titolo (e opzionalmente anno)
    coincidono con i parametri (titolo,anno)
    :param cat: il catalogo da modificare
    :param titolo: il titolo del libro (obbligatorio) che deve coincidere a meno di case (maiuscole/minuscole)
    :param anno: l' anno di pubblicazione (opzionale)
    :return: il numero dei record cancellati
    :return: None se i parametri non hanno il tipo corretto
    """
    count = 0
    titolo = titolo.lower()

    if type(titolo) != str:
        return None
    if anno != None and type(anno) != int:
        return None

    for i in cat:
        if anno != None:
            # se anno e titolo nel catalogo coincidono con i parametri cancelliamo il record
            if i[2].lower() == titolo and i[3] == anno:
                cat.remove(i)
                count += 1
        else:  # altrimenti se coincide solo il titolo rimuoviamo ugualmente il record
            if i[2].lower() == titolo:
                cat.remove(i)
                count += 1
    return count


def cerca(cat, pctitolo):
    """Verifica che esista almeno un titolo che contiene la stringa pctitolo come sottostringa (attenzione agli spazi bianchi
     e a maiuscole e minuscole)
    :param cat: il catalogo (non viene modificato)
    :param pctitolo: la sottostringa che deve comparire nel titolo del libro
    :return: True se c'è almeno un record che contiene pctitolo, False altrimenti
    :return: None se i parametri non hanno il tipo corretto
    """
    result = False

    if (type(pctitolo) != str) or pctitolo.isspace() or (pctitolo == ""):
        return None
    for i in cat:
        # rendiamo tutte le stringhe minuscole e verifichiamo se la sottostringa è presente nel catalogo
        if pctitolo.lower() in i[2].lower():
            result = True
        else:
            continue
    return result

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
    n = len(cat)
    # utilizziamo bubble sort per l'ordinamento
    # quindi si confrontano i record vicini tra loro portando sempre il maggiore in ultima posizione
    # poi si procede a ritroso finché il catalogo non è ordinato
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            libro1 = (cat[j][0], cat[j][1], cat[j][3], cat[j][2], cat[j][4], cat[j][5])
            libro2 = (cat[j + 1][0], cat[j + 1][1], cat[j + 1][3], cat[j + 1][2], cat[j + 1][4], cat[j + 1][5])
            if libro1 > libro2:
                cat[j], cat[j + 1] = cat[j + 1], cat[j]
    return None

