# Övning 5: Hämta Python-version

#Utan funktion och anropning:
import sys

print("Python-version:", sys.version)
print("Plattform:", sys.platform)
print("Sökvägar:", sys.path)

#Med funktion och anropning
import sys

def python_version():
    return sys.version

print ("Aktuell Python-version", python_version()) 
      
