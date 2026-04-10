import logging

# Configuration minimale
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("L'application a démarré.")
logging.warning("Attention, la mémoire est presque pleine.")
logging.error("Une erreur est survenue lors de l'appel API.")

logging.basicConfig(
    filename='app.log',
    filemode='a', # 'a' pour ajouter à la suite, 'w' pour écraser à chaque lancement
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logging.debug("Ce message sera écrit dans app.log")

#try:
#    resultat = 10 / 0
#except ZeroDivisionError:
    # exc_info=True ajoute automatiquement le détail de l'erreur au log
#    logging.error("Tentative de division par zéro !", exc_info=True)