"""
Calculateur de Taux d'Engagement Instagram - Version Interface Graphique
Auteur: HANS BRAYANE HEZANGOYE
Description: Interface GUI avec Tkinter pour calculer l'engagement et exporter en CSV
"""

import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime


class EngagementCalculatorGUI:
    """Classe pour l'interface graphique du calculateur d'engagement."""
    
    def __init__(self, root):
        """Initialise la fenêtre principale."""
        self.root = root
        self.root.title("📊 Calculateur de Taux d'Engagement Instagram")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Appliquer un thème
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crée les widgets de l'interface."""
        
        # En-tête
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        
        title = ttk.Label(header_frame, text="📊 Calculateur d'Engagement", 
                         font=("Arial", 18, "bold"))
        title.pack()
        
        subtitle = ttk.Label(header_frame, text="Calculez votre taux d'engagement Instagram",
                            font=("Arial", 10))
        subtitle.pack()
        
        # Formulaire
        form_frame = ttk.LabelFrame(self.root, text="Informations de la publication", padding=20)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Description
        ttk.Label(form_frame, text="Description (optionnel) :").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.description_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.description_var, width=40).grid(row=0, column=1, pady=5)
        
        # Likes
        ttk.Label(form_frame, text="Nombre de likes :").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.likes_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.likes_var, width=40).grid(row=1, column=1, pady=5)
        
        # Commentaires
        ttk.Label(form_frame, text="Nombre de commentaires :").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.commentaires_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.commentaires_var, width=40).grid(row=2, column=1, pady=5)
        
        # Abonnés
        ttk.Label(form_frame, text="Nombre d'abonnés :").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.abonnes_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.abonnes_var, width=40).grid(row=3, column=1, pady=5)
        
        # Résultat
        self.result_frame = ttk.LabelFrame(self.root, text="Résultat", padding=20)
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.result_label = ttk.Label(self.result_frame, text="En attente du calcul...",
                                     font=("Arial", 14, "bold"), foreground="gray")
        self.result_label.pack(pady=20)
        
        # Boutons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        ttk.Button(button_frame, text="🧮 Calculer", command=self.calculer).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="💾 Sauvegarder CSV", command=self.sauvegarder_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🔄 Réinitialiser", command=self.reinitialiser).pack(side=tk.LEFT, padx=5)
    
    def calculer(self):
        """Calcule le taux d'engagement."""
        try:
            likes = int(self.likes_var.get())
            commentaires = int(self.commentaires_var.get())
            abonnes = int(self.abonnes_var.get())
            
            if likes < 0 or commentaires < 0:
                messagebox.showerror("Erreur", "Les likes et commentaires doivent être positifs.")
                return
            
            if abonnes <= 0:
                messagebox.showerror("Erreur", "Le nombre d'abonnés doit être supérieur à 0.")
                return
            
            resultat = ((likes + commentaires) / abonnes) * 100
            
            # Stocker le résultat pour sauvegarde
            self.last_result = {
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Description": self.description_var.get() or "Sans description",
                "Likes": likes,
                "Commentaires": commentaires,
                "Abonnés": abonnes,
                "Taux d'engagement (%)": f"{resultat:.2f}"
            }
            
            # Afficher le résultat
            self.result_label.config(
                text=f"Taux d'engagement : {resultat:.2f}%",
                foreground="green"
            )
            
            messagebox.showinfo("Succès", f"Taux d'engagement calculé : {resultat:.2f}%")
            
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")
    
    def sauvegarder_csv(self):
        """Sauvegarde le résultat en CSV."""
        if not hasattr(self, 'last_result'):
            messagebox.showwarning("Attention", "Calculez d'abord un résultat.")
            return
        
        try:
            nom_fichier = "resultats_engagement.csv"
            with open(nom_fichier, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.last_result.keys())
                
                if f.tell() == 0:
                    writer.writeheader()
                
                writer.writerow(self.last_result)
            
            messagebox.showinfo("Succès", f"Résultat sauvegardé dans '{nom_fichier}'")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde : {e}")
    
    def reinitialiser(self):
        """Réinitialise tous les champs."""
        self.description_var.set("")
        self.likes_var.set("")
        self.commentaires_var.set("")
        self.abonnes_var.set("")
        self.result_label.config(text="En attente du calcul...", foreground="gray")


if __name__ == "__main__":
    root = tk.Tk()
    app = EngagementCalculatorGUI(root)
    root.mainloop()
