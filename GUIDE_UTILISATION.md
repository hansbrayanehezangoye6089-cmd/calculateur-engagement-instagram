# 📖 Guide d'Utilisation - Calculateur d'Engagement Instagram

---

## 🚀 Démarrage rapide

### Installation
```bash
git clone https://github.com/hansbrayanehezangoye6089-cmd/calculateur-engagement-instagram.git
cd calculateur-engagement-instagram
```

### Utilisation
```bash
# Version simple
python engagement.py

# Avec export CSV
python engagement_csv.py

# Avec interface graphique
python engagement_gui.py
```

---

## 🎯 Choisir votre version

### 1️⃣ Version Simple (`engagement.py`)
**Idéale pour :** Apprendre Python, utilisation rapide en ligne de commande

**Avantages :**
- Légère et rapide
- Pas de dépendances externes
- Parfaite pour l'apprentissage

**Utilisation :**
```bash
python engagement.py
Nombre de likes : 450
Nombre de commentaires : 35
Nombre d'abonnés : 5000
```

---

### 2️⃣ Version CSV (`engagement_csv.py`)
**Idéale pour :** Analyser plusieurs publications, créer des historiques

**Avantages :**
- Export automatique en CSV
- Historique de tous les calculs
- Facile à analyser dans Excel/Google Sheets
- Timestamp pour chaque entrée

**Utilisation :**
```bash
python engagement_csv.py
Description : Photo vacances
Nombre de likes : 450
Nombre de commentaires : 35
Nombre d'abonnés : 5000
Voulez-vous sauvegarder le résultat ? oui
```

**Résultat CSV :**
```
Date,Description,Likes,Commentaires,Abonnés,Taux d'engagement (%)
2024-01-15 10:30:45,Photo vacances,450,35,5000,9.70
```

---

### 3️⃣ Version Interface Graphique (`engagement_gui.py`)
**Idéale pour :** Utilisation professionnelle, présentation, interface conviviale

**Avantages :**
- Interface intuitive et visuelle
- Pas besoin d'ouvrir le terminal
- Export CSV directement depuis l'interface
- Plus accessible pour les non-développeurs

**Utilisation :**
1. Ouvrez le programme
2. Remplissez les champs
3. Cliquez sur "🧮 Calculer"
4. Voyez le résultat instantanément
5. Cliquez sur "💾 Sauvegarder CSV" pour exporter

---

## 📊 Interpréter vos résultats

### Tableau de référence

| Taux | Performance | Action recommandée |
|------|-------------|-------------------|
| < 1% | 🔴 Très faible | Révoir la stratégie de contenu |
| 1-3% | 🟠 Faible | Améliorer la qualité du contenu |
| 3-5% | 🟡 Moyen | Maintenir et optimiser |
| 5-10% | 🟢 Bon | Continue comme ça ! |
| > 10% | 🟢 Excellent | Reproduire cette stratégie |

### Exemples réels

**Post haute performance :**
```
Likes : 1,500
Commentaires : 120
Abonnés : 10,000
Engagement : 16.2% 🌟
```

**Post moyen :**
```
Likes : 350
Commentaires : 25
Abonnés : 8,000
Engagement : 4.69% 👍
```

**Post faible :**
```
Likes : 50
Commentaires : 5
Abonnés : 12,000
Engagement : 0.46% 📉
```

---

## 📁 Gérer vos données CSV

### Ouvrir le fichier CSV

**Option 1 : Excel/Google Sheets**
1. Téléchargez `resultats_engagement.csv`
2. Ouvrez-le avec Excel ou Google Sheets
3. Analysez vos données avec des graphiques

**Option 2 : Python/Pandas**
```python
import pandas as pd

df = pd.read_csv('resultats_engagement.csv')
print(df)
print(df.describe())  # Statistiques
```

### Analyser vos données

```python
import pandas as pd

df = pd.read_csv('resultats_engagement.csv')

# Engagement moyen
print(f"Engagement moyen : {df['Taux d\'engagement (%)'].mean():.2f}%")

# Publication avec meilleur engagement
best = df.loc[df['Taux d\'engagement (%)'].idxmax()]
print(f"Meilleur post : {best['Description']} ({best['Taux d\'engagement (%)']})%")
```

---

## 🔧 Paramètres avancés

### Modifier les fichiers

**Changer le nom du fichier CSV :**
```python
# Dans engagement_csv.py, ligne ~70
sauvegarder_csv(donnees, nom_fichier="mes_resultats.csv")
```

**Ajouter des champs personnalisés :**
```python
# Ajouter dans le dictionnaire "donnees"
donnees["Hashtags"] = "input du hashtag"
donnees["Contenu"] = "photo/video/carousel"
```

---

## ❓ FAQ

### Q : Pourquoi mon engagement est-il bas ?
**R :** Plusieurs facteurs peuvent l'expliquer :
- Horaire de publication non optimal
- Contenu moins engageant
- Pas assez de hashtags pertinents
- Audience pas assez intéressée par le sujet

### Q : Comment améliorer mon engagement ?
**R :**
1. Publier aux heures de peak (généralement 18h-21h)
2. Utiliser des hashtags pertinents (5-30)
3. Créer du contenu de qualité
4. Engager régulièrement avec votre audience
5. Utiliser des appels à l'action (CTA)

### Q : Puis-je récupérer mes données Instagram réelles ?
**R :** Pas directement avec ce projet, mais vous pouvez :
1. Accéder à Instagram Insights sur votre compte
2. Noter manuellement les chiffres
3. Les entrer dans le calculateur

### Q : Comment automatiser l'extraction depuis Instagram ?
**R :** C'est possible avec l'API Instagram, mais :
- Nécessite une approbation de Meta/Facebook
- Demande une authentification
- Projet futur : implémenter cette fonctionnalité

### Q : Mes données CSV disparaissent ?
**R :** 
- Vérifiez que le fichier n'est pas supprimé
- Il est créé dans le même dossier que `engagement_csv.py`
- Sauvegardez-le ailleurs en sécurité

### Q : Puis-je utiliser cela pour d'autres réseaux sociaux ?
**R :** Oui ! La formule marche pour :
- TikTok
- Facebook
- YouTube
- Twitter/X
- LinkedIn

---

## 💡 Conseils pour l'analyse

### 1. Créer un système de suivi
```python
# Exemple : suivi hebdomadaire
# Date, Publication, Engagement, Notes
```

### 2. Comparer les périodes
- Engagement avant/après changement de stratégie
- Engagement par type de contenu
- Engagement par jour de la semaine

### 3. Identifier les patterns
- Quel type de contenu performe le mieux ?
- Quel horaire est optimal ?
- Quels hashtags attirent le plus ?

### 4. A/B Testing
- Testez deux versions du même contenu
- Comparez les engagement rates
- Reproduisez ce qui marche

---

## 🔐 Confidentialité et sécurité

- ✅ Aucune donnée ne sort de votre ordinateur
- ✅ Les résultats sont stockés localement en CSV
- ✅ Pas de connexion à Internet requise
- ✅ Open source : vérifiez le code vous-même

---

## 🤝 Contribuer

Vous avez une idée pour améliorer ce projet ?

1. Fork le dépôt
2. Créez une branche : `git checkout -b ma-feature`
3. Committez vos changes : `git commit -am 'Ajout de ma feature'`
4. Poussez vers la branche : `git push origin ma-feature`
5. Ouvrez une Pull Request

---

## 📞 Support

Des questions ? Ouvrez une issue sur GitHub !

---

**Bon calcul d'engagement ! 📊✨**
