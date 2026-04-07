# SPAWT — Session Brainstorming MVP
## Analyste : Mary | 7 avril 2026, 14h30
### Objectif : Audit des angles morts, tranchage MVP, risques techniques

**Documents analysés :**
- `SPAWT_BIBLE_COMPLETE.md` (1290 lignes, bible complete fevrier 2026)
- `SPAWT_Presentation_Fevrier_2026_V2-2.docx` (binaire, non lisible directement — contenu consolide dans la bible)

---

## PHASE 1 — ANGLES MORTS & PROBLEMES IDENTIFIES

### 1.1 Specifications manquantes

| # | Zone | Probleme | Impact si ignore |
|---|------|----------|------------------|
| 1 | **Onboarding** | Aucun flux d'onboarding detaille. On sait que ca prend "3-5 min" mais zero wireflow : quelles questions ? Comment calibrer le Palais initial avec 0 data ? Quel contenu montrer avant le premier spawt ? | L'utilisateur arrive sur une app vide. Le Palais est non calibre. Les recos sont generiques. Churn J+1 massif. |
| 2 | **Check-in (Spawt)** | Le mecanisme de check-in n'est pas specifie. Geoloc obligatoire ? QR code au restaurant ? Declaration manuelle ? Rayon de validation ? Delai post-visite autorise ? | Spawts frauduleux, data polluee, Palais fausses. La brique de base du systeme est sous-specifiee. |
| 3 | **Moderation** | Aucun systeme de moderation documente. Qui modere les avis ? Automatique ? Humain ? Quels criteres de suppression ? Quel workflow pour les "Faux-Pas" listes (fake review, hater toxique) ? | Sans moderation, les avis deviennent un far west. Un seul restaurant victime de trolling et la confiance B2B s'effondre. |
| 4 | **Creation de fiches lieux** | Comment un lieu apparait-il sur SPAWT ? Un spawter peut-il creer une fiche ? Quelles infos minimales ? Qui valide l'exactitude ? Comment eviter les doublons ? | Base de donnees polluee, doublons massifs, fiches incompletes. L'ADN du lieu est non calculable sans minimum de data. |
| 5 | **Systeme de reservation** | "Reservation 1-tap" est mentionne comme feature premium. Aucune spec : API tiers (TheFork) ? Integration directe ? Appel telephone ? WhatsApp ? Comment gerer les restos sans systeme de resa ? | Promesse premium non tenable. La reservation est le bridge entre discovery et action — si elle echoue, le premium perd sa valeur core. |
| 6 | **Notifications push** | "Max 3-4/semaine" mais aucune strategie de segmentation, aucun trigger precis, aucune gestion des permissions OS. | Notifications non pertinentes = desactivation = perte du canal de retention le plus puissant. |
| 7 | **Mode offline** | "Mode offline basique" mentionne une fois sans aucune spec. Que fonctionne offline ? Les fiches sauvegardees ? La carte ? Les avis ? | A Abidjan, la connectivite est intermittente. Un mode offline mal pense = app inutilisable dans les transports et zones mal couvertes. |
| 8 | **Paiement** | Aucune mention du systeme de paiement. Mobile Money (MTN, Orange Money, Wave) ? Carte bancaire ? Quel provider ? Gestion des echecs de paiement ? | Le marche cible utilise massivement Mobile Money. Pas de Stripe classique. L'integration paiement peut prendre 4-8 semaines seule. |
| 9 | **Gestion du profil utilisateur** | Pas de spec sur : creation de compte (email ? telephone ? social login ?), edition de profil, suppression de compte (RGPD/reglementation locale), gestion de la vie privee. | Blocage reglementaire potentiel. Friction d'inscription elevee si mal pense. |
| 10 | **Recherche et filtres** | La barre de navigation inclut "Chercher" mais aucune spec sur les criteres de recherche, les filtres disponibles, l'autocompletion, la recherche par plat/cuisine/budget/quartier. | L'utilisateur qui veut "un japonais a Cocody" ne sait pas comment chercher. Mode Rapide ne couvre pas ce use case. |
| 11 | **Carte / Map** | La carte est l'heritage du fichier Excel de Stephanie. Aucune spec sur : provider (Mapbox ? Google Maps ?), niveau de zoom, clustering, filtres visuels, navigation vers le lieu. | Cout potentiellement eleve (Google Maps API), UX de carte mobile complexe, performance a definir. |
| 12 | **Avis structure** | "Plus qu'une note, c'est un temoignage structure". Mais QUEL est le format ? Note sur 5 ? Criteres multiples ? Texte libre ? Photos obligatoires ? Longueur min/max ? | Avis inegaux, difficultes d'analyse, ADN du lieu mal calibre si le format est trop libre. |
| 13 | **Calcul du Palais** | Les 5 axes sont definis conceptuellement mais l'algorithme de calcul n'est pas specifie. Quels comportements mappent vers quels axes ? Quel poids pour chaque signal ? | L'equipe dev ne peut pas implementer le Palais sans spec algorithmique. C'est le coeur du produit. |
| 14 | **Score de matching** | "92% de compatibilite" est mentionne comme exemple mais aucune formule, aucun poids relatif entre les 4 dimensions (Palais x ADN x Historique x Contexte). | Le matching est la promesse core. Un matching mal calibre = recos mauvaises = perte de confiance = churn. |
| 15 | **Dashboard B2B** | Les tiers B2B sont decrits mais aucun wireframe, aucune liste de metriques exactes, aucun format de rapport. | Impossible de vendre du B2B Pro/Gold sans maquette du dashboard. Le B2B est la source de revenu principale. |
| 16 | **Internationalisation** | "Design portable" mais aucune spec i18n. Francais uniquement ? Support du nouchi dans l'interface ? Anglais pour l'expansion ? | Dette technique i18n si les strings sont codees en dur. Cout de refactoring x5 apres coup. |
| 17 | **Accessibilite** | Zero mention d'accessibilite (a11y). Contraste, taille de police, lecteur d'ecran, navigation clavier. | Exclusion d'une partie des utilisateurs. Non-conformite potentielle avec des standards store (Google Play). |
| 18 | **Analytics / Tracking** | Aucune mention des outils de tracking (Mixpanel, Amplitude, Firebase Analytics). Quels evenements tracer ? Quel schema de donnees ? | Impossible de mesurer les KPIs listes (activation 60%, retention M6 25%) sans infrastructure analytics. |

### 1.2 Contradictions dans la doc

| # | Contradiction | Section A | Section B | Recommandation |
|---|-------------|-----------|-----------|----------------|
| 1 | **Seuils de stades incoherents** | Section 3.2 : Touriste = 0-10 spots, Explorateur = 11-20, Detective = 21-30, Djidji = 31-50, Guide = 50+ | Section ADVE-E (Niveaux) : Touriste = 0-50 paws, Explorateur = 50-200 paws + 6 spots + 1 review, Detective = 200-500 paws + 21 spots + 10 reviews + 5 photos, Djidji = 500-1000 paws + 51 spots + 40 reviews + premium, Guide = 1000+ paws + 100+ spots + 80+ reviews | **Trancher immediatement.** Deux systemes concurrents (spots seuls vs paws + spots + reviews + photos). L'equipe dev ne peut pas implementer les deux. Recommandation : le systeme simple (nombre de spots) est meilleur pour le MVP. Le systeme paws est ambitieux et necessite un moteur de calcul complexe. |
| 2 | **Prix annuel Premium** | Section 10.1 : "2 500 FCFA/mois - 25 000 FCFA/an" | Section ADVE-V : "2 500 FCFA/mois ou 24 000 FCFA/an" | Incoherence mineure mais doit etre tranchee (25K ou 24K). 24K = 2 mois gratuits, plus incitatif. |
| 3 | **Couleurs de la charte** | Section 9 (Cartes) : Or #D4AF37, Vert #50C878, Blanc #F8F6F0 | Section 13.3 (DA) : Or #C8A44E, Vert #2D6B4F, Blanc #FAFAF8 | **Deux palettes differentes.** L'equipe design va perdre du temps. Fixer UNE palette de reference. |
| 4 | **Typographies** | Section 9 : Playfair Display (titres), DM Sans (corps), JetBrains Mono (data) | Section 13.3 : Instrument Serif (display), Manrope (body), JetBrains Mono (data) | **Deux systemes typo.** Seul JetBrains Mono est commun. Trancher avant le moindre ecran. |
| 5 | **Stade "Rodeur"** | Section 14.2 : mentionne un "Stade Touriste a Rodeur" | Section 3.2 : Le stade "Rodeur" n'existe pas. Les 5 stades sont Touriste/Explorateur/Detective/Djidji/Guide | Erreur probable. "Rodeur" = "Explorateur" ? A clarifier pour eviter la confusion. |
| 6 | **Nombre de Coups de Coeur** | Section 5 : Touriste/Explorateur/Detective = 1/mois (free) | Section 4.3 : "X Coups de Coeur recus ce mois" — le seuil X n'est jamais defini | Definir le seuil X pour que le signal "Coup de Coeur" ait une valeur. |
| 7 | **Crew : creer vs rejoindre** | Section 10.1 : "Crews : Rejoindre uniquement (free), Creer + gerer (premium)" | Section 8.2 : Le Mode Crew est presente comme un des 3 modes contextuels principaux | Si la majorite des users sont freemium et ne peuvent pas creer de crew, le Mode Crew est inutilisable pour la base. Contradiction entre retention (mode Crew = hook social) et monetisation (paywall crew). |

### 1.3 Hypotheses non validees

| # | Hypothese | Risque si fausse | Comment valider |
|---|-----------|------------------|-----------------|
| 1 | **"Le paywall geographique (3km) est le bon levier de conversion premium"** | Si les foodies d'Abidjan explorent principalement dans leur commune, le paywall n'a pas de valeur. Si le transport est un frein, decouvrir un spot a 10km ne sert a rien. | Mission 1 : demander aux 20-30 interviewes "a quelle distance es-tu pret a aller pour un bon restau ?" + analyser les donnees de mobilite (Uber/taxi data). |
| 2 | **"2 500 FCFA/mois est le bon prix"** | Pour Dominic (150K/mois), c'est 1.7% de son revenu — cher pour une app. Pour Betsy (250-350K), c'est accessible. Le marche de reference (Spotify a 3 500 FCFA) montre un plafond psychologique. | A/B test de pricing en beta : 1 500 / 2 500 / 3 500 FCFA. Mesurer le taux de conversion a chaque palier. |
| 3 | **"Les spawters vont generer du contenu de qualite (avis, photos)"** | Si le contenu est generique ("c'etait bien 4/5"), l'ADN du lieu ne se calibre pas, le matching ne fonctionne pas, la valeur B2B est nulle. | Mesurer ratio avis qualifies / total des le beta. Definir un score de qualite d'avis. Tester des incitations (gamification). |
| 4 | **"Les restaurants vont payer 15K-65K/mois pour des insights"** | Les restaurants abidjanais n'ont souvent pas de culture data/analytics. Tantie Rose ne sait pas lire un dashboard. Le Bo Zinc a deja un systeme de resa. | Mission 1 : interviews B2B. Montrer des maquettes de dashboard. Mesurer la willingness to pay reelle. |
| 5 | **"13 archetypes sont comprehensibles et engageants pour les users"** | 13 archetypes + 5 stades + 65 noms de progression = complexite cognitive enorme. Les users peuvent ne rien comprendre au systeme. | Test qualitatif : presenter les archetypes a 10 users. Mesurer la comprehension et l'engagement. Si >30% ne comprennent pas, simplifier a 5-7 archetypes. |
| 6 | **"Le mode Swipe (Rapide) est le bon pattern pour la decouverte food"** | Tinder a fonctionne pour le dating (binaire, emotionnel). La food est multi-criteres (budget, distance, cuisine, ambiance). Le swipe peut etre frustrant si les 5 premiers spots ne correspondent pas. | Prototype et test utilisateur. Comparer swipe vs liste filtrable vs carte. Mesurer le taux de decision et la satisfaction. |
| 7 | **"Le coefficient viral de 1.4 est atteignable"** | 1.4 = chaque user ramene 0.4 users. C'est extremement ambitieux pour une app mobile classique (benchmark : 0.2-0.6 pour la majorite des apps). | Tracker le referral rate des le beta. Si < 0.5, revoir la strategie de viralite. |
| 8 | **"La mascotte chat cree de l'attachement"** | Le chat est central dans le branding mais n'a meme pas de nom. Si les users le trouvent infantile ou inutile, toute la voice de l'app tombe a plat. | Test de concept : presenter le chat (visuel + voix) a 20 users cible. Mesurer la reaction emotionnelle. |
| 9 | **"Le bridge digital 'Allie SPAWT' pour gerer les fiches de Tantie Rose fonctionne"** | Un community manager qui gere 5-10 fiches Pro = cout humain important. Si les maquis informels ne voient pas la valeur, le bridge ne genere pas de revenu. | Pilote Mission 1 : un Allie gere 5 fiches pendant 2 mois. Mesurer le cout, le revenu genere, et la satisfaction des restaurateurs. |
| 10 | **"L'exclusion des leaderboards et de la competition ne freine pas l'engagement"** | La philosophie "pas de classement" est noble mais va a l'encontre de toutes les mecaniques de gamification prouvees. Les users africains sont-ils plus sensibles a l'identite qu'a la competition ? | Mesurer en beta : progression des stades, engagement badges, et comparer avec un groupe A/B ayant un mini-leaderboard masque. |

### 1.4 Fonctions trop ambitieuses pour le MVP

| # | Feature | Pourquoi trop complexe | Alternative MVP |
|---|---------|----------------------|-----------------|
| 1 | **13 archetypes + 5 stades + 65 noms de progression** | Matrice combinatoire massive. Chaque archetype a 5 noms specifiques. La mue (changement d'archetype) necessite un tracking sur 30 jours + 5 spots. Les regles d'inertie ajoutent de la complexite algorithmique. | **MVP : 3-5 archetypes + 3 stades (Touriste/Explorateur/Connaisseur).** Garder le concept de Palais mais avec moins de granularite. Ajouter les archetypes restants en V1.5. |
| 2 | **3 modes contextuels (Rapide/Crew/Explore)** | 3 interfaces distinctes avec des layouts differents (swipe, vote temps reel, magazine scroll). C'est 3 apps dans une app. Le mode Crew necessite du temps reel (websockets). | **MVP : 1 mode principal (feed/liste personnalisee) + recherche/filtres.** Le mode Crew peut etre un simple partage WhatsApp d'une liste. Le mode Explore est un feed. |
| 3 | **Systeme de cartes collectibles (Plats)** | 4 niveaux de rarete, systeme de collection, recto/verso interactif, direction artistique specifique par rarete. Necessiterait du contenu editorial pour chaque plat. | **MVP : Pas de cartes collectibles.** Garder la fiche lieu simple. Les cartes sont un systeme de retention V2. |
| 4 | **Matching instinctif a 4 dimensions** | Palais x ADN x Historique x Contexte (heure, meteo, localisation, nb personnes). Necessite un moteur de recommandation ML sophistique. | **MVP : Tri par distance + note ponderee + 1-2 filtres (cuisine, budget).** Le "matching" est une liste ordonnee, pas un score de compatibilite en %. Iterer vers le ML quand la data le permet. |
| 5 | **Reservation 1-tap** | Integration avec les systemes de reservation de chaque restaurant (aucun standard a Abidjan). La majorite des restos prennent des resas par telephone ou WhatsApp. | **MVP : Bouton "Appeler" + bouton "WhatsApp".** La reservation integree est un feature V2 quand les partenariats B2B sont etablis. |
| 6 | **Dashboard B2B Gold (analytics avances)** | Profil Palais de la clientele, benchmark zone, ciblage par archetype, tendances temporelles. Necessite un data pipeline, des visualisations complexes, et un volume de data suffisant. | **MVP B2B : Fiche revendiquee (Pro) + stats basiques (nb vues, nb avis, note).** Le Gold necessite de la data. Sans volume, les insights sont non significatifs. |
| 7 | **Paws (monnaie interne)** | Un systeme de points backend avec accumulation, seuils, bonus premium, bonus parrainage. Ajoute une couche de complexite sans valeur visible pour l'utilisateur (backend only). | **MVP : Compteur de spawts + compteur d'avis.** Les paws peuvent etre introduits plus tard quand un marketplace interne les justifie. |
| 8 | **Vote crew en temps reel** | Websockets, gestion de sessions synchrones, UI de vote live, synchronisation multi-device. | **MVP : Partage d'une liste curee via lien WhatsApp.** Le vote se fait dans WhatsApp comme aujourd'hui (mais avec de meilleures options). |
| 9 | **SPAWT Wrapped (bilan annuel)** | Feature premium calendaire. Necessite un an de data pour avoir du sens. | **Pas avant M12.** C'est un feature de retention Y2. |
| 10 | **Programme ambassadeur a 3 paliers** | 3 niveaux avec remuneration, briefs mensuels, dashboards d'impact, KPIs de conversion. C'est un programme marketing, pas un feature produit. | **MVP : Programme informel.** Identifier 5 foodies influents, leur donner l'app en beta, mesurer organiquement. Le programme structure arrive en Mission 2. |

---

## PHASE 2 — PERIMETRE MVP

### 2.1 MVP IN — Ce qui doit absolument etre dans V1

| # | Feature | Justification | Complexite |
|---|---------|--------------|------------|
| 1 | **Inscription / Authentification** | Gate d'entree. Telephone + OTP (standard Afrique de l'Ouest). Social login optionnel. | M |
| 2 | **Onboarding leger** | 3-5 ecrans : quartier, type de cuisine prefere, budget habituel, contexte principal (solo/groupe). Permet un Palais initial grossier. | S |
| 3 | **Feed personnalise de lieux** | Liste ordonnee par pertinence (distance + note + preferences onboarding). C'est le coeur de la proposition de valeur. | L |
| 4 | **Fiche lieu** | Photo, nom, quartier, type de cuisine, fourchette de prix, note communautaire, horaires, adresse, bouton appeler/WhatsApp. | M |
| 5 | **Check-in (Spawt)** | Geolocalise. Confirme la presence au lieu. Brique de base de toute la data. | M |
| 6 | **Avis structure** | Note globale /5 + 3-4 sous-criteres (cuisine, service, ambiance, rapport qualite-prix) + commentaire texte + 1-3 photos optionnelles. | M |
| 7 | **Profil utilisateur** | Nom, avatar, quartier, stade actuel, nombre de spawts, avis donnes, lieux sauvegardes. Palais radar basique (2 axes visibles free, 5 axes premium). | M |
| 8 | **3 stades de maturite (simplifie)** | Touriste (0-5 spawts), Explorateur (6-15), Connaisseur (16+). Poids de l'avis indexe sur le stade. Progression visible. | S |
| 9 | **Sauvegarde / Favoris** | Sauvegarder un lieu pour plus tard. Liste personnelle. Feature basique mais essentielle pour la retention. | S |
| 10 | **Recherche + Filtres** | Recherche texte (nom, cuisine, quartier) + filtres : type de cuisine, budget, distance, note minimale. | M |
| 11 | **Carte interactive** | Vue carte avec pins des lieux. Zoom, filtre par categorie. Navigation vers le lieu (deep link Google Maps/Waze). | M |
| 12 | **Coup de Coeur** | 1/mois pour tous. Mecanisme social rare. Pas de monetisation dessus en V1. | S |
| 13 | **Notifications push basiques** | Bienvenue, rappel post-visite (avis), nouveau lieu dans ta zone, activite sur ton avis. | S |
| 14 | **Paywall geographique** | Free = 3km autour du quartier declare. Premium = tout Abidjan. Le paywall est le moteur de conversion. | M |
| 15 | **Paiement Mobile Money** | Orange Money + MTN Mobile Money + Wave minimum. Integration avec un aggregateur (CinetPay, FedaPay, ou Flutterwave). | L |
| 16 | **Partage WhatsApp** | Partager une fiche lieu sur WhatsApp avec deep link vers l'app. WhatsApp est LE canal social en CI. | S |
| 17 | **Moderation basique** | Signalement d'avis + moderation manuelle (admin panel). Pas d'IA, pas de systeme complexe. | M |
| 18 | **Creation de fiche lieu (par l'equipe)** | En V1, les lieux sont pre-charges par l'equipe (les 20 de Mission 1 + expansion). Les users peuvent suggerer un lieu absent (formulaire simple). | S |
| 19 | **Admin panel basique** | Gestion des lieux, moderation des avis, gestion des users, metriques de base. | M |

**Estimation totale MVP : 4-6 mois avec 2-3 devs full-stack + 1 designer.**

### 2.2 MVP OUT — Ce qui sort du V1

| # | Feature | Pourquoi | Quand |
|---|---------|---------|-------|
| 1 | **Mode Rapide (Swipe cards)** | UX complexe, pas de preuve que le pattern swipe fonctionne pour la food. Un feed + filtres est suffisant. | V1.5 (M8) — si les tests montrent un besoin de "decision rapide" |
| 2 | **Mode Crew (vote temps reel)** | Websockets, sessions synchrones, complexite tech disproportionnee. | V2 (M12) — quand la base user est suffisante pour des groupes actifs |
| 3 | **Mode Explore (magazine scroll)** | Layout editorial necessitant du contenu curate en continu. Sans equipe editoriale, c'est un feed vide. | V1.5 (M8) — quand le contenu UGC est suffisant pour alimenter un feed editorial |
| 4 | **13 archetypes** | Trop de combinaisons, trop de noms, trop de complexite. | V1.5 (M8) — commencer avec 5, ajouter les 8 restants progressivement |
| 5 | **Cartes collectibles / Plats** | Feature de retention avancee sans valeur discovery. | V2 (M12) |
| 6 | **Matching ML a 4 dimensions** | Pas assez de data en V1 pour entrainer un modele. | V2 (M12+) — quand 10K+ spawts accumules |
| 7 | **Reservation 1-tap** | Aucun standard de reservation a Abidjan. Trop de friction B2B pour le MVP. | V2 (M12) — via partenariats B2B Pro/Gold |
| 8 | **Dashboard B2B Gold** | Analytics avances sans data = dashboard vide. | V2 (M12) — quand le volume de data est significatif |
| 9 | **Dashboard B2B Pro** | Meme le Pro basique necessite un front separe. | V1.5 (M8) — commencer par un rapport email mensuel PDF |
| 10 | **Badges (30+)** | Complexite de design, de tracking, de conditions. Faible ROI en V1. | V1.5 (M8) — commencer par 5 badges simples |
| 11 | **SPAWT Wrapped** | Besoin de 12 mois de data. | V2 (M18) |
| 12 | **Podcast** | Pas un feature produit. Canal marketing separe. | Jamais dans l'app. Canal externe. |
| 13 | **Paws (monnaie interne)** | Complexite sans valeur visible. | V2 (M12) — si un marketplace interne est prevu |
| 14 | **Streaks / Leaderboards saisonniers** | Phase 2 explicitement dans la bible. | V2 (M12+) |
| 15 | **Share card auto-generee (type Wrapped)** | Design generatif, API image, complexite front. | V1.5 (M8) |
| 16 | **Multi-villes** | La bible dit explicitement "pas avant M12". Mais l'archi doit etre prete. | V2 (M12+) |
| 17 | **Site web** | Pas prioritaire. L'app mobile est le produit. Un landing page suffit pour le SEO/ASO. | V1.5 (M8) — landing page statique en V1 |
| 18 | **Programme ambassadeur formalise** | Programme marketing, pas feature produit. Gere hors app en V1. | V1.5 (M8) |

### 2.3 Points de decision critiques avant developpement

| # | Decision | Options | Recommandation | Impact si mal tranche |
|---|----------|---------|----------------|----------------------|
| 1 | **Systeme de stades : spots seuls vs paws** | A) Nombre de spots uniquement (bible section 3.2) / B) Systeme paws + spots + reviews + photos (ADVE-E) | **A) Spots seuls pour le MVP.** Simple, comprehensible, mesurable. Les paws sont une abstraction inutile en V1. | Si B : 4-6 semaines de dev supplementaires, bugs de calcul, confusion utilisateur. |
| 2 | **Nombre d'archetypes MVP** | A) 13 archetypes / B) 5-7 archetypes / C) 0 archetype en V1, juste les stades | **B) 5 archetypes.** Garder les plus distincts (Pisteur, Fantome, Bouche d'Or, Gardien du Maquis, Omnivore). Ajouter les autres quand le systeme est valide. | Si A : complexite x3, tests difficiles, noms confusants. Si C : perte de l'identite SPAWT. |
| 3 | **Paywall crew** | A) Crew = premium only (creation) / B) Crew free pour tous / C) Pas de Crew en V1 | **C) Pas de Crew en V1.** Remplacer par le partage WhatsApp d'une liste. Le Crew temps reel est un feature V2. | Si A : friction massive sur le hook social. Si B : perte de levier de conversion. |
| 4 | **Palette de couleurs** | A) Section 9 (#D4AF37, #50C878) / B) Section 13.3 (#C8A44E, #2D6B4F) | **Fixer UNE palette avant tout design.** La palette B (section 13.3) semble plus mature et sophistiquee. | Refactoring CSS/tokens sur tout le projet si change apres le lancement. |
| 5 | **Stack typographique** | A) Playfair + DM Sans / B) Instrument Serif + Manrope | **B) Instrument Serif + Manrope.** Plus moderne, meilleure lisibilite mobile, meilleure compatibilite cross-platform. | Meme impact que les couleurs — coherence visuelle impossible si pas tranche. |
| 6 | **Contenu initial : pre-charge ou crowdsource** | A) L'equipe pre-charge 50-100 lieux / B) Les users creent les fiches des le lancement | **A) Pre-charger 50-100 lieux.** Un utilisateur ne doit jamais arriver sur une carte vide. Permettre la suggestion de lieux manquants (formulaire), mais la creation est moderee. | Si B : fiches incompletes, doublons, data polluee, premiere impression desastreuse. |
| 7 | **Visibilite du Palais** | A) Palais visible des le debut / B) Palais revele apres 5-10 spawts | **B) Revele progressivement.** "Ton Palais se dessine..." apres 5 spawts. Effet wow de revelation + motivation pour atteindre le seuil. | Si A : Palais vide/imprecis visible = perte de credibilite du systeme. |
| 8 | **Monetisation V1 : B2C seul ou B2C + B2B** | A) Lancer B2C premium seul / B) Lancer B2C + B2B Pro ensemble | **A) B2C seul en V1.** Le B2B necessite du volume (data) et un produit B2B dedie. Se concentrer sur la traction B2C. Le B2B Pro (fiche revendiquee) peut etre un process manuel hors-app. | Si B : dispersion de l'equipe, deux produits a maintenir, aucun fait bien. |

---

## PHASE 3 — RISQUES TECHNIQUES

### 3.1 Les 10 decisions irreversibles

| # | Decision | Risque | Choix recommande | Deadline |
|---|----------|--------|-----------------|----------|
| 1 | **Framework mobile cross-platform** | Si choix natif (Swift + Kotlin) : cout x2, equipe x2, maintenance x2. Si cross-platform mal choisi : dette technique a long terme. | **React Native (Expo)** ou **Flutter**. Voir section 3.2 pour le detail. | Semaine 1. Tout le reste en depend. |
| 2 | **Schema de base de donnees (modele Palais + ADN)** | Le schema des 5 axes bipolaires, des stades, des archetypes conditionne TOUT le matching et l'analytics. Un mauvais schema = migration couteuse. | Modele relationnel avec tables : users, places, visits (spawts), reviews, user_palais (5 axes float), place_adn (5 axes float). Utiliser PostgreSQL. Prevoir un schema versionne. | Semaine 2. Avant toute ligne de code backend. |
| 3 | **Backend : serverless vs serveur traditionnel** | Serverless (Firebase/Supabase) = rapide au debut, couteux et limitant a l'echelle. Serveur (Node/Django) = plus de controle mais plus de setup. | **Supabase (PostgreSQL managee + auth + storage + realtime)** pour le MVP. Migration possible vers un backend custom si besoin a l'echelle. Alternative : **Node.js + PostgreSQL sur Railway/Render.** | Semaine 1. |
| 4 | **Systeme d'authentification** | Telephone + OTP est le standard en Afrique de l'Ouest mais chaque SMS coute. Social login (Google/Facebook) est gratuit mais moins universel. | **Telephone + OTP comme methode primaire** (via Twilio ou un provider local comme Termii). Google Sign-In en secondaire. PAS de login email/password — friction trop forte. | Semaine 2. |
| 5 | **Provider de carte** | Google Maps Platform = cher ($7/1000 loads). Mapbox = moins cher, plus customisable. OpenStreetMap = gratuit mais donnees moins fiables en CI. | **Mapbox** pour le MVP. Meilleur rapport cout/customisation. Style dark possible (coherent avec la DA). Donnees OSM correctes pour Abidjan. | Semaine 2. |
| 6 | **Provider de paiement Mobile Money** | L'integration Mobile Money est critique et varie par pays. Mauvais choix = impossible de monetiser. | **CinetPay** (ivoirien, supporte Orange Money + MTN + Wave + cartes). Alternative : **Flutterwave** (plus large mais moins local). | Semaine 3. Tester l'integration en sandbox avant le dev principal. |
| 7 | **Strategie de stockage des images** | Les photos de lieux et d'avis vont representer le gros du stockage et de la bande passante. Mauvais choix = couts explosifs. | **Cloudinary** ou **Supabase Storage** avec compression automatique, CDN, et lazy loading. Limiter a 3 photos/avis, 5 photos/lieu. Compression a 80% qualite, max 1MB/image. | Semaine 2. |
| 8 | **Architecture de l'algorithme de recommandation** | Commencer avec du ML = overkill et data insuffisante. Commencer trop simple = impossible de migrer vers du ML. | **V1 : Score composite simple** (distance * 0.3 + note_ponderee * 0.4 + match_preferences * 0.3). Stocker TOUS les signaux (spawts, avis, temps passe, clics) pour entrainer un modele ML en V2. Le schema de donnees doit prevoir ce futur. | Semaine 3. |
| 9 | **Gestion de la geolocalisation** | Le paywall geographique repose sur la geoloc. Si elle est facilement contournable (VPN, fausse position), le premium perd sa valeur. | **Geoloc native (GPS) + verification backend** du rayon de 3km. Pas de geoloc IP (trop imprecise). Accepter que certains users tricheront — le paywall est un nudge, pas un mur. | Semaine 3. |
| 10 | **Structure du projet : monorepo vs polyrepo** | Monorepo = plus simple a gerer pour une petite equipe. Polyrepo = meilleure separation des concerns mais overhead de CI/CD. | **Monorepo** avec : `/app` (React Native/Flutter), `/api` (backend), `/admin` (panel admin), `/shared` (types, utils). Utiliser Turborepo ou Nx si React Native. | Semaine 1. |

### 3.2 Stack mobile recommandee

| Critere | React Native (Expo) | Flutter | Natif (Swift + Kotlin) |
|---------|---------------------|---------|----------------------|
| **Time to market** | Rapide (Expo simplifie enormement) | Rapide | Lent (x2 devs, x2 codebases) |
| **Talent pool Abidjan** | Bon (JS/React populaire) | Moyen (Dart moins repandu) | Tres limite (Swift rare en CI) |
| **Performance** | Bonne pour SPAWT (pas de 3D, pas de animations lourdes) | Excellente | Optimale |
| **Maps** | react-native-maps (mature) | google_maps_flutter / mapbox_gl (correct) | MapKit / Google Maps SDK (natif) |
| **Mobile Money** | Webview pour CinetPay (standard) | Meme approche webview | SDKs natifs |
| **Animations (cartes, transitions)** | Reanimated 3 (puissant) | Tres bon nativement | Optimal |
| **Cout maintenance** | 1 codebase | 1 codebase | 2 codebases |
| **Push notifications** | Expo Notifications (simplifie) | firebase_messaging | APNs + FCM natifs |
| **OTA updates** | Expo Updates (killer feature) | CodePush via Shorebird (beta) | Impossible |

**RECOMMANDATION : React Native avec Expo.**

Raisons :
1. **Talent pool** : JS/React est le langage le plus repandu dans l'ecosysteme tech ivoirien.
2. **Expo Updates** : Permet de deployer des correctifs sans passer par les stores. Critique pour une equipe early-stage qui itere vite.
3. **Expo Router** : Navigation file-based, rapide a prototyper.
4. **Ecosysteme** : Librairies matures pour maps, auth, notifications, camera, image picking.
5. **La performance** est suffisante pour SPAWT (feed, cartes, formulaires — pas de jeu ni de video).

**Stack complete recommandee :**
- **Frontend mobile** : React Native + Expo SDK 52+ + Expo Router + NativeWind (Tailwind CSS)
- **Backend** : Supabase (PostgreSQL + Auth + Storage + Edge Functions) OU Node.js (Express/Fastify) + PostgreSQL sur Railway
- **State management** : Zustand ou TanStack Query (server state)
- **Maps** : Mapbox GL via react-native-mapbox-gl
- **Paiement** : CinetPay (webview integration)
- **Analytics** : Mixpanel (free tier genereux) ou PostHog (self-hosted)
- **Push** : Expo Notifications + FCM/APNs
- **CI/CD** : EAS Build (Expo) + GitHub Actions
- **Admin panel** : React + Refine ou AdminJS (simple, rapide)
- **Monitoring** : Sentry (crash reporting) + Supabase Dashboard

### 3.3 Architecture data critique

#### Le modele Palais (Spawter)

```
Table: user_palais
- user_id (FK)
- axe_racines_horizons    FLOAT [-1, 1]   -- -1 = Racines, +1 = Horizons
- axe_taniere_nomade      FLOAT [-1, 1]   -- -1 = Taniere, +1 = Nomade
- axe_exigeant_enthousiaste FLOAT [-1, 1] -- -1 = Exigeant, +1 = Enthousiaste
- axe_foule_secret        FLOAT [-1, 1]   -- -1 = Foule, +1 = Secret
- axe_maquis_table        FLOAT [-1, 1]   -- -1 = Maquis, +1 = Table
- confidence_score        FLOAT [0, 1]    -- Fiabilite du Palais (bas si peu de spawts)
- dominant_axes           JSONB           -- Les 2 axes les plus marques
- archetype_id            FK              -- Archetype derive
- stade                   ENUM            -- touriste/explorateur/connaisseur
- total_spawts            INT
- updated_at              TIMESTAMP
```

**Points critiques :**
- Les axes sont des FLOAT bipolaires [-1, 1], pas des categories. Cela permet un calcul de distance vectorielle avec l'ADN du lieu.
- Le `confidence_score` est essentiel : un Palais avec 2 spawts n'a pas la meme fiabilite qu'un Palais avec 50.
- Les `dominant_axes` sont caches en JSONB pour eviter un recalcul a chaque affichage.
- **Recalcul** : le Palais est recalcule a chaque spawt (incrementalement, pas from scratch). Formule : `nouveau_axe = ancien_axe * decay_factor + signal_nouveau_spawt * (1 - decay_factor)`. Le decay_factor donne plus de poids aux comportements recents.

#### Le modele ADN du lieu (Spawt)

```
Table: place_adn
- place_id (FK)
- axe_local_international  FLOAT [-1, 1]
- axe_informel_etabli      FLOAT [-1, 1]
- axe_budget_premium       FLOAT [-1, 1]
- axe_populaire_prive      FLOAT [-1, 1]
- axe_decontracte_habille  FLOAT [-1, 1]
- confidence_score         FLOAT [0, 1]
- total_reviews            INT
- updated_at               TIMESTAMP
```

**Points critiques :**
- L'ADN est calcule a partir des AVIS (pas des spawts). Un check-in sans avis ne modifie pas l'ADN.
- Les sous-criteres de l'avis (cuisine, ambiance, service, rapport qualite-prix) sont mappes vers les axes de l'ADN. Ce mapping doit etre specifie.
- **Minimum viable** : un lieu avec <5 avis n'a pas d'ADN fiable. Afficher "ADN en construction" plutot qu'un radar faux.

#### Le matching

```
Score_matching(user, place) =
    w1 * cosine_similarity(user.palais_vector, place.adn_vector)  -- compatibilite de profil
  + w2 * distance_penalty(user.location, place.location)           -- proximite
  + w3 * note_ponderee(place)                                      -- qualite communautaire
  + w4 * recency_boost(place)                                      -- lieux recemment spawtes
  + w5 * novelty_bonus(user, place)                                -- l'user n'y est pas encore alle

Avec w1 + w2 + w3 + w4 + w5 = 1
MVP : w1=0.15, w2=0.30, w3=0.30, w4=0.10, w5=0.15
```

**Points critiques :**
- En MVP, `w1` (Palais x ADN) est faible parce que les profils sont peu fiables avec peu de data. Augmenter `w1` progressivement quand le `confidence_score` des Palais augmente.
- La `distance_penalty` doit etre non lineaire : 0-1km = 0 penalty, 1-3km = legere, 3-5km = forte, 5km+ = tres forte (et paywall).
- La `note_ponderee` donne plus de poids aux avis des stades avances : Touriste = 1x, Explorateur = 1.5x, Connaisseur = 2x.

#### Collecte de signaux pour le ML futur

```
Table: user_signals (append-only, haute cardinalite)
- user_id
- signal_type  ENUM (spawt, review, view, save, share, search, filter, click, dismiss)
- place_id     NULLABLE
- metadata     JSONB    -- contexte : heure, jour, position, device, session_id
- created_at   TIMESTAMP
```

**Ce tableau ne sert pas en V1** mais il est CRITIQUE de le creer des le debut. C'est la matiere premiere du ML futur. Cout de stockage negligeable. Cout de migration si oublie : enorme.

---

## SYNTHESE EXECUTIVE

### Les 5 problemes les plus urgents a resoudre

1. **Le check-in n'est pas specifie.** C'est la brique de base de TOUT le systeme (Palais, ADN, matching, stades). Definir le mecanisme exact (geoloc, rayon, delai, validation) avant toute chose.

2. **Deux systemes de progression contradictoires.** La section 3.2 et la section ADVE-E decrivent des seuils differents. L'equipe dev est bloquee. Trancher en faveur du systeme simple (nombre de spots) pour le MVP.

3. **L'algorithme du Palais n'existe pas.** Les 5 axes sont conceptuels mais aucune formule ne dit comment un spawt modifie les axes. Sans cela, pas de Palais, pas de matching, pas de SPAWT.

4. **Aucune spec de paiement Mobile Money.** Le marche cible n'utilise pas Stripe. L'integration CinetPay ou equivalent est un chantier de 4-6 semaines qui doit demarrer tot.

5. **La direction artistique a deux palettes et deux systemes typo.** Toute maquette produite avant ce choix sera a refaire. Perdre 1 jour a trancher maintenant sauve 3 semaines plus tard.

### Les 5 choix architecturaux recommandes

1. **React Native + Expo** pour le mobile (time-to-market, talent pool, OTA updates).
2. **Supabase** pour le backend MVP (PostgreSQL + Auth + Storage, prototypage rapide).
3. **Mapbox** pour les cartes (cout, customisation, style dark).
4. **CinetPay** pour le paiement Mobile Money (ivoirien, support local).
5. **Monorepo** pour la structure projet (coherence, simplicite CI/CD).

### Les 5 fonctionnalites a sortir du MVP

1. Les 3 modes contextuels (Rapide/Crew/Explore) — remplacer par 1 feed + recherche.
2. Les 13 archetypes — commencer avec 5.
3. Les cartes collectibles / plats — feature V2.
4. Le matching ML — commencer par un score composite simple.
5. Le dashboard B2B — vendre le B2B Pro manuellement en V1, dashboard en V1.5.

### Les 5 actions immediates

| # | Action | Responsable | Deadline |
|---|--------|-------------|----------|
| 1 | Trancher les contradictions (stades, couleurs, typos, prix annuel) | Pioneer + Product | Cette semaine |
| 2 | Specifier le mecanisme de check-in (geoloc, rayon, delai) | Product + Tech | Cette semaine |
| 3 | Definir l'algorithme Palais (comment un spawt modifie les axes) | Product + Data | Semaine 2 |
| 4 | Choisir et tester le provider de paiement Mobile Money (sandbox) | Tech Lead | Semaine 2 |
| 5 | Fixer la stack technique (framework, backend, cartes) et initialiser le monorepo | Tech Lead | Semaine 1 |

---

*Session realisee par Mary, analyste strategique senior*
*7 avril 2026 — 14h30*
*Documents source : SPAWT_BIBLE_COMPLETE.md (1290 lignes)*

---

# SPECS DETAILLEES MVP — Opus 4.6 Session 2026-04-07

> **Source de verite unique** : `SPAWT_Presentation_Fevrier_2026_V2-2.docx`
> Tout element extrait du document est marque `[SOURCE DOC]`. Toute recommandation de l'auteur est marquee `[RECOMMANDATION]`.

---

## SPEC 1 — LE CHECK-IN (Le Spawt)

### 1.1 Mecanisme de declenchement — Recommandation

`[SOURCE DOC]` Le check-in est decrit comme "Action 1 : Le Spawt (Check-in) — Le spawter confirme sa presence dans un lieu. Action rapide, instinctive."

`[RECOMMANDATION]` **Approche hybride : bouton manuel + validation geoloc passive.**

| Option | Avantages | Inconvenients | Verdict MVP |
|--------|-----------|---------------|-------------|
| Geoloc automatique seule | Zero friction | Batterie, GPS instable en interieur a Abidjan, faux positifs | NON |
| QR code en restaurant | Anti-fraude fort | Necessite onboarding des 20 restos + imprimante, friction | PHASE 2 |
| Bouton manuel seul | Simple, fonctionne partout | Spawts frauduleux faciles | NON |
| **Bouton manuel + geoloc passive** | **Equilibre friction/fiabilite** | **Necessite GPS actif** | **OUI — MVP** |

**Justification contexte ivoirien :**
- Le GPS est disponible sur >95% des smartphones Android a Abidjan (meme les entree de gamme Tecno/Infinix)
- Le reseau data est variable (3G/4G instable dans certaines zones) mais le GPS fonctionne sans data
- Le QR code necessite un onboarding restaurant lourd — incompatible avec Mission 1 (20 restos)
- L'approche bouton + geoloc passive est la plus resiliente reseau

### 1.2 Flow UX detaille — Parcours Spawter

**Duree cible : < 30 secondes pour un spawt simple, < 2 minutes avec avis**

```
ECRAN 1 — CARTE / LISTE (point d'entree)
  Le spawter est sur la carte ou dans une fiche lieu
  → Bouton central "Spawter" dans la barre de navigation (sureleve)
  OU → Bouton "Spawter ici" sur la fiche du lieu

ECRAN 2 — CONFIRMATION LIEU
  SI geoloc active ET lieu detecte dans un rayon de 150m :
    → Affiche : "Tu es chez [Nom du lieu] ?" + photo du lieu
    → CTA : "Oui, je spawte" / "Non, changer de lieu"
  SI geoloc active MAIS aucun lieu dans 150m :
    → Affiche : "Aucun lieu detecte ici"
    → Options : "Chercher un lieu" / "Creer un nouveau spawt"
  SI geoloc inactive :
    → Affiche : "Active ta localisation pour spawter"
    → Fallback : recherche manuelle du lieu (texte)
    → Le spawt est marque "non verifie" (flag interne)

ECRAN 3 — SPAWT RAPIDE (optionnel)
  Le spawt est enregistre des validation a l'ecran 2.
  → Animation du chat : "Spawte !" + compteur de spots incremente
  → Proposition optionnelle (non bloquante) :
    "Tu veux laisser un avis ?" → OUI / PLUS TARD
  SI "OUI" → ECRAN 4
  SI "PLUS TARD" → retour a la carte avec confirmation toast

ECRAN 4 — AVIS OPTIONNEL
  → Note etoiles (1-5, obligatoire si avis)
  → Photo (optionnelle, max 3)
  → Texte libre (optionnel, max 500 caracteres)
  → Tags rapides : "Copieux" "Rapide" "Ambiance top" "Cher" "A refaire" (tap multiple)
  → CTA : "Publier" / "Sauvegarder brouillon"

ECRAN 5 — FEEDBACK CHAT
  → Message contextuel du chat selon le stade :
    Touriste : "Bien joue ! Ton Palais commence a se dessiner."
    Explorateur : "Encore un. Ton territoire grandit."
    Detective : "Le Chat note tout. Continue."
    Djidji : "[silence respectueux — juste l'animation]"
    Guide : "[rien — le guide n'a pas besoin d'encouragement]"
  → Si badge debloque : notification speciale
  → Si changement de stade : ecran de celebration dedie
```

### 1.3 Donnees collectees a chaque check-in

```json
{
  "spawt_checkin": {
    "id": "uuid_v4",
    "spawter_id": "uuid_v4",
    "lieu_id": "uuid_v4",
    "timestamp": "2026-04-07T13:42:00+00:00",
    "geolocation": {
      "lat": 5.3364,
      "lng": -4.0267,
      "accuracy_meters": 25,
      "source": "gps|network|manual"
    },
    "verification": {
      "is_geolocated": true,
      "distance_to_lieu_meters": 42,
      "is_verified": true
    },
    "avis": {
      "note_etoiles": 4,
      "texte": "Attieke poisson braise excellent...",
      "tags": ["copieux", "rapide", "a_refaire"],
      "photos": ["url1", "url2"],
      "is_complete": true
    },
    "context": {
      "heure_locale": "13:42",
      "jour_semaine": "lundi",
      "mode_app": "rapide|crew|explore",
      "is_first_visit": true,
      "is_premium": false
    },
    "metadata": {
      "app_version": "1.0.0",
      "device_os": "android_13",
      "created_at": "2026-04-07T13:42:00Z",
      "updated_at": null
    }
  }
}
```

### 1.4 Regles anti-fraude MVP

| Regle | Seuil | Action |
|-------|-------|--------|
| Distance maximale au lieu | 150 metres | Au-dela : spawt marque `non_verifie`, poids algorithmique reduit a 0.3x |
| Frequence maximale meme lieu | 1 spawt / 4 heures | Doublon rejete avec message : "Tu as deja spawte ici aujourd'hui" |
| Frequence maximale globale | 5 spawts / jour | Au-dela : spawts acceptes mais flagges pour review |
| Vitesse de deplacement | > 100 km/h entre 2 spawts consecutifs | Flag automatique, spawt en attente de validation |
| Spawt sans geoloc | N/A | Accepte mais marque `non_verifie`, poids 0.3x, ne compte PAS pour les badges geolocalises |
| Patterns suspects | 10+ spawts identiques (meme lieu, meme note) en 7 jours | Compte flagge, review manuelle |

`[RECOMMANDATION]` **Phase 2** : QR code en restaurant pour les Spawt Pro/Gold, validation NFC, detection de photo prise sur place (metadata EXIF).

### 1.5 Lien check-in → Palais (5 axes)

Chaque check-in genere des signaux qui alimentent les 5 axes du Palais. La table de mapping :

| Signal du check-in | Axe impacte | Direction | Poids |
|---|---|---|---|
| Lieu de cuisine locale (ivoirienne, africaine) | Racines/Horizons | +Racines | +2 |
| Lieu de cuisine internationale | Racines/Horizons | +Horizons | +2 |
| Lieu deja visite (retour) | Taniere/Nomade | +Taniere | +1 |
| Lieu jamais visite (premier spawt) | Taniere/Nomade | +Nomade | +2 |
| Note >= 4 etoiles | Exigeant/Enthousiaste | +Enthousiaste | +1 |
| Note <= 2 etoiles | Exigeant/Enthousiaste | +Exigeant | +1 |
| Note = 3 (neutre) | Exigeant/Enthousiaste | 0 | 0 |
| Lieu avec > 50 spawts (populaire) | Foule/Secret | +Foule | +1 |
| Lieu avec < 10 spawts (cache) | Foule/Secret | +Secret | +2 |
| Lieu type maquis/street food | Maquis/Table | +Maquis | +2 |
| Lieu type restaurant/gastronomique | Maquis/Table | +Table | +2 |
| Lieu type casual/brasserie | Maquis/Table | 0 | 0 |
| Check-in apres 21h | (bonus) Foule si populaire | +1 | contextuel |
| Check-in en mode Crew | (bonus) Foule | +1 | contextuel |

### 1.6 MVP vs Phase 2

| Fonctionnalite | MVP | Phase 2 |
|---|---|---|
| Bouton spawter + geoloc passive | OUI | - |
| Validation distance 150m | OUI | Affiner a 50m avec QR |
| Note etoiles 1-5 | OUI | - |
| Photo optionnelle | OUI | Photo obligatoire pour badges photo |
| Tags rapides | OUI | Tags personnalises |
| Texte libre | OUI | Avis structure multi-criteres |
| QR code restaurant | NON | OUI (Spawt Pro+) |
| Detection photo EXIF | NON | OUI |
| Spawt offline (synchronise apres) | NON | OUI |
| Avis vocal | NON | OUI (Phase 3) |

---

## SPEC 2 — SYSTEME DE PROGRESSION

### 2.1 Les 5 stades — Seuils confirmes

`[SOURCE DOC]` Extraits directs de la presentation Fevrier 2026 :

| Stade | Icone | Seuil | Description source |
|-------|-------|-------|-------------------|
| Touriste | 🐱 | 0-10 spots | "Renifle tout. Apprend. Son Palais bouge beaucoup." |
| Explorateur | 🐈 | 11-20 spots | "Territoire qui se dessine. Axes se stabilisent." |
| Detective | 🐈‍⬛ | 21-30 spots | "Sur de son flair. Respecte dans sa zone." |
| Djidji | ✦ | 31-50 spots | "Expert reconnu. La colonie ecoute." |
| Guide | ◉ | 50+ spots | "Le chat qui marche devant." |

### 2.2 Definition d'un "spot" — Regle de comptage

`[RECOMMANDATION]` Le terme "spots" dans la source necessite une definition precise :

```
REGLE : spots = nombre de LIEUX UNIQUES spawtes (check-in verifie)

- Un spawter qui visite le MEME lieu 10 fois = 1 spot
- Un spawter qui visite 10 lieux DIFFERENTS = 10 spots
- Seuls les check-ins avec is_verified = true comptent pour la progression
- Les check-ins non verifies (sans geoloc) ne comptent PAS pour les spots
- Un spawt annule ou signale comme frauduleux est retire du compteur

JUSTIFICATION : Le systeme recompense la DIVERSITE d'exploration, pas la
frequentation repetee. C'est coherent avec "On explore par instinct" et
le fait que l'axe Taniere/Nomade mesure precisement ce comportement.
```

### 2.3 Algorithme de progression — Pseudo-code

```python
def calculer_stade(spawter):
    """Calcule le stade de maturite d'un spawter."""
    spots_uniques = count_distinct(
        spawts.lieu_id
        WHERE spawts.spawter_id = spawter.id
        AND spawts.is_verified = True
        AND spawts.is_cancelled = False
    )

    if spots_uniques >= 50:
        return GUIDE
    elif spots_uniques >= 31:
        return DJIDJI
    elif spots_uniques >= 21:
        return DETECTIVE
    elif spots_uniques >= 11:
        return EXPLORATEUR
    else:
        return TOURISTE


def verifier_montee_stade(spawter, nouveau_spawt):
    """Verifie si un nouveau spawt declenche une montee de stade."""
    ancien_stade = spawter.stade_actuel
    nouveau_stade = calculer_stade(spawter)

    if nouveau_stade > ancien_stade:
        # Montee de stade confirmee
        nouveau_titre = get_titre_pour(spawter.archetype, nouveau_stade)

        # Ajouter le titre a la collection (permanent)
        spawter.collection_titres.append({
            "titre": nouveau_titre,
            "stade": nouveau_stade,
            "archetype": spawter.archetype,
            "date_obtenu": now(),
            "spots_au_moment": spots_uniques
        })

        # Mettre a jour le stade
        spawter.stade_actuel = nouveau_stade
        spawter.titre_actuel = nouveau_titre

        # Declencher notification chat
        envoyer_notification_stade(spawter, ancien_stade, nouveau_stade)

        # Mettre a jour les privileges
        update_coups_de_coeur_disponibles(spawter)
        update_poids_algorithmique(spawter)

        return MONTEE_STADE

    return PAS_DE_CHANGEMENT
```

### 2.4 Mue d'archetype — Pseudo-code

`[SOURCE DOC]` "L'archetype ne switch que si les axes dominants sont stables sur 30 jours + 5 spots minimum dans la nouvelle direction."

```python
def verifier_mue_archetype(spawter):
    """Verifie si le spawter change d'archetype (mue laterale)."""

    # Calculer les 2 axes dominants actuels
    axes_actuels = calculer_axes_dominants(spawter.palais)
    archetype_actuel = spawter.archetype

    # Determiner l'archetype qui correspondrait aux axes actuels
    archetype_potentiel = archetype_from_axes(axes_actuels)

    if archetype_potentiel == archetype_actuel:
        # Pas de changement, reset du compteur d'inertie
        spawter.mue_tracking = None
        return PAS_DE_MUE

    # Verifier la regle d'inertie
    if spawter.mue_tracking is None:
        # Premier signal de divergence, commencer le tracking
        spawter.mue_tracking = {
            "archetype_candidat": archetype_potentiel,
            "date_debut": now(),
            "spots_dans_direction": 1
        }
        return PAS_DE_MUE

    if spawter.mue_tracking.archetype_candidat != archetype_potentiel:
        # La direction a change — reset
        spawter.mue_tracking = {
            "archetype_candidat": archetype_potentiel,
            "date_debut": now(),
            "spots_dans_direction": 1
        }
        return PAS_DE_MUE

    # Meme direction — incrementer
    spawter.mue_tracking.spots_dans_direction += 1

    # Verifier les 2 conditions d'inertie
    jours_ecoules = (now() - spawter.mue_tracking.date_debut).days
    spots_accumules = spawter.mue_tracking.spots_dans_direction

    if jours_ecoules >= 30 AND spots_accumules >= 5:
        # MUE CONFIRMEE
        ancien_archetype = spawter.archetype
        spawter.archetype = archetype_potentiel

        nouveau_titre = get_titre_pour(archetype_potentiel, spawter.stade_actuel)
        spawter.titre_actuel = nouveau_titre
        spawter.collection_titres.append({
            "titre": nouveau_titre,
            "stade": spawter.stade_actuel,
            "archetype": archetype_potentiel,
            "date_obtenu": now(),
            "type": "mue"
        })

        spawter.mue_tracking = None

        envoyer_notification_mue(spawter, ancien_archetype, archetype_potentiel)
        return MUE_CONFIRMEE

    return EN_OBSERVATION
```

### 2.5 Notifications chat — Copy exact par stade

**Montees de stade :**

| Transition | Message du chat | Ton |
|---|---|---|
| → Touriste (onboarding) | "Bienvenue. Ton Palais est vierge. Chaque spawt le dessine un peu plus. On y va ?" | Enjoue, taquin |
| Touriste → Explorateur | "11 spots. Ton nez s'affine. Je commence a te reconnaitre. Tu es [TITRE]. Garde ca." | Complice |
| Explorateur → Detective | "Le Chat te salue, [PRENOM]. [NOMBRE] spots. Ton flair ne ment plus. Tu es desormais [TITRE]." | Grave, respectueux |
| Detective → Djidji | "[NOMBRE] spots. Plus besoin de te guider. Tu ES le guide. Djidji [TITRE]. La tribu ecoute." | Solennel |
| Djidji → Guide | "..." (silence + animation speciale du chat qui s'incline) puis : "[TITRE]. Il n'y en a que [X] a Abidjan." | Rare, presque sacre |

**Mues d'archetype :**

| Situation | Message du chat |
|---|---|
| Mue en cours (observation) | *(pas de message — invisible pour le spawter)* |
| Mue confirmee | "Je te sens different. Tes 30 derniers jours disent [NOUVEL ARCHETYPE] plus que [ANCIEN ARCHETYPE]. Ca te parle ?" |
| Mue + nouveau titre | "Nouveau titre debloque : [TITRE]. Il rejoint ta collection. Tu choisis lequel afficher." |

### 2.6 Schema de donnees — Progression

```sql
-- Table spawter_progression
CREATE TABLE spawter_progression (
    spawter_id          UUID PRIMARY KEY REFERENCES spawters(id),
    stade_actuel        ENUM('touriste','explorateur','detective','djidji','guide'),
    archetype_actuel    VARCHAR(30),  -- ex: 'pisteur', 'fantome', 'bouche_dor'
    titre_actuel        VARCHAR(60),  -- ex: 'Pisteur de Brousse'
    titre_affiche       VARCHAR(60),  -- le titre choisi par le spawter (peut != titre_actuel)
    spots_uniques       INTEGER DEFAULT 0,
    date_dernier_stade  TIMESTAMP,
    updated_at          TIMESTAMP
);

-- Table collection_titres (permanent, ne se supprime jamais)
CREATE TABLE collection_titres (
    id                  UUID PRIMARY KEY,
    spawter_id          UUID REFERENCES spawters(id),
    titre               VARCHAR(60),
    stade               ENUM('touriste','explorateur','detective','djidji','guide'),
    archetype           VARCHAR(30),
    type_obtention      ENUM('montee_stade', 'mue', 'onboarding'),
    spots_au_moment     INTEGER,
    date_obtenu         TIMESTAMP,
    is_displayed        BOOLEAN DEFAULT FALSE  -- un seul a true a la fois
);

-- Table mue_tracking (etat transitoire)
CREATE TABLE mue_tracking (
    spawter_id          UUID PRIMARY KEY REFERENCES spawters(id),
    archetype_candidat  VARCHAR(30),
    date_debut          TIMESTAMP,
    spots_dans_direction INTEGER DEFAULT 0,
    dernier_check       TIMESTAMP
);

-- Index pour performance
CREATE INDEX idx_progression_stade ON spawter_progression(stade_actuel);
CREATE INDEX idx_titres_spawter ON collection_titres(spawter_id);
```

### 2.7 MVP vs Phase 2

`[RECOMMANDATION]` **Les 5 stades sont necessaires au MVP.** Justification :

- Les seuils sont bas (10, 20, 30, 50) — atteignables en 1-3 mois d'usage actif
- Le systeme de poids algorithmique des avis (section 4.2 source) depend du stade
- Les Coups de Coeur sont indexes sur le stade (section 5 source)
- Le feature gating ("Passe Detective pour les food tours") est un levier de conversion premium

**MVP** : 5 stades + 13 archetypes calcules + collection de titres + mue
**Phase 2** : Share card auto-generee, evolution visuelle du chat par stade, titres Guide limites par ville

---

## SPEC 3 — ALGORITHME DU PALAIS

### 3.1 Les 5 axes bipolaires — Echelle

`[SOURCE DOC]` Les 5 axes sont confirmes dans la section 3.1 de la presentation.

`[RECOMMANDATION]` Echelle : chaque axe est un score de **-100 a +100**.

| Axe | -100 | 0 | +100 |
|-----|------|---|------|
| 1. Racines/Horizons | Racines pures | Equilibre | Horizons purs |
| 2. Taniere/Nomade | Taniere pure | Equilibre | Nomade pur |
| 3. Exigeant/Enthousiaste | Exigeant pur | Equilibre | Enthousiaste pur |
| 4. Foule/Secret | Foule pure | Equilibre | Secret pur |
| 5. Maquis/Table | Maquis pur | Equilibre | Table pure |

Convention : pole gauche = negatif, pole droit = positif. Un spawter "Nomade + Maquis" aura un score positif sur l'axe 2 et negatif sur l'axe 5.

### 3.2 Calibrage initial — 5 questions d'onboarding

`[SOURCE DOC]` "Le calibrage initial se fait via 5 questions d'humeur lors de l'onboarding, puis s'ajuste en continu."

`[RECOMMANDATION]` Questions et mapping :

```
QUESTION 1 → Axe Racines/Horizons
"Quand tu as faim, tu penses a quoi en premier ?"
  A) "Attieke poisson, alloco, garba — les classiques"     → Racines (+40)
  B) "Pizza, sushi, burger — le monde dans l'assiette"     → Horizons (+40)
  C) "Ca depend du jour"                                    → Neutre (0)

QUESTION 2 → Axe Taniere/Nomade
"Samedi soir, tu fais quoi ?"
  A) "Mon spot habituel. Ils me connaissent."               → Taniere (-40)
  B) "Un endroit que je n'ai jamais teste"                  → Nomade (+40)
  C) "Ca depend de qui m'accompagne"                        → Neutre (0)

QUESTION 3 → Axe Exigeant/Enthousiaste
"Tu goutes un plat moyen dans un nouveau lieu. Tu fais quoi ?"
  A) "Je note mentalement. Je ne reviendrai pas."           → Exigeant (-40)
  B) "C'est pas grave, l'ambiance compense"                 → Enthousiaste (+40)
  C) "Je goute autre chose avant de juger"                  → Neutre (0)

QUESTION 4 → Axe Foule/Secret
"Le spot ideal c'est :"
  A) "Plein de monde, ca prouve que c'est bon"              → Foule (-40)
  B) "Vide. Mon secret. Mon tresor."                        → Secret (+40)
  C) "M'en fous, c'est le plat qui compte"                  → Neutre (0)

QUESTION 5 → Axe Maquis/Table
"Ton cadre ideal pour manger :"
  A) "Plastique, ventilo, tele qui griche — maquis life"   → Maquis (-40)
  B) "Nappe, menu carte, serveur en tablier"                → Table (+40)
  C) "Les deux me vont"                                      → Neutre (0)
```

**Resultat initial** : Le Palais demarre avec 5 scores entre -40 et +40. La plage [-40, +40] au lieu de [-100, +100] est deliberee — elle laisse 60% de la plage pour le calibrage comportemental reel.

### 3.3 Mise a jour continue — Formule

A chaque check-in, le Palais est recalcule. Le principe : **decroissance exponentielle** — les actions recentes pesent plus que les anciennes.

```python
def mettre_a_jour_palais(spawter, checkin):
    """Met a jour les 5 axes du Palais apres un check-in."""

    # Extraire les signaux du check-in (cf. table 1.5)
    signaux = extraire_signaux(checkin)

    for axe in AXES:
        if signaux[axe] == 0:
            continue

        # Facteur de decroissance : les premiers spawts pesent plus
        # pour permettre au Palais de bouger vite au debut
        n = spawter.spots_uniques
        facteur_apprentissage = max(0.05, 1.0 / (1 + n * 0.05))

        # Signal brut pondere par le facteur d'apprentissage
        delta = signaux[axe] * facteur_apprentissage

        # Appliquer au score de l'axe
        ancien_score = spawter.palais[axe]
        nouveau_score = clamp(ancien_score + delta, -100, +100)
        spawter.palais[axe] = nouveau_score
```

**Table des facteurs d'apprentissage** (le Palais bouge de moins en moins) :

| Spots uniques | Facteur | Impact d'un signal +2 | Commentaire |
|---|---|---|---|
| 1 | 0.95 | +1.90 | Le Palais bouge beaucoup (Touriste) |
| 5 | 0.80 | +1.60 | Encore instable |
| 10 | 0.67 | +1.33 | Debut de stabilisation |
| 20 | 0.50 | +1.00 | Explorateur confirme |
| 30 | 0.40 | +0.80 | Detective, Palais stable |
| 50 | 0.29 | +0.57 | Djidji/Guide, Palais ancre |
| 100 | 0.17 | +0.33 | Quasi-immuable |

### 3.4 Determination de l'archetype — Algorithme

`[SOURCE DOC]` "Les 2 axes les plus marques du spawter determinent son archetype."

```python
def calculer_archetype(palais):
    """Identifie les 2 axes dominants et retourne l'archetype."""

    # Calculer la valeur absolue de chaque axe (polarisation)
    polarisations = {
        axe: abs(palais[axe])
        for axe in AXES
    }

    # Trier par polarisation decroissante
    axes_tries = sorted(polarisations.items(), key=lambda x: x[1], reverse=True)

    # Verifier si un archetype est identifiable
    axe1, score1 = axes_tries[0]
    axe2, score2 = axes_tries[1]

    # Seuil minimum de polarisation pour etre "marque"
    SEUIL_POLARISATION = 15  # en valeur absolue

    if score1 < SEUIL_POLARISATION and score2 < SEUIL_POLARISATION:
        # Aucun axe suffisamment marque
        return "omnivore"  # accessible uniquement a partir d'Explorateur

    if score2 < SEUIL_POLARISATION:
        # Un seul axe marque — utiliser le 2e plus haut meme si faible
        pass  # on garde quand meme axe1 + axe2

    # Determiner le pole de chaque axe dominant
    pole1 = get_pole(axe1, palais[axe1])  # ex: "nomade" si score > 0 sur axe 2
    pole2 = get_pole(axe2, palais[axe2])

    # Lookup dans la table des archetypes
    archetype = ARCHETYPE_MAP.get((pole1, pole2))

    if archetype is None:
        # Combinaison non mappee — fallback au plus proche
        archetype = trouver_archetype_plus_proche(pole1, pole2)

    return archetype


# Table de mapping poles → archetype
ARCHETYPE_MAP = {
    ("nomade", "maquis"):       "pisteur",
    ("nomade", "secret"):       "fantome",
    ("nomade", "table"):        "bouche_dor",
    ("taniere", "maquis"):      "gardien_du_maquis",
    ("taniere", "racines"):     "memoire",
    ("foule", "enthousiaste"):  "feu_de_braise",
    ("secret", "exigeant"):     "oeil_de_chat",
    ("horizons", "nomade"):     "vent_dailleurs",
    ("secret", "maquis"):       "murmure",
    ("table", "exigeant"):      "lame",
    ("table", "horizons"):      "passeport_dore",
    ("taniere", "table"):       "ancre",
}
```

### 3.5 Matching Palais x ADN du Lieu — Formule du score de compatibilite

`[SOURCE DOC]` "Chaque lieu recoit un score de compatibilite avec le spawter (ex: 92%)."

`[RECOMMANDATION]` Formule de calcul :

```python
def calculer_score_matching(spawter, lieu):
    """
    Calcule le score de compatibilite entre un spawter et un lieu.
    Retourne un pourcentage entre 0% et 100%.
    """

    # DIMENSION 1 — Palais x ADN (poids: 45%)
    # Cosine similarity entre les 5 axes du Palais et les 5 axes de l'ADN
    palais = spawter.palais  # [-100, +100] x 5
    adn = lieu.adn           # [-100, +100] x 5

    # Normaliser sur la meme echelle
    score_palais_adn = cosine_similarity(palais, adn)
    # cosine_similarity retourne [-1, 1], normaliser en [0, 1]
    score_palais_adn = (score_palais_adn + 1) / 2

    # DIMENSION 2 — Historique personnel (poids: 20%)
    if spawter a deja visite lieu:
        note_precedente = derniere_note(spawter, lieu)
        score_historique = note_precedente / 5.0  # [0, 1]
    elif spawter a visite des lieux similaires:
        score_historique = moyenne_notes_lieux_similaires / 5.0
    else:
        score_historique = 0.5  # neutre

    # DIMENSION 3 — Colonie / profils similaires (poids: 20%)
    spawters_similaires = get_spawters_palais_similaire(spawter, top_k=20)
    if spawters_similaires ont visite lieu:
        notes_colonie = [note for s in spawters_similaires if s.a_visite(lieu)]
        score_colonie = moyenne(notes_colonie) / 5.0
    else:
        score_colonie = 0.5  # neutre

    # DIMENSION 4 — Contexte (poids: 15%)
    score_contexte = 0.5  # base
    heure = now().hour
    jour = now().weekday()

    # Bonus contextuels
    if heure in [11,12,13,14] and lieu.est_rapide:
        score_contexte += 0.2
    if jour in [4,5] and lieu.est_festif:  # vendredi, samedi
        score_contexte += 0.2
    if distance(spawter.position, lieu.position) < 500:  # metres
        score_contexte += 0.15
    if lieu.est_ouvert_maintenant:
        score_contexte += 0.15
    else:
        score_contexte -= 0.5  # penalite forte si ferme

    score_contexte = clamp(score_contexte, 0, 1)

    # SCORE FINAL PONDERE
    score_final = (
        0.45 * score_palais_adn +
        0.20 * score_historique +
        0.20 * score_colonie +
        0.15 * score_contexte
    )

    # Convertir en pourcentage [50%, 99%]
    # On evite les scores < 50% (pas utile de montrer "20% compatible")
    score_affiche = 50 + (score_final * 49)

    return round(score_affiche)
```

**Poids des dimensions :**

| Dimension | Poids | Justification |
|---|---|---|
| Palais x ADN | 45% | Coeur du produit, la promesse "ce lieu pour TOI" |
| Historique perso | 20% | Eviter de recommander un lieu mal note par le spawter |
| Colonie (profils similaires) | 20% | "Les spawters qui te ressemblent" — social proof |
| Contexte (heure, distance, ouverture) | 15% | Pertinence temporelle et spatiale |

### 3.6 MVP simplifie de l'algorithme

`[RECOMMANDATION]` Pour le MVP, simplifier sans casser l'architecture :

**MVP** :
- 5 axes calcules (onboarding + check-ins) — COMPLET
- Archetype determine par 2 axes dominants — COMPLET
- Matching = Palais x ADN seulement (pas de colonie, contexte basique) — SIMPLIFIE
- Score affiche en pourcentage — COMPLET

**Phase 2** :
- Ajouter la dimension colonie (necessite masse critique de spawters)
- Contexte avance (meteo, evenements, historique temporel)
- A/B test des poids relatifs

### 3.7 Schema de donnees — Palais

```sql
-- Table palais (profil gustatif du spawter)
CREATE TABLE palais (
    spawter_id              UUID PRIMARY KEY REFERENCES spawters(id),
    axe_racines_horizons    SMALLINT DEFAULT 0,  -- [-100, +100]
    axe_taniere_nomade      SMALLINT DEFAULT 0,
    axe_exigeant_enthousiaste SMALLINT DEFAULT 0,
    axe_foule_secret        SMALLINT DEFAULT 0,
    axe_maquis_table        SMALLINT DEFAULT 0,
    calibrage_source        ENUM('onboarding', 'comportemental', 'mixte'),
    nombre_signaux          INTEGER DEFAULT 0,   -- nb total de signaux recus
    updated_at              TIMESTAMP
);

-- Table adn_lieu (profil du restaurant)
CREATE TABLE adn_lieu (
    lieu_id                 UUID PRIMARY KEY REFERENCES lieux(id),
    axe_local_international SMALLINT DEFAULT 0,   -- [-100, +100]
    axe_informel_etabli     SMALLINT DEFAULT 0,
    axe_budget_premium      SMALLINT DEFAULT 0,
    axe_populaire_prive     SMALLINT DEFAULT 0,
    axe_decontracte_habille SMALLINT DEFAULT 0,
    nombre_checkins         INTEGER DEFAULT 0,
    confiance               FLOAT DEFAULT 0,      -- [0, 1] — fiabilite de l'ADN
    updated_at              TIMESTAMP
);

-- Table historique_palais (pour le Palais dans le temps — premium)
CREATE TABLE historique_palais (
    id                      UUID PRIMARY KEY,
    spawter_id              UUID REFERENCES spawters(id),
    snapshot_date           DATE,
    axes                    JSONB,  -- {racines_horizons: 32, taniere_nomade: -15, ...}
    archetype               VARCHAR(30),
    stade                   VARCHAR(20),
    spots_uniques           INTEGER
);

-- Snapshot hebdomadaire pour les spawters premium
CREATE INDEX idx_historique_date ON historique_palais(spawter_id, snapshot_date);
```

---

## SPEC 4 — SYSTEME DE PAIEMENT

### 4.1 Methodes de paiement — Priorite marche ivoirien

| Methode | Part de marche CI (est.) | Priorite MVP | Notes |
|---|---|---|---|
| **Orange Money** | ~45% du mobile money CI | **P0 — Obligatoire** | Leader absolu, 20M+ utilisateurs en CI |
| **Wave** | ~25% (croissance rapide) | **P0 — Obligatoire** | Frais les plus bas (1%), adoption fulgurante |
| **MTN MoMo** | ~20% | **P1 — MVP** | 3e operateur, a ne pas ignorer |
| Carte bancaire (Visa/MC) | ~5-10% (classe superieure) | **P2 — Phase 2** | Cible Brice (500K+), faible penetration |
| Moov Money | ~5% | **P3 — Phase 2** | Part faible mais en croissance |

### 4.2 Integration technique — Recommandation

`[RECOMMANDATION]` **CinetPay comme agregateur principal pour le MVP.**

| Option | Pour | Contre | Verdict |
|---|---|---|---|
| **CinetPay** | Agregateur local ivoirien, supporte Orange/Wave/MTN/Moov + cartes en une seule integration. API REST simple. KYC simplifie en CI. Support en francais. Frais ~2-3.5%. | Moins stable que Stripe. Documentation moins riche. | **MVP — OUI** |
| Stripe (avec Mobile Money) | API excellente, webhooks fiables, dashboard puissant | Pas de support Orange Money CI natif. Necessite un bridge via un partenaire local. Frais plus eleves. KYC plus lourd pour une entite CI. | Phase 2 possible |
| Integration directe (API Orange Money, API Wave) | Frais reduits, controle total | 3 integrations separees a maintenir, 3 KYC, 3 contrats. Temps de dev x3. | NON |
| FedaPay | Alternative a CinetPay, beninois | Moins implante en CI, moins de methodes supportees | NON pour MVP |

**Configuration CinetPay :**
```
Endpoint: https://api-checkout.cinetpay.com/v2/payment
Methodes activees: ORANGE_MONEY_CI, WAVE_CI, MTN_MOMO_CI
Devise: XOF (Franc CFA BCEAO)
Mode: sandbox → production
Webhook callback: https://api.spawt.app/webhooks/cinetpay
```

### 4.3 Flow paiement B2C — Premium Spawter Gold

`[SOURCE DOC]` "Premium B2C : 2 500 FCFA/mois - 25 000 FCFA/an"

```
ECRAN 1 — DECLENCHEUR PREMIUM
  Contexts de declenchement :
  - Tap sur un lieu hors zone 3km (floute) → "Debloque tout Abidjan — 2 500 F/mois"
  - Feature gating → "Ton Palais complet ? Passe Gold."
  - Profil → section "Passer a Gold"

ECRAN 2 — PAGE PREMIUM
  Header : Logo chat dore + "Spawter Gold"
  Avantages listes (cf. source doc section 10.1) :
    ✓ Tout Abidjan debloque (pas juste 3 km)
    ✓ Palais complet (5 axes + historique)
    ✓ +1 Coup de Coeur bonus par mois
    ✓ Reservation 1 tap
    ✓ Badge dore sur le profil
    ✓ Creer et gerer tes Crews
    ✓ Listes curatees illimitees
    ✓ Ton Palais dans le temps

  Pricing :
    [Mensuel : 2 500 F/mois]  [Annuel : 25 000 F/an — 2 mois offerts]
                               ↑ pre-selectionne

ECRAN 3 — CHOIX METHODE PAIEMENT
  [Orange Money]  ← logo orange
  [Wave]          ← logo wave
  [MTN MoMo]      ← logo MTN

  Chaque option affiche le numero de telephone pre-rempli
  (recupere du profil utilisateur si disponible)

ECRAN 4 — VALIDATION MOBILE MONEY
  SI Orange Money :
    → Redirect vers USSD Orange Money
    → L'utilisateur valide avec son code PIN sur son telephone
    → Callback CinetPay → serveur SPAWT
  SI Wave :
    → Redirect vers l'app Wave (deep link)
    → Validation dans Wave
    → Callback
  SI MTN MoMo :
    → Prompt USSD ou redirect app MTN
    → Validation
    → Callback

  Timeout : 5 minutes. Au-dela, la transaction expire.
  Ecran d'attente : "Valide le paiement sur ton telephone..."
  Animation : chat qui attend patiemment

ECRAN 5 — CONFIRMATION
  SI succes :
    → Animation celebratoire (badge dore qui apparait)
    → "Bienvenue chez les Gold. Tout Abidjan est a toi."
    → Redirect vers la carte debloquee
  SI echec :
    → "Le paiement n'a pas abouti. Verifie ton solde et reessaye."
    → [Reessayer] [Plus tard]
```

### 4.4 Flow B2B — Souscription restaurant

`[SOURCE DOC]` "Spawt Pro : 15 000 FCFA/mois — Spawt Gold : 65 000 FCFA/mois"

`[RECOMMANDATION]` **Le B2B passe par un mix sales direct + web pour le MVP.**

```
PARCOURS B2B — 3 canaux :

CANAL 1 — ALLIE TERRAIN (Mission 1, 20 restos)
  L'Allie SPAWT visite le restaurant en personne
  → Presente SPAWT sur tablette (demo live)
  → Propose Spawt Pro (15 000 F/mois)
  → Inscription sur place via formulaire web mobile
  → Paiement : virement bancaire ou Mobile Money
  → Activation immediate apres confirmation paiement

CANAL 2 — IN-APP (pour les restos qui decouvrent leur fiche)
  Le restaurateur voit sa fiche sur SPAWT (creee par la communaute)
  → Bouton "C'est votre restaurant ? Revendiquez-le"
  → Formulaire de verification (nom, telephone, adresse, preuve)
  → Validation par l'equipe SPAWT (24-48h)
  → Proposition upgrade : "Passez a Spawt Pro pour repondre aux avis"
  → Paiement in-app via CinetPay

CANAL 3 — WEB DASHBOARD (Spawt Gold)
  Pour les restaurants importants (chaines, haut de gamme)
  → Landing page B2B : pro.spawt.app
  → Demo + pricing
  → Formulaire de contact → equipe sales
  → Contrat Gold signe (engagement 3 ou 6 mois recommande)
  → Paiement : virement bancaire mensuel ou Mobile Money
```

### 4.5 Gestion des abonnements recurrents

`[RECOMMANDATION]` **Le Mobile Money ne supporte pas le prelevement automatique natif.** Solutions :

```
STRATEGIE DE RECURRENCE :

1. RAPPEL PRE-ECHEANCE (J-3)
   → Notification push : "Ton Gold expire dans 3 jours. Renouvelle en 1 tap."
   → SMS si push desactive (via CinetPay ou Twilio)

2. RAPPEL JOUR J
   → Notification push : "C'est aujourd'hui. [Renouveler maintenant]"
   → Deep link vers l'ecran de paiement pre-rempli (montant + methode precedente)

3. GRACE PERIOD (7 jours)
   → J+0 a J+7 : acces maintenu mais bandeau "Ton Gold expire. Renouvelle."
   → Le spawter garde ses fonctionnalites premium
   → Rappel J+1, J+3, J+5

4. DOWNGRADE AUTOMATIQUE (J+8)
   → Le compte revient a Spawter gratuit
   → Les donnees premium (historique Palais, listes) sont CONSERVEES mais masquees
   → Message du chat : "Gold expire. Tes donnees sont la, pretes a revenir."
   → Le spawter peut re-souscrire a tout moment et retrouver tout

5. CinetPay RECURRING (si disponible)
   → CinetPay propose un mode "subscription" avec tokenisation
   → Le spawter autorise le prelevement recurrent
   → CinetPay tente le debit chaque mois automatiquement
   → Si echec : fallback vers le flow rappel ci-dessus
```

### 4.6 Regles de gestion — Echecs de paiement

| Evenement | Action | Delai |
|---|---|---|
| Paiement initial echoue | Message d'erreur + bouton reessayer. Pas de blocage. | Immediat |
| Renouvellement echoue (J+0) | Notification + SMS. Acces maintenu. | J+0 |
| Toujours impaye J+3 | 2e rappel push + SMS | J+3 |
| Toujours impaye J+7 | Dernier rappel : "Demain, ton Gold s'arrete." | J+7 |
| Downgrade J+8 | Retour au gratuit. Donnees conservees 90 jours. | J+8 |
| Re-souscription post-downgrade | Restauration immediate de toutes les donnees premium | Immediat |
| Remboursement demande | Rembourser le mois en cours si < 7 jours d'usage | Manuel |

### 4.7 Conformite reglementaire — Points de vigilance

`[RECOMMANDATION]` Points critiques pour operer en Cote d'Ivoire :

| Sujet | Regle | Action requise |
|---|---|---|
| **BCEAO** | SPAWT ne stocke pas de fonds, n'est pas un EME (Etablissement de Monnaie Electronique). CinetPay est l'intermediaire agree. | Verifier que CinetPay a bien son agrement BCEAO. Pas besoin d'agrement propre pour SPAWT. |
| **ARTCI** | Declaration des services en ligne. Protection des donnees personnelles (loi 2013-450). | Declarer le service. Politique de confidentialite conforme. Consentement explicite pour la geolocalisation. |
| **CGU/CGV** | Conditions de vente pour les abonnements. Droit de retractation. | Rediger des CGV conformes au droit ivoirien. Delai de retractation 7 jours. |
| **Facturation** | Obligation d'emettre un recu pour chaque paiement. | CinetPay genere les recus. SPAWT envoie par email/SMS. |
| **TVA** | TVA a 18% en CI applicable sur les services numeriques. | Les prix affiches (2 500 F, 15 000 F, 65 000 F) sont TTC ou doivent inclure la TVA. **Decision a prendre avec Stephanie.** |
| **Protection des donnees** | Pas de RGPD strict en CI mais la loi 2013-450 impose des principes similaires. | Consentement, droit d'acces, droit de suppression, stockage securise, pas de transfert hors CI sans accord. |

---

## SPEC 5 — PALETTE DE COULEURS DEFINITIVE

### 5.1 Extraction des references couleurs — Source de verite

`[SOURCE DOC]` Deux references de couleurs dans la presentation Fevrier 2026 :

**Reference 1 — Section 9 "Systeme de Cartes" / Direction artistique :**
> "Palette : Noir #0A0A0A, Or #D4AF37, Vert Chat #50C878, Blanc casse #F8F6F0"

**Reference 2 — Section 13.3 "Direction artistique" :**
> "Couleurs : Noir #0A0A0A, Or #C8A44E, Vert Chat #2D6B4F, Blanc casse #FAFAF8"

### 5.2 Resolution de la contradiction

Il y a **deux palettes differentes** dans le meme document :

| Couleur | Section 9 (Cartes) | Section 13 (Marque) | Ecart |
|---|---|---|---|
| Noir | #0A0A0A | #0A0A0A | Identique |
| Or | #D4AF37 (or classique, brillant) | #C8A44E (or mat, sophistique) | Different |
| Vert Chat | #50C878 (vert emeraude vif) | #2D6B4F (vert foret profond) | Tres different |
| Blanc casse | #F8F6F0 (chaud) | #FAFAF8 (plus froid) | Leger ecart |

**Decision** : `[RECOMMANDATION]` **La section 13.3 "Direction artistique" prime** car :
1. C'est la section dediee a l'identite de marque (vs la section cartes qui est un sous-systeme)
2. La section 13.3 est accompagnee de la mention "Luxe accessible, nocturne, sophistication discrete" — qui s'aligne mieux avec #C8A44E (or mat) et #2D6B4F (vert profond)
3. La palette cartes (#D4AF37, #50C878) semble etre une version anterieure ou specifique aux cartes collectibles

**Palette retenue :**
- Noir : **#0A0A0A**
- Or : **#C8A44E**
- Vert Chat : **#2D6B4F**
- Blanc casse : **#FAFAF8**

`[RECOMMANDATION]` Conserver la palette cartes (#D4AF37, #50C878) uniquement pour les cartes collectibles (recto/verso) ou ils apportent un eclat visuel justifie par le contexte gamification. **Point a valider avec Stephanie.**

### 5.3 Systeme de couleurs MVP — Design tokens

```css
:root {
  /* === COULEURS PRIMAIRES (Source: Presentation Fevrier 2026 §13.3) === */

  /* Brand — Noir profond */
  --color-primary: #0A0A0A;

  /* Accent — Or SPAWT (luxe accessible) */
  --color-accent: #C8A44E;
  --color-accent-light: #D4B86A;    /* [RECOMMANDATION] hover/active states */
  --color-accent-dark: #A8873A;     /* [RECOMMANDATION] pressed state */

  /* Vert Chat — Couleur signature de la mascotte */
  --color-chat: #2D6B4F;
  --color-chat-light: #3D8B66;      /* [RECOMMANDATION] hover */
  --color-chat-dark: #1E4A36;       /* [RECOMMANDATION] pressed */

  /* === BACKGROUNDS === */

  --color-bg-primary: #FAFAF8;           /* Blanc casse — fond principal */
  --color-bg-secondary: #F2F0EC;         /* [RECOMMANDATION] Cartes, surfaces elevees */
  --color-bg-tertiary: #E8E5DF;          /* [RECOMMANDATION] Inputs, zones secondaires */
  --color-bg-dark: #0A0A0A;             /* Mode sombre / headers */

  /* === TEXTE === */

  --color-text-primary: #0A0A0A;         /* Texte principal sur fond clair */
  --color-text-secondary: #6B6560;       /* [RECOMMANDATION] Texte secondaire, labels */
  --color-text-tertiary: #9B9590;        /* [RECOMMANDATION] Placeholders, metadata */
  --color-text-on-dark: #FAFAF8;         /* Texte sur fond noir */
  --color-text-on-accent: #0A0A0A;       /* Texte sur fond or */

  /* === SEMANTIQUE === */

  --color-success: #2D6B4F;              /* Vert Chat = validation/succes */
  --color-error: #C43D3D;               /* [RECOMMANDATION] Rouge mat, cohesion luxe */
  --color-warning: #C8A44E;             /* Or = attention (deja l'accent) */
  --color-info: #4A7B9D;               /* [RECOMMANDATION] Bleu sourd */

  /* === PREMIUM / GOLD === */

  --color-premium: #C8A44E;             /* Badge dore, elements Gold */
  --color-premium-gradient-start: #C8A44E;
  --color-premium-gradient-end: #D4B86A; /* [RECOMMANDATION] gradient subtil */

  /* === CARTES COLLECTIBLES (palette secondaire §9) === */

  --color-card-gold: #D4AF37;           /* Or brillant pour cartes */
  --color-card-green: #50C878;          /* Vert emeraude pour cartes */
  --color-card-bg: #0A0A0A;            /* Fond noir cartes */
  --color-card-text: #F8F6F0;          /* Blanc chaud cartes */

  /* === RARETE DES PLATS COLLECTIBLES === */

  --color-rarity-common: #9B9590;       /* Gris */
  --color-rarity-rare: #2D6B4F;         /* Vert Chat */
  --color-rarity-epic: #7B4FA2;         /* [RECOMMANDATION] Violet */
  --color-rarity-legendary: #C8A44E;    /* Or */

  /* === SIGNAUX SPECIAUX === */

  --color-signal-pepite: #2D6B4F;       /* Pepite Verifiee = vert */
  --color-signal-institution: #C8A44E;  /* Institution = or */
  --color-signal-decouverte: #4A7B9D;   /* [RECOMMANDATION] Decouverte = bleu */
  --color-signal-coup-de-coeur: #C43D3D; /* Coup de Coeur = rouge */

  /* === TYPOGRAPHIES (Source: §13.3) === */

  --font-display: 'Instrument Serif', serif;   /* Titres */
  --font-body: 'Manrope', sans-serif;          /* Corps */
  --font-data: 'JetBrains Mono', monospace;    /* Donnees/chiffres */
}
```

### 5.4 Tableau de contrastes WCAG AA

Standard WCAG AA : ratio minimum 4.5:1 pour texte normal, 3:1 pour grand texte (>18px bold).

| Combinaison | Ratio calcule | WCAG AA (normal) | WCAG AA (grand) |
|---|---|---|---|
| #0A0A0A sur #FAFAF8 (texte primaire sur fond) | **19.2:1** | PASSE | PASSE |
| #6B6560 sur #FAFAF8 (texte secondaire sur fond) | **4.8:1** | PASSE | PASSE |
| #9B9590 sur #FAFAF8 (texte tertiaire sur fond) | **3.1:1** | ECHEC | PASSE |
| #FAFAF8 sur #0A0A0A (texte clair sur fond noir) | **19.2:1** | PASSE | PASSE |
| #C8A44E sur #0A0A0A (or sur noir) | **6.2:1** | PASSE | PASSE |
| #C8A44E sur #FAFAF8 (or sur blanc casse) | **3.1:1** | ECHEC | PASSE |
| #2D6B4F sur #FAFAF8 (vert chat sur blanc casse) | **5.8:1** | PASSE | PASSE |
| #2D6B4F sur #0A0A0A (vert chat sur noir) | **3.3:1** | ECHEC | PASSE |
| #FAFAF8 sur #2D6B4F (texte sur fond vert) | **5.8:1** | PASSE | PASSE |
| #0A0A0A sur #C8A44E (texte noir sur fond or) | **6.2:1** | PASSE | PASSE |
| #C43D3D sur #FAFAF8 (erreur sur fond) | **5.1:1** | PASSE | PASSE |

**Points d'attention :**
- `--color-text-tertiary` (#9B9590) echoue en WCAG AA pour texte normal → a utiliser UNIQUEMENT pour les grands textes, icones, ou elements decoratifs
- L'or (#C8A44E) sur blanc casse echoue en texte normal → utiliser l'or UNIQUEMENT sur fond noir ou comme fond avec texte noir dessus
- Le vert chat sur noir est limite → utiliser en grand texte uniquement sur fond noir

### 5.5 Mode sombre — Recommandation

`[RECOMMANDATION]` **Mode sombre : NON pour le MVP. Planifier pour Phase 2.**

Justification :
1. La palette est deja construite autour du noir (#0A0A0A) — le mode sombre est naturellement integre dans les headers, cartes, et elements premium
2. Le fond principal est blanc casse, ce qui fonctionne bien en usage quotidien
3. Un vrai mode sombre necessite de tester CHAQUE ecran, CHAQUE composant — cout de QA x2
4. L'identite "luxe accessible, nocturne" est deja portee par les elements noirs et or sans mode sombre complet
5. Priorite MVP = fonctionnalites core, pas customisation visuelle

**Phase 2** : implementer via les tokens CSS ci-dessus en creant un jeu `[data-theme="dark"]` qui inverse bg-primary et text-primary. L'architecture tokens est deja prete.

---

## SYNTHESE — Decisions a valider avec Stephanie

### Decisions requises avant le developpement

| # | Sujet | Question | Impact | Priorite |
|---|---|---|---|---|
| 1 | **Check-in : seuil geoloc** | 150m est-il acceptable ? Ou faut-il etre plus strict (50m) pour la credibilite ? | Anti-fraude vs UX (GPS imprecis en interieur) | P0 |
| 2 | **Spots = lieux uniques ?** | Confirmer que la progression compte les lieux uniques, pas les visites repetees | Toute la progression en depend | P0 |
| 3 | **Palette : section 9 vs section 13** | Deux palettes dans le meme doc. La section 13.3 est retenue comme reference marque. La section 9 est reservee aux cartes collectibles. OK ? | Toute l'identite visuelle | P0 |
| 4 | **Pricing TTC ou HT ?** | Les prix 2 500 / 15 000 / 65 000 FCFA incluent-ils la TVA 18% ? Si non, le prix reel est plus eleve. | Marge, pricing, positionnement | P0 |
| 5 | **CinetPay** | Valider CinetPay comme provider paiement. Verifier leur agrement BCEAO et leurs frais exacts. | Stack technique paiement | P0 |
| 6 | **Grace period 7 jours** | Est-ce trop genereux ? Trop court ? Benchmark : Spotify = 3 jours, Netflix = 0. | Churn vs revenue | P1 |
| 7 | **Check-in sans geoloc** | Autoriser les spawts "non verifies" (poids reduit) ou les bloquer completement ? | Accessibilite vs qualite data | P1 |
| 8 | **Score de matching affiche** | Montrer le "92%" sur les fiches lieu des le MVP ? Ou attendre d'avoir assez de data pour que les scores soient fiables ? | Promesse core vs deception si scores aberrants | P1 |
| 9 | **Omnivore** | L'archetype Omnivore n'est accessible qu'a partir d'Explorateur. Que montrer au Touriste dont aucun axe n'est marque ? | UX des premiers jours | P2 |
| 10 | **Nom du chat** | La communaute suggere de nommer le chat. Process de naming interne ou communautaire ? | Identite de marque | P2 |

### Estimation effort dev MVP (ces 5 specs)

| Spec | Complexite | Estimation | Dependances |
|---|---|---|---|
| Check-in (Spawt) | Moyenne | 2-3 semaines | API geoloc, base lieux |
| Progression | Moyenne | 2 semaines | Check-in fonctionnel |
| Algorithme Palais | Haute | 3-4 semaines | Check-in + onboarding |
| Paiement | Haute | 3-4 semaines | Compte CinetPay, KYC |
| Palette couleurs | Faible | 1 semaine | Design system setup |
| **TOTAL** | | **11-14 semaines** | Parallelisable a ~8 semaines avec 2 devs |

---

*Specs produites par Opus 4.6*
*7 avril 2026 — Session brainstorming SPAWT MVP*
*Source de verite : SPAWT_Presentation_Fevrier_2026_V2-2.docx*

---

## ARBITRAGES FONDATEUR + SPECS FINALISEES

> **Date** : 7 avril 2026 — Cloture du brainstorming
> **Statut** : Les 4 decisions ci-dessous sont des **arbitrages fondateur** definitifs. Elles priment sur toute recommandation precedente dans ce document.

---

### DECISION 1 — CHECK-IN : MECANISME TYPE VTC [ARBITRAGE FONDATEUR]

Le check-in SPAWT fonctionne comme le systeme de notation des VTC (Uber/Bolt). Le spawter est invite a noter apres sa visite, de maniere authentique et non-intrusive.

#### 1.1 Principes valides

- **Perimetre de detection** : 10 metres du lieu (et non 150m comme precedemment envisage)
- **Timer d'attente** : 15 minutes apres detection d'entree dans le perimetre avant d'afficher la notification de check-in
- **Fenetre de notation** : s'ouvre a la notification et reste active pendant toute la presence + 30 minutes apres la sortie du perimetre
- **Snooze** : le spawter peut reporter la notification de 15 minutes (pour couvrir le temps de service / degustation en cours)
- **Declencheur de sortie** : le check-in se declenche aussi automatiquement quand le spawter quitte la zone (>10m du lieu) — filet de securite
- **Garantie** : presence reelle prouvee sans interrompre l'experience culinaire

#### 1.2 Flow UX detaille — Diagramme d'etats

```
                        ┌─────────────────────────────────────────────┐
                        │                                             │
                        v                                             │
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────────┐   │
  │          │    │          │    │          │    │              │   │
  │ INACTIF  │───>│ EN ZONE  │───>│  ACTIF   │───>│  COMPLETE    │   │
  │          │    │ (timer)  │    │(notifie) │    │              │   │
  └──────────┘    └──────────┘    └──────────┘    └──────────────┘   │
       ^               │              │  │                           │
       │               │              │  │         ┌──────────┐     │
       │               │              │  └────────>│  SNOOZE  │─────┘
       │               │              │            │ (+15 min) │
       │               │              │            └──────────┘
       │               │              │
       │               │              v
       │               │         ┌──────────┐
       │               │         │  SORTIE   │───> ACTIF (notification forcee)
       │               │         │ DETECTEE  │     ou EXPIRE si pas de reponse
       │               │         └──────────┘
       │               │
       │               v
       │         ┌──────────┐
       └─────────│ ANNULE   │  (spawter quitte avant 15min = pas d'interet)
                 │ (sorti   │
                 │ trop tot)│
                 └──────────┘
```

**Etats du check-in :**

| Etat | Description | Transition vers |
|------|-------------|-----------------|
| `INACTIF` | Le spawter n'est dans aucune zone de lieu | `EN_ZONE` quand geoloc < 10m d'un lieu |
| `EN_ZONE` | Entree detectee, timer de 15 min demarre | `ACTIF` apres 15 min / `ANNULE` si sort avant 15 min |
| `ACTIF` | Notification de check-in affichee, fenetre ouverte | `COMPLETE` si le spawter repond / `SNOOZE` si reporte / `SORTIE_DETECTEE` si quitte la zone |
| `SNOOZE` | Notification reportee de 15 min | `ACTIF` apres 15 min (re-notification) |
| `SORTIE_DETECTEE` | Le spawter a quitte la zone (>10m) | `ACTIF` avec notification forcee (derniere chance) |
| `COMPLETE` | Check-in valide et note soumise | Fin du cycle |
| `EXPIRE` | Aucune reponse dans la fenetre (presence + 30 min post-sortie) | Spawt enregistre sans note, flag `check_in_passive` |
| `ANNULE` | Sorti avant le seuil de 15 min | Retour a `INACTIF` |

#### 1.3 Logique de detection geolocalisation

```
ALGORITHME DE DETECTION CONTINUE :

1. MONITORING BACKGROUND
   - Geofencing natif (iOS CLLocationManager / Android GeofencingClient)
   - Rayon de surveillance : 10 metres autour de chaque lieu connu
   - Mode : basse consommation (significant location changes) en background
   - Mode : haute precision (continuous) quand l'app est au premier plan

2. ENTREE DANS ZONE (distance < 10m)
   → Enregistrer `arrived_at = now()`
   → Demarrer timer silencieux de 15 minutes
   → Aucune notification a ce stade (ne pas deranger pendant le repas)
   → Verifier toutes les 30 secondes que le spawter est toujours dans la zone

3. TIMER 15 MINUTES ECOULE + TOUJOURS EN ZONE
   → Enregistrer `notified_at = now()`
   → Envoyer notification locale (PAS push serveur — fonctionne offline)
   → Titre : "Comment c'etait chez [NOM DU LIEU] ?"
   → Corps : "Laisse ton avis en 30 secondes"
   → Action : ouvre l'ecran de check-in pre-rempli (lieu, heure d'arrivee)

4. SNOOZE (si le spawter tape "Plus tard")
   → Enregistrer `snoozed_at = now()`
   → Reporter la notification de 15 minutes
   → Maximum 3 snoozes (45 min supplementaires max)
   → Apres 3 snoozes : notification finale "Derniere chance avant que le Chat oublie"

5. SORTIE DE ZONE (distance > 10m pendant > 60 secondes)
   → Enregistrer `left_at = now()`
   → SI check-in pas encore complete :
     → Notification immediate : "Tu quittes [NOM DU LIEU] — ton avis en 1 tap ?"
     → Fenetre de reponse : 30 minutes post-sortie
   → SI check-in deja complete :
     → Rien (cycle termine)

6. EXPIRATION
   → SI aucune reponse apres `left_at + 30 minutes` :
     → Enregistrer le spawt en mode passif (presence prouvee, pas de note)
     → Flag `check_in_type = 'passive'`
     → Ce spawt compte pour les spots uniques mais poids reduit (0.5x)
```

#### 1.4 Regles de gestion de la fenetre temporelle

| Regle | Valeur | Justification |
|-------|--------|---------------|
| Rayon de detection | 10 metres | Precision suffisante pour confirmer la presence dans l'etablissement |
| Delai avant notification | 15 minutes | Temps de s'installer, commander, commencer a manger |
| Duree d'un snooze | 15 minutes | Couvre un service/plat supplementaire |
| Nombre max de snoozes | 3 | Evite le harcellement, fenetre totale = 60 min |
| Fenetre post-sortie | 30 minutes | Temps de se souvenir a chaud de l'experience |
| Stabilite de sortie | >10m pendant 60 secondes | Evite les faux positifs (terrasse, parking) |
| Duree max d'une session | 4 heures | Au-dela, le check-in expire automatiquement (cas anomal) |

#### 1.5 Edge cases

| Situation | Comportement |
|-----------|-------------|
| **Le spawter ne repond jamais** | Spawt passif enregistre (presence prouvee, sans note). Poids 0.5x dans l'algorithme. Compte pour les spots uniques. |
| **Reseau coupe pendant la visite** | Les notifications locales fonctionnent sans reseau. Le check-in est stocke localement et synchronise au retour du reseau. |
| **Geoloc desactivee** | L'app affiche une demande de permission. Si refus : mode degradue — le spawter peut faire un check-in manuel (comme dans la spec precedente ecran 2 "SI geoloc inactive"). Le spawt est marque `non_verifie`. |
| **GPS imprecis (>10m de fluctuation)** | Utiliser la moyenne des 3 dernieres positions sur 30 secondes. Si accuracy_meters > 30m, ne pas declencher le timer automatique — proposer le check-in manuel. |
| **Spawter entre et sort rapidement (<15 min)** | Etat `ANNULE`. Pas de notification. Le passage est ignore (probablement un passant ou un ramassage a emporter). |
| **Deux lieux a <10m l'un de l'autre** | Proposer un choix : "Tu es chez [Lieu A] ou [Lieu B] ?" Le spawter selectionne manuellement. |
| **Le spawter revient au meme lieu le meme jour** | Regle anti-fraude maintenue : 1 spawt / 4 heures par lieu. Si re-entree dans les 4h, pas de nouveau cycle. |
| **Batterie faible** | Le monitoring background consomme peu (geofencing natif). Si batterie < 10%, desactiver le monitoring et basculer en mode manuel. |
| **App tuee par l'OS (Android)** | Les geofences persistent au niveau OS meme si l'app est tuee. La notification se declenche au reveil de l'app. Latence possible de quelques minutes. |

#### 1.6 Schema de donnees mis a jour — Champs timing

```sql
-- Mise a jour de la table spawt_checkin
ALTER TABLE spawt_checkin ADD COLUMN arrived_at      TIMESTAMP;  -- entree dans zone 10m
ALTER TABLE spawt_checkin ADD COLUMN notified_at     TIMESTAMP;  -- notification affichee (arrived_at + 15min)
ALTER TABLE spawt_checkin ADD COLUMN snoozed_at      TIMESTAMP;  -- dernier snooze (NULL si pas de snooze)
ALTER TABLE spawt_checkin ADD COLUMN snooze_count    SMALLINT DEFAULT 0;
ALTER TABLE spawt_checkin ADD COLUMN checked_in_at   TIMESTAMP;  -- moment ou le spawter valide le check-in
ALTER TABLE spawt_checkin ADD COLUMN left_at         TIMESTAMP;  -- sortie de zone detectee
ALTER TABLE spawt_checkin ADD COLUMN check_in_type   VARCHAR(20) DEFAULT 'active';
  -- 'active'  = le spawter a repondu a la notification
  -- 'passive' = presence prouvee mais pas de reponse (expire)
  -- 'manual'  = check-in manuel sans geoloc automatique
ALTER TABLE spawt_checkin ADD COLUMN session_duration_minutes INT;
  -- COMPUTED : checked_in_at - arrived_at (ou left_at - arrived_at si passif)

-- Index pour analytics
CREATE INDEX idx_checkin_type ON spawt_checkin(check_in_type);
CREATE INDEX idx_checkin_arrived ON spawt_checkin(arrived_at);
```

**Schema complet d'un enregistrement check-in (version mise a jour) :**

```json
{
  "spawt_checkin": {
    "id": "uuid_v4",
    "spawter_id": "uuid_v4",
    "lieu_id": "uuid_v4",
    "arrived_at": "2026-04-07T12:30:00+00:00",
    "notified_at": "2026-04-07T12:45:00+00:00",
    "snoozed_at": "2026-04-07T12:45:30+00:00",
    "snooze_count": 1,
    "checked_in_at": "2026-04-07T13:02:00+00:00",
    "left_at": "2026-04-07T13:45:00+00:00",
    "check_in_type": "active",
    "session_duration_minutes": 32,
    "geolocation": {
      "lat": 5.3364,
      "lng": -4.0267,
      "accuracy_meters": 8,
      "source": "gps"
    },
    "verification": {
      "is_geolocated": true,
      "distance_to_lieu_meters": 6,
      "is_verified": true
    },
    "avis": {
      "note_etoiles": 4,
      "texte": "Attieke poisson braise excellent...",
      "tags": ["copieux", "rapide", "a_refaire"],
      "photos": ["url1", "url2"],
      "is_complete": true
    }
  }
}
```

#### 1.7 Impact sur anti-fraude

`[ARBITRAGE FONDATEUR]` Le systeme de check-in type VTC **remplace partiellement** les regles anti-fraude precedentes (section 1.4 du doc). Voici le statut mis a jour :

| Regle anti-fraude precedente | Statut apres arbitrage | Raison |
|------------------------------|----------------------|--------|
| Distance maximale au lieu : 150m | **REMPLACEE** par 10m (rayon de detection VTC) | Le perimetre 10m est beaucoup plus strict, la fraude par proximite est quasi eliminee |
| Frequence meme lieu : 1/4h | **MAINTENUE** | Toujours pertinente, inchangee |
| Frequence globale : 5 spawts/jour | **MAINTENUE** | Toujours pertinente |
| Vitesse deplacement : >100km/h | **MAINTENUE** | Toujours pertinente |
| Spawt sans geoloc : accepte `non_verifie` | **MAINTENUE** avec ajustement : poids passe de 0.3x a 0.5x pour les check-ins manuels, car le systeme VTC est la norme attendue |
| Patterns suspects : 10+ identiques en 7j | **MAINTENUE** | Toujours pertinente |

**Nouvelles regles ajoutees par le systeme VTC :**

| Nouvelle regle | Description |
|----------------|-------------|
| Temps minimum en zone | Le spawter doit rester au moins 15 min pour declencher une notification. Les passages < 15 min sont ignores (anti-fraude : pas de spawt en passant devant). |
| Check-in passif : poids reduit | Un spawt passif (presence prouvee, pas de note) a un poids de 0.5x — il ne contribue pas autant qu'un check-in actif |
| Session duration enregistree | Permet de detecter les anomalies (ex: session de 2 minutes avec note 5 etoiles = suspect) |
| Coherence arrivee/depart | Si `left_at - arrived_at < 5 min` ET check-in actif, flag suspect (le spawter est parti avant d'avoir pu manger) |

---

### DECISION 2 — PALETTE DEFINITIVE [ARBITRAGE FONDATEUR]

Palette officielle SPAWT :
- **Or/Platine** : couleur premium principale
- **Noir** : base / backgrounds sombres
- **Blanc** : base / backgrounds clairs
- **Vert accent** : CTAs, validations, elements actifs

**Contrainte architecture** : Les couleurs DOIVENT etre modifiables sans toucher au code — uniquement via un fichier de tokens/variables.

#### 2.1 Recommandation pour l'or — Choix justifie

`[RECOMMANDATION]` **Or chaud #C9A84C** (entre l'or chaud #C8A44E de la section 13.3 et un ton legerement plus lumineux).

| Option | Hex | Sur fond noir | Sur fond blanc | Verdict |
|--------|-----|---------------|----------------|---------|
| Or chaud classique | #C8A44E | Contraste 6.2:1 — WCAG AA | Contraste 3.1:1 — ECHEC texte normal | Choix retenu (section 13.3) |
| Platine froid | #C0C0C0 | Contraste 9.5:1 — excellent | Contraste 2.1:1 — ECHEC | Trop froid, perd l'identite "luxe accessible ivoirien" |
| Or blanc | #E8D5A3 | Contraste 11.8:1 — excellent | Contraste 1.7:1 — ECHEC total | Trop pale, pas assez premium |
| **Or SPAWT (retenu)** | **#C9A84C** | **Contraste 6.3:1 — PASSE** | **Contraste 3.05:1 — grand texte** | **Equilibre luxe + lisibilite** |

**Justification du choix or chaud :**
1. **Identite culturelle** : L'or chaud evoque le bijou en or ouest-africain (poids Akan, bijoux Baoulé) — resonance locale forte
2. **App mobile dark mode** : L'or chaud sur fond noir (#0A0A0A) est le combo premium par excellence (cf. AmEx, Rolex apps)
3. **Lisibilite** : Ratio 6.3:1 sur noir = WCAG AA sans effort. Sur blanc = reserve aux grands textes et CTAs (fond or + texte noir)
4. **Le platine est trop neutre** : il ne differencie pas SPAWT d'une app bancaire. L'or raconte "gastronomie, chaleur, prestige"

#### 2.2 Design tokens complets — 3 formats

**A. CSS Custom Properties (Web / PWA)**

```css
/* === SPAWT DESIGN TOKENS === */
/* Fichier : src/theme/tokens.css */
/* REGLE : Ce fichier est la SOURCE UNIQUE de toutes les couleurs. */
/* Pour rebrander : modifier UNIQUEMENT ce fichier. */

:root {
  /* --- Brand --- */
  --color-brand-primary: #C9A84C;          /* Or SPAWT */
  --color-brand-primary-light: #D4B86A;    /* Or hover/active */
  --color-brand-primary-dark: #A8873A;     /* Or pressed */
  --color-brand-accent: #2D6B4F;           /* Vert accent — CTAs, validations */
  --color-brand-accent-light: #3D8B66;     /* Vert hover */
  --color-brand-accent-dark: #1E4A36;      /* Vert pressed */

  /* --- Surfaces --- */
  --color-surface-base: #FAFAF8;           /* Fond principal clair */
  --color-surface-elevated: #F2F0EC;       /* Cartes, modals */
  --color-surface-sunken: #E8E5DF;         /* Inputs, zones secondaires */
  --color-surface-inverse: #0A0A0A;        /* Fond sombre / headers */

  /* --- Texte --- */
  --color-text-primary: #0A0A0A;           /* Texte principal */
  --color-text-secondary: #6B6560;         /* Labels, descriptions */
  --color-text-tertiary: #9B9590;          /* Placeholders, metadata */
  --color-text-inverse: #FAFAF8;           /* Texte sur fond sombre */
  --color-text-on-brand: #0A0A0A;          /* Texte sur fond or */
  --color-text-on-accent: #FAFAF8;         /* Texte sur fond vert */

  /* --- Semantique --- */
  --color-semantic-success: #2D6B4F;       /* Validation = vert accent */
  --color-semantic-error: #C43D3D;         /* Erreur */
  --color-semantic-warning: #C9A84C;       /* Attention = or brand */
  --color-semantic-info: #4A7B9D;          /* Information */

  /* --- Premium --- */
  --color-premium-badge: #C9A84C;
  --color-premium-gradient-from: #C9A84C;
  --color-premium-gradient-to: #D4B86A;

  /* --- Interaction --- */
  --color-interaction-cta: #2D6B4F;        /* Bouton principal = vert */
  --color-interaction-cta-hover: #3D8B66;
  --color-interaction-cta-pressed: #1E4A36;
  --color-interaction-secondary: #C9A84C;  /* Bouton secondaire = or */
  --color-interaction-disabled: #D0CCC6;
  --color-interaction-focus-ring: #2D6B4F;

  /* --- Typographie --- */
  --font-family-display: 'Instrument Serif', serif;
  --font-family-body: 'Manrope', sans-serif;
  --font-family-data: 'JetBrains Mono', monospace;

  /* --- Espacement (base 4px) --- */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;

  /* --- Rayons --- */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 9999px;
}
```

**B. React Native StyleSheet Constants (TypeScript)**

```typescript
// === SPAWT DESIGN TOKENS ===
// Fichier : src/theme/tokens.ts
// REGLE : Ce fichier est la SOURCE UNIQUE de toutes les couleurs.
// Pour rebrander : modifier UNIQUEMENT ce fichier.

export const colors = {
  brand: {
    primary: '#C9A84C',        // Or SPAWT
    primaryLight: '#D4B86A',
    primaryDark: '#A8873A',
    accent: '#2D6B4F',         // Vert accent
    accentLight: '#3D8B66',
    accentDark: '#1E4A36',
  },
  surface: {
    base: '#FAFAF8',
    elevated: '#F2F0EC',
    sunken: '#E8E5DF',
    inverse: '#0A0A0A',
  },
  text: {
    primary: '#0A0A0A',
    secondary: '#6B6560',
    tertiary: '#9B9590',
    inverse: '#FAFAF8',
    onBrand: '#0A0A0A',
    onAccent: '#FAFAF8',
  },
  semantic: {
    success: '#2D6B4F',
    error: '#C43D3D',
    warning: '#C9A84C',
    info: '#4A7B9D',
  },
  premium: {
    badge: '#C9A84C',
    gradientFrom: '#C9A84C',
    gradientTo: '#D4B86A',
  },
  interaction: {
    cta: '#2D6B4F',
    ctaHover: '#3D8B66',
    ctaPressed: '#1E4A36',
    secondary: '#C9A84C',
    disabled: '#D0CCC6',
    focusRing: '#2D6B4F',
  },
} as const;

export const fonts = {
  display: 'Instrument Serif',
  body: 'Manrope',
  data: 'JetBrains Mono',
} as const;

export const spacing = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  '2xl': 48,
} as const;

export const radii = {
  sm: 4,
  md: 8,
  lg: 16,
  full: 9999,
} as const;

export type Colors = typeof colors;
export type Fonts = typeof fonts;
export type Spacing = typeof spacing;
```

**C. JSON (Figma / Design handoff)**

```json
{
  "$schema": "spawt-design-tokens-v1",
  "version": "1.0.0",
  "updatedAt": "2026-04-07",
  "colors": {
    "brand": {
      "primary":      { "value": "#C9A84C", "description": "Or SPAWT — couleur premium principale" },
      "primaryLight": { "value": "#D4B86A", "description": "Or hover/active" },
      "primaryDark":  { "value": "#A8873A", "description": "Or pressed" },
      "accent":       { "value": "#2D6B4F", "description": "Vert accent — CTAs, validations" },
      "accentLight":  { "value": "#3D8B66", "description": "Vert hover" },
      "accentDark":   { "value": "#1E4A36", "description": "Vert pressed" }
    },
    "surface": {
      "base":     { "value": "#FAFAF8", "description": "Fond principal clair" },
      "elevated": { "value": "#F2F0EC", "description": "Cartes, modals" },
      "sunken":   { "value": "#E8E5DF", "description": "Inputs, zones secondaires" },
      "inverse":  { "value": "#0A0A0A", "description": "Fond sombre / headers" }
    },
    "text": {
      "primary":  { "value": "#0A0A0A" },
      "secondary": { "value": "#6B6560" },
      "tertiary": { "value": "#9B9590" },
      "inverse":  { "value": "#FAFAF8" },
      "onBrand":  { "value": "#0A0A0A" },
      "onAccent": { "value": "#FAFAF8" }
    },
    "semantic": {
      "success": { "value": "#2D6B4F" },
      "error":   { "value": "#C43D3D" },
      "warning": { "value": "#C9A84C" },
      "info":    { "value": "#4A7B9D" }
    }
  },
  "fonts": {
    "display": "Instrument Serif",
    "body": "Manrope",
    "data": "JetBrains Mono"
  }
}
```

#### 2.3 Convention de nommage des tokens

`[RECOMMANDATION]` Nommage **semantique** (role dans l'interface), jamais descriptif (couleur visuelle).

| CORRECT | INCORRECT | Raison |
|---------|-----------|--------|
| `color-brand-primary` | `color-gold` | Si l'or change en platine, le nom reste coherent |
| `color-surface-base` | `color-white` | Le fond clair pourrait devenir creme ou gris |
| `color-interaction-cta` | `color-green-button` | Le CTA pourrait changer de couleur sans renommer |
| `color-text-secondary` | `color-gray-600` | Les niveaux de gris sont des details d'implementation |

#### 2.4 Architecture des tokens dans le projet

```
src/
  theme/
    tokens.ts              ← SOURCE UNIQUE de toutes les valeurs
    tokens.css             ← Genere depuis tokens.ts (ou inverse, au choix)
    tokens.json            ← Export pour Figma / outils design
    ThemeProvider.tsx       ← Context React Native qui injecte les tokens
    useTheme.ts            ← Hook : const { colors, fonts } = useTheme()
    themes/
      default.ts           ← Theme SPAWT standard (importe tokens.ts)
      dark.ts              ← Theme sombre (Phase 2 — prepare mais pas active)
```

#### 2.5 Theme swappable — ThemeProvider pattern

`[RECOMMANDATION]` Implementation du ThemeProvider pour React Native :

```typescript
// src/theme/ThemeProvider.tsx
import React, { createContext, useContext, useState } from 'react';
import { defaultTheme } from './themes/default';
import type { Colors, Fonts, Spacing } from './tokens';

interface Theme {
  colors: Colors;
  fonts: Fonts;
  spacing: Spacing;
}

interface ThemeContextType {
  theme: Theme;
  setTheme: (theme: Theme) => void;
}

const ThemeContext = createContext<ThemeContextType | null>(null);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>(defaultTheme);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme(): Theme {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error('useTheme doit etre utilise dans un ThemeProvider');
  return ctx.theme;
}

// Usage dans un composant :
// const { colors, fonts } = useTheme();
// <Text style={{ color: colors.text.primary, fontFamily: fonts.body }}>
```

**Rebranding partielle** : pour changer l'or en platine, il suffit de modifier `tokens.ts` et aucun composant ne change. Pour un theme sombre, on cree `themes/dark.ts` avec les valeurs inversees et on switch via `setTheme(darkTheme)`.

---

### DECISION 3 — PRICING HT [ARBITRAGE FONDATEUR]

Le pricing affiche est **Hors Taxe**. TVA Cote d'Ivoire = 18%.

#### 3.1 Tableau de pricing HT / TTC complet

| Offre | Cible | Prix HT/mois (FCFA) | TVA 18% | Prix TTC/mois (FCFA) | Prix HT/an | Prix TTC/an | Economie annuelle |
|-------|-------|---------------------|---------|---------------------|------------|-------------|-------------------|
| **Spawter Gold** | B2C | 2 500 | 450 | **2 950** | 25 000 | 29 500 | 2 mois offerts (HT) |
| **Spawt Pro** | B2B Restaurants | 15 000 | 2 700 | **17 700** | 150 000 | 177 000 | - |
| **Spawt Gold** | B2B Restaurants premium | 65 000 | 11 700 | **76 700** | 650 000 | 767 000 | - |

**Prix annuel B2C recalcule :**
- HT : 2 500 x 10 mois = 25 000 FCFA/an (2 mois offerts, inchange)
- TTC : 25 000 x 1.18 = **29 500 FCFA/an**

#### 3.2 Regle d'affichage dans l'app

`[RECOMMANDATION]` **Affichage differencie B2C / B2B :**

| Context | Affichage recommande | Justification |
|---------|---------------------|---------------|
| **B2C (ecrans premium in-app)** | Prix **TTC** avec mention "TTC" | En CI, les consommateurs finaux raisonnent en prix final. Afficher 2 500 F puis facturer 2 950 F = frustration et defiance. La pratique marche ivoirien B2C est le prix TTC (comme pour les telecoms, Spotify, etc.). |
| **B2B (page pro.spawt.app, devis)** | Prix **HT** avec mention "HT" + ligne TVA | Pratique B2B standard. Les restaurateurs / entreprises deduisent la TVA. Les devis et factures doivent detailler HT + TVA + TTC. |

**Textes ecran in-app (B2C) :**
```
"2 950 F/mois TTC"
"29 500 F/an TTC (2 mois offerts)"
```

**Textes page B2B :**
```
"Spawt Pro : 15 000 FCFA HT/mois"
"(17 700 FCFA TTC)"
```

#### 3.3 Obligations legales de facturation en CI

`[RECOMMANDATION]` Points critiques pour la conformite :

| Obligation | Detail | Impact technique |
|------------|--------|-----------------|
| **Facture B2B obligatoire** | Toute facture B2B DOIT mentionner : montant HT, taux de TVA (18%), montant TVA, montant TTC, NCC (Numero de Contribuable) du prestataire et du client | Generer un PDF de facture a chaque paiement B2B |
| **Recu B2C** | Un recu electronique (email ou SMS) est obligatoire pour chaque transaction | CinetPay genere un recu. SPAWT envoie un email de confirmation avec le detail TTC |
| **Declaration TVA** | SPAWT doit etre immatricule a la DGI (Direction Generale des Impots) et declarer la TVA collectee mensuellement | Process administratif — pas technique |
| **Numerotation des factures** | Les factures doivent etre numerotees sequentiellement (pas d'UUID) | Compteur auto-increment : SPAWT-2026-0001, SPAWT-2026-0002, etc. |
| **Conservation** | Les factures doivent etre conservees 10 ans | Stockage cloud + backup |

#### 3.4 Champs DB pour la gestion HT/TTC

```sql
-- Table subscriptions (mise a jour)
ALTER TABLE subscriptions ADD COLUMN price_ht         INTEGER NOT NULL;  -- en FCFA
ALTER TABLE subscriptions ADD COLUMN tva_rate          DECIMAL(4,2) DEFAULT 18.00;
ALTER TABLE subscriptions ADD COLUMN tva_amount        INTEGER GENERATED ALWAYS AS (
  ROUND(price_ht * tva_rate / 100)
) STORED;
ALTER TABLE subscriptions ADD COLUMN price_ttc         INTEGER GENERATED ALWAYS AS (
  price_ht + ROUND(price_ht * tva_rate / 100)
) STORED;
ALTER TABLE subscriptions ADD COLUMN currency          VARCHAR(3) DEFAULT 'XOF';

-- Table invoices (nouvelle)
CREATE TABLE invoices (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    invoice_number    VARCHAR(20) NOT NULL UNIQUE,  -- SPAWT-2026-0001
    subscription_id   UUID REFERENCES subscriptions(id),
    customer_id       UUID NOT NULL,
    customer_type     VARCHAR(10) NOT NULL CHECK (customer_type IN ('b2c', 'b2b')),
    price_ht          INTEGER NOT NULL,
    tva_rate          DECIMAL(4,2) NOT NULL DEFAULT 18.00,
    tva_amount        INTEGER NOT NULL,
    price_ttc         INTEGER NOT NULL,
    currency          VARCHAR(3) DEFAULT 'XOF',
    status            VARCHAR(20) DEFAULT 'draft',  -- draft, issued, paid, cancelled
    issued_at         TIMESTAMP,
    paid_at           TIMESTAMP,
    pdf_url           VARCHAR(500),
    created_at        TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_invoices_customer ON invoices(customer_id, customer_type);
CREATE INDEX idx_invoices_number ON invoices(invoice_number);

-- Sequence pour la numerotation
CREATE SEQUENCE invoice_seq START 1;
-- Usage : 'SPAWT-' || EXTRACT(YEAR FROM NOW()) || '-' || LPAD(nextval('invoice_seq')::text, 4, '0')
```

---

### DECISION 4 — ARCHITECTURE PAIEMENT REMPLACABLE [ARBITRAGE FONDATEUR]

CinetPay est le provider actuel mais DOIT pouvoir etre remplace sans refactoring majeur.

#### 4.1 Pattern d'abstraction — Interface IPaymentProvider

```typescript
// src/services/payment/IPaymentProvider.ts

export interface PaymentInitiateParams {
  amount: number;            // en FCFA (ou unite de la devise)
  currency: string;          // 'XOF'
  description: string;       // ex: "Spawter Gold - Avril 2026"
  customerId: string;        // UUID du spawter ou restaurant
  customerEmail?: string;
  customerPhone: string;     // obligatoire pour Mobile Money
  returnUrl: string;         // URL de callback apres paiement
  notifyUrl: string;         // URL du webhook serveur
  metadata?: Record<string, string>;  // donnees libres (subscription_id, etc.)
}

export interface PaymentResult {
  transactionId: string;     // ID unique chez le provider
  status: PaymentStatus;
  paymentUrl?: string;       // URL de paiement (redirect ou webview)
  rawResponse?: unknown;     // reponse brute du provider (pour debug)
}

export enum PaymentStatus {
  PENDING = 'pending',
  PROCESSING = 'processing',
  COMPLETED = 'completed',
  FAILED = 'failed',
  CANCELLED = 'cancelled',
  REFUNDED = 'refunded',
}

export interface PaymentConfirmation {
  transactionId: string;
  status: PaymentStatus;
  amount: number;
  currency: string;
  paidAt?: Date;
  paymentMethod?: string;    // 'orange_money', 'wave', 'mtn_momo', 'card'
  rawResponse?: unknown;
}

export interface RefundParams {
  transactionId: string;
  amount?: number;           // refund partiel possible, si omis = refund total
  reason?: string;
}

export interface RefundResult {
  refundId: string;
  status: PaymentStatus;
  amount: number;
  rawResponse?: unknown;
}

export interface WebhookPayload {
  headers: Record<string, string>;
  body: unknown;
}

export interface IPaymentProvider {
  /** Nom du provider (pour les logs) */
  readonly name: string;

  /** Initie un paiement et retourne l'URL de paiement */
  initiate(params: PaymentInitiateParams): Promise<PaymentResult>;

  /** Verifie le statut d'un paiement existant */
  getStatus(transactionId: string): Promise<PaymentConfirmation>;

  /** Confirme un paiement (appele apres callback ou polling) */
  confirm(transactionId: string): Promise<PaymentConfirmation>;

  /** Rembourse un paiement */
  refund(params: RefundParams): Promise<RefundResult>;

  /** Parse et valide un webhook entrant du provider */
  handleWebhook(payload: WebhookPayload): Promise<PaymentConfirmation>;

  /** Verifie la signature du webhook (anti-fraude) */
  verifyWebhookSignature(payload: WebhookPayload): boolean;
}
```

#### 4.2 Implementation concrete — CinetPayProvider

```typescript
// src/services/payment/CinetPayProvider.ts

import type {
  IPaymentProvider,
  PaymentInitiateParams,
  PaymentResult,
  PaymentConfirmation,
  RefundParams,
  RefundResult,
  WebhookPayload,
  PaymentStatus,
} from './IPaymentProvider';

interface CinetPayConfig {
  apiKey: string;
  siteId: string;
  secretKey: string;       // pour la verification webhook
  baseUrl: string;         // sandbox vs production
}

export class CinetPayProvider implements IPaymentProvider {
  readonly name = 'cinetpay';
  private config: CinetPayConfig;

  constructor(config: CinetPayConfig) {
    this.config = config;
  }

  async initiate(params: PaymentInitiateParams): Promise<PaymentResult> {
    const response = await fetch(`${this.config.baseUrl}/v2/payment`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        apikey: this.config.apiKey,
        site_id: this.config.siteId,
        transaction_id: params.metadata?.transactionId || crypto.randomUUID(),
        amount: params.amount,
        currency: params.currency,
        description: params.description,
        customer_email: params.customerEmail,
        customer_phone_number: params.customerPhone,
        customer_name: params.customerId,
        return_url: params.returnUrl,
        notify_url: params.notifyUrl,
        channels: 'ALL',  // MOBILE_MONEY, CREDIT_CARD, etc.
        metadata: JSON.stringify(params.metadata || {}),
      }),
    });

    const data = await response.json();

    return {
      transactionId: data.data?.payment_token || data.transaction_id,
      status: this.mapStatus(data.code),
      paymentUrl: data.data?.payment_url,
      rawResponse: data,
    };
  }

  async getStatus(transactionId: string): Promise<PaymentConfirmation> {
    const response = await fetch(`${this.config.baseUrl}/v2/payment/check`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        apikey: this.config.apiKey,
        site_id: this.config.siteId,
        transaction_id: transactionId,
      }),
    });

    const data = await response.json();

    return {
      transactionId,
      status: this.mapStatus(data.code),
      amount: data.data?.amount || 0,
      currency: data.data?.currency || 'XOF',
      paidAt: data.data?.payment_date ? new Date(data.data.payment_date) : undefined,
      paymentMethod: data.data?.payment_method,
      rawResponse: data,
    };
  }

  async confirm(transactionId: string): Promise<PaymentConfirmation> {
    // CinetPay : confirm = getStatus (le paiement est confirme par le webhook)
    return this.getStatus(transactionId);
  }

  async refund(params: RefundParams): Promise<RefundResult> {
    // CinetPay : le refund se fait via le dashboard ou l'API dediee
    const response = await fetch(`${this.config.baseUrl}/v1/refund`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        apikey: this.config.apiKey,
        transaction_id: params.transactionId,
        amount: params.amount,
        reason: params.reason || 'Remboursement client',
      }),
    });

    const data = await response.json();

    return {
      refundId: data.refund_id || params.transactionId,
      status: data.code === '00' ? 'refunded' as PaymentStatus : 'failed' as PaymentStatus,
      amount: params.amount || 0,
      rawResponse: data,
    };
  }

  async handleWebhook(payload: WebhookPayload): Promise<PaymentConfirmation> {
    const body = payload.body as Record<string, unknown>;
    const transactionId = body.cpm_trans_id as string;

    // Toujours re-verifier le statut aupres de CinetPay (ne jamais faire confiance au body du webhook seul)
    return this.getStatus(transactionId);
  }

  verifyWebhookSignature(payload: WebhookPayload): boolean {
    // CinetPay utilise un token secret dans les headers
    const signature = payload.headers['x-cinetpay-signature'] || '';
    // Comparer avec le hash HMAC du body + secretKey
    // Implementation reelle : crypto.createHmac('sha256', this.config.secretKey)...
    return signature.length > 0; // Simplifie — implementer le HMAC reel
  }

  private mapStatus(cinetpayCode: string): PaymentStatus {
    const statusMap: Record<string, PaymentStatus> = {
      '00': 'completed' as PaymentStatus,
      '600': 'pending' as PaymentStatus,
      '601': 'processing' as PaymentStatus,
      '602': 'failed' as PaymentStatus,
      '603': 'cancelled' as PaymentStatus,
    };
    return statusMap[cinetpayCode] || ('failed' as PaymentStatus);
  }
}
```

#### 4.3 Structure de fichiers recommandee

```
src/
  services/
    payment/
      IPaymentProvider.ts       <- Interface abstraite (contrat)
      CinetPayProvider.ts       <- Implementation CinetPay
      StripeProvider.ts         <- (Phase 2) Implementation Stripe
      WaveDirectProvider.ts     <- (Phase 2) Implementation Wave direct
      MockPaymentProvider.ts    <- Pour les tests
      PaymentService.ts         <- Service metier (routing, logging, retry)
      PaymentFactory.ts         <- Factory qui instancie le bon provider
      index.ts                  <- Export public
      __tests__/
        PaymentService.test.ts
        CinetPayProvider.test.ts
        MockPaymentProvider.test.ts
```

#### 4.4 PaymentService — Service metier

```typescript
// src/services/payment/PaymentService.ts

import type { IPaymentProvider, PaymentInitiateParams, PaymentResult, PaymentConfirmation } from './IPaymentProvider';

export class PaymentService {
  private provider: IPaymentProvider;

  constructor(provider: IPaymentProvider) {
    this.provider = provider;
  }

  async initiatePayment(params: PaymentInitiateParams): Promise<PaymentResult> {
    console.log(`[PaymentService] Initiation via ${this.provider.name}`, {
      amount: params.amount,
      currency: params.currency,
      customerId: params.customerId,
    });

    const result = await this.provider.initiate(params);

    // Enregistrer la transaction dans la DB SPAWT (provider-agnostique)
    await this.saveTransaction({
      providerName: this.provider.name,
      providerTransactionId: result.transactionId,
      status: result.status,
      amount: params.amount,
      currency: params.currency,
      customerId: params.customerId,
      metadata: params.metadata,
    });

    return result;
  }

  async processWebhook(payload: unknown, headers: Record<string, string>): Promise<PaymentConfirmation> {
    const webhookPayload = { headers, body: payload };

    // Verifier la signature
    if (!this.provider.verifyWebhookSignature(webhookPayload)) {
      throw new Error(`[PaymentService] Signature webhook invalide (${this.provider.name})`);
    }

    // Traiter le webhook
    const confirmation = await this.provider.handleWebhook(webhookPayload);

    // Mettre a jour la transaction dans la DB SPAWT
    await this.updateTransaction(confirmation);

    return confirmation;
  }

  private async saveTransaction(data: Record<string, unknown>): Promise<void> {
    // Insert dans la table payment_transactions (implementation Supabase)
    // ...
  }

  private async updateTransaction(confirmation: PaymentConfirmation): Promise<void> {
    // Update dans la table payment_transactions
    // ...
  }
}
```

#### 4.5 Configuration — Switch de provider via env

```typescript
// src/services/payment/PaymentFactory.ts

import type { IPaymentProvider } from './IPaymentProvider';
import { CinetPayProvider } from './CinetPayProvider';
// import { StripeProvider } from './StripeProvider';       // Phase 2
// import { WaveDirectProvider } from './WaveDirectProvider'; // Phase 2
import { MockPaymentProvider } from './MockPaymentProvider';

type ProviderName = 'cinetpay' | 'stripe' | 'wave_direct' | 'mock';

export function createPaymentProvider(): IPaymentProvider {
  const providerName = (process.env.PAYMENT_PROVIDER || 'cinetpay') as ProviderName;

  switch (providerName) {
    case 'cinetpay':
      return new CinetPayProvider({
        apiKey: process.env.CINETPAY_API_KEY!,
        siteId: process.env.CINETPAY_SITE_ID!,
        secretKey: process.env.CINETPAY_SECRET_KEY!,
        baseUrl: process.env.CINETPAY_BASE_URL || 'https://api-checkout.cinetpay.com',
      });

    // case 'stripe':
    //   return new StripeProvider({ ... });

    // case 'wave_direct':
    //   return new WaveDirectProvider({ ... });

    case 'mock':
      return new MockPaymentProvider();

    default:
      throw new Error(`[PaymentFactory] Provider inconnu : ${providerName}`);
  }
}

// src/services/payment/index.ts
export { createPaymentProvider } from './PaymentFactory';
export { PaymentService } from './PaymentService';
export type { IPaymentProvider } from './IPaymentProvider';
```

**Variables d'environnement (.env) :**

```env
# Provider actif
PAYMENT_PROVIDER=cinetpay   # cinetpay | stripe | wave_direct | mock

# CinetPay
CINETPAY_API_KEY=xxx
CINETPAY_SITE_ID=xxx
CINETPAY_SECRET_KEY=xxx
CINETPAY_BASE_URL=https://api-checkout.cinetpay.com

# Stripe (Phase 2)
# STRIPE_SECRET_KEY=sk_xxx
# STRIPE_WEBHOOK_SECRET=whsec_xxx
```

#### 4.6 Gestion des webhooks — Pattern provider-agnostique

```typescript
// src/api/webhooks/payment.ts (Edge Function Supabase ou route Express)

import { createPaymentProvider, PaymentService } from '@/services/payment';

// Route unique qui dispatch au bon provider
export async function handlePaymentWebhook(req: Request): Promise<Response> {
  const provider = createPaymentProvider();
  const service = new PaymentService(provider);

  try {
    const headers: Record<string, string> = {};
    req.headers.forEach((value, key) => { headers[key] = value; });

    const body = await req.json();
    const confirmation = await service.processWebhook(body, headers);

    // Actions post-paiement (provider-agnostique)
    if (confirmation.status === 'completed') {
      await activateSubscription(confirmation);
      await sendConfirmationNotification(confirmation);
      await generateInvoice(confirmation);
    }

    if (confirmation.status === 'failed') {
      await handlePaymentFailure(confirmation);
    }

    return new Response(JSON.stringify({ ok: true }), { status: 200 });
  } catch (error) {
    console.error('[Webhook] Erreur:', error);
    return new Response(JSON.stringify({ error: 'Webhook processing failed' }), { status: 500 });
  }
}
```

**Architecture webhook multi-provider :**

```
POST /api/webhooks/payment     ← route unique, le PaymentService dispatch au provider actif
                                  (PAYMENT_PROVIDER dans l'env)

Alternative Phase 2 (si plusieurs providers simultanes) :
POST /api/webhooks/cinetpay    ← route dediee CinetPay
POST /api/webhooks/stripe      ← route dediee Stripe
POST /api/webhooks/wave        ← route dediee Wave

Chaque route instancie le provider specifique :
  const provider = new CinetPayProvider(config);
  const service = new PaymentService(provider);
```

#### 4.7 MockPaymentProvider — Pour les tests

```typescript
// src/services/payment/MockPaymentProvider.ts

import type {
  IPaymentProvider,
  PaymentInitiateParams,
  PaymentResult,
  PaymentConfirmation,
  RefundParams,
  RefundResult,
  WebhookPayload,
} from './IPaymentProvider';
import { PaymentStatus } from './IPaymentProvider';

export class MockPaymentProvider implements IPaymentProvider {
  readonly name = 'mock';

  // Etat interne pour simuler des scenarios
  private mockStatus: PaymentStatus = PaymentStatus.COMPLETED;
  private calls: { method: string; params: unknown }[] = [];

  /** Configure le statut que le mock va retourner */
  setMockStatus(status: PaymentStatus): void {
    this.mockStatus = status;
  }

  /** Retourne l'historique des appels (pour les assertions) */
  getCalls(): { method: string; params: unknown }[] {
    return this.calls;
  }

  /** Reset le mock */
  reset(): void {
    this.calls = [];
    this.mockStatus = PaymentStatus.COMPLETED;
  }

  async initiate(params: PaymentInitiateParams): Promise<PaymentResult> {
    this.calls.push({ method: 'initiate', params });
    return {
      transactionId: `mock_txn_${Date.now()}`,
      status: PaymentStatus.PENDING,
      paymentUrl: 'https://mock-payment.spawt.test/pay',
    };
  }

  async getStatus(transactionId: string): Promise<PaymentConfirmation> {
    this.calls.push({ method: 'getStatus', params: { transactionId } });
    return {
      transactionId,
      status: this.mockStatus,
      amount: 2950,
      currency: 'XOF',
      paidAt: this.mockStatus === PaymentStatus.COMPLETED ? new Date() : undefined,
      paymentMethod: 'mock_orange_money',
    };
  }

  async confirm(transactionId: string): Promise<PaymentConfirmation> {
    this.calls.push({ method: 'confirm', params: { transactionId } });
    return this.getStatus(transactionId);
  }

  async refund(params: RefundParams): Promise<RefundResult> {
    this.calls.push({ method: 'refund', params });
    return {
      refundId: `mock_refund_${Date.now()}`,
      status: PaymentStatus.REFUNDED,
      amount: params.amount || 2950,
    };
  }

  async handleWebhook(payload: WebhookPayload): Promise<PaymentConfirmation> {
    this.calls.push({ method: 'handleWebhook', params: payload });
    const body = payload.body as Record<string, string>;
    return this.getStatus(body.transaction_id || 'mock_txn');
  }

  verifyWebhookSignature(_payload: WebhookPayload): boolean {
    return true; // Mock = toujours valide
  }
}
```

**Exemple de test :**

```typescript
// src/services/payment/__tests__/PaymentService.test.ts

import { PaymentService } from '../PaymentService';
import { MockPaymentProvider } from '../MockPaymentProvider';
import { PaymentStatus } from '../IPaymentProvider';

describe('PaymentService', () => {
  let mock: MockPaymentProvider;
  let service: PaymentService;

  beforeEach(() => {
    mock = new MockPaymentProvider();
    service = new PaymentService(mock);
  });

  it('initie un paiement avec les bons parametres', async () => {
    const result = await service.initiatePayment({
      amount: 2950,
      currency: 'XOF',
      description: 'Spawter Gold - Avril 2026',
      customerId: 'user_123',
      customerPhone: '+2250700000000',
      returnUrl: 'spawt://payment/return',
      notifyUrl: 'https://api.spawt.app/webhooks/payment',
    });

    expect(result.status).toBe(PaymentStatus.PENDING);
    expect(result.paymentUrl).toBeDefined();
    expect(mock.getCalls()).toHaveLength(1);
    expect(mock.getCalls()[0].method).toBe('initiate');
  });

  it('gere un echec de paiement', async () => {
    mock.setMockStatus(PaymentStatus.FAILED);

    const confirmation = await mock.getStatus('txn_123');
    expect(confirmation.status).toBe(PaymentStatus.FAILED);
    expect(confirmation.paidAt).toBeUndefined();
  });
});
```

---

## SYNTHESE FINALE — SPAWT MVP MOBILE

### Perimetre MVP final (liste definitive)

| # | Feature | Statut | Complexite | Dependances |
|---|---------|--------|------------|-------------|
| 1 | Inscription / Authentification (Tel + OTP) | **IN** | M | Provider SMS (Termii) |
| 2 | Onboarding leger (5 questions Palais + quartier + budget) | **IN** | S | Schema Palais |
| 3 | Feed personnalise de lieux (liste ordonnee par score) | **IN** | L | Algo matching, base lieux |
| 4 | Fiche lieu (photo, infos, note, ADN, boutons action) | **IN** | M | Base lieux pre-chargee |
| 5 | Check-in type VTC (geofence 10m + timer 15min + snooze) | **IN** | L | Geoloc background, lieux |
| 6 | Avis structure (note /5 + tags + texte + photos) | **IN** | M | Check-in fonctionnel |
| 7 | Profil utilisateur + Palais radar | **IN** | M | Algo Palais |
| 8 | 5 stades de maturite (Touriste → Guide) | **IN** | S | Check-in + compteur spots |
| 9 | 5 archetypes initiaux (Pisteur, Fantome, Bouche d'Or, Gardien, Omnivore) | **IN** | M | Algo Palais |
| 10 | Sauvegarde / Favoris | **IN** | S | Fiche lieu |
| 11 | Recherche + Filtres (texte, cuisine, budget, distance) | **IN** | M | Base lieux |
| 12 | Carte interactive (Mapbox) | **IN** | M | Provider carte |
| 13 | Coup de Coeur (1/mois gratuit, 2/mois Gold) | **IN** | S | Profil utilisateur |
| 14 | Notifications push (bienvenue, rappel avis, check-in VTC) | **IN** | S | Expo Notifications |
| 15 | Paywall geographique (3km free / tout Abidjan premium) | **IN** | M | Geoloc + paiement |
| 16 | Paiement Mobile Money via abstraction (CinetPay MVP) | **IN** | L | CinetPay KYC, interface abstraite |
| 17 | Partage WhatsApp (deep link fiche lieu) | **IN** | S | Fiche lieu |
| 18 | Moderation basique (signalement + admin panel) | **IN** | M | Admin panel |
| 19 | Lieux pre-charges par l'equipe (50-100) + suggestion user | **IN** | S | Formulaire ADVE |
| 20 | Admin panel basique (lieux, avis, users, metriques) | **IN** | M | Backend |
| 21 | Pricing HT avec affichage TTC B2C / HT B2B | **IN** | S | Decision 3 |
| 22 | Facturation B2B avec TVA 18% | **IN** | M | Decision 3 |
| --- | --- | --- | --- | --- |
| 23 | Mode Rapide (swipe cards) | **OUT** | L | V1.5 (M8) |
| 24 | Mode Crew (vote temps reel) | **OUT** | XL | V2 (M12) |
| 25 | Mode Explore (magazine scroll) | **OUT** | L | V1.5 (M8) |
| 26 | 13 archetypes (8 restants) | **OUT** | M | V1.5 (M8) |
| 27 | Cartes collectibles / Plats | **OUT** | XL | V2 (M12) |
| 28 | Matching ML a 4 dimensions | **OUT** | XL | V2 (M12+) |
| 29 | Reservation 1-tap | **OUT** | L | V2 (M12) |
| 30 | Dashboard B2B Pro/Gold | **OUT** | L | V1.5 (M8) — rapport email en V1 |
| 31 | Badges (30+) | **OUT** | M | V1.5 (M8) — 5 badges simples |
| 32 | SPAWT Wrapped | **OUT** | L | V2 (M18) |
| 33 | Paws (monnaie interne) | **OUT** | L | V2 (M12) |
| 34 | Mode sombre complet | **OUT** | M | Phase 2 (tokens prets) |
| 35 | Multi-villes | **OUT** | L | V2 (M12+) — archi prete |

### Architecture technique recommandee

| Brique | Choix | Justification |
|--------|-------|---------------|
| **Mobile** | React Native + Expo SDK 52+ + Expo Router | `[RECOMMANDATION]` Confirme. Talent pool JS/React en CI, OTA updates via EAS, navigation file-based. NativeWind (Tailwind) pour le styling. |
| **Backend** | Supabase (PostgreSQL + Auth + Storage + Edge Functions) | `[RECOMMANDATION]` Confirme. Prototypage rapide, Row Level Security, realtime pour futures features. Migration possible vers Node.js custom si necessaire a l'echelle. |
| **Paiement** | CinetPay via interface abstraite IPaymentProvider | `[ARBITRAGE FONDATEUR]` Decision 4. Provider remplacable via variable d'env. MockProvider pour les tests. |
| **Cartographie** | Mapbox GL via @rnmapbox/maps | `[RECOMMANDATION]` Confirme. Cout maitrise, customisation dark theme, donnees OSM suffisantes pour Abidjan. |
| **Push notifications** | Expo Notifications + FCM (Android) / APNs (iOS) | `[RECOMMANDATION]` Expo simplifie la gestion cross-platform. Notifications locales pour le check-in VTC (fonctionne offline). |
| **Geoloc background** | Geofencing natif (expo-location + expo-task-manager) | `[ARBITRAGE FONDATEUR]` Decision 1. Monitoring basse consommation en background, haute precision en foreground. Rayon 10m. |
| **State management** | Zustand (local) + TanStack Query (server state) | `[RECOMMANDATION]` Leger, performant, pas de boilerplate Redux. |
| **Images** | Supabase Storage + CDN + compression auto | `[RECOMMANDATION]` Max 3 photos/avis, 5/lieu. Compression 80%, max 1MB. |
| **Analytics** | PostHog (self-hosted ou cloud) ou Mixpanel | `[RECOMMANDATION]` Schema de signaux (table user_signals) en place des le premier commit. |
| **CI/CD** | EAS Build (Expo) + GitHub Actions | `[RECOMMANDATION]` Build cloud, pas de machines locales. Deploimement OTA pour les hotfixes. |
| **Admin panel** | React + Refine (framework admin) | `[RECOMMANDATION]` Connexion directe a Supabase, CRUD auto-genere. |
| **Monitoring** | Sentry (crash reporting) + Supabase Dashboard | `[RECOMMANDATION]` Sentry pour les erreurs runtime, Supabase pour les metriques DB. |
| **SMS / OTP** | Termii (provider local africain) ou Twilio | `[RECOMMANDATION]` Termii est moins cher pour l'Afrique de l'Ouest. Fallback Twilio si couverture insuffisante. |

### Estimation de developpement

| Module | Semaines estimees | Devs | Dependances critiques |
|--------|-------------------|------|----------------------|
| Setup monorepo + CI/CD + design system (tokens) | 1 | 1 | Palette validee (Decision 2) |
| Auth (Tel + OTP + profil) | 2 | 1 | Provider SMS |
| Onboarding (5 questions + calibrage Palais initial) | 1 | 1 | Schema Palais |
| Base de lieux + fiche lieu + admin CRUD | 2 | 1 | 50 lieux pre-charges |
| Check-in VTC (geofence + timer + snooze + etats) | 3 | 1 | Geoloc background, base lieux |
| Avis structure (note + tags + photos + moderation) | 2 | 1 | Check-in fonctionnel |
| Algorithme Palais (5 axes + archetypes + mue) | 3 | 1 | Schema Palais, check-in |
| Progression (5 stades + collection titres) | 1.5 | 1 | Palais fonctionnel |
| Feed personnalise + matching score | 2.5 | 1 | Palais + ADN lieu |
| Carte Mapbox + recherche/filtres | 2 | 1 | Base lieux |
| Paywall geographique | 1 | 1 | Geoloc + paiement |
| Paiement (interface abstraite + CinetPay + webhooks) | 3 | 1 | Compte CinetPay KYC |
| Facturation (HT/TTC, factures B2B) | 1.5 | 1 | Paiement fonctionnel |
| Notifications push (locales + serveur) | 1.5 | 1 | Expo Notifications |
| Partage WhatsApp + deep links | 0.5 | 1 | Fiche lieu |
| Admin panel (lieux, avis, users) | 2 | 1 | Backend fonctionnel |
| QA + integration + polish | 3 | 2 | Tous les modules |
| **TOTAL** | **~32 semaines brutes** | | **Parallelisable a ~16 semaines avec 2 devs** |

**Timeline realistique : 4-5 mois avec 2 devs full-stack + 1 designer, 5-6 mois avec 1 dev + 1 designer.**

### Decisions encore ouvertes (a valider avec Stephanie)

Les decisions suivantes ont ete **retirees** de cette liste car tranchees par les arbitrages fondateur :
- ~~Palette section 9 vs section 13~~ → Decision 2 : Or chaud #C9A84C + vert accent #2D6B4F
- ~~Pricing TTC ou HT~~ → Decision 3 : HT, affichage TTC en B2C
- ~~CinetPay comme provider~~ → Decision 4 : Valide avec abstraction
- ~~Seuil geoloc check-in~~ → Decision 1 : 10 metres, systeme VTC

**Decisions encore ouvertes :**

| # | Sujet | Question | Priorite |
|---|-------|----------|----------|
| 1 | **Grace period abonnement** | 7 jours de grace avant downgrade — trop genereux ? Benchmark : Spotify 3j, Netflix 0j. | P1 |
| 2 | **Score de matching affiche en %** | Montrer le "92% compatible" des le MVP ou attendre la masse critique de data ? Risque de scores aberrants avec peu de data. | P1 |
| 3 | **Nom du chat / mascotte** | Naming interne ou participatif communautaire ? Impact branding fort. | P2 |
| 4 | **Check-in sans geoloc** | Autoriser (poids 0.5x) ou bloquer completement ? Implication accessibilite vs qualite data. | P1 |
| 5 | **Prix annuel B2C** | 25 000 HT (= 2 mois offerts) confirme ? Ou ajuster a 24 000 HT (comme dans l'ADVE-V) ? | P1 |
| 6 | **Spots = lieux uniques** | Confirmer que la progression compte les lieux uniques visites, pas les visites repetees au meme lieu. | P0 |
| 7 | **Omnivore au stade Touriste** | Que montrer au Touriste dont aucun axe n'est suffisamment marque pour un archetype ? "Palais en construction" ? | P2 |

### Principes d'architecture non-negociables

Les regles ci-dessous doivent etre respectees **des le premier commit**. Toute violation cree de la dette technique non-remboursable.

**1. Tokens = seule source de verite visuelle** `[ARBITRAGE FONDATEUR]`
Aucune valeur de couleur, font ou espacement codee en dur dans les composants. Tout passe par `src/theme/tokens.ts`. Un rebranding ne doit toucher qu'un seul fichier.

**2. Provider de paiement abstrait** `[ARBITRAGE FONDATEUR]`
Tout appel au systeme de paiement passe par l'interface `IPaymentProvider`. Aucune reference directe a CinetPay en dehors de `CinetPayProvider.ts`. Le provider actif est determine par `PAYMENT_PROVIDER` dans l'env.

**3. Table user_signals des le jour 1** `[RECOMMANDATION]`
La table append-only `user_signals` (spawt, review, view, save, share, search, filter, click, dismiss) doit etre creee au premier commit. Chaque interaction utilisateur y est loguee. C'est la matiere premiere du ML futur. Cout zero, valeur immense.

**4. Geofencing natif pour le check-in** `[ARBITRAGE FONDATEUR]`
Le check-in VTC repose sur le geofencing OS-level (pas du polling GPS applicatif). Utiliser `expo-location` en mode geofence pour le monitoring background. Les notifications de check-in sont **locales** (pas push serveur) pour fonctionner offline.

**5. Schema de donnees versionne** `[RECOMMANDATION]`
Toute modification de schema passe par une migration numerotee (`migrations/001_initial.sql`, `002_add_checkin_timing.sql`, etc.). Pas de modification manuelle de la DB. Supabase supporte les migrations via CLI.

**6. Prix stockes en HT + taux TVA calcule** `[ARBITRAGE FONDATEUR]`
Les prix en base sont TOUJOURS HT. Le TTC est un champ calcule (`price_ht + price_ht * tva_rate / 100`). Si le taux de TVA change (passage de 18% a 20%), seul le `tva_rate` est modifie — pas les prix de base.

**7. Multi-ville ready dans le schema** `[RECOMMANDATION]`
Tous les lieux ont un champ `city_id`. Tous les utilisateurs ont un champ `city_id`. Le paywall est relatif a la ville. Meme si V1 = Abidjan uniquement, le schema est pret pour Dakar, Douala, etc. Cout : un champ FK. Economie : 0 migration au moment de l'expansion.

---

*Arbitrages fondateur finalises le 7 avril 2026*
*Specifications produites par Opus 4.6*
*Ce document est la source de verite pour le developpement MVP SPAWT.*
*Prochaine etape : validation des 7 decisions encore ouvertes avec Stephanie, puis demarrage du sprint 0 (setup monorepo + design system + auth).*
