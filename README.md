# Website de Consultanță Corporativă

## Descriere
Un site web modern și responsiv pentru o firmă de consultanță, construit cu Django. Site-ul prezintă serviciile companiei și oferă funcționalități pentru clienți potențiali de a intra în contact cu firma.

## Tehnologii Utilizate
- **Backend:** Django 4+
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework CSS:** Bootstrap 5
- **Animații:** AOS (Animate On Scroll)
- **Iconițe:** Font Awesome
- **Fonturi:** Google Fonts (Poppins)

## Caracteristici
- Design modern cu animații și efecte vizuale
- Layout complet responsiv pentru toate dispozitivele
- Animații la scroll utilizând biblioteca AOS
- Efecte de parallax pentru imagini
- Contoare animate pentru statistici
- Galerie de testimoniale
- Formular de contact
- Integrare social media
- Buton de revenire la începutul paginii
- Banner pentru consimțământ cookie-uri

## Instrucțiuni de Instalare

1. Clonați repository-ul:
```bash
git clone https://github.com/NaviAndrei/consulting-firm-website.git
cd consulting-firm-website
```

2. Creați și activați un mediu virtual:
```bash
python -m venv consulting_env
# Pentru Windows
consulting_env\Scripts\activate
# Pentru macOS/Linux
source consulting_env/bin/activate
```

3. Instalați dependențele:
```bash
pip install -r requirements.txt
```

4. Aplicați migrările:
```bash
python manage.py migrate
```

5. Creați un superuser (opțional):
```bash
python manage.py createsuperuser
```

6. Rulați serverul de dezvoltare:
```bash
python manage.py runserver
```

7. Accesați site-ul la `http://127.0.0.1:8000/`

## Structura Proiectului
- `consulting_website/` - Directorul principal al proiectului Django
- `consulting_website/templates/` - Template-uri HTML
- `consulting_website/static/` - Fișiere statice (CSS, JavaScript, imagini)
- `consulting_website/core/` - Aplicația principală Django
- `consulting_env/` - Mediul virtual Python

## Notă Personală
Acest proiect face parte din portofoliul meu personal de proiecte. A fost dezvoltat pentru a demonstra abilitățile mele de web development, design modern și implementare de funcționalități utilizând Django și tehnologii front-end actuale.

