# note
## bandit/overthewire: 
Commande à retenir :
* `ls -la`
*  git status
*  git add .
*  git commit -m "nom des changement"
*  git push
*  git pull (recuperé)
*  IL : Instruction list de l'ordi : dépend du language du pc en lui même
*  Lexis : facilité la segmentation de texte : découper le texte en unités comme les phrases ou les mots.
L'analyse de fréquence : compter la fréquence des mots ou des phrases.
Le calcul de statistiques lexicales : analyser la richesse et la diversité du vocabulaire.
* sémantic : suite de règle qui determine si certaine phrase ont du sens.
* fichier contenant le code source (source code = programme écrit dans un langage de programmation de haut niveau) = source file
  le code source doit etre écrit sans aucune décoration comme des polices différentes, des couleurs, des images intégrées ou d'autres médias
### 4 Règles a respecté pour qu'un programme fonctionne :

* Synctactically : chaque language a ces règles et doivent être respecté.
* Sementically = programme qui doit avoir du sens sinon ne donnera pas le résultat voulu.
* alphabetically : programme doit etre ecris dans une langue reconnue.
* Lexically : ​chaque langage de programmation a son dictionnaire
#### Créateur du python
* Guido Van Rossum né en 1956 à Haarlem au Pays-bas 


```mermaid
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
C -->|Three| F[Result 3]
```
Test debut
== Vérification

```pandas
data = {
    "Type": ["int", "float", "str", "bool", "list", "tuple", "set", "dict", "complex", "NoneType", "bytes", "range"],
    "Description": [
        "Nombres entiers",
        "Nombres décimaux",
        "Chaînes de caractères",
        "Valeurs logiques",
        "Liste ordonnée et modifiable",
        "Liste ordonnée mais immuable",
        "Ensemble sans doublons",
        "Dictionnaire clé-valeur",
        "Nombres complexes",
        "Absence de valeur",
        "Données binaires",
        "Séquence de nombres"
    ],
    "Exemple": [
        "42, -5",
        "3.14, -2.0",
        '"Python", "Hello"',
        "True, False",
        "[1, 2, 3], ['a', 'b']",
        "(1, 2, 3)",
        "{1, 2, 3}",
        '{"clé": "valeur"}',
        "3 + 4j",
        "None",
        'b"data"',
        "range(5)"
    ]
}

df = pd.DataFrame(data)
print(df)



