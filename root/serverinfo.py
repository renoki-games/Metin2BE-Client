import app
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
app.ServerName = None

SRV1 = {
	"name":"Mosha",
	"host":"45.85.218.22",
	"auth1":11000,
	"ch1":13100,
	"ch2":13200,
	"ch3":13300,
	"ch4":13400,
}

STATE_LOAD = "Load.."
STATE_NONE = "OFF"

STATE_DICT = {
	0 : "....",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

SRV1_LIST = {
	1:{"key":11,"name":"CH1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"CH2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":11,"name":"CH3","ip":SRV1["host"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
	4:{"key":12,"name":"CH4","ip":SRV1["host"],"tcp_port":SRV1["ch4"],"udp_port":SRV1["ch4"],"state":STATE_NONE,},
}

REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : SRV1_LIST, },
	},
}



