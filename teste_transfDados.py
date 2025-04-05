import tabula
import pandas as pd
import zipfile
import os

nome = "Álefh"  

columns_order = [
    "PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA",
    "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
]

def extract_tables(file, pages, method, area=None, guess=True):
    # method: "lattice" ou "stream"
    try:
        if area:
            dfs = tabula.read_pdf(
                file,
                pages=pages,
                multiple_tables=True,
                **{method: True},
                area=area,
                guess=guess
            )
        else:
            dfs = tabula.read_pdf(
                file,
                pages=pages,
                multiple_tables=True,
                **{method: True}
            )
    except Exception as e:
        print(f"Erro na extração das páginas {pages} com {method}: {e}")
        dfs = None
    return dfs

dfs_main = extract_tables("anexo2.pdf", "3-180", "lattice")
if not dfs_main or len(dfs_main) == 0:
    print("Falha na extração das páginas 3-180 sem área, tentando com área definida.")
    area_main = [130.43677230834962, 54.304299710998315, 776.4093589782715, 1365.7706226480102]
    dfs_main = extract_tables("anexo2.pdf", "3-180", "lattice", area=area_main)

if not dfs_main or len(dfs_main) == 0:
    print("Nenhuma tabela encontrada nas páginas 3-180.")
    exit()

dfs_last = extract_tables("anexo2.pdf", "181", "lattice")
if not dfs_last or len(dfs_last) == 0:
    print("Falha na extração da página 181 com lattice, tentando com stream e área definida.")
    area_last = [130.43677230834962, 54.304299710998315, 776.4093589782715, 1365.7706226480102]
    dfs_last = extract_tables("anexo2.pdf", "181", "stream", area=area_last, guess=False)

if not dfs_last or len(dfs_last) == 0:
    print("Nenhuma tabela encontrada na página 181.")
    exit()

df_main = pd.concat(dfs_main, ignore_index=True)
df_last = pd.concat(dfs_last, ignore_index=True)
df_final = pd.concat([df_main, df_last], ignore_index=True)

df_final.dropna(how="all", inplace=True)

def strip_cell(x):
    return x.strip() if isinstance(x, str) else x

df_final = df_final.apply(lambda col: col.map(strip_cell) if col.dtype == "object" else col)

if "PROCEDIMENTO" in df_final.columns:
    df_final = df_final[df_final["PROCEDIMENTO"].str.strip() != "PROCEDIMENTO"]

df_final.rename(
    columns=lambda x: "Seg. Odontológica" if x.strip().upper() == "OD" 
                      else ("Seg. Ambulatorial" if x.strip().upper() == "AMB" else x),
    inplace=True
)

for col in columns_order:
    if col not in df_final.columns:
        df_final[col] = ""

final_columns_order = [
    "PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA",
    "Seg. Odontológica", "Seg. Ambulatorial", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
]
df_final = df_final[final_columns_order]

df_final.reset_index(drop=True, inplace=True)

excel_filename = f"Teste_{nome}.xlsx"
with pd.ExcelWriter(excel_filename, engine="xlsxwriter") as writer:
    df_final.to_excel(writer, index=False, sheet_name="Dados")
    workbook  = writer.book
    worksheet = writer.sheets["Dados"]
    header_format = workbook.add_format({'bold': True})
    for col_num, value in enumerate(df_final.columns.values):
        worksheet.write(0, col_num, value, header_format)
print(f"Arquivo Excel salvo: {excel_filename}")