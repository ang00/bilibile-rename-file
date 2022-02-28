# -*-coding: UTF-8 -*-
import json
import os.path
import shutil

bastFilePath = "C:\\Users\\zhang\\Downloads\\下载\\"

project_id = "680890718"


def rename_file():
    dir_list = os.listdir(bastFilePath + project_id + "\\")
    dir_list.sort(key=len)
    new_dir = ""
    for dir in dir_list:
        dir_c = os.path.join(bastFilePath + project_id + "\\" + dir)
        if os.path.isdir(dir_c):
            dir_list_c = os.listdir(dir_c)
            for d in dir_list_c:
                c = os.path.join(dir_c, d)
                old_path = dir_c + "\\" + project_id + "_" + dir + "_" + "0" + ".mp4"
                if os.path.isfile(c) and d == project_id + ".info":
                    with open(c, "r", encoding="utf-8") as fp:
                        json_data = json.load(fp)
                        new_file_name = json_data["PartName"]
                        new_path = bastFilePath + project_id + "\\" + new_file_name + ".mp4"
                        # 判断视频信息重命名
                        if os.path.exists(old_path) and os.path.isfile(old_path) and not os.path.exists(new_path):
                            os.rename(old_path, new_path)
            # 删除子文件夹
            shutil.rmtree(dir_c)
        elif os.path.isfile(dir_c) and project_id + ".dvi" == dir:
            with open(dir_c, "r", encoding="utf-8") as fp:
                json_data = json.load(fp)
                dir_name = json_data['Title']
                new_dir = dir_name
                if not os.path.exists(bastFilePath + dir_name):
                    os.mkdir(bastFilePath + dir_name)
        elif os.path.isfile(dir_c) and ".mp4" != os.path.splitext(dir_c)[-1]:
            os.remove(dir_c)
    for dir in dir_list:
        dir_c = os.path.join(bastFilePath + project_id + "\\" + dir)
        if os.path.isfile(dir_c) and ".mp4" == os.path.splitext(dir_c)[-1]:
            os.rename(dir_c, bastFilePath + new_dir + "\\" + dir)
    # if os.path.exists(bastFilePath + project_id):
        # shutil.rmtree(bastFilePath + project_id)
        # os.remove(bastFilePath + project_id)


if __name__ == '__main__':
    rename_file()
    print("success")
