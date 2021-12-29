package main

import (
	"fmt"
	"github.com/tidwall/gjson"
	"io/ioutil"
	"os"
	"time"
)

func main() {
	fmt.Printf(time.Now().Format("2006-01-02 15:04:05"))
	const baseDir = "D:/test-name/test/"
	files, err := ioutil.ReadDir(baseDir)
	if err != nil {
		panic(err)
	}
	for _, file := range files {
		if file.IsDir() {
			var oldPathName string
			var newPathName string
			fs, er := ioutil.ReadDir(baseDir + file.Name())
			if er != nil {
				panic(er)
			}
			for _, f := range fs {
				if f.IsDir() {
					as, e := ioutil.ReadDir(baseDir + file.Name() + "/" + f.Name())
					if e != nil {
						panic(e)
					}
					for _, a := range as {
						if a.Name() == "audio.m4s" {
							oldPathName = baseDir + file.Name() + "/" + f.Name() + "/" + a.Name()
						}
					}
				} else if f.Size() > 0 && "entry.json" == f.Name() {
					entry, e := ioutil.ReadFile(baseDir + file.Name() + "/" + f.Name())
					if e != nil {
						panic(e)
					}
					content := string(entry)
					value := gjson.Get(content, "page_data.part")
					newPathName = baseDir + value.String() + ".mp3"
					os.Rename(oldPathName, newPathName)
				}
			}
			//
			os.RemoveAll(baseDir + file.Name())
		}
	}
	fmt.Println("success ")
}
