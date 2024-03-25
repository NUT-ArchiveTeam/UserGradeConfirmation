from unittest import result
import openpyxl
from src.config import AppConfig


def 

def main():
    # AppConfigのインスタンスを作成
    config = AppConfig()
    result = config.get_files_and_sheets()

    if result is None:
        return print(".envの読みこみにエラーがありました。内容を確認してください")

    files = result["files"]
    sheets = result["sheets"]
    # 設定が有効かどうかをチェック

    # 保存するファイル
    wb_result = openpyxl.Workbook()
    ws_result = wb_result.active

    # 読み込むデータ
    wb_OldList = openpyxl.load_workbook(files["OldList"])
    wb_NewList = openpyxl.load_workbook(files["NewList"])
    wb_ResidualList = openpyxl.load_workbook(files["ResidualList"])

    # シートの読み込み
    ws_OldList = wb_OldList[sheets["SheetOldList"]]
    ws_NewList = wb_NewList[sheets["SheetNewList"]]
    ws_ResidualList = wb_ResidualList[sheets["SheetResidualList"]]



    # 保存する
    wb_result.save('files/input_file.xlsx')


    return 0


if __name__ == "__main__":
    main()