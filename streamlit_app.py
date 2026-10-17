# -*- coding: utf-8 -*-
"""
Wrapper para Streamlit Cloud
Este archivo permite a Streamlit ejecutar el script existente llamado "dipploy" (archivo sin extensión)

Streamlit espera que la "Ruta del archivo principal" apunte a un .py válido; este wrapper llama al script original.
"""
import runpy

runpy.run_path('dipploy', run_name='__main__')
