questions = {
    "comment allez-vous aujourd'hui ?": "à propos",
    "comment configurer un téléphone portable ?": "configuration",
    "à quelle heure ouvrez-vous ?": "heure_de_fermeture",
    "quels sont les facteurs influençant les ventes ?": "facteurs_impactant_les_ventes",
    "je ne comprends pas le fonctionnement de votre service": "résoudre_des_problèmes",
    "j'ai oublié mon mot de passe, comment le réinitialiser ?": "mot_de_passe_oublié",
    "affichez-moi ma liste de rendez-vous s'il vous plaît": "statut_du_rendez-vous",
    "puis-je prendre rendez-vous avec votre manager ?": "prendre_rdv",
    "merci pour votre aide": "merci",
    "quelle sorte d'informations sont disponibles auprès de vos fournisseurs ?": "informations_fournisseur",
    "qui est le fournisseur de vos produits ?": "problèmes_de_fabrication",
    "que pensent vos clients de votre service ?": "satisfaction_des_clients",
    "quels produits sont actuellement disponibles ?": "gadgets",
    "où puis-je trouver votre magasin ?": "emplacement_du_magasin",
    "quel est l'avis général de vos clients ?": "satisfaction_des_clients"
}


from chat import get_response
from prettytable import PrettyTable

t = PrettyTable(["Question", "Tag Réel", "Tag Prédit", "Correspondance Tag"])

for question in questions:
    _, tag = get_response(question)
    t.add_row([question, questions[question], tag, tag == questions[question]])

print(t)
