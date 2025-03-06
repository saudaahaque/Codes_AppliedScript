# Övning 9: Övning 9: Logiska operatorer i funktioner
def minst_två_sanna(a, b, c):
    counter = 0
    if a: 
        counter += 1
    if b:
        counter += 1
    if c:
        counter += 1

    if counter > 1: 
        return True
    else:
        return False

print(minst_två_sanna(True, True, False))
