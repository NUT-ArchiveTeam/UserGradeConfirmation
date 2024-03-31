import numpy as np
import pandas as pd

from src.config import AppConfig

# データが上から何個目から貼っているか記載
DIFF = 3
# M1,残留、退学などを記入する横のindex
RevisionColumn = 2


# アドレスを6桁の番号に変更
def address_to_number(address):
    if isinstance(address, str):
        number = address.translate(str.maketrans("", "", "@stn.nagaokaut.ac.jp"))
        return number


# 昨年度学生リストの「学籍番号」を読み取り、他ファイルに一致するものを探す
def OldList_loop(
    number_OldLists, number_NewLists, number_ResidualLists, np_save, grades
):
    for index_number_OldList in range(number_OldLists.shape[0]):
        # indexからデータにする
        number_OldList = number_OldLists[index_number_OldList]

        # 次年度の修士M1リストにあった場合
        for number_index_NewList in range(number_NewLists.shape[0]):
            number_NewList = str(number_NewLists[number_index_NewList])[:-2]
            if len(number_NewList) == 6:
                if number_OldList == number_NewList:
                    np_save[index_number_OldList, RevisionColumn] = grades["NewGrade"]

        # 次年度の学部4年リストにあった場合
        for number_index_ResidualList in range(number_ResidualLists.shape[0]):
            number_ResidualList = str(number_ResidualLists[number_index_ResidualList])[
                :-2
            ]
            if len(number_ResidualList) == 6:
                if number_OldList == number_ResidualList:
                    np_save[index_number_OldList, RevisionColumn] = grades["OldGrade"]

        if not np_save[index_number_OldList, RevisionColumn]:
            np_save[index_number_OldList, RevisionColumn] = "退学等"

    return np_save


# 次年度の学生リストの「学籍番号」を読み取り、昨年度学生リストに一致する者がない場合、追加を示す
def NewList_loop(number_OldLists, number_NewLists, np_NewList, np_save, grades):
    # 次年度の学生一覧でforを回す
    for number_index_NewList in range(number_NewLists.shape[0]):
        # 次年度の学生は8桁の学籍番号が数値で入っているため文字にして最後2桁を削る
        number_NewList = number_NewLists[number_index_NewList]
        if isinstance(number_NewList, int):
            number_NewList = str(number_NewList)[:-2]
            # 昨年度学生一覧の中に、今回のインデックスの次年度学生が存在するか判定
            contains_OldLists = np.vectorize(lambda element: number_NewList in element)(
                number_OldLists
            )
            # 次年度学生が昨年度学生に含まれていない場合の処理
            if not np.any(contains_OldLists):
                np_save = np.append(
                    np_save,
                    [
                        [
                            np_NewList[DIFF + number_index_NewList + 1, 3],
                            "s" + str(number_NewList),
                            grades["NewGrade"] + "追加",
                        ]
                    ],
                    axis=0,
                )

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
    grades = result["grades"]

    # エクセルファイルを読み取り、シートを全て読み込む
    np_OldList = pd.read_excel(files["OldList"], header=None, index_col=None).to_numpy()
    np_NewList = pd.read_excel(files["NewList"], header=None, index_col=None).to_numpy()
    np_ResidualList = pd.read_excel(
        files["ResidualList"], header=None, index_col=None
    ).to_numpy()

    # print("addresses_OldLists", np_OldList)
    # print("number_NewLists", np_NewList)
    # print("number_ResidualLists", np_ResidualList)

    # 保存用
    np_save = np_OldList
    new_column_empty_str = np.empty((np_save.shape[0], 1), dtype=str)
    new_column_empty_str[:] = ""
    np_save = np.hstack((np_save, new_column_empty_str))

    # 必要な値を取得する
    addresses_OldLists = np_OldList[:, 1]
    number_NewLists = np_NewList[DIFF:, 1]
    number_ResidualLists = np_ResidualList[DIFF:, 1]

    # address を6桁の数字に変換
    vectorized_function = np.vectorize(address_to_number)
    number_OldLists = vectorized_function(addresses_OldLists)

    np_save = OldList_loop(
        number_OldLists, number_NewLists, number_ResidualLists, np_save, grades
    )

    np_save = NewList_loop(
        number_OldLists, number_NewLists, np_NewList, np_save, grades
    )

    # np_saveをpandas.Dataframeに変換してelsxで保存
    df_save = pd.DataFrame(np_save)
    df_save.to_excel(files["CreateList"], index=False, header=False)

    return 0


if __name__ == "__main__":
    main()
