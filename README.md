# Gestión de Instalaciones — PWA

App web móvil **sin servidor** para gestionar las instalaciones y supervisiones de tus trabajadores.
Todos los datos se guardan en el navegador (`localStorage`), sin base de datos ni registro.

## Archivos

| Archivo | Función |
|---|---|
| `index.html` | Toda la app (HTML + CSS + JavaScript) |
| `manifest.json` | Metadatos para instalarla como PWA |
| `sw.js` | Service Worker (funciona sin conexión) |
| `icons/` | Iconos de la app (192, 512 y apple-touch 180) |

## Funcionalidades

- **Dashboard** con formulario rápido: trabajador/equipo, cliente/lugar, tipo (instalación o supervisión), fecha-hora y notas.
- **Lista ordenada** por próximos servicios, con colores de urgencia (¡AHORA!, MUY PRONTO, HOY, MAÑANA…).
- **Filtro** por tipo: Todas / Instalaciones / Supervisiones.
- **Alertas**: aviso interno (toast) y banner fijo con cuenta atrás que funcionan con la app abierta, sin depender de notificaciones del sistema.
- **Notificaciones del sistema** (Android/escritorio) con el botón 🔔.

## Probar en local

Necesitas servirse por **HTTPS** para que el service worker y la instalación funcionen. Para probar:

```bash
# Con Node instalado:
npx serve .
```

O abre la carpeta en **VS Code** con la extensión **Live Server**. Abrir `index.html` directamente (doble clic) funciona para ver la app, pero las funciones PWA no se activan.https://github.com/victoryanezllauca-sketch/app-supervision/blob/main/README.md

## Publicar en GitHub Pages

1. Crea un repositorio nuevo en GitHub.
2. Sube estos archivos a la **raíz** del repositorio (no los metas en una subcarpeta).
3. Ve a **Settings → Pages**, en "Source" elige la rama (ej. `main`) y la carpeta `/ (root)`, y pulsa **Save**.
4. En unos minutos tu app estará disponible en:

```
https://TU_USUARIO.github.io/NOMBRE_DEL_REPO/
```

> Las rutas de `manifest.json` y `sw.js` son **relativas**, así que funcionan igual aunque GitHub Pages sirva la app en un subdirectorio (`usuario.github.io/repo/`).

## Instalar en iPhone (Safari)

1. Abre la URL enn **Safari**.
2. Toca **Compartir (⤴️) → Añadir a pantalla de inicio**.
3. Toca **Añadir**. ¡Listo! Aparecerá con su icono en la pantalla de inicio.

## Nota sobre notificaciones

- **Android / escritorio (Chrome)**: el botón 🔔 activa las notificaciones del sistema.
- **iPhone**: iOS no permite notificaciones locales programadas en apps 100% locales. La app lo compensa con un **aviso interno** (toast destacado) y un **banner fijo con cuenta atrás** que aparecen mientras la app está abierta.
