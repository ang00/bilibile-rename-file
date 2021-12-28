#!/usr/bin/env bash

# 本地文件
bash_dir="D:\\test-name\\test"


if [ -d $bash_dir ]; then
  echo "开始转换"
  for dir in $(ls $bash_dir)
  do
     dr=$bash_dir"\\"$dir
     new_file_path=$bash_dir
     old_file_path=$bash_dir
    if [ -d "$dr" ]; then
      for d in $(ls "$dr")
      do
        c=$dr"\\"$d
        if [[ -d "$c" ]]; then
          for d in $(ls $c)
          do
            if [ "audio.m4s" == "$d" ]; then
#              获取原来文件路径和文件名
              old_file_path=$c"\\$d"
            fi
          done
        elif [[ -f "$c" && "entry.json" == $d ]]; then
#          读取 json 文件获取原来文件名
          read_result=$(cat "$c" | jq -r '.page_data.part')
          new_file_path=$new_file_path"\\"$read_result".mp3"
        fi
      done
    fi
    if test ! -f "$new_file_path" ; then
#      重新命名移动到目录下
        $(mv "$old_file_path" "$new_file_path")
    fi
  done
#  删除原来文件夹
  $(cd $bash_dir && rm -rf c_*)
else
  echo "填写的要转换的目录不正确"
fi
echo "转换完成"