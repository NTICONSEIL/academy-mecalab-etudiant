# Matériel et recette préalable
Uno R3 (ATmega328P), motoréducteur DC avec encodeur A/B, TB6612FNG, alimentation moteur basse tension limitée en courant, potentiomètre linéaire 10 kΩ, support rigide, protection mécanique, coupure physique de puissance, câbles et USB.

Avant achat : relever tension nominale, courant à vide et de blocage, vitesse, rapport de réduction, tension et type de sorties encodeur, comptages par tour. Vérifier les limites continues et thermiques du module de puissance (pas uniquement son courant de crête). Ne pas supposer que tout encodeur accepte 5 V. Prévoir adaptation de niveau si nécessaire. Ne pas utiliser de bras chargé pour les premiers essais.

Recette enseignant : moteur hors tension, vérifier masses et câblage ; tester potentiomètre ; tourner l'arbre à la main si mécaniquement possible, sinon procédure constructeur ; mesurer les comptages sur plusieurs tours ; vérifier sens et origine ; fixer limites de course et PWM ; tester coupure physique et arrêt logiciel ; seulement ensuite autoriser un essai à faible puissance. Aucun réglage universel de PID n'est fourni pour le matériel inconnu.
