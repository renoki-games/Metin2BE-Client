import os
import localeInfo
#import os.path

STATE_NONE = "red"

STATE_DICT = {
	0 : "red",
	1 : "green",
	2 : "yellow",
	3 : "cyan"
}
STATE_TEXT_NONE = "off"

STATE_TEXT_DICT = {
	0 : "....",
	1 : "NORM",
	2 : "BUSY",
	3 : "FULL"
}

MAIN_SERVER_IP = "45.85.218.22"

SRV_LIST = ((
	(
		"Mosha",							 				#[1]
		11000,
		(MAIN_SERVER_IP, 13100, "10.tga", "10"),		#[1][0, 1, 2, 3]
		[
			("CH1   ", MAIN_SERVER_IP, 13100, 13100, 0),   #[2][0][0, 1, 2, 3]
			("CH2   ", MAIN_SERVER_IP, 13200, 13200, 0),	
			("CH3   ", MAIN_SERVER_IP, 13030, 11002, 0),
			("CH4   ", MAIN_SERVER_IP, 13040, 11002, 0),
			# NAME   ,     IP        , GAMEP, SLAVE
		]
	),
),
)

# Used for server state determination - filled by introLogin.py
SERVER_STATE_TABLE = {}