def generate_html():
    # Simula i dati del treno come esempio
    train_data = [
        {"departure_time": "08:00", "arrival_time": "10:00", "duration": "2h", "train_category": "Express"},
        {"departure_time": "09:00", "arrival_time": "11:30", "duration": "2h 30m", "train_category": "Regional"}
    ]

    # Genera le righe della tabella come stringhe HTML
    rows = ""
    for row in train_data:
        rows += "<tr>"
        for value in row.values():
            rows += f"<td>{value}</td>"
        rows += "</tr>"

    # Legge il contenuto del file HTML esistente
    with open('index.html', 'r') as file:
        html_content = file.read()

    # Sostituisce il segnaposto {{rows}} con le righe della tabella generate
    html_content = html_content.replace("{{rows}}", rows)

    # Scrive il nuovo contenuto HTML in un file (può essere lo stesso o uno nuovo)
    with open('index_filled.html', 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    generate_html()
