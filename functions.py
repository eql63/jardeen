from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from jdd import *
from functions import *

def open_jardeen(driver):
    driver.get("http://localhost:8080/index.xhtml")
    try:
        driver.maximize_window()
        assert "Accueil Visiteur" in driver.title
        # print("Application correctement chargée.")
        return driver
    except:
        raise ValueError("Impossible d'accéder à la page d'accueil de Jardeen")

def page_de_connexion(driver):
    try:
        driver.implicitly_wait(10)

        # Trouve l'élément avec le texte "Connexion" dans le lien en utilisant un sélecteur CSS
        bouton_connexion = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/div[2]/ul/li[4]/a")
        bouton_connexion.click()
        assert "Connexion" in driver.title
        # print("Page de connexion correctement chargée.")
    except:
        raise ValueError("Impossible d'accéder la page de connexion")

def connexion(driver, id, password):
    try:
        element_id = driver.find_element(By.XPATH, '//*[@id="input_j_idt27:email"]')
        element_password = driver.find_element(By.XPATH, '//*[@id="input_j_idt27:password"]')
        element_id.clear()
        element_id.send_keys(id)
        element_password.send_keys(password)

        # bouton pour valider l'authentification
        bouton = driver.find_element("xpath", '//*[@id="j_idt27:j_idt32"]')
        bouton.click()
    except:
        raise ValueError("Impossible de valider l'authentification")

def check_page(driver, liste_de_titre):
    try:
        driver.implicitly_wait(10)

        assert any(titre in driver.title for titre in liste_de_titre), f"Titre inattendu: {driver.title}"

        #print(f"Page de {title} correctement chargée.")
        return True
    except:
        #print(f"La page de {title} n'a pas pu être chargé")
        return False
    


### FONCTION ADP-02 ###

def MonEspace(driver):
    try:
        driver.implicitly_wait(5)

        # Trouve l'élément avec le texte "Connexion" dans le lien en utilisant un sélecteur CSS
        bouton_monEspace = driver.find_element(By.XPATH, "/html/body/nav[1]/div/div[2]/ul/li[2]/a")
        bouton_monEspace.click()
        assert "Espace adhérent" in driver.title
        # print("Page de connexion correctement chargée.")
    except:
        raise ValueError("La page Espace adhérent n'a pas pu être chargée")


def MesInformations(driver):
    try:
        driver.implicitly_wait(5)

        # Trouve l'élément avec le texte "Connexion" dans le lien en utilisant un sélecteur CSS
        bouton_mesInformations = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div/ul/li[1]/a")
        bouton_mesInformations.click()
        assert "Formulaire Adherent" in driver.title
    except:
        raise ValueError("La page Formulaire Adherent n'a pas pu être chargée")


def ChangePassword(driver, new_password):
    try:

        driver.implicitly_wait(5)

        element_password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div/div/div/div/div[4]/input[3]')
        element_password.clear()
        element_password.send_keys(new_password)

        # bouton pour valider l'authentification
        bouton = driver.find_element("xpath", '//*[@id="j_idt31:j_idt50"]')
        bouton.click()
    except:
        raise ValueError("Impossible de valider le changement de mot de passe")
    
def Deconnexion(driver):
    try:
        driver.implicitly_wait(5)

        bouton_deconnexion = driver.find_element(By.XPATH, '//*[@id="j_idt24:j_idt25"]')
        
        bouton_deconnexion.click()
        assert "Accueil Visiteur" in driver.title
    except:
        raise ValueError("Impossible de se déconnecter")
        
    
### Fin Fonctions ADP-02 ###

def status_JDD(true_or_false, suite_de_test, expected):
    if true_or_false and expected or not true_or_false and not expected:
        print(f'[PASS] Suite de test a réussi. Jeu de données = {suite_de_test}')
        return True
    else:
        print(f'[FAIL] Suite de test a échoué. Jeu de données = {suite_de_test}')
        return False
    pass




def calcul_SuiteDeTest(status_SuiteDeTest, summary_suite_de_test, jdd):
    if status_SuiteDeTest: 
        summary_suite_de_test["total_sdt"] +=1
        summary_suite_de_test["success"] +=1
    else:
        summary_suite_de_test["total_sdt"] +=1
        summary_suite_de_test["fail"] +=1

    return summary_suite_de_test

def results_SuiteDeTest(stats_suite_de_test):
    print('------------------------------------------------------------------------------')
    print("Ma suite de Tests")
    print(f'{stats_suite_de_test["total_sdt"]} test, {stats_suite_de_test["success"]} réussi, {stats_suite_de_test["fail"]} échoué')
    print("==============================================================================")

