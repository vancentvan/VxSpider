#!/usr/bin/env python

def parseTicketInfo(soup):
	infos = ''
	info_list = []

	# Debugging or not
	isDebug = True

	# ticket info
	ticket_infos = soup.find_all("div", class_="visible-xs")
	for info in ticket_infos:
		info = info.get_text().strip().replace('\n\n', '')
		infos += (info + '\n\n')
		if isDebug:
			isDebug = False
			info_list = info.split('\n')
			# ['周杰倫 香港演唱會 2018', '演出日期: 2018年3月15日 - 25日 (共10場)', '門票價錢: HK$1180 / $780 / $480', '演出場館: ', '
			# 紅磡香港體育館', '', '', '優先購票: 2017年11月20日(一) (東亞信用卡)', '公開發售: 2017年12月1日(五)10am起', '加場公開發售
			# : 2017年12月14日(四)08am起']
			print(info_list)
	return infos