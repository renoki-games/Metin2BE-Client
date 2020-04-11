@echo off
if "%~1"=="" (
	echo "drag n drop the .eix on this .bat"
) else (
	if not exist "%~1\nul" (
		PackMakerLite --nolog -u "%~n1"
	) else (
		echo "%~1 not a .eix/epk to unpack"
	)
)
pause
