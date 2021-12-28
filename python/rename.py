import json
import os.path
import shutil

bastFilePath = "D:\\test-name\\test\\"

file_name = "audio.m4s"


def rename_file():
    dir_list = os.listdir(bastFilePath)
    for dir in dir_list:
        dir_c = os.path.join(bastFilePath + dir)
        if os.path.isdir(dir_c):
            new_path = ''
            dir_list_c = os.listdir(dir_c)
            for d in dir_list_c:
                c = os.path.join(dir_c, d)
                if os.path.isdir(c):
                    # 是文件夹进行遍历修改文件
                    s = os.listdir(c)
                    for m in s:
                        a = os.path.join(c, m)
                        if os.path.isfile(a) and (file_name == m):
                            new_path = a
                # 只有读取到文件才读取要修改的文件并且能获取到保存文件名的文件
                elif len(new_path) > 0 and os.path.isfile(c) and d == "entry.json":
                    with open(c, "r", encoding="utf8") as fp:
                        # 读取文件数据
                        json_data = json.load(fp)
                        # 获取到文件名称
                        new_file_name = json_data['page_data']['part']
                        # 改名文件移动到根文件夹下
                        os.rename(new_path, os.path.join(bastFilePath + new_file_name + ".mp3"))

    # 删除原来文件夹
    for f in dir_list:
        dir_c = os.path.join(bastFilePath, f)
        if os.path.isdir(dir_c):
            shutil.rmtree(dir_c)


if __name__ == '__main__':
    rename_file()
    print("success")
