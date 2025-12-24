from manim import *
import numpy as np

class ZoomRadiographieIntro(Scene):
    """Introduction au projet"""
    def construct(self):
        # Titre principal
        titre = Text("Zoom d'Images Radiographiques", font_size=48, weight=BOLD)
        titre.set_color_by_gradient(BLUE, GREEN)
        sous_titre = Text("Application de l'Algèbre Linéaire", font_size=32)
        sous_titre.next_to(titre, DOWN)
        
        # Mention images en niveaux de gris
        note_gris = Text("(Images en niveaux de gris)", font_size=24, color=GRAY)
        note_gris.next_to(sous_titre, DOWN, buff=0.3)
        
        self.play(Write(titre))
        self.play(FadeIn(sous_titre))
        self.play(FadeIn(note_gris))
        self.wait(2)
        self.play(FadeOut(titre), FadeOut(sous_titre), FadeOut(note_gris))

class ProblématiqueRadiographique(Scene):
    """Présentation de la problématique des images radiographiques"""
    def construct(self):
        # Titre
        titre = Text("Problématique : Images Radiographiques", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Contexte médical
        contexte = VGroup(
            Text("🏥 Contexte Médical", font_size=32, color=BLUE),
            Text("• Analyse de radiographies pour diagnostic", font_size=24),
            Text("• Nécessité de zoomer sur des détails", font_size=24),
            Text("• Images en niveaux de gris uniquement", font_size=24)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        contexte.shift(UP * 1)
        
        for elem in contexte:
            self.play(FadeIn(elem, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(1)
        
        # Problème
        probleme = VGroup(
            Text("⚠️ Problème", font_size=32, color=RED),
            Text("Comment agrandir une image", font_size=24),
            Text("pour mieux voir les détails ?", font_size=24)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        probleme.shift(DOWN * 1.5)
        
        for elem in probleme:
            self.play(FadeIn(elem, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(2)

class RGBvsNiveauxGris(Scene):
    """Différence entre images RGB et niveaux de gris"""
    def construct(self):
        # Titre
        titre = Text("RGB vs Niveaux de Gris", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Partie gauche: RGB
        rgb_titre = Text("Image RGB (Couleur)", font_size=28, color=BLUE)
        rgb_titre.shift(UP * 2 + LEFT * 3.5)
        
        # Créer 3 petites matrices pour R, G, B
        matrices_rgb = VGroup()
        couleurs = [RED, GREEN, BLUE]
        labels = ["R", "G", "B"]
        
        for idx, (couleur, label) in enumerate(zip(couleurs, labels)):
            grille = VGroup()
            for i in range(3):
                for j in range(3):
                    carre = Square(side_length=0.25)
                    carre.set_fill(couleur, opacity=0.3 + (i+j)*0.1)
                    carre.set_stroke(couleur, width=1)
                    carre.move_to([j * 0.25, -i * 0.25, 0])
                    grille.add(carre)
            
            label_text = Text(label, font_size=20, color=couleur)
            label_text.next_to(grille, UP, buff=0.2)
            
            grille_complete = VGroup(label_text, grille)
            grille_complete.shift(DOWN * idx * 1.2)
            matrices_rgb.add(grille_complete)
        
        matrices_rgb.next_to(rgb_titre, DOWN, buff=0.4)
        matrices_rgb.shift(LEFT * 3.5)
        
        self.play(Write(rgb_titre))
        self.play(FadeIn(matrices_rgb))
        
        # Formule RGB
        formule_rgb = MathTex(r"I_{RGB} \in \mathbb{R}^{n \times n \times 3}", font_size=24)
        formule_rgb.next_to(matrices_rgb, DOWN, buff=0.3)
        self.play(Write(formule_rgb))
        
        self.wait(1)
        
        # Partie droite: Niveaux de gris
        gris_titre = Text("Image en Niveaux de Gris", font_size=28, color=GREEN)
        gris_titre.shift(UP * 2 + RIGHT * 3.5)
        
        # Une seule matrice en niveaux de gris
        grille_gris = VGroup()
        for i in range(4):
            for j in range(4):
                valeur = (i + j) / 6
                carre = Square(side_length=0.4)
                carre.set_fill(WHITE, opacity=valeur)
                carre.set_stroke(GRAY, width=1.5)
                carre.move_to([j * 0.4, -i * 0.4, 0])
                grille_gris.add(carre)
        
        grille_gris.next_to(gris_titre, DOWN, buff=0.4)
        grille_gris.shift(RIGHT * 3.5)
        
        self.play(Write(gris_titre))
        self.play(FadeIn(grille_gris))
        
        # Formule niveaux de gris
        formule_gris = MathTex(r"I_{Gris} \in \mathbb{R}^{n \times n}", font_size=24)
        formule_gris.next_to(grille_gris, DOWN, buff=0.3)
        self.play(Write(formule_gris))
        
        # Conversion
        conversion = MathTex(
            r"Gris = 0.299R + 0.587G + 0.114B",
            font_size=24,
            color=YELLOW
        )
        conversion.next_to(formule_gris, DOWN, buff=0.5)
        self.play(Write(conversion))
        
        self.wait(1)
        
        # Conclusion pour radiographies
        conclusion = VGroup(
            Text("📌 Images Radiographiques", font_size=28, weight=BOLD, color=ORANGE),
            Text("→ Toujours en Niveaux de Gris", font_size=24)
        ).arrange(DOWN, buff=0.2)
        conclusion.to_edge(DOWN, buff=0.5)
        
        box_conclusion = SurroundingRectangle(conclusion, color=ORANGE, buff=0.2)
        self.play(Create(box_conclusion), Write(conclusion))
        self.wait(2)

class DefautsZoomNaturel(Scene):
    """Démonstration des défauts du zoom naturel par interpolation"""
    def construct(self):
        # Titre
        titre = Text("Problème du Zoom Naturel", font_size=40, color=RED)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Sous-titre explicatif
        sous_titre = Text("(Étirement par interpolation)", font_size=28)
        sous_titre.next_to(titre, DOWN)
        self.play(FadeIn(sous_titre))
        
        # Image originale 4x4
        original_label = Text("Image Originale 4×4", font_size=24, color=BLUE)
        original_label.shift(UP * 1.5 + LEFT * 4)
        
        grille_orig = VGroup()
        n = 4
        taille = 0.5
        for i in range(n):
            for j in range(n):
                valeur = 0.3 + (i + j) / (2 * n) * 0.6
                carre = Square(side_length=taille)
                carre.set_fill(WHITE, opacity=valeur)
                carre.set_stroke(BLUE, width=2)
                carre.move_to([j * taille, -i * taille, 0])
                grille_orig.add(carre)
        
        grille_orig.next_to(original_label, DOWN, buff=0.3)
        grille_orig.shift(LEFT * 4)
        
        self.play(Write(original_label))
        self.play(Create(grille_orig))
        
        # Info pixels
        info_orig = Text("16 pixels", font_size=20, color=BLUE)
        info_orig.next_to(grille_orig, DOWN, buff=0.2)
        self.play(Write(info_orig))
        
        self.wait(1)
        
        # Flèche
        fleche = Arrow(LEFT * 1.5, RIGHT * 0.5, color=RED, stroke_width=6)
        label_fleche = Text("Zoom Naturel ×2", font_size=24, color=RED)
        label_fleche.next_to(fleche, UP)
        self.play(Create(fleche), Write(label_fleche))
        
        # Zoom naturel (étirement avec flou)
        zoom_label = Text("Zoom Naturel 8×8", font_size=24, color=RED)
        zoom_label.shift(UP * 1.5 + RIGHT * 3.5)
        
        # Créer une grille "étirée" avec effet flou (même pixels, juste étiré)
        grille_zoom = VGroup()
        for i in range(n):
            for j in range(n):
                valeur = 0.3 + (i + j) / (2 * n) * 0.6
                # Carré plus grand pour simuler l'étirement
                carre = Square(side_length=taille)
                carre.set_fill(WHITE, opacity=valeur)
                carre.set_stroke(RED, width=1, opacity=0.3)  # Contours flous
                carre.move_to([j * taille, -i * taille, 0])
                grille_zoom.add(carre)
        
        grille_zoom.next_to(zoom_label, DOWN, buff=0.3)
        grille_zoom.shift(RIGHT * 3.5)
        
        self.play(Write(zoom_label))
        self.play(Transform(grille_orig.copy(), grille_zoom))
        self.play(FadeIn(grille_zoom))
        
        # Info pixels (même nombre!)
        info_zoom = Text("Toujours 16 pixels!", font_size=20, color=RED, weight=BOLD)
        info_zoom.next_to(grille_zoom, DOWN, buff=0.2)
        self.play(Write(info_zoom))
        
        self.wait(1)
        
        # Défauts listés
        defauts = VGroup(
            Text("❌ Défauts du Zoom Naturel:", font_size=26, color=RED, weight=BOLD),
            Text("• Pas de nouveaux pixels créés", font_size=22),
            Text("• Interpolation floue entre pixels", font_size=22),
            Text("• Perte de netteté", font_size=22),
            Text("• Difficile d'analyser les détails", font_size=22)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        defauts.to_edge(DOWN, buff=0.5)
        
        for defaut in defauts:
            self.play(FadeIn(defaut, shift=UP))
            self.wait(0.4)
        
        self.wait(2)

class ComparaisonZoomMethods(Scene):
    """Comparaison entre zoom naturel et zoom par duplication"""
    def construct(self):
        # Titre
        titre = Text("Comparaison des Méthodes de Zoom", font_size=38)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Gauche: Zoom Naturel (mauvais)
        label_naturel = Text("Zoom Naturel", font_size=28, color=RED)
        label_naturel.shift(UP * 2.2 + LEFT * 4)
        
        # Droite: Notre Méthode (bon)
        label_notre = Text("Notre Méthode", font_size=28, color=GREEN)
        label_notre.shift(UP * 2.2 + RIGHT * 3.5)
        
        self.play(Write(label_naturel), Write(label_notre))
        
        # Image originale commune (petite au centre)
        img_orig_center = self.creer_mini_grille(2, 0.3, UP * 0.5)
        label_orig = Text("Original 2×2", font_size=18)
        label_orig.next_to(img_orig_center, DOWN, buff=0.1)
        self.play(FadeIn(img_orig_center), Write(label_orig))
        self.wait(1)
        
        # Zoom naturel (gauche)
        grille_naturel = self.creer_mini_grille(2, 0.6, UP * 0.3 + LEFT * 4)
        info_naturel = VGroup(
            Text("Affichage 4×4", font_size=20),
            Text("4 pixels (étirés)", font_size=18, color=RED)
        ).arrange(DOWN, buff=0.1)
        info_naturel.next_to(grille_naturel, DOWN, buff=0.3)
        
        fleche_g = Arrow(img_orig_center.get_left(), grille_naturel.get_right(), 
                        color=RED, stroke_width=3, buff=0.2)
        
        self.play(Create(fleche_g))
        self.play(FadeIn(grille_naturel), Write(info_naturel))
        
        # Défauts zoom naturel
        defauts_nat = VGroup(
            Text("❌ Flou", font_size=20, color=RED),
            Text("❌ Interpolation", font_size=20, color=RED),
            Text("❌ Pas de pixels réels", font_size=20, color=RED)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        defauts_nat.next_to(info_naturel, DOWN, buff=0.4)
        
        for d in defauts_nat:
            self.play(FadeIn(d))
            self.wait(0.3)
        
        self.wait(1)
        
        # Notre méthode (droite)
        grille_notre = self.creer_grille_dupliquee(2, 0.3, UP * 0.3 + RIGHT * 3.5)
        info_notre = VGroup(
            Text("Image 4×4", font_size=20),
            Text("16 pixels réels", font_size=18, color=GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.1)
        info_notre.next_to(grille_notre, DOWN, buff=0.3)
        
        fleche_d = Arrow(img_orig_center.get_right(), grille_notre.get_left(),
                        color=GREEN, stroke_width=3, buff=0.2)
        
        self.play(Create(fleche_d))
        self.play(FadeIn(grille_notre), Write(info_notre))
        
        # Avantages notre méthode
        avantages = VGroup(
            Text("✅ Pixels nets", font_size=20, color=GREEN),
            Text("✅ Vrais nouveaux pixels", font_size=20, color=GREEN),
            Text("✅ 4× plus de pixels", font_size=20, color=GREEN)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        avantages.next_to(info_notre, DOWN, buff=0.4)
        
        for a in avantages:
            self.play(FadeIn(a))
            self.wait(0.3)
        
        self.wait(1)
        
        # Formules comparatives
        formules = VGroup(
            MathTex(r"\text{Naturel: } \mathbb{R}^{n \times n} \rightarrow \text{affichage flou}", 
                   font_size=24, color=RED),
            MathTex(r"\text{Notre: } \mathbb{R}^{n \times n} \rightarrow \mathbb{R}^{2n \times 2n}",
                   font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.3)
        formules.to_edge(DOWN, buff=0.5)
        
        self.play(Write(formules))
        self.wait(3)
    
    def creer_mini_grille(self, n, taille, position):
        grille = VGroup()
        for i in range(n):
            for j in range(n):
                valeur = 0.4 + (i + j) / (2 * n) * 0.5
                carre = Square(side_length=taille)
                carre.set_fill(WHITE, opacity=valeur)
                carre.set_stroke(BLUE, width=2)
                carre.move_to([j * taille, -i * taille, 0])
                grille.add(carre)
        grille.move_to(position)
        return grille
    
    def creer_grille_dupliquee(self, n_orig, taille, position):
        """Créer une grille 2n×2n avec duplication visible"""
        grille = VGroup()
        for i in range(n_orig):
            for j in range(n_orig):
                valeur = 0.4 + (i + j) / (2 * n_orig) * 0.5
                # Créer bloc 2×2
                for di in range(2):
                    for dj in range(2):
                        carre = Square(side_length=taille)
                        carre.set_fill(WHITE, opacity=valeur)
                        carre.set_stroke(GREEN, width=1.5)
                        carre.move_to([(2*j + dj) * taille, -(2*i + di) * taille, 0])
                        grille.add(carre)
        grille.move_to(position)
        return grille

class ConceptImage(Scene):
    """Concept de base : image comme matrice"""
    def construct(self):
        # Titre
        titre = Text("Image = Matrice de Pixels", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Note sur niveaux de gris
        note_gris = Text("(Image radiographique en niveaux de gris)", font_size=24, color=YELLOW)
        note_gris.next_to(titre, DOWN, buff=0.2)
        self.play(FadeIn(note_gris))
        
        # Création d'une petite image 4x4
        matrice_values = np.array([
            [0.9, 0.7, 0.3, 0.1],
            [0.8, 0.5, 0.4, 0.2],
            [0.6, 0.4, 0.6, 0.3],
            [0.2, 0.3, 0.5, 0.8]
        ])
        
        # Créer la grille visuelle
        grille = VGroup()
        taille_cellule = 0.8
        
        for i in range(4):
            for j in range(4):
                valeur = matrice_values[i][j]
                carre = Square(side_length=taille_cellule)
                carre.set_fill(WHITE, opacity=valeur)
                carre.set_stroke(BLUE, width=2)
                carre.move_to([j * taille_cellule, -i * taille_cellule, 0])
                
                # Ajouter la valeur numérique
                texte = Text(f"{valeur:.1f}", font_size=20)
                texte.move_to(carre.get_center())
                texte.set_color(RED if valeur < 0.5 else BLACK)
                
                grille.add(carre, texte)
        
        grille.move_to(ORIGIN)
        self.play(Create(grille), run_time=2)
        
        # Ajouter indices
        label_i = Text("i (lignes)", font_size=24, color=YELLOW)
        label_i.next_to(grille, LEFT)
        label_j = Text("j (colonnes)", font_size=24, color=YELLOW)
        label_j.next_to(grille, DOWN)
        
        self.play(Write(label_i), Write(label_j))
        self.wait(2)
        
        # Explication intensité
        explication = Text(
            "Chaque pixel = intensité (niveau de gris)",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(explication))
        self.wait(2)

class TransformationLineaire(Scene):
    """Présentation de la transformation linéaire"""
    def construct(self):
        # Titre
        titre = Text("Transformation Linéaire f : ℝⁿ² → ℝ⁴ⁿ²", font_size=36)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Espaces vectoriels
        espace_depart = VGroup(
            Text("Espace de départ", font_size=28, color=BLUE),
            Text("ℝⁿ²", font_size=32, weight=BOLD),
            Text("Image n×n", font_size=24)
        ).arrange(DOWN, buff=0.3)
        espace_depart.shift(LEFT * 4)
        
        espace_arrivee = VGroup(
            Text("Espace d'arrivée", font_size=28, color=GREEN),
            Text("ℝ⁴ⁿ²", font_size=32, weight=BOLD),
            Text("Image 2n×2n", font_size=24)
        ).arrange(DOWN, buff=0.3)
        espace_arrivee.shift(RIGHT * 4)
        
        # Flèche de transformation
        fleche = Arrow(
            espace_depart.get_right(),
            espace_arrivee.get_left(),
            buff=0.3,
            color=YELLOW,
            stroke_width=6
        )
        label_fleche = Text("f (zoom ×2)", font_size=28, color=YELLOW)
        label_fleche.next_to(fleche, UP)
        
        self.play(FadeIn(espace_depart))
        self.wait()
        self.play(Create(fleche), Write(label_fleche))
        self.wait()
        self.play(FadeIn(espace_arrivee))
        self.wait(2)
        
        # Formule mathématique
        formule = MathTex(
            r"f(I)[2i:2i+2, 2j:2j+2] = \begin{bmatrix} I[i,j] & I[i,j] \\ I[i,j] & I[i,j] \end{bmatrix}",
            font_size=32
        ).to_edge(DOWN)
        
        box_formule = SurroundingRectangle(formule, color=RED, buff=0.2)
        self.play(Write(formule))
        self.play(Create(box_formule))
        self.wait(3)

class ProcessusZoom(Scene):
    """Animation du processus de zoom détaillé"""
    def construct(self):
        titre = Text("Processus de Zoom ×2", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Image originale 3x3
        original = self.creer_grille(3, 0.6, LEFT * 3.5, "Image Originale")
        self.play(Create(original))
        self.wait()
        
        # Sélectionner un pixel
        i, j = 1, 1
        pixel_origine = original[i * 3 + j]
        highlight = SurroundingRectangle(pixel_origine, color=YELLOW, stroke_width=4)
        label_pixel = Text(f"Pixel I[{i},{j}]", font_size=24, color=YELLOW)
        label_pixel.next_to(pixel_origine, DOWN, buff=0.5)
        
        self.play(Create(highlight), Write(label_pixel))
        self.wait()
        
        # Image zoomée 6x6
        zoomee = self.creer_grille(6, 0.4, RIGHT * 3, "Image Zoomée")
        self.play(Create(zoomee))
        
        # Montrer le bloc 2x2 correspondant
        blocs = VGroup()
        for di in range(2):
            for dj in range(2):
                idx = (2*i + di) * 6 + (2*j + dj)
                bloc = zoomee[idx]
                rect = SurroundingRectangle(bloc, color=YELLOW, stroke_width=3)
                blocs.add(rect)
        
        self.play(Create(blocs))
        
        # Flèche de transformation
        fleche = Arrow(
            pixel_origine.get_right(),
            blocs.get_left(),
            color=RED,
            stroke_width=4,
            buff=0.2
        )
        self.play(Create(fleche))
        
        # Formule explicite
        formule = MathTex(
            r"I[1,1] \rightarrow \begin{bmatrix} I[1,1] & I[1,1] \\ I[1,1] & I[1,1] \end{bmatrix}",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(formule))
        self.wait(3)
        
        # Nettoyer et montrer tous les pixels
        self.play(
            FadeOut(highlight), 
            FadeOut(label_pixel),
            FadeOut(blocs),
            FadeOut(fleche),
            FadeOut(formule)
        )
        
        # Animation de tous les pixels
        self.animer_tous_pixels(original, zoomee)
        self.wait(2)
    
    def creer_grille(self, n, taille, position, label):
        grille = VGroup()
        
        for i in range(n):
            for j in range(n):
                valeur = (i + j) / (2 * n)
                carre = Square(side_length=taille)
                carre.set_fill(WHITE, opacity=0.3 + valeur * 0.7)
                carre.set_stroke(BLUE, width=1.5)
                carre.move_to([j * taille, -i * taille, 0])
                grille.add(carre)
        
        grille.move_to(position)
        
        # Ajouter label
        texte_label = Text(label, font_size=24)
        texte_label.next_to(grille, DOWN, buff=0.3)
        grille.add(texte_label)
        
        return grille
    
    def animer_tous_pixels(self, original, zoomee):
        n_orig = 3
        animations = []
        
        for i in range(n_orig):
            for j in range(n_orig):
                pixel_orig = original[i * n_orig + j]
                
                # Bloc 2x2 correspondant
                for di in range(2):
                    for dj in range(2):
                        idx = (2*i + di) * 6 + (2*j + dj)
                        pixel_zoom = zoomee[idx]
                        
                        fleche = Arrow(
                            pixel_orig.get_center(),
                            pixel_zoom.get_center(),
                            color=YELLOW,
                            stroke_width=2,
                            buff=0.1,
                            max_tip_length_to_length_ratio=0.1
                        )
                        animations.append(fleche)
        
        self.play(*[Create(a) for a in animations], run_time=2)
        self.wait()
        self.play(*[FadeOut(a) for a in animations])

class MatriceTransformation(Scene):
    """Représentation matricielle"""
    def construct(self):
        titre = Text("Représentation Matricielle", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Explication
        explication = VGroup(
            Text("Pour un zoom ×2 d'une image 2×2 → 4×4", font_size=28),
            Text("On peut représenter f comme une matrice", font_size=28)
        ).arrange(DOWN, buff=0.3)
        explication.next_to(titre, DOWN, buff=0.5)
        
        self.play(Write(explication))
        self.wait(2)
        
        # Vecteur image original
        vec_original = MathTex(
            r"\vec{v} = \begin{bmatrix} I[0,0] \\ I[0,1] \\ I[1,0] \\ I[1,1] \end{bmatrix}",
            font_size=32
        )
        vec_original.shift(LEFT * 4)
        
        # Matrice de transformation (simplifiée pour l'exemple)
        matrice = MathTex(
            r"M_{4 \times 16}",
            font_size=36
        )
        matrice.next_to(vec_original, RIGHT, buff=1)
        
        # Vecteur résultat
        vec_result = MathTex(
            r"\vec{w} = \begin{bmatrix} I[0,0] \\ I[0,0] \\ I[0,1] \\ I[0,1] \\ \vdots \\ I[1,1] \end{bmatrix}",
            font_size=32
        )
        vec_result.next_to(matrice, RIGHT, buff=1)
        
        # Symboles
        fois = MathTex(r"\times", font_size=40)
        fois.move_to((vec_original.get_right() + matrice.get_left()) / 2)
        
        egal = MathTex(r"=", font_size=40)
        egal.move_to((matrice.get_right() + vec_result.get_left()) / 2)
        
        self.play(Write(vec_original))
        self.wait()
        self.play(Write(fois), Write(matrice))
        self.wait()
        self.play(Write(egal), Write(vec_result))
        self.wait(3)

class ProprietesLineaires(Scene):
    """Vérification des propriétés linéaires"""
    def construct(self):
        titre = Text("Propriétés de Linéarité", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Propriété 1: Additivité
        prop1_titre = Text("1. Additivité", font_size=32, color=BLUE)
        prop1_titre.shift(UP * 2)
        
        prop1 = MathTex(
            r"f(I_1 + I_2) = f(I_1) + f(I_2)",
            font_size=36
        )
        prop1.next_to(prop1_titre, DOWN)
        
        self.play(Write(prop1_titre))
        self.play(Write(prop1))
        self.wait(2)
        
        # Démonstration visuelle
        demo1 = VGroup(
            MathTex(r"f(I_1 + I_2)[2i,2j] = (I_1 + I_2)[i,j]", font_size=28),
            MathTex(r"= I_1[i,j] + I_2[i,j]", font_size=28),
            MathTex(r"= f(I_1)[2i,2j] + f(I_2)[2i,2j]", font_size=28)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        demo1.next_to(prop1, DOWN, buff=0.5)
        
        for line in demo1:
            self.play(Write(line))
            self.wait()
        
        checkmark1 = Text("✓", font_size=48, color=GREEN)
        checkmark1.next_to(demo1, RIGHT)
        self.play(FadeIn(checkmark1, scale=2))
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != titre])
        
        # Propriété 2: Homogénéité
        prop2_titre = Text("2. Homogénéité", font_size=32, color=BLUE)
        prop2_titre.shift(UP * 2)
        
        prop2 = MathTex(
            r"f(\lambda \cdot I) = \lambda \cdot f(I)",
            font_size=36
        )
        prop2.next_to(prop2_titre, DOWN)
        
        self.play(Write(prop2_titre))
        self.play(Write(prop2))
        self.wait(2)
        
        demo2 = VGroup(
            MathTex(r"f(\lambda I)[2i,2j] = (\lambda I)[i,j]", font_size=28),
            MathTex(r"= \lambda \cdot I[i,j]", font_size=28),
            MathTex(r"= \lambda \cdot f(I)[2i,2j]", font_size=28)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        demo2.next_to(prop2, DOWN, buff=0.5)
        
        for line in demo2:
            self.play(Write(line))
            self.wait()
        
        checkmark2 = Text("✓", font_size=48, color=GREEN)
        checkmark2.next_to(demo2, RIGHT)
        self.play(FadeIn(checkmark2, scale=2))
        self.wait(3)

class NoyauImage(Scene):
    """Analyse du noyau et de l'image"""
    def construct(self):
        titre = Text("Noyau et Image de f", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Noyau
        noyau_titre = Text("Noyau de f : Ker(f)", font_size=32, color=RED)
        noyau_titre.shift(UP * 1.5 + LEFT * 3)
        
        noyau_def = MathTex(
            r"\text{Ker}(f) = \{ I \in \mathbb{R}^{n^2} : f(I) = 0 \}",
            font_size=28
        )
        noyau_def.next_to(noyau_titre, DOWN, buff=0.3)
        
        noyau_result = VGroup(
            MathTex(r"f(I) = 0 \Rightarrow I[i,j] = 0 \; \forall i,j", font_size=24),
            MathTex(r"\text{Ker}(f) = \{ 0 \}", font_size=28, color=RED)
        ).arrange(DOWN, buff=0.3)
        noyau_result.next_to(noyau_def, DOWN, buff=0.4)
        
        self.play(Write(noyau_titre))
        self.play(Write(noyau_def))
        self.wait()
        self.play(Write(noyau_result))
        
        # Conclusion : injective
        injective = Text("f est injective", font_size=28, color=GREEN)
        injective.next_to(noyau_result, DOWN, buff=0.4)
        box_inj = SurroundingRectangle(injective, color=GREEN)
        self.play(Write(injective), Create(box_inj))
        self.wait(2)
        
        # Image
        image_titre = Text("Image de f : Im(f)", font_size=32, color=BLUE)
        image_titre.shift(UP * 1.5 + RIGHT * 3)
        
        image_def = MathTex(
            r"\text{Im}(f) = \{ f(I) : I \in \mathbb{R}^{n^2} \}",
            font_size=28
        )
        image_def.next_to(image_titre, DOWN, buff=0.3)
        
        image_desc = VGroup(
            Text("Images avec blocs 2×2", font_size=22),
            Text("de pixels identiques", font_size=22),
            MathTex(r"\dim(\text{Im}(f)) = n^2", font_size=26, color=BLUE)
        ).arrange(DOWN, buff=0.2)
        image_desc.next_to(image_def, DOWN, buff=0.4)
        
        self.play(Write(image_titre))
        self.play(Write(image_def))
        self.wait()
        self.play(Write(image_desc))
        self.wait(2)
        
        # Conclusion : non surjective
        surjective = Text("f n'est pas surjective", font_size=28, color=ORANGE)
        surjective.next_to(image_desc, DOWN, buff=0.4)
        box_surj = SurroundingRectangle(surjective, color=ORANGE)
        self.play(Write(surjective), Create(box_surj))
        self.wait(3)

class ApplicationPratique(Scene):
    """Application pratique avec image médicale simulée"""
    def construct(self):
        titre = Text("Application Pratique", font_size=40)
        titre.to_edge(UP)
        self.play(Write(titre))
        
        # Créer une "radiographie" simulée (image avec structure)
        n = 4
        radio_data = self.creer_radiographie(n)
        
        # Image originale
        radio_orig = self.afficher_image(radio_data, 0.7, LEFT * 3.5)
        label_orig = Text(f"Radiographie {n}×{n}", font_size=24)
        label_orig.next_to(radio_orig, DOWN)
        
        self.play(FadeIn(radio_orig), Write(label_orig))
        self.wait()
        
        # Flèche de zoom
        fleche = Arrow(LEFT * 1, RIGHT * 1, color=YELLOW, stroke_width=6)
        label_zoom = Text("Zoom ×2", font_size=28, color=YELLOW)
        label_zoom.next_to(fleche, UP)
        
        self.play(Create(fleche), Write(label_zoom))
        self.wait()
        
        # Image zoomée
        radio_zoom_data = self.appliquer_zoom(radio_data)
        radio_zoom = self.afficher_image(radio_zoom_data, 0.35, RIGHT * 3.5)
        label_zoom_img = Text(f"Radiographie {2*n}×{2*n}", font_size=24)
        label_zoom_img.next_to(radio_zoom, DOWN)
        
        self.play(FadeIn(radio_zoom), Write(label_zoom_img))
        self.wait(2)
        
        # Avantages
        avantages = VGroup(
            Text("✓ Conservation de l'information", font_size=24, color=GREEN),
            Text("✓ Visualisation de détails", font_size=24, color=GREEN),
            Text("✓ Transformation linéaire", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        avantages.to_edge(DOWN, buff=0.5)
        
        self.play(Write(avantages))
        self.wait(3)
    
    def creer_radiographie(self, n):
        """Créer une image simulant une radiographie"""
        image = np.random.rand(n, n) * 0.3 + 0.3
        # Ajouter une "structure" (zone plus claire au centre)
        centre = n // 2
        for i in range(n):
            for j in range(n):
                dist = np.sqrt((i - centre)**2 + (j - centre)**2)
                image[i, j] += 0.3 * np.exp(-dist / 2)
        return np.clip(image, 0, 1)
    
    def appliquer_zoom(self, image):
        """Appliquer le zoom ×2"""
        n = image.shape[0]
        zoom = np.zeros((2*n, 2*n))
        for i in range(n):
            for j in range(n):
                zoom[2*i:2*i+2, 2*j:2*j+2] = image[i, j]
        return zoom
    
    def afficher_image(self, data, taille, position):
        """Afficher une image comme grille de carrés"""
        n = data.shape[0]
        grille = VGroup()
        
        for i in range(n):
            for j in range(n):
                carre = Square(side_length=taille)
                carre.set_fill(WHITE, opacity=data[i, j])
                carre.set_stroke(BLUE_D, width=0.5)
                carre.move_to([j * taille, -i * taille, 0])
                grille.add(carre)
        
        grille.move_to(position)
        return grille

class Conclusion(Scene):
    """Conclusion du projet"""
    def construct(self):
        titre = Text("Conclusion", font_size=48, weight=BOLD)
        titre.set_color_by_gradient(BLUE, GREEN)
        self.play(Write(titre))
        self.wait()
        self.play(titre.animate.to_edge(UP))
        
        points = VGroup(
            Text("• Images radiographiques en niveaux de gris", font_size=26),
            Text("• Zoom naturel = interpolation floue (défaut)", font_size=26),
            Text("• Notre méthode = duplication de pixels (nette)", font_size=26),
            Text("• Le zoom par duplication est une transformation linéaire", font_size=26),
            Text("• f : ℝⁿ² → ℝ⁴ⁿ² est injective mais pas surjective", font_size=26),
            Text("• Quadruple le nombre de pixels réels", font_size=26),
            Text("• Application en imagerie médicale", font_size=26)
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        points.shift(DOWN * 0.5)
        
        for point in points:
            self.play(FadeIn(point, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(2)
        
        merci = Text("Merci !", font_size=60, weight=BOLD)
        merci.set_color_by_gradient(YELLOW, RED)
        self.play(
            FadeOut(points),
            Transform(titre, merci)
        )
        self.wait(2)

class ToutesLesScenes(Scene):
    """Classe pour générer toutes les scènes en une seule fois"""
    def construct(self):
        # Liste de toutes les scènes dans l'ordre
        scenes = [
            ZoomRadiographieIntro(self.renderer),
            ProblématiqueRadiographique(self.renderer),
            RGBvsNiveauxGris(self.renderer),
            ConceptImage(self.renderer),
            DefautsZoomNaturel(self.renderer),
            ComparaisonZoomMethods(self.renderer),
            TransformationLineaire(self.renderer),
            ProcessusZoom(self.renderer),
            MatriceTransformation(self.renderer),
            ProprietesLineaires(self.renderer),
            NoyauImage(self.renderer),
            ApplicationPratique(self.renderer),
            Conclusion(self.renderer)
        ]
        
        # Exécuter chaque scène
        for scene in scenes:
            scene.construct()
            self.wait(1)
            self.clear()  # Nettoyer entre chaque scène