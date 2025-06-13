@echo off
title Pie Face Recognition System
color 08
cls

:menu
cls
echo ==================================================
echo              PIE FACE RECOGNITION SYSTEM          
echo ==================================================
echo.
echo  [1]  Capture Face Images        (recognizer.py)
echo  [2]  Train Model                (trainer.py)
echo  [3]  Start Face Recognition     (webcam.py)
echo  [4]  Exit
echo.
choice /c 1234 /n /m "Enter your choice (1-4): "

if errorlevel 4 goto exit
if errorlevel 3 goto webcam
if errorlevel 2 goto trainer
if errorlevel 1 goto recognizer

:recognizer
cls
echo --------------------------------------------------
echo             Running Face Image Capture...
echo --------------------------------------------------
echo.
python recognizer.py
echo.
echo --------------------------------------------------
echo     Automatically training model after capture...
echo --------------------------------------------------
echo.
python trainer.py
echo.
pause
goto menu

:trainer
cls
echo --------------------------------------------------
echo         Training Face Recognition Model...
echo --------------------------------------------------
echo.
python trainer.py
echo.
pause
goto menu

:webcam
cls
echo --------------------------------------------------
echo         Starting Face Recognition System...
echo --------------------------------------------------
echo.
python webcam.py
echo.
pause
goto menu

:exit
cls
echo --------------------------------------------------
echo                 Exiting Program...
echo --------------------------------------------------
timeout /t 2 >nul
exit /b 0
