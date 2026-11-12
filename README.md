# retrieval-duplicate-credit

## Français

Exposer le gain artificiel des documents dupliqués.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m retrieval_duplicate_credit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Exposer le gain artificiel des documents dupliqués : calcul déterministe sur entrées structurées, témoins et cas limites explicites.

### Limites

Modèle borné, données fictives, aucun service ou matériel de production validé. Méthodes classiques ; aucune supériorité SOTA générale ni adoption humaine démontrée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Expose artificial retrieval gains from duplicate documents.

Synthetic data; no network access or secret required.

```sh
python -m retrieval_duplicate_credit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Expose artificial retrieval gains from duplicate documents: deterministic computation over structured inputs, explicit witnesses and boundary cases.

### Limits

Bounded model and synthetic data; no production service or hardware validated. Classical methods; no general SOTA superiority or human adoption demonstrated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Revelar ganancias artificiales por documentos duplicados.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m retrieval_duplicate_credit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Revelar ganancias artificiales por documentos duplicados: cálculo determinista con entradas estructuradas, testigos y casos límite explícitos.

### Límites

Modelo acotado y datos ficticios; ningún servicio ni hardware de producción validado. Métodos clásicos; sin superioridad SOTA general ni adopción humana demostrada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://scikit-learn.org/stable/modules/calibration.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html

## Projets voisins / Neighboring projects / Proyectos vecinos

FR : [prompt-ablation-paired](https://github.com/gbesse/prompt-ablation-paired) est un autre diagnostic du portefeuille. Ici : Exposer le gain artificiel des documents dupliqués. Comparaison de périmètres seulement, sans affiliation ni benchmark de supériorité.

EN: [prompt-ablation-paired](https://github.com/gbesse/prompt-ablation-paired) is a different portfolio diagnostic. Here: Expose artificial retrieval gains from duplicate documents. Scope comparison only, no affiliation or superiority benchmark.

ES: [prompt-ablation-paired](https://github.com/gbesse/prompt-ablation-paired) es otro diagnóstico del portafolio. Aquí: Revelar ganancias artificiales por documentos duplicados. Comparación de alcance, sin afiliación ni benchmark de superioridad.
