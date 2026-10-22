# Daily Learning - Actualisation quotidienne

$ErrorActionPreference = "Stop"

$Rainmeter = "D:\App\Rainmeter\Rainmeter.exe"

Write-Host "Daily Learning : génération du contenu..."

& wsl.exe -d Ubuntu --cd /mnt/d/Git/DailyLearning -- python3 scripts/daily_content.py

if ($LASTEXITCODE -ne 0) {
    Write-Error "La génération Python a échoué."
    exit 1
}

Write-Host "Actualisation du widget Histoire..."

if (-not (Test-Path $Rainmeter)) {
    Write-Error "Rainmeter introuvable : $Rainmeter"
    exit 1
}

& $Rainmeter '!Refresh' 'DailyLearning\Histoire'
& $Rainmeter '!Refresh' 'DailyLearning\Geographie'
& $Rainmeter '!Refresh' 'DailyLearning\Culture'
& $Rainmeter '!Refresh' 'DailyLearning\Anglais'
& $Rainmeter '!Refresh' 'DailyLearning\Chinois'
& $Rainmeter '!Refresh' 'DailyLearning\Cyber'

Write-Host "Daily Learning : actualisation terminée."
