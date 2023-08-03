def handle_uploaded_file(f):
    with open("prime_antique/static/images/" + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_uploaded_file_certy(f):
    with open("prime_antique/static/certy/" + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_uploaded_file_expert_certy(f):
    with open("prime_antique/static/certy/" + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)