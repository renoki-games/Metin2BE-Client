@echo off
if "%~1"=="" (
	echo "drag n drop the folder on this .bat"
) else (
	if exist "%~1" (
		PackMakerLite --nolog -p "%~n1"
		move %~n1.epk ../Metin2/pack/
		move %~n1.eix ../Metin2/pack/
	) else (
		echo "%~1 not a folder to pack"
	)
)