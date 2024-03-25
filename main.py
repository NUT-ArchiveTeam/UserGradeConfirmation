from unittest import result
import openpyxl
from src.config import AppConfig


def main():
    # AppConfigのインスタンスを作成
    config = AppConfig()
    result = config.get_files_and_sheets()

    if result is None:
        return print(".envを確認してください")

    files = result["files"]
    sheets = result["sheets"]
    # 設定が有効かどうかをチェック

    # 保存するファイル
    wb_result = openpyxl.Workbook()
    ws_result = wb_result.active

    # 読み込むデータ
    wb_OldUserList = openpyxl.load_workbook(files["OldUserList"])
    wb_newM1List = openpyxl.load_workbook(files["newM1List"])
    wb_newResidualList = openpyxl.load_workbook(files["newResidualList"])

    # シートの読み込み
    ws_OldUserList = wb_OldUserList[sheets["SheetOldUserList"]]
    ws_newM1List = wb_newM1List[sheets["SheetNewM1List"]]
    ws_newResidualList = wb_newResidualList[sheets["SheetNewResidualList"]]

    # 保存する
    wb_result.save('files/input_file.xlsx')


    return 0


if __name__ == "__main__":
    main()