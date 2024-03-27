from unittest import result
from numpy import add, index_exp, number
import openpyxl
from src.config import AppConfig
import pandas as pd
import numpy as np

# データが上から何個目から貼っているか記載
DIFF = 2
# M1,残留、退学などを記入する横のindex
RevisionColumn = 3

# アドレスを6桁の番号に変更
def address_to_number(address):
    if(type(address) is str):
        number = address.translate(str.maketrans("","","@stn.nagaokaut.ac.jp"))
        return number

# 昨年度学生リストの「学籍番号」を読み取り、他ファイルに一致するものを探す
def OldList_loop(number_OldLists,number_NewLists,number_ResidualLists,np_save):
    for index_number_OldList in range(number_OldLists.shape[0]):
        
        # indexからデータにする
        number_OldList = number_OldLists[index_number_OldList]

        # number_NewListsにnumber_OldListがいたらtrue、いなかったらFalseのある配列を作成
        contains_NewLists = np.vectorize(lambda element: number_OldList in element)(number_NewLists)
        contains_ResidualLists = np.vectorize(lambda element: number_OldList in element)(number_ResidualLists)

        # 次年度の修士M1リストにあった場合
        if(np.any(contains_NewLists)):
            # リスト内包括表記で書いている
            # number_NewListsのfor文を回したときに、要素とindexを取り出して、取り出した要素が一致したら先頭のindexに値が格納されている
            matched_indexes = [index for index, element in enumerate(number_NewLists) if number_OldList in element]
            # 昨年度学生リストの「改訂箇所欄」に「M1」と入力
            np_save[DIFF + index_number_OldList + matched_indexes[0],RevisionColumn] = "M1"
        
        # 次年度の学部4年リストにあった場合
        elif (np.any(contains_ResidualLists)):
            matched_indexes = [index for index, element in enumerate(number_ResidualLists) if number_OldList in element]
            np_save[DIFF + index_number_OldList + matched_indexes[0],RevisionColumn] = "B4"

        # どちらにもなかった場合
        elif (np.any(contains_ResidualLists) == False and np.any(contains_NewLists) == False):
            np_save[DIFF + index_number_OldList,RevisionColumn] = "退学等"

    return np_save

def main():
    # AppConfigのインスタンスを作成
    config = AppConfig()
    result = config.get_files_and_sheets()

    # 設定が有効かどうかをチェック
    if result is None:
        return print(".envの読みこみにエラーがありました。内容を確認してください")

    # 必要なパスと名前を取得
    files = result["files"]
    sheets = result["sheets"]

    # エクセルファイルを読み取り、シートを全て読み込む
    np_OldList = pd.read_excel(files["OldList"], sheet_name=sheets["SheetOldList"]).to_numpy()
    np_NewList = pd.read_excel(files["NewList"], sheet_name=sheets["SheetNewList"]).to_numpy()
    np_ResidualList = pd.read_excel(files["ResidualList"], sheet_name=sheets["SheetResidualList"]).to_numpy()

    # 保存用
    np_save= np_OldList

    # 必要な値を取得する
    addresses_OldLists = np_OldList[DIFF:,2]
    number_NewLists = np_NewList[DIFF:,0]
    number_ResidualLists = np_ResidualList[DIFF:,0]

    print("addresses_OldLists",addresses_OldLists.shape[0])
    print("number_NewLists",number_NewLists)
    print("number_ResidualLists",number_ResidualLists)

    # address を6桁の数字に変換
    vectorized_function = np.vectorize(address_to_number)
    number_OldLists = vectorized_function(addresses_OldLists)
    print("number_OldLists",number_OldLists)

    np_save = OldList_loop(number_OldLists,number_NewLists,number_ResidualLists,np_save)

    # np_saveをpandas.Dataframeに変換してelsxで保存
    df_save = pd.DataFrame(np_save)
    df_save.to_excel('files/output.xlsx',index=False, header=False)

    return 0

if __name__ == "__main__":
    main()
