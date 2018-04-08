:: Script to setup/re-setup everything.
:: NOTE: Prior Git installation with git bash extensions is required.

REM ---------- 1. Setup global env variables and enable sh execution.
call setup_admin.bat

REM ---------- 2. Clone all repos.
call clone_repos.bat

REM ---------- 3. RC files.
call rc_files.bat

REM ---------- DONE.
