# Template: django + tailwind

Template para proyectos con django + tailwind.
Con configuracion de linters, formatters y las dependencias necesarias con `poetry`.

## Configuracion

### Requisitos

- Nodejs (para poder utilizar tailwind)
- Poetry (manejo de dependencias de python)

# Instalacion de dependencias 

Para la instalacion de las dependencias utilizar:

```bash
npm install 
poetry install
```

### Tailwind:

Cada vez que se agregan nuevos estilos a los archivos html se debe re-compilar tailwind con:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --minify
```
