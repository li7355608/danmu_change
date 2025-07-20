@echo off
set script_name = ChangeXmlToCsv.py

:input
set /p filename = 请输入XML文件名:
if "%filename%" == "" (
    echo 输入为空，请重新输入。
    goto input
)
if not exist %filename% (
    echo 文件不存在，请重新输入。
    goto input
)

python %script_name% %filename%
echo.
echo 处理完成。
set /p continue = 按 y 继续，其他键退出:
if /i "%continue%" == "y" (
    goto input
)