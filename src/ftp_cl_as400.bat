:: Connect to IBM i (AS/400) and call the Payroll  adjustment process.
:: By Clay Lanzino.  Noviembre del 2022


@echo off
SetLocal EnableDelayedExpansion
color A
echo.
echo.
echo ###  Starting running Client Interface to ---> IBM i.  Please wait for the process to finish...   ###
echo Argumentos: %*


set _tst=0
for /f %%@ in (.env) do (call :sub %%@
               set _str=%%@)  
               echo Total = %_tst%
               goto :_next
:sub
echo [%1] & set /a _tst+=1
if %_tst%  == 3 (set _host=%2)
if %_tst%  == 4 (set _str1=%2 
                 set _user=!_str1:~1,5!)
if %_tst%  == 5 (set _str2=%2
                 set _pass=!_str2:~1,8!)

exit /b         :: back to the for loop ...     
:_next

:: echo  servidor   !_host!
:: echo  usuario    !_user!
:: echo  password   !_pass!

set FTPSCRIPT=clubtech.fts
set HOST=!_host!
set USER=!_user!
set PASS=!_pass!

:: echo ... !HOST!
:: echo ... !USER!
:: echo ... !PASS!

echo %USER% > %FTPSCRIPT%
echo %PASS% >> %FTPSCRIPT%
echo cd SPIDATA >> %FTPSCRIPT%
echo quote site namefmt 0 >> %FTPSCRIPT%
echo quote rcmd call Temporal/Uti933_C >> %FTPSCRIPT%
echo ascii >> %FTPSCRIPT%
echo quit >> %FTPSCRIPT%
ftp -s:%FTPSCRIPT% %HOST%
echo PAUSE
del %FTPSCRIPT%



