"""
Calculateur Professionnel de Taux d'Engagement Instagram
Version Streamlit - Interface Web Interactive
Auteur: HANS BRAYANE HEZANGOYE
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
import csv

# Configuration de la page
st.set_page_config(
    page_title="Calculateur d'Engagement Instagram",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS personnalisés
st.markdown("""
    <style>
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            font-weight: bold;
        }
        .good-engagement {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        }
        .poor-engagement {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
        }
        .title {
            text-align: center;
            color: #667eea;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown("<h1 class='title'>📊 Calculateur d'Engagement Instagram</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Analyse professionnelle des performances de vos publications</p>", unsafe_allow_html=True)

# Initialiser les données en session
if 'historique' not in st.session_state:
    # Charger l'historique s'il existe
    if os.path.exists('resultats_engagement.csv'):
        st.session_state.historique = pd.read_csv('resultats_engagement.csv')
    else:
        st.session_state.historique = pd.DataFrame()

# Sidebar - Navigation
st.sidebar.title("🎯 Navigation")
section = st.sidebar.radio(
    "Choisissez une section",
    ["📝 Calculer", "📊 Analyse", "📈 Statistiques", "💾 Historique", "ℹ️ À propos"]
)

# ===== SECTION 1: CALCULER =====
if section == "📝 Calculer":
    st.header("Calculer le taux d'engagement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        description = st.text_input(
            "📌 Description de la publication",
            placeholder="Ex: Photo de vacances, Story produit, etc."
        )
        likes = st.number_input("👍 Nombre de likes", min_value=0, step=1)
        commentaires = st.number_input("💬 Nombre de commentaires", min_value=0, step=1)
    
    with col2:
        abonnes = st.number_input("👥 Nombre d'abonnés", min_value=1, step=1, value=1000)
        contenu_type = st.selectbox(
            "📱 Type de contenu",
            ["Photo", "Vidéo", "Carousel", "Reel", "Story", "Autre"]
        )
        hashtags = st.text_input(
            "#️⃣ Hashtags utilisés (séparés par des espaces)",
            placeholder="Ex: #Instagram #Marketing #Python"
        )
    
    # Bouton de calcul
    if st.button("🧮 Calculer l'engagement", use_container_width=True):
        if abonnes > 0:
            engagement = ((likes + commentaires) / abonnes) * 100
            
            # Créer l'enregistrement
            nouveau_resultat = {
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Description": description or "Sans description",
                "Type": contenu_type,
                "Likes": likes,
                "Commentaires": commentaires,
                "Abonnés": abonnes,
                "Interactions": likes + commentaires,
                "Hashtags": hashtags or "N/A",
                "Taux d'engagement (%)": round(engagement, 2)
            }
            
            # Ajouter à l'historique
            if isinstance(st.session_state.historique, pd.DataFrame) and not st.session_state.historique.empty:
                st.session_state.historique = pd.concat(
                    [st.session_state.historique, pd.DataFrame([nouveau_resultat])],
                    ignore_index=True
                )
            else:
                st.session_state.historique = pd.DataFrame([nouveau_resultat])
            
            # Sauvegarder en CSV
            st.session_state.historique.to_csv('resultats_engagement.csv', index=False, encoding='utf-8')
            
            # Afficher le résultat
            st.success("✅ Calcul effectué avec succès !")
            
            # Afficher métriques
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Likes", f"{likes:,}")
            with col2:
                st.metric("Commentaires", commentaires)
            with col3:
                st.metric("Interactions totales", likes + commentaires)
            with col4:
                st.metric("Engagement %", f"{engagement:.2f}%")
            
            # Interprétation
            st.markdown("---")
            
            if engagement > 10:
                st.success(f"🌟 **Excellent !** Votre taux d'engagement de {engagement:.2f}% est exceptionnel !")
            elif engagement > 5:
                st.info(f"👍 **Bon !** Votre taux d'engagement de {engagement:.2f}% est satisfaisant.")
            elif engagement > 1:
                st.warning(f"📉 **Moyen.** Votre taux d'engagement de {engagement:.2f}% peut être amélioré.")
            else:
                st.error(f"⚠️ **À améliorer.** Votre taux d'engagement de {engagement:.2f}% est faible.")
            
            # Recommandations
            st.markdown("### 💡 Recommandations")
            recommendations = []
            
            if engagement < 3:
                recommendations.append("- Optez pour un meilleur moment de publication (18h-21h généralement)")
                recommendations.append("- Améliorez la qualité visuelle de votre contenu")
                recommendations.append("- Utilisez des appels à l'action plus percutants")
            
            if likes < commentaires * 5:
                recommendations.append("- Encouragez plus de commentaires avec des questions ou des défis")
            
            if not hashtags:
                recommendations.append("- Utilisez 15-30 hashtags pertinents pour augmenter la portée")
            
            if recommendations:
                for rec in recommendations:
                    st.write(rec)
            else:
                st.write("✅ Continuez ainsi, votre stratégie fonctionne bien !")
        else:
            st.error("❌ Le nombre d'abonnés doit être supérieur à 0")

# ===== SECTION 2: ANALYSE =====
elif section == "📊 Analyse":
    st.header("Analyse détaillée")
    
    if not st.session_state.historique.empty:
        df = st.session_state.historique.copy()
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Métriques principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📝 Total publications", len(df))
        with col2:
            st.metric("⭐ Engagement moyen", f"{df['Taux d\'engagement (%)'].mean():.2f}%")
        with col3:
            st.metric("🔝 Meilleur engagement", f"{df['Taux d\'engagement (%)'].max():.2f}%")
        with col4:
            st.metric("📊 Pire engagement", f"{df['Taux d\'engagement (%)'].min():.2f}%")
        
        st.markdown("---")
        
        # Graphiques
        col1, col2 = st.columns(2)
        
        with col1:
            # Engagement dans le temps
            fig = px.line(
                df.sort_values('Date'),
                x='Date',
                y='Taux d\'engagement (%)',
                title="Evolution de l'engagement",
                markers=True,
                color_discrete_sequence=['#667eea']
            )
            fig.update_layout(hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Engagement par type de contenu
            fig = px.bar(
                df.groupby('Type')['Taux d\'engagement (%)'].mean(),
                title="Engagement moyen par type",
                color_discrete_sequence=['#764ba2']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Distribution des interactions
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.scatter(
                df,
                x='Likes',
                y='Commentaires',
                size='Taux d\'engagement (%)',
                hover_data=['Description'],
                title="Likes vs Commentaires",
                color_discrete_sequence=['#38ef7d']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Box plot engagement
            fig = go.Figure()
            fig.add_trace(go.Box(
                y=df['Taux d\'engagement (%)'],
                name="Engagement",
                marker_color='#11998e'
            ))
            fig.update_layout(title="Distribution de l'engagement")
            st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.info("📭 Aucune donnée pour l'analyse. Calculez d'abord quelques engagements !")

# ===== SECTION 3: STATISTIQUES =====
elif section == "📈 Statistiques":
    st.header("Statistiques avancées")
    
    if not st.session_state.historique.empty:
        df = st.session_state.historique.copy()
        
        # Statistiques descriptives
        st.subheader("📊 Résumé statistique")
        
        stats_cols = ['Likes', 'Commentaires', 'Interactions', 'Taux d\'engagement (%)']
        stats_df = df[stats_cols].describe().round(2)
        
        st.dataframe(stats_df, use_container_width=True)
        
        # Comparaison par type de contenu
        st.subheader("🎯 Performance par type de contenu")
        
        type_stats = df.groupby('Type').agg({
            'Taux d\'engagement (%)': ['mean', 'max', 'min', 'count'],
            'Likes': 'mean',
            'Commentaires': 'mean'
        }).round(2)
        
        st.dataframe(type_stats, use_container_width=True)
        
        # Corrélation
        st.subheader("📈 Analyse de corrélation")
        
        fig = px.imshow(
            df[['Likes', 'Commentaires', 'Abonnés', 'Taux d\'engagement (%)']].corr(),
            labels=dict(color="Corrélation"),
            title="Matrice de corrélation"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Top 5 publications
        st.subheader("🏆 Top 5 publications")
        
        top_5 = df.nlargest(5, 'Taux d\'engagement (%)')
        
        for idx, row in top_5.iterrows():
            with st.container():
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.write(f"**{row['Description']}**")
                    st.caption(f"{row['Date']} • {row['Type']}")
                with col2:
                    st.metric("Engagement", f"{row['Taux d\'engagement (%)']:.2f}%")
                with col3:
                    st.metric("Interactions", int(row['Interactions']))
    
    else:
        st.info("📭 Aucune donnée pour les statistiques.")

# ===== SECTION 4: HISTORIQUE =====
elif section == "💾 Historique":
    st.header("Historique des calculs")
    
    if not st.session_state.historique.empty:
        df = st.session_state.historique.copy()
        
        # Filtres
        col1, col2, col3 = st.columns(3)
        
        with col1:
            type_filter = st.multiselect(
                "Filtrer par type",
                df['Type'].unique(),
                default=df['Type'].unique()
            )
        
        with col2:
            min_engagement = st.slider(
                "Engagement minimum (%)",
                min_value=float(df['Taux d\'engagement (%)'].min()),
                max_value=float(df['Taux d\'engagement (%)'].max()),
                value=float(df['Taux d\'engagement (%)'].min())
            )
        
        with col3:
            sort_by = st.selectbox(
                "Trier par",
                ["Date (récent)", "Date (ancien)", "Engagement (haut)", "Engagement (bas)"]
            )
        
        # Appliquer les filtres
        filtered_df = df[df['Type'].isin(type_filter)]
        filtered_df = filtered_df[filtered_df['Taux d\'engagement (%)'] >= min_engagement]
        
        # Trier
        if sort_by == "Date (récent)":
            filtered_df = filtered_df.sort_values('Date', ascending=False)
        elif sort_by == "Date (ancien)":
            filtered_df = filtered_df.sort_values('Date', ascending=True)
        elif sort_by == "Engagement (haut)":
            filtered_df = filtered_df.sort_values('Taux d\'engagement (%)', ascending=False)
        else:
            filtered_df = filtered_df.sort_values('Taux d\'engagement (%)', ascending=True)
        
        # Afficher le tableau
        st.dataframe(filtered_df, use_container_width=True)
        
        # Export
        col1, col2 = st.columns(2)
        
        with col1:
            csv = filtered_df.to_csv(index=False, encoding='utf-8')
            st.download_button(
                "📥 Télécharger en CSV",
                csv,
                f"engagement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                "text/csv"
            )
        
        with col2:
            # Export Excel
            try:
                import openpyxl
                from openpyxl.styles import PatternFill, Font
                
                excel_buffer = pd.ExcelWriter('temp.xlsx', engine='openpyxl')
                filtered_df.to_excel(excel_buffer, index=False, sheet_name='Engagement')
                
                with open('temp.xlsx', 'rb') as f:
                    excel_data = f.read()
                
                st.download_button(
                    "📊 Télécharger en Excel",
                    excel_data,
                    f"engagement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            except:
                st.info("💡 Installez openpyxl pour l'export Excel: pip install openpyxl")
        
        # Supprimer une ligne
        st.markdown("---")
        st.subheader("🗑️ Gérer les données")
        
        if st.button("🔄 Réinitialiser l'historique", type="secondary"):
            if st.checkbox("✅ Confirmer la suppression"):
                st.session_state.historique = pd.DataFrame()
                if os.path.exists('resultats_engagement.csv'):
                    os.remove('resultats_engagement.csv')
                st.success("✅ Historique supprimé")
                st.rerun()
    
    else:
        st.info("📭 Aucun historique pour le moment.")

# ===== SECTION 5: À PROPOS =====
elif section == "ℹ️ À propos":
    st.header("À propos")
    
    st.markdown("""
    ### 📊 Calculateur d'Engagement Instagram
    
    **Version :** 2.0.0 (Streamlit)  
    **Auteur :** HANS BRAYANE HEZANGOYE  
    **Licence :** MIT
    
    ---
    
    ## 🎯 Qu'est-ce que c'est ?
    
    Un outil professionnel pour calculer et analyser le taux d'engagement de vos publications Instagram.
    
    **Formule utilisée :**
    ```
    Taux d'engagement (%) = ((Likes + Commentaires) / Nombre d'abonnés) × 100
    ```
    
    ---
    
    ## ✨ Fonctionnalités
    
    - 🧮 Calcul automatique du taux d'engagement
    - 📊 Analyse détaillée des performances
    - 📈 Graphiques interactifs
    - 💾 Historique sauvegardé automatiquement
    - 📥 Export en CSV/Excel
    - 🎯 Comparaisons par type de contenu
    - 💡 Recommandations personnalisées
    
    ---
    
    ## 🚀 Interprétation des résultats
    
    | Taux | Performance | Signification |
    |------|-------------|---------------|
    | < 1% | 🔴 Très faible | Contenu peu engageant |
    | 1-3% | 🟠 Faible | À améliorer |
    | 3-5% | 🟡 Moyen | Acceptable |
    | 5-10% | 🟢 Bon | Stratégie fonctionnelle |
    | > 10% | 🟢 Excellent | Performance exceptionnelle |
    
    ---
    
    ## 💡 Conseils pour améliorer l'engagement
    
    1. **Timing** : Publiez aux heures de peak (18h-21h généralement)
    2. **Hashtags** : Utilisez 15-30 hashtags pertinents
    3. **Contenu** : Privilégiez la qualité à la quantité
    4. **Appels à l'action** : Posez des questions, créez des défis
    5. **Interaction** : Répondez aux commentaires rapidement
    6. **Diversité** : Alternez photos, vidéos et reels
    
    ---
    
    ## 🔐 Confidentialité
    
    ✅ Tous vos données restent locales  
    ✅ Aucun upload sur des serveurs externes  
    ✅ Vous pouvez vérifier le code source  
    
    ---
    
    ## 📞 Support
    
    Des questions ? Visitez notre GitHub :
    [calculateur-engagement-instagram](https://github.com/hansbrayanehezangoye6089-cmd/calculateur-engagement-instagram)
    
    ---
    
    ## 🎓 Technologie utilisée
    
    - **Python 3.8+**
    - **Streamlit** (Interface web)
    - **Pandas** (Analyse de données)
    - **Plotly** (Visualisations)
    - **Matplotlib** (Graphiques)
    
    ---
    
    **Développé avec ❤️ pour les créateurs de contenu**
    """)
    
    # Stat personnelles
    st.markdown("---")
    st.markdown("### 👨‍💻 À propos de l'auteur")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **HANS BRAYANE HEZANGOYE**
        
        Étudiant en Communication et Médias Numériques
        
        Compétences :
        - 🐍 Python
        - 📊 Analyse de données
        - 📱 Marketing numérique
        - 🎯 Médias sociaux
        """)
    
    with col2:
        st.markdown("""
        **Liens**
        - 🔗 [GitHub](https://github.com/hansbrayanehezangoye6089-cmd)
        - 💼 [LinkedIn](https://linkedin.com/in/hans-brayane-hezangoye)
        - 📧 Email: hansbrayanehezangoye6089@gmail.com
        """)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>"
    "Calculateur d'Engagement Instagram v2.0 | Développé avec Streamlit | "
    f"{datetime.now().year}"
    "</p>",
    unsafe_allow_html=True
)
