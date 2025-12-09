"""
Script pour analyser les résultats du questionnaire Feedback Moodle
Exporter d'abord les résultats depuis Moodle en format CSV
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def analyser_feedback(fichier_csv):
    """
    Analyse les données exportées du feedback Moodle

    Args:
        fichier_csv: Chemin vers le fichier CSV exporté depuis Moodle
    """
    # Charger les données
    df = pd.read_csv(fichier_csv)

    print("=" * 80)
    print("ANALYSE DU QUESTIONNAIRE D'ORIENTATION - TRIMESTRE 1")
    print("=" * 80)
    print(f"\nNombre total de réponses : {len(df)}")

    # 1. ANALYSE DES INFORMATIONS GÉNÉRALES
    print("\n" + "=" * 80)
    print("1. INFORMATIONS GÉNÉRALES")
    print("=" * 80)

    if 'Classe' in df.columns:
        print("\nRépartition par classe :")
        print(df['Classe'].value_counts())

    if 'Regime' in df.columns:
        print("\nRépartition par régime :")
        print(df['Regime'].value_counts())
        print(f"Pourcentages : ")
        print(df['Regime'].value_counts(normalize=True) * 100)

    # 2. ANALYSE DES AUTOÉVALUATIONS
    print("\n" + "=" * 80)
    print("2. AUTOÉVALUATIONS PAR MATIÈRE")
    print("=" * 80)

    matieres = ['Auto_Francais', 'Auto_Maths', 'Auto_HG', 'Auto_LV1',
                'Auto_LV2', 'Auto_SVT', 'Auto_Physique', 'Auto_EPS', 'Auto_SNT']

    for matiere in matieres:
        if matiere in df.columns:
            print(f"\n{matiere.replace('Auto_', '')} :")
            print(df[matiere].value_counts().sort_index())

            # Calculer la moyenne (convertir en numérique)
            mapping = {
                'Très insuffisant': 1,
                'Insuffisant': 2,
                'Satisfaisant': 3,
                'Bien': 4,
                'Très bien': 5
            }
            if df[matiere].notna().any():
                notes = df[matiere].map(mapping)
                moyenne = notes.mean()
                print(f"Moyenne : {moyenne:.2f}/5")

    # 3. ANALYSE DE L'ÉVOLUTION
    print("\n" + "=" * 80)
    print("3. ÉVOLUTION DEPUIS LE DÉBUT DE L'ANNÉE")
    print("=" * 80)

    if 'Evolution' in df.columns:
        print(df['Evolution'].value_counts())

    # 4. ANALYSE DES MÉTHODES DE TRAVAIL
    print("\n" + "=" * 80)
    print("4. MÉTHODES DE TRAVAIL")
    print("=" * 80)

    if 'Temps_travail' in df.columns:
        print("\nTemps de travail quotidien :")
        print(df['Temps_travail'].value_counts())

    if 'Anticipation' in df.columns:
        print("\nAnticipation du travail :")
        print(df['Anticipation'].value_counts())

    if 'Revisions' in df.columns:
        print("\nDébut des révisions :")
        print(df['Revisions'].value_counts())

    # 5. ANALYSE NUMÉRIQUE
    print("\n" + "=" * 80)
    print("5. VIE NUMÉRIQUE")
    print("=" * 80)

    if 'Ordinateur' in df.columns:
        print("\nAccès à un ordinateur :")
        print(df['Ordinateur'].value_counts())

    if 'Tablette' in df.columns:
        print("\nAccès à une tablette :")
        print(df['Tablette'].value_counts())

    # 6. ANALYSE DE L'ORIENTATION
    print("\n" + "=" * 80)
    print("6. PROJET D'ORIENTATION")
    print("=" * 80)

    if 'Metier_connu' in df.columns:
        print("\nMétier connu :")
        print(df['Metier_connu'].value_counts())

    if 'Type_bac' in df.columns:
        print("\nType de bac envisagé :")
        print(df['Type_bac'].value_counts())

    if 'Specialites_connues' in df.columns:
        print("\nSpécialités déjà choisies :")
        print(df['Specialites_connues'].value_counts())

    # 7. ACCOMPAGNEMENT
    print("\n" + "=" * 80)
    print("7. ACCOMPAGNEMENT")
    print("=" * 80)

    if 'COP_RDV' in df.columns:
        print("\nSouhait RDV avec COP :")
        print(df['COP_RDV'].value_counts())

    if 'Envie_stage' in df.columns:
        print("\nEnvie de faire un stage :")
        print(df['Envie_stage'].value_counts())


def generer_graphiques(fichier_csv, dossier_sortie='resultats_feedback'):
    """
    Génère des graphiques à partir des données du feedback

    Args:
        fichier_csv: Chemin vers le fichier CSV exporté depuis Moodle
        dossier_sortie: Dossier où sauvegarder les graphiques
    """
    import os
    os.makedirs(dossier_sortie, exist_ok=True)

    df = pd.read_csv(fichier_csv)

    # Graphique 1 : Autoévaluations par matière
    matieres = ['Auto_Francais', 'Auto_Maths', 'Auto_HG', 'Auto_LV1',
                'Auto_LV2', 'Auto_SVT', 'Auto_Physique', 'Auto_EPS', 'Auto_SNT']

    mapping = {
        'Très insuffisant': 1,
        'Insuffisant': 2,
        'Satisfaisant': 3,
        'Bien': 4,
        'Très bien': 5
    }

    moyennes = {}
    for matiere in matieres:
        if matiere in df.columns and df[matiere].notna().any():
            notes = df[matiere].map(mapping)
            moyennes[matiere.replace('Auto_', '')] = notes.mean()

    if moyennes:
        plt.figure(figsize=(12, 6))
        plt.bar(moyennes.keys(), moyennes.values(), color='steelblue')
        plt.axhline(y=3, color='red', linestyle='--', label='Satisfaisant')
        plt.xlabel('Matières')
        plt.ylabel('Moyenne autoévaluation')
        plt.title('Autoévaluation moyenne par matière')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, 5)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f'{dossier_sortie}/autoevaluations.png', dpi=300)
        print(f"\nGraphique sauvegardé : {dossier_sortie}/autoevaluations.png")

    # Graphique 2 : Temps de travail
    if 'Temps_travail' in df.columns:
        plt.figure(figsize=(10, 6))
        df['Temps_travail'].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title('Temps de travail quotidien')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig(f'{dossier_sortie}/temps_travail.png', dpi=300)
        print(f"Graphique sauvegardé : {dossier_sortie}/temps_travail.png")

    # Graphique 3 : Orientation
    if 'Type_bac' in df.columns:
        plt.figure(figsize=(10, 6))
        df['Type_bac'].value_counts().plot(kind='bar', color='green')
        plt.xlabel('Type de bac')
        plt.ylabel('Nombre d\'élèves')
        plt.title('Type de bac envisagé')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'{dossier_sortie}/type_bac.png', dpi=300)
        print(f"Graphique sauvegardé : {dossier_sortie}/type_bac.png")


def generer_rapport_individuel(fichier_csv, nom_eleve):
    """
    Génère un rapport individuel pour un élève

    Args:
        fichier_csv: Chemin vers le fichier CSV exporté depuis Moodle
        nom_eleve: Nom de l'élève (ou index de ligne)
    """
    df = pd.read_csv(fichier_csv)

    # Supposons que la première colonne contient le nom ou un identifiant
    eleve = df.iloc[nom_eleve] if isinstance(nom_eleve, int) else df[df.iloc[:, 0] == nom_eleve].iloc[0]

    print("=" * 80)
    print(f"RAPPORT INDIVIDUEL")
    print("=" * 80)

    for col in df.columns:
        if pd.notna(eleve[col]) and eleve[col] != '':
            print(f"\n{col} : {eleve[col]}")


if __name__ == "__main__":
    print("""
    UTILISATION :

    1. Exportez les résultats depuis Moodle ELEA :
       - Allez dans votre activité Feedback
       - Onglet "Analyse" ou "Afficher les réponses"
       - Cliquez sur "Télécharger au format Excel" ou "Exporter"
       - Enregistrez le fichier CSV

    2. Modifiez le chemin du fichier ci-dessous et exécutez le script :

       analyser_feedback('resultats_feedback.csv')
       generer_graphiques('resultats_feedback.csv')
    """)

    # Exemple d'utilisation (décommentez et adaptez) :
    # analyser_feedback('resultats_feedback.csv')
    # generer_graphiques('resultats_feedback.csv')
    # generer_rapport_individuel('resultats_feedback.csv', 0)  # Premier élève
