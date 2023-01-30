from typing import List
import pandas as pd

class Article:
    def __init__(self, reference, designation, prix, quantite) -> None:
        self.reference = reference
        self.designation = designation
        self.prix = prix
        self.quantite = quantite

    def __str__(self) -> str:
        return f"Référence: {self.reference}\nDesignation: {self.designation}\nPrix: {self.prix}\nQuantité: {self.quantite}"
    
    def exists(self, other_reference: int) -> bool:
        if self.reference == other_reference:
            return True
        return False
 
class Stock:
    def __init__(self, liste_articles: List[Article] = []) -> None:
        self.liste_articles = liste_articles

    def afficher(self):
        for article in self.liste_articles:
            print(article, "\n")

    def rechercher_article_par_reference(self, reference: int):
        for article in self.liste_articles:
            if article.reference == reference:
                return article
        print("Article introuvable")

    def rechercher_article_par_designation(self, designation: str):
        for article in self.liste_articles:
            if article.designation == designation:
                return article
        print("Article introuvable")

    def rechercher_article_par_prix(self, prix_inf, prix_sup):
        article_trouves = []
        for article in self.liste_articles:
            if(article.prix > prix_inf) & (article.prix < prix_sup):
                article_trouves.append(article)
        if len(article_trouves) == 0:
            print("Aucun article trouvé")
        return article_trouves
        
    def ajouter_article(self, new_article: Article) -> None:
        for article in self.liste_articles:
            if article.exists(new_article.reference):
                print("Référence de produit déjà existante")
                return
        self.liste_articles.append(new_article)
    
    def supprimer_article(self, old_reference: int) -> None:
        for article in self.liste_articles:
            if article.exists(old_reference):
                self.liste_articles.remove(article)
                return
        print("Article introuvable")
    
    def modifier_article(self, reference: int, new_designation=None, new_prix=None, new_quantite=None) -> None:
        for article in self.liste_articles:
            if article.exists(reference):
                article.designation = new_designation if new_designation else article.designation
                article.prix = new_prix if new_prix else article.prix
                article.quantite = new_quantite if new_quantite else article.quantite
                return
        print("Article introuvable")

    
def menu():
    print("Choisir une option parmi les suivantes:\n")
    print()


if __name__ == "__main__":
    article1 = Article(
        reference=1,
        designation="Table à manger",
        prix=120.0,
        quantite=12
    )

    article2 = Article(
        reference=2,
        designation="Table basse",
        prix=99.99,
        quantite=40
    )

    stock = Stock(liste_articles=[article1, article2])
    print(stock)


    print("\n****Stock du magasin:")
    stock.afficher()

    print("\n****Recherche d'un article par référence")
    found = stock.rechercher_article_par_reference(reference=1)
    print(found)
    found = stock.rechercher_article_par_reference(reference=5)
    print(found)

    print("\n****Recherche d'un article par designation")
    found = stock.rechercher_article_par_designation(designation="Table à manger")
    print(found)
    found = stock.rechercher_article_par_designation(designation="Chaise de bureau")
    print(found)

    print("\n****Ajout d'un article:")
    stock.ajouter_article(new_article=Article(reference=1, designation="Chaise de bureau", prix=10.5, quantite=5))
    stock.ajouter_article(new_article=Article(reference=3, designation="Chaise de bureau", prix=10.5, quantite=5))
    stock.afficher()

    print("\n****Suppression d'un article:")
    stock.supprimer_article(old_reference=5)
    stock.supprimer_article(old_reference=3)
    stock.afficher()

    print("\n****Modifer un article:")
    stock.modifier_article(reference=1, new_prix=125.99)
    stock.modifier_article(reference=3, new_quantite=10)
    stock.afficher()
     
    print("\n****Rechercher un article par prix:")
    found = stock.rechercher_article_par_prix(prix_inf=10, prix_sup=100)
    for f in found:
        print(f)
    found = stock.rechercher_article_par_prix(prix_inf=130, prix_sup=400)
    print(found)
    