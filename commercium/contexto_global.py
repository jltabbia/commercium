from static import globales  # Ajusta la importación según la ubicación exacta del archivo

def variables_globales(request):
    return {
        'TITULO_SITIO': globales.TITULO,
        'DESCRIPCION_SITIO' : globales.DESCRIPCION
    }