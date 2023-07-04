import pandas as pd
import glob


# def xlsx_concat(df, filename, sheetname):
#     new_df = pd.read_excel(filename, sheet_name=sheetname, dtype=str)
#     try:
#         df = pd.concat([df, new_df])
#     except Exception as e:
#         msg = 'Failed to concatenate table with previous tables'
#         print(msg)
#         log.append(msg)
#         global count
#         count += 1
#     return df
#
#
# # Function joins all xlsx tables inside the selected folder into two big csv tables
#
# def tbl_join(folder):
#     fld_msg = f'Work folder is {folder}'
#     log.append(fld_msg)
#     print(fld_msg)
#
#     files = glob.glob(folder + "*.xlsx")  # list of .xlsx files inside the folder
#     df1, df2 = pd.DataFrame(), pd.DataFrame()  # Dataframes for distinct types of tables
#
#     for file in files:
#         print(file)
#         log.append(file)
#         try:
#             df1 = xlsx_concat(df1, file, sheet_name_1)  # Tables with 'ГТД' number
#         except Exception as e:
#             try:
#                 df2 = xlsx_concat(df2, file, sheet_name_2)  # Tables without 'ГТД' number
#             except Exception as e:
#                 msg = 'Failed to read excel'
#                 print(msg)
#                 log.append(msg)
#                 count += 1
#                 continue
#     df1 = df1.reset_index(drop=True)
#     return [df1, df2]
#
#
dir1 = 'c:/Kotomin/StatWorks/6_Маркетинг/2023_06_analysis/1/'
dir2 = 'c:/Kotomin/StatWorks/6_Маркетинг/2023_06_analysis/2/'
dir3 = 'c:/Kotomin/StatWorks/6_Маркетинг/2023_06_analysis/2/'
dir4 = 'c:/Kotomin/StatWorks/6_Маркетинг/2023_06_analysis/2/'

sheet_name_1 = 'Sheet1'  # type 1 table name (with 'ГТД')
sheet_name_2 = 'ВЭД РФ'  # type 2 table name (without 'ГТД')
#
# for dir in [dir1, dir2, dir3, dir4]:
#     log = []  # error log
#     count = 0  # error counter
#
#     df_list = tbl_join(dir)
#     df_w_gtd, df_wo_gtd = df_list  # dataframes with distinct table types
#
#     log.append(f'Unprocessed files: {count}')
#
#     df_w_gtd.to_csv(dir + sheet_name_1 + '.csv', sep=';')
#     df_wo_gtd.to_csv(dir + sheet_name_2 + '.csv', sep=';')
#
#     df_w_gtd, df_wo_gtd = df_w_gtd.drop(df_w_gtd.index), df_wo_gtd.drop(df_wo_gtd.index)  # memory clean
#
#     logfile = pd.Series(log)
#     logfile.to_csv(dir + 'log' + '.csv')


# Concatenate 'Sheet1' tables from folders from 1 to 4

gtd_df_1 = pd.read_csv(dir1 + sheet_name_1 + '.csv', dtype=str, sep=';')
gtd_df_2 = pd.read_csv(dir2 + sheet_name_1 + '.csv', dtype=str, sep=';')
gtd_df_3 = pd.read_csv(dir3 + sheet_name_1 + '.csv', dtype=str, sep=';')
gtd_df_4 = pd.read_csv(dir4 + sheet_name_1 + '.csv', dtype=str, sep=';')

gtd_df_full = pd.concat([gtd_df_1, gtd_df_2, gtd_df_3, gtd_df_4]).reset_index(drop=True)
del gtd_df_full['Unnamed: 0']
gtd_df_full.to_csv(dir1 + 'Database' + '.csv', sep=';')
