#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 00:00:17 2026

@author: dianaabanero
"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import sqlite3 as sql

database = 'fcp_database.db'

'''

Tu gerente de portafolios te pide que utilizando el método optimize.minimize 
le construyas un portafolios especial, llamado "long-only", el cual es el 
portafolios de mínima varianza que satisface dos condiciones:
    
1. long-only es un portafolios unitario en la norma L1.
2. long-only debe tener todas sus componentes no negativas (se valen ceros).

Inputs:
1. assets: una lista de los activos que el gerente desea optimizar.

Outputs:
1. weights: un np.array con los pesos del portafolios long-only.

'''

def get_prices(assets):
    """
    Obtiene los precios de cierre de varios activos desde SQLite y 
    los combina por la columna 'Date'.

    Parameters
    ----------
    assets : list[str]
        Lista de tickers.

    Returns
    -------
    DataFrame
        DataFrame con columna Date y los precios de cierre de cada activo.
    """
    try:
        if isinstance(assets, str): 
            assets = [assets]
            
        conn = sql.connect(database)

        # Lista donde guardaremos cada DataFrame individual
        dfs = []

        for asset in assets:
            query = f'SELECT Date, Close AS "{asset}" FROM "{asset}"'
            df_asset = (
                pd.read_sql_query(query, conn)
                  .set_index("Date")
            )
            dfs.append(df_asset)

        # Unión horizontal de todos los DataFrames
        df_final = pd.concat(dfs, axis=1).reset_index()
        df_final = df_final.dropna()
        return df_final

    except sql.Error as e:
        print(f"Error al obtener precios: {e}")
        return None

    finally:
        conn.close()

def get_returns(assets):
    """
    Calcula los rendimientos diarios de varios activos.

    Parameters
    ----------
    assets : list[str]
        Lista de tickers.

    Returns
    -------
    DataFrame
        DataFrame con columna Date y los rendimientos diarios de cada activo.
    """
    try:
        # Obtener precios
        df_prices = get_prices(assets)
        df_returns = df_prices.copy()
        df_returns.set_index("Date", inplace=True)

        # Calcular rendimientos diarios
        df_returns = df_returns.pct_change().dropna().reset_index()

        return df_returns

    except Exception as e:
        print(f"Error al calcular rendimientos: {e}")
        return None
    


def portfolio_covariance(x,A):
    return x.T @ A @ x

def long_only_portfolio(assets):
    '''
    x0 es el portafolios equiponderado unitario bajo la norma L1.
    '''
    x0 = np.ones(len(assets))
    normL1 = np.sum(np.abs(x0))
    x0 /= normL1 
    '''
    'A' es la matriz de varianza-covarianza en formato np.array o DataFrame.
    
    '''
    
    factor = 252
    df = get_returns(assets)
    df.set_index("Date", inplace=True)
    covariance_matrix = df.cov() * factor
    
    
    A = covariance_matrix.values
    args = (A)
    '''
    'bounds' son los intervalos aceptados para cada componente de 
    la solución x = (x_1,....x_n).
    Para asegurar que la solución x tiene todos sus componentes no
    negativos, el intervalo para cada x_j debe ser de la forma 
    (0,np.inf) o (0,None).
    El formato de bounds es una lista, cuyos elementos son tuplas (a,b),
    con tantas tuplas como activos en assets.
    '''
    bounds = []
    
    for bound in range(len(assets)):
        bounds.append((0,None))
    '''
    'constraints' son las restricciones que vamos a necesitar para calcular
    el portafolios long-only.
    En este caso vamos a necesitar sólo una restricción:
    1. const_L1: una restricción de igualdad para asegurar que la solución 
    long-only tenga norma L1 unitaria.
    '''
    const_L1 = {'type':'eq', 'fun': lambda x: np.sum(np.abs(x)) - 1}
    constraints = (const_L1)
    result = minimize(fun=portfolio_covariance,
                      x0=x0,
                      args=args,
                      bounds=bounds,
                      constraints=constraints)
    weights = result.x
    return weights


assets = ['SPY','QQQ','XLK','XLF','BTC-USD']

print(long_only_portfolio(assets))

''' 

Comprobacion: 
    
weights = [0.7395,0,0,0.2605,0] y que por construcción es unitario en la norma L1.

'''