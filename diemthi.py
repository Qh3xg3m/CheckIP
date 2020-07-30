#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import re

# max = 350388
def getText(sbd):
	url = "http://ninhbinh.edu.vn/?module=Content.Listing&moduleId=1011&cmd=redraw&site=19216&url_mode=rewrite&submitFormId=1011&moduleId=1011&page=&site=19216"
	data = {
		"layout" : "Decl.DataSet.Detail.default",
		"itemsPerPage" : "-1",
		"pageNo" : "1",
		"service" : "Content.Decl.DataSet.Grouping.select",
		"itemId" : "5f1e41cee1382373bc7e9eb2",
		"gridModuleParentId" : "11",
		"type" : "Decl.DataSet",
		"modulePosition" : "0",
		"moduleParentId" : "-1",
		"keyword" : "350388",
		"_t" : "1595831489200"
		}
	data["keyword"] = sbd
	res = requests.post(url,data = data)
	return(res.text)

f = open("diem.txt","w")
for i in range(350001,350089):
	text = getText(i)
	match = """<em>Có 1 bản ghi.</em><div class="table-responsive" >\n<table class="table table-bordered table-hover"> <thead>  <tr>  <th style=""  >SBD</th>\n <th style=""  >Điểm thi môn Ngữ văn</th>\n <th style=""  >Điểm thi môn Toán</th>\n <th style=""  >Điểm thi môn Tiếng Anh</th>\n <th style=""  >Điểm bài thi môn chuyên</th>\n</tr> </thead> <tbody>  <tr>  <td  >(\\d{6}.*) </td>  <td  >(.*) </td>  <td  >(.*) </td>  <td  >(.*) </td>  <td  >(.*)</td> </tr> </tbody> </table></div><style>"""
	data = re.search(match,text)
	sbd,van,toan,anh,chuyen = data[1], data[2], data[3], data[4],data[5]
	tongdiem = float(van) + float(toan) + float(anh)
	ketqua = "{0} {1} {2} {3} {4} {5} \n".format(sbd,van,toan,anh,chuyen,tongdiem)
	f.write(ketqua)
	print(sbd,van,toan,anh,tongdiem)
f.close()





