from selenium import webdriver
from selenium.webdriver.common.by import By
from jdd import *
from functions import *

summary_suite_de_test={
    'total_sdt': 0,
    'success': 0,
    'fail': 0
}

#liste des titres de page possibles après connexion
liste_de_titre = ['Dashboard', 'Espace adhérent']


for jdd in all_credentials:
    driver = webdriver.Chrome()  # Assurez-vous d'avoir le pilote approprié installé

    try:
        open_jardeen(driver)
        page_de_connexion(driver)
        connexion(driver, all_credentials[jdd]['id'], all_credentials[jdd]['password'])
        MonEspace(driver)
        MesInformations(driver)
        ChangePassword(driver, "newPassword")

        # On vérifie si le changement de mot de passe est effectif en se reconnectant
        Deconnexion(driver)
        page_de_connexion(driver)
        connexion(driver, all_credentials[jdd]['id'], "newPassword")

        # On retourne changer le mot de passe d'origine
        MonEspace(driver)
        MesInformations(driver)
        ChangePassword(driver, all_credentials[jdd]['password'])
        
        
        status_SuiteDeTest = status_JDD(True, jdd, adp_01[jdd]['expected']) # on ajuste le status en fonction de si on s'attendait à du ko ou non


    except ValueError as e:
        print(f"Erreur: {e}")
        status_SuiteDeTest = status_JDD(False, jdd, adp_01[jdd]['expected']) # on ajuste le status en fonction de si on s'attendait à du ko ou non



    stats_suite_de_test = calcul_SuiteDeTest(status_SuiteDeTest, summary_suite_de_test, jdd) # on met à jour les statistique de notre cas de test

    driver.quit()


results_SuiteDeTest(stats_suite_de_test) # on affiche les résultat de la suite de test
