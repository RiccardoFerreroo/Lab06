import mysql
from mysql.connector import errorcode

from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = "SELECT codice, marca, modello, anno,posti, disponibile FROM automobile;"
            cursor.execute(query)

            automobili = []
            for row in cursor:
                automobili.append(Automobile(row[0], row[1], row[2], row[3], row[4]))
            cursor.close()
            conn.close()
            if len(automobili) == 0 :
                return None
            else:
                return automobili
        except Exception as e:
            print(f"Errore durante lettura automobili: {e}")
            return None




        # TODO

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        try :
           conn = get_connection()
           cursor = conn.cursor()
           query = "SELECT * FROM automobile WHERE modello = %s;"
           cursor.execute(query, ( modello,))

           automobili = []
           for row in cursor:
               automobili.append(Automobile(row[0], row[1], row[2], row[3], row[4]))
           cursor.close()
           conn.close()
           if len(automobili) == 0 :
               return None
           else:
                return automobili
        except Exception as e:
           print(f"Errore durante lettura automobili: {e}")
           return None

        # TODO
