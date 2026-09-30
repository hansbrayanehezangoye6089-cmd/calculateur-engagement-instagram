"""
Calculateur de Taux d'Engagement Instagram - Version Simple
Auteur: HANS BRAYANE HEZANGOYE
Description: Calcule le taux d'engagement d'une publication Instagram
"""

def calculer_engagement(likes, commentaires, abonnes):
    """
    Calcule le taux d'engagement.
    
    Args:
        likes (int): Nombre de likes
        commentaires (int): Nombre de commentaires
        abonnes (int): Nombre d'abonnés
        
    Returns:
        float: Taux d'engagement en pourcentage
        
    Raises:
        ValueError: Si le nombre d'abonnés est <= 0
    """
    if abonnes <= 0:
        raise ValueError("Le nombre d'abonnés doit être supérieur à 0.")
    return ((likes + commentaires) / abonnes) * 100


def main():
    """Fonction principale du programme."""
    print("=" * 50)
    print("📊 Calculateur de Taux d'Engagement Instagram")
    print("=" * 50)
    
    try:
        likes = int(input("\nNombre de likes : "))
        commentaires = int(input("Nombre de commentaires : "))
        abonnes = int(input("Nombre d'abonnés : "))
        
        if likes < 0 or commentaires < 0:
            print("❌ Les nombres de likes et commentaires doivent être positifs.")
            return
        
        resultat = calculer_engagement(likes, commentaires, abonnes)
        
        print("\n" + "=" * 50)
        print(f"✅ Taux d'engagement : {resultat:.2f}%")
        print("=" * 50)
        
    except ValueError as e:
        print(f"❌ Erreur : {e}")
    except Exception as e:
        print(f"❌ Une erreur inattendue s'est produite : {e}")


if __name__ == "__main__":
    main()
