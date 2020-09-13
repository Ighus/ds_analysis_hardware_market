import pandas as pd
import numpy as np

def transforma_campo_str_int(campo):
  return campo.replace('.', '').replace(',', '.').astype(float)