import openpyxl
from src import config


def main():
    files = config.files

    # 保存するファイル
    wb_result = openpyxl.Workbook()

    # 読み込むデータ
    wb_OldUserList = openpyxl.load_workbook(files["OldUserList"])
    wb_newM1List = openpyxl.load_workbook(files["newM1List"])
    wb_newResidualList = openpyxl.load_workbook(files["newResidualList"])

    # 保存する
    wb_result.save('files/input_file.xlsx')


    return 0


if __name__ == "__main__":
    main()