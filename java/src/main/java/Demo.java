import cn.hutool.core.util.StrUtil;
import cn.hutool.json.JSONUtil;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * @Author: zhangyy
 * @Email: zhang10092009@hotmail.com
 * @Date: 2021/12/7 10:11:32
 * @Version: v1.0
 * @Modified：
 * @Description:
 */
public class Demo {
    //要替换的文件夹路径
    private static final String bashPathStr = "D:\\test-name\\test";
    //替换后的文件后缀
    private static final String fileSuffix = "mp3";
    /**
     * 需要替换修改的文件名称
     */
    private static final List<String> fileNames = Arrays.asList("audio.m4s", "audio.mp3");

    public static void main(String[] args) throws IOException {
        Demo demo = new Demo();
        demo.reName();
    }

    public void reName() throws IOException {

        File bashList = new File(bashPathStr);
        File[] files = bashList.listFiles();
        for (File file : files) {
            if (file.isDirectory()) {
                File[] fs = file.listFiles();
                HashMap<String, String> stringStringHashMap = new HashMap<>(16);
                for (File f : fs) {
                    if (f.isFile()) {
                        //获取文件后缀文件名
                        String fName = f.getName();
                        String suffix = fName.substring(fName.lastIndexOf("."));
                        if (suffix.equals(".json")) {
                            String jsonStr = Files.readString(f.toPath());
                            Map page_data = JSONUtil.parseObj(jsonStr).get("page_data", Map.class);
                            if (page_data != null) {
                                String part = (String) page_data.get("part");
                                if (StrUtil.isNotBlank(part)) {
                                    stringStringHashMap.put("newName", part);
                                }
                            }
                        }
                    }
                    if (f.isDirectory()) {
                        File[] fs1 = f.listFiles();
                        for (File f1 : fs1) {
                            if (f1.isFile() && fileNames.contains(f1.getName())) {
                                String pathStr = f1.toPath().toString();
                                if (StrUtil.isNotBlank(pathStr)) {
                                    stringStringHashMap.put("path", pathStr);
                                }
                            }
                        }
                    }
                }
                String path = stringStringHashMap.get("path");
                String fileName = stringStringHashMap.get("newName");
                if (null != path && null != fileName && StrUtil.isNotBlank(path) && StrUtil.isNotBlank(fileName)) {
                    File fileOld = new File(path);
                    //拼接新的文件路径
                    String newFilePath = bashPathStr + File.separator + fileName + "." + fileSuffix;
                    File newFile = new File(newFilePath);
                    if (fileOld.exists() && fileOld.isFile()) {
                        //判断文件名是否有重名文件
                        if (!newFile.exists()) {
                            //重命名文件
                            fileOld.renameTo(newFile);
                        }
                    }
                }
            }
            // 删除文件夹及子文件
            if (file.exists() && file.isDirectory()) {
                deleteFile(file);
            }
        }
    }

    private void deleteFile(File file) {
        if (file.exists()) {
            File[] files = file.listFiles();
            if (file.isDirectory() && files.length > 0) {
                if (files.length == 1) {
                    files[0].delete();
                } else {
                    for (File f : files) {
                        if (f.isFile()) {
                            f.delete();
                        }
                        deleteFile(f);
                    }
                }
            }
            file.delete();
        }
    }
}
