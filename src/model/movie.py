#!/usr/bin/env python

def parseMovieInfo(soup):
	infos = ''
	info_list = []

	# Debugging or not
	isDebug = True

	# columns
	# fs = soup.find("tr", class_="firstr")
	# infos = fs.get_text()

	# movie info
	movie_infos = soup.find_all("tr", class_="odd")
	for info in movie_infos:
		info = info.get_text().strip().replace('\t\r\n\t', '')
		infos += (info + '\n\n')
		if isDebug:
			isDebug = False
			info_list = info.split('\n')
			# ['猜火车2 T2.Trainspotting.2017.2160p.BluRay.x264.8bit.SDR.DTS-HD.MA.TrueHD.7.1.Atmos-SWTYBLZ 74.15GB bt下', '《猜火车2
			# T2 Trainspotting ,T2 Trainspotting 》 主演：伊万·麦克格雷格,约翰尼·李·米勒,罗伯特·卡莱尔,艾文·布莱纳,雪莉·亨德森,
			# 安杰拉·奈迪亚科娃,史蒂文·罗伯特森,戈登·肯尼迪,西蒙·韦尔,詹姆斯·卡沙莫,梁佩诗,阿塔·雅谷伯,埃文·威尔什,凯莉·麦克唐
			# 纳,艾琳·尼古拉斯,凯文·麦克基德,艾米·曼森,波林·林奇\t\r', '\t ', '74.15GB', '14小时前', '171']
			print(info_list)
	return infos