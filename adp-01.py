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





for jdd in adp_01:
    driver = webdriver.Chrome()  # Assurez-vous d'avoir le pilote approprié installé


    open_jardeen(driver)
    page_de_connexion(driver)
    connexion(driver, adp_01[jdd]['id'], adp_01[jdd]['password'])
    status_SuiteDeTest = check_page(driver, liste_de_titre) # si on a atteint la page voulu alors status_SuiteDeTest = True, sinon False


    status_SuiteDeTest = status_JDD(status_SuiteDeTest, jdd, adp_01[jdd]['expected']) #on ajuste le status en fonction de si on s'attendait à du ko ou non
    stats_suite_de_test = calcul_SuiteDeTest(status_SuiteDeTest, summary_suite_de_test, jdd) # on met à jour les statistique de notre cas de test
    driver.quit()


results_SuiteDeTest(stats_suite_de_test) # on affiche les résultat de la suite de test
