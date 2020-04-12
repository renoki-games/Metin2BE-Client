import app
import localeInfo
app.ServerName = None

SRV1 = {
	"name":"ServerName",
	"host":"45.85.216.15",
	"auth1":30001,
	"ch1":30003,
	"ch2":30007,
}

STATE_NONE = "..."

STATE_DICT = {
	0 : "....",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

SERVER1_CHANNEL_DICT = {
	1:{"key":11,"name":"Channel 1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"Channel 2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : SRV1["name"],
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
		2 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
	}
}

REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : SERVER1_CHANNEL_DICT, },
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
}

TESTADDR = { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "udp_port" : SRV1["ch1"], }

#DONE


