import itertools

# Lista de cuvinte
cuvinte = ['cristian', 'boitos', 'cristi', '2009', 'daniel', 'grasu']

# Generare permutări
permutari = itertools.permutations(cuvinte)

# Salvarea tuturor combinațiilor într-o listă
parole = [''.join(p) for p in permutari]

# Afișarea numărului total de parole generate
print(f"Numărul total de parole generate: {len(parole)}")

# Opțional: afișarea tuturor parolelor (atenție, va fi o listă lungă)
for parola in parole:
    print(parola)
