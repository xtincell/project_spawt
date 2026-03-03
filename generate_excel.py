#!/usr/bin/env python3
"""Generate SPAWT field collection Excel template with data validation & formatting."""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import date

wb = Workbook()

# ── Color palette ──
GOLD = "B8960C"
DARK = "1A1A1A"
WHITE = "FFFFFF"
BG = "F8F7F4"
GREEN = "5B8C5A"
MUTED = "6B7280"
LIGHT_GOLD = "FFF8E7"
LIGHT_GREEN = "EFF6EE"
LIGHT_BLUE = "EBF0FA"
LIGHT_PINK = "FDF0F0"
LIGHT_PURPLE = "F3EEFA"
LIGHT_GREY = "F5F5F5"

# Styles
header_font = Font(name="Calibri", bold=True, size=11, color=WHITE)
section_font = Font(name="Calibri", bold=True, size=11, color=GOLD)
sub_font = Font(name="Calibri", size=10, color=MUTED, italic=True)
data_font = Font(name="Calibri", size=11, color=DARK)
title_font = Font(name="Calibri", bold=True, size=14, color=DARK)

header_fill_gold = PatternFill("solid", fgColor=GOLD)
header_fill_green = PatternFill("solid", fgColor=GREEN)
header_fill_dark = PatternFill("solid", fgColor=DARK)
fill_light_gold = PatternFill("solid", fgColor=LIGHT_GOLD)
fill_light_green = PatternFill("solid", fgColor=LIGHT_GREEN)
fill_light_blue = PatternFill("solid", fgColor=LIGHT_BLUE)
fill_light_pink = PatternFill("solid", fgColor=LIGHT_PINK)
fill_light_purple = PatternFill("solid", fgColor=LIGHT_PURPLE)
fill_light_grey = PatternFill("solid", fgColor=LIGHT_GREY)
fill_bg = PatternFill("solid", fgColor=BG)

center = Alignment(horizontal="center", vertical="center", wrap_text=True)
left_wrap = Alignment(horizontal="left", vertical="center", wrap_text=True)
thin_border = Border(
    left=Side(style="thin", color="E0E0E0"),
    right=Side(style="thin", color="E0E0E0"),
    top=Side(style="thin", color="E0E0E0"),
    bottom=Side(style="thin", color="E0E0E0"),
)

# ── Data constants (mirror from app) ──
TYPES = "Maquis,Restaurant,Gargote,Street food,Bistrot,Fine dining,Snack"
CUISINES = "Ivoirienne,Africaine (autre),Française,Libanaise,Asiatique,Fast food,Fusion"
QUARTIERS = "Cocody,Plateau,Marcory,Treichville,Yopougon,Abobo,Adjamé,Koumassi,Port-Bouët,Bingerville,Riviera,2 Plateaux,Angré,Zone 4,Vallon,Bassam,Assinie,Bouaké"
PAIEMENTS = "Cash,Orange Money,MTN,Moov,Wave,CB,Virement"
PARKING = "Facile,Modéré,Difficile,Impossible"
SERVICES = "Livraison,À emporter,Climatisation,WiFi,Terrasse,Bar,Fumeurs acceptés"
POTENTIEL = "🔥 PÉPITE,❤️ COUP DE CŒUR,✅ SOLIDE,⚠️ MOYEN,❌ SKIP"
RECO = "Absolument,Oui,Peut-être,Non"
CLIENTELE = "Cadres/Pro,Étudiants,Familles,Couples,Solo,Touristes,Mixte"
MOMENTS = "Petit-déj,Déjeuner,Goûter,Dîner,Tard dans la nuit"
AFFLUENCE = "Vide,Calme,Modérée,Bondé,File d'attente"
SONORE = "Calme,Ambiance musicale,Animé,Bruyant"
PROPRETE = "Impeccable,Correcte,Passable,Problématique"
ACCUEIL = "Chaleureux,Pro,Distant,Désagréable"
TAGS = "🎯 Exact,🤩 Surprise,💸 Qualité-prix,😐 Banal,😞 Décevant"
RECEPTIVITE = "Très intéressé,Ouvert,Sceptique,Refus"
FONCTION = "Propriétaire,Gérant,Responsable"
MATERIEL = "Flyer,Pitch deck,Carte de visite"
MENU_TYPE = "Carte physique photographiée,Ardoise,Verbal uniquement"
DIGITAL = "WhatsApp,Facebook,Instagram,Site web"
OUI_NON = "Oui,Non"

# ═══════════════════════════════════════════════════════════════
# SHEET 1 — Fiches de collecte (main data entry)
# ═══════════════════════════════════════════════════════════════
ws = wb.active
ws.title = "Fiches SPAWT"
ws.sheet_properties.tabColor = GOLD

# Columns definition: (header, sub_hint, width, section_fill, validation_list_or_None)
COLUMNS = [
    # ── BLOC 1 : Identification ──
    ("N°", "Auto", 5, fill_light_grey, None),
    ("Date visite", "JJ/MM/AAAA", 14, fill_light_gold, None),
    ("Spawter", "Qui collecte", 16, fill_light_gold, None),
    ("Nom du lieu", "Obligatoire", 28, fill_light_gold, None),
    ("Adresse", "Rue, repère", 30, fill_light_gold, None),
    ("Quartier", "Liste", 16, fill_light_gold, QUARTIERS),
    ("GPS Lat", "Decimal", 12, fill_light_gold, None),
    ("GPS Long", "Decimal", 12, fill_light_gold, None),
    ("Téléphone", "+225...", 16, fill_light_gold, None),
    ("Digital", "WhatsApp, FB...", 20, fill_light_gold, DIGITAL),
    # ── BLOC 2 : Offre ──
    ("Type", "Maquis, Resto...", 18, fill_light_green, TYPES),
    ("Cuisine(s)", "Ivoirienne...", 20, fill_light_green, CUISINES),
    ("Spécialité 1", "Plat phare", 20, fill_light_green, None),
    ("Spécialité 2", "", 20, fill_light_green, None),
    ("Spécialité 3", "", 20, fill_light_green, None),
    ("Plats signature", "Détails", 25, fill_light_green, None),
    ("Type de menu", "Carte, ardoise", 22, fill_light_green, MENU_TYPE),
    # ── BLOC 3 : Prix ──
    ("Prix éco min (F)", "CFA", 14, fill_light_blue, None),
    ("Prix éco max (F)", "CFA", 14, fill_light_blue, None),
    ("Prix moyen min (F)", "CFA", 14, fill_light_blue, None),
    ("Prix moyen max (F)", "CFA", 14, fill_light_blue, None),
    ("Prix premium min (F)", "CFA", 15, fill_light_blue, None),
    ("Prix premium max (F)", "CFA", 15, fill_light_blue, None),
    ("Boissons min (F)", "CFA", 14, fill_light_blue, None),
    ("Boissons max (F)", "CFA", 14, fill_light_blue, None),
    ("Budget /12", "1=bas 12=haut", 11, fill_light_blue, None),
    ("Cadence /12", "1=lent 12=rapide", 12, fill_light_blue, None),
    # ── BLOC 4 : Logistique ──
    ("Horaires L-V", "ex: 07h-22h", 14, fill_light_grey, None),
    ("Horaires Sam", "ex: 08h-23h", 14, fill_light_grey, None),
    ("Horaires Dim", "ex: Fermé", 14, fill_light_grey, None),
    ("Capacité int.", "nb places", 11, fill_light_grey, None),
    ("Capacité ext.", "nb places", 11, fill_light_grey, None),
    ("Paiements", "Cash, OM...", 20, fill_light_grey, PAIEMENTS),
    ("Parking", "Facile → Impossible", 14, fill_light_grey, PARKING),
    ("Services", "WiFi, terrasse...", 22, fill_light_grey, SERVICES),
    # ── BLOC 5 : Dégustation ──
    ("Testé ?", "Oui/Non", 9, fill_light_pink, OUI_NON),
    ("Plats testés", "Détails", 25, fill_light_pink, None),
    ("Budget test (F)", "CFA dépensé", 14, fill_light_pink, None),
    ("Note /5", "⭐", 8, fill_light_pink, None),
    ("Points forts", "3 max, virgules", 30, fill_light_pink, None),
    ("Points faibles", "3 max, virgules", 30, fill_light_pink, None),
    ("Tag ressenti", "🎯🤩💸😐😞", 18, fill_light_pink, TAGS),
    ("Recommandation", "Absolument → Non", 16, fill_light_pink, RECO),
    ("Accroche", "Phrase clé", 30, fill_light_pink, None),
    # ── BLOC 6 : Ambiance ──
    ("Ambiance /12", "1=simple 12=haut", 12, fill_light_purple, None),
    ("Sociabilité /12", "1=intime 12=festif", 13, fill_light_purple, None),
    ("Notoriété /12", "1=inconnu 12=célèbre", 13, fill_light_purple, None),
    ("Clientèle", "Cadres, familles...", 22, fill_light_purple, CLIENTELE),
    ("Moments", "Déjeuner, dîner...", 22, fill_light_purple, MOMENTS),
    ("Affluence", "Vide → File", 14, fill_light_purple, AFFLUENCE),
    ("Ambiance sonore", "Calme → Bruyant", 16, fill_light_purple, SONORE),
    ("Propreté", "Impeccable → Prob.", 14, fill_light_purple, PROPRETE),
    ("Accueil", "Chaleureux → Dés.", 14, fill_light_purple, ACCUEIL),
    ("Potentiel SPAWT", "🔥❤️✅⚠️❌", 18, fill_light_purple, POTENTIEL),
    ("Notes terrain", "Libre", 35, fill_light_purple, None),
    # ── BLOC 7 : B2B ──
    ("Contact établi ?", "Oui/Non", 14, fill_light_grey, OUI_NON),
    ("Nom contact", "Prénom Nom", 20, fill_light_grey, None),
    ("Fonction", "Proprio, gérant", 16, fill_light_grey, FONCTION),
    ("Réceptivité", "Intéressé → Refus", 16, fill_light_grey, RECEPTIVITE),
    ("RDV pris ?", "Oui/Non", 10, fill_light_grey, OUI_NON),
    ("Date RDV", "JJ/MM/AAAA", 14, fill_light_grey, None),
    ("Matériel laissé", "Flyer, pitch...", 18, fill_light_grey, MATERIEL),
    ("Notes B2B", "Suivi", 30, fill_light_grey, None),
]

# ── Section headers row (row 1) ──
sections = [
    (1, 10, "📍 IDENTIFICATION", header_fill_dark),
    (11, 17, "🍽️ OFFRE & CUISINE", PatternFill("solid", fgColor=GREEN)),
    (18, 27, "💰 PRIX & RYTHME", PatternFill("solid", fgColor="3B82F6")),
    (28, 35, "🏢 LOGISTIQUE", PatternFill("solid", fgColor="6B7280")),
    (36, 44, "⭐ DÉGUSTATION", PatternFill("solid", fgColor="DC2626")),
    (45, 55, "🎭 AMBIANCE & VERDICT", PatternFill("solid", fgColor="7C3AED")),
    (56, 63, "🤝 B2B / COMMERCIAL", PatternFill("solid", fgColor="6B7280")),
]

for start, end, title, fill in sections:
    ws.merge_cells(start_row=1, start_column=start, end_row=1, end_column=end)
    cell = ws.cell(row=1, column=start, value=title)
    cell.font = Font(name="Calibri", bold=True, size=12, color=WHITE)
    cell.fill = fill
    cell.alignment = center
    cell.border = thin_border

# ── Column headers (row 2) + hints (row 3) ──
for i, (header, hint, width, fill, _) in enumerate(COLUMNS, 1):
    col_letter = get_column_letter(i)
    ws.column_dimensions[col_letter].width = width

    # Header
    cell = ws.cell(row=2, column=i, value=header)
    cell.font = Font(name="Calibri", bold=True, size=10, color=DARK)
    cell.fill = fill
    cell.alignment = center
    cell.border = thin_border

    # Hint
    cell_hint = ws.cell(row=3, column=i, value=hint)
    cell_hint.font = sub_font
    cell_hint.fill = fill
    cell_hint.alignment = center
    cell_hint.border = thin_border

# ── Data validation (dropdowns) ──
for i, (header, _, _, _, validation_list) in enumerate(COLUMNS, 1):
    if validation_list:
        col_letter = get_column_letter(i)
        dv = DataValidation(
            type="list",
            formula1=f'"{validation_list}"',
            allow_blank=True,
            showDropDown=False,
        )
        dv.error = f"Choisir parmi les options proposées"
        dv.errorTitle = header
        dv.prompt = f"Sélectionner : {validation_list.replace(',', ', ')}"
        dv.promptTitle = header
        dv.showInputMessage = True
        dv.showErrorMessage = True
        ws.add_data_validation(dv)
        dv.add(f"{col_letter}4:{col_letter}104")

# ── Pre-fill 100 rows with formatting + row numbers ──
today = date.today().strftime("%d/%m/%Y")
for row in range(4, 104):
    for i, (_, _, _, _, _) in enumerate(COLUMNS, 1):
        cell = ws.cell(row=row, column=i)
        cell.font = data_font
        cell.alignment = left_wrap
        cell.border = thin_border
        # Alternate row colors
        if row % 2 == 0:
            cell.fill = PatternFill("solid", fgColor="FAFAFA")

    # N°
    ws.cell(row=row, column=1, value=row - 3).alignment = center
    # Date pre-fill
    ws.cell(row=row, column=2, value=today)

# ── Freeze panes ──
ws.freeze_panes = "D4"

# ── Row heights ──
ws.row_dimensions[1].height = 28
ws.row_dimensions[2].height = 30
ws.row_dimensions[3].height = 20
for r in range(4, 104):
    ws.row_dimensions[r].height = 22

# ═══════════════════════════════════════════════════════════════
# SHEET 2 — Légende / Guide
# ═══════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Légende & Guide")
ws2.sheet_properties.tabColor = GREEN

ws2.column_dimensions["A"].width = 25
ws2.column_dimensions["B"].width = 55
ws2.column_dimensions["C"].width = 5
ws2.column_dimensions["D"].width = 25
ws2.column_dimensions["E"].width = 55

guide_data = [
    ("SPAWT — Guide de collecte terrain", "", "", "", ""),
    ("", "", "", "", ""),
    ("CHAMP", "VALEURS POSSIBLES", "", "CHAMP", "VALEURS POSSIBLES"),
    ("Type de lieu", TYPES.replace(",", ", "), "", "Potentiel SPAWT", "🔥 PÉPITE — Exceptionnel, priorité absolue"),
    ("Cuisine(s)", CUISINES.replace(",", ", "), "", "", "❤️ COUP DE CŒUR — Très bon, à suivre"),
    ("Quartier", QUARTIERS.replace(",", ", "), "", "", "✅ SOLIDE — Bon niveau, fiable"),
    ("Paiements", PAIEMENTS.replace(",", ", "), "", "", "⚠️ MOYEN — Correct sans plus"),
    ("Services", SERVICES.replace(",", ", "), "", "", "❌ SKIP — Pas intéressant"),
    ("Parking", PARKING.replace(",", ", "), "", "", ""),
    ("", "", "", "Tag ressenti", "🎯 Exact — Conforme aux attentes"),
    ("ÉCHELLES /12", "SIGNIFICATION", "", "", "🤩 Surprise — Au-delà des attentes"),
    ("Budget", "1 = très bas → 12 = très cher", "", "", "💸 Qualité-prix — Bon rapport"),
    ("Cadence", "1 = très lent → 12 = ultra rapide", "", "", "😐 Banal — Rien de marquant"),
    ("Ambiance", "1 = simple → 12 = luxe/raffiné", "", "", "😞 Décevant — En dessous"),
    ("Sociabilité", "1 = intime → 12 = festif/convivial", "", "", ""),
    ("Notoriété", "1 = inconnu → 12 = très célèbre", "", "Recommandation", RECO.replace(",", ", ")),
    ("", "", "", "Clientèle", CLIENTELE.replace(",", ", ")),
    ("NOTE /5", "SIGNIFICATION", "", "Moments", MOMENTS.replace(",", ", ")),
    ("⭐", "Mauvais", "", "Affluence", AFFLUENCE.replace(",", ", ")),
    ("⭐⭐", "Passable", "", "Ambiance sonore", SONORE.replace(",", ", ")),
    ("⭐⭐⭐", "Correct", "", "Propreté", PROPRETE.replace(",", ", ")),
    ("⭐⭐⭐⭐", "Très bon", "", "Accueil", ACCUEIL.replace(",", ", ")),
    ("⭐⭐⭐⭐⭐", "Exceptionnel", "", "", ""),
    ("", "", "", "Réceptivité B2B", RECEPTIVITE.replace(",", ", ")),
    ("", "", "", "Fonction contact", FONCTION.replace(",", ", ")),
]

for r, (a, b, c, d, e) in enumerate(guide_data, 1):
    ws2.cell(row=r, column=1, value=a)
    ws2.cell(row=r, column=2, value=b)
    ws2.cell(row=r, column=4, value=d)
    ws2.cell(row=r, column=5, value=e)

# Title
ws2.merge_cells("A1:E1")
t = ws2["A1"]
t.font = Font(name="Calibri", bold=True, size=16, color=DARK)
t.alignment = Alignment(horizontal="center", vertical="center")
t.fill = PatternFill("solid", fgColor=LIGHT_GOLD)

# Section headers
for cell_ref in ["A3", "B3", "D3", "E3"]:
    c = ws2[cell_ref]
    c.font = Font(name="Calibri", bold=True, size=11, color=WHITE)
    c.fill = header_fill_dark
    c.alignment = center

for cell_ref in ["A11", "B11"]:
    c = ws2[cell_ref]
    c.font = Font(name="Calibri", bold=True, size=11, color=WHITE)
    c.fill = PatternFill("solid", fgColor=GREEN)
    c.alignment = center

for cell_ref in ["A18", "B18"]:
    c = ws2[cell_ref]
    c.font = Font(name="Calibri", bold=True, size=11, color=WHITE)
    c.fill = header_fill_gold
    c.alignment = center

# Style all data cells
for r in range(3, len(guide_data) + 1):
    for col in [1, 2, 4, 5]:
        c = ws2.cell(row=r, column=col)
        if not c.font.bold:
            c.font = Font(name="Calibri", size=10, color=DARK)
        c.alignment = left_wrap
        c.border = thin_border
    ws2.row_dimensions[r].height = 22

ws2.row_dimensions[1].height = 36

# ═══════════════════════════════════════════════════════════════
# SHEET 3 — Grille prix par quartier (bonus)
# ═══════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Grille Prix Quartiers")
ws3.sheet_properties.tabColor = "3B82F6"

price_headers = ["Quartier", "Éco min (F)", "Éco max (F)", "Moyen min (F)", "Moyen max (F)", "Premium min (F)", "Premium max (F)", "Nb lieux"]
ws3.column_dimensions["A"].width = 20
for i in range(2, 9):
    ws3.column_dimensions[get_column_letter(i)].width = 15

for i, h_text in enumerate(price_headers, 1):
    c = ws3.cell(row=1, column=i, value=h_text)
    c.font = header_font
    c.fill = PatternFill("solid", fgColor="3B82F6")
    c.alignment = center
    c.border = thin_border

quartiers = QUARTIERS.split(",")
for r, q in enumerate(quartiers, 2):
    ws3.cell(row=r, column=1, value=q).font = Font(name="Calibri", bold=True, size=11)
    for col in range(1, 9):
        c = ws3.cell(row=r, column=col)
        c.border = thin_border
        c.alignment = center
        if r % 2 == 0:
            c.fill = PatternFill("solid", fgColor="F0F4FA")
    ws3.row_dimensions[r].height = 22

ws3.freeze_panes = "B2"

# ── Save ──
output_path = "/home/user/project_spawt/SPAWT_Fiches_Collecte.xlsx"
wb.save(output_path)
print(f"✅ Fichier créé : {output_path}")
print(f"   → {len(COLUMNS)} colonnes")
print(f"   → 100 lignes pré-formatées")
print(f"   → Listes déroulantes sur {sum(1 for _,_,_,_,v in COLUMNS if v)} champs")
print(f"   → 3 onglets : Fiches SPAWT, Légende & Guide, Grille Prix Quartiers")
