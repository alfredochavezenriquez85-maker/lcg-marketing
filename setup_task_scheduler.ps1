# setup_task_scheduler.ps1
# Configura Windows Task Scheduler para enviar el reporte cada lunes a las 07:00 AM
# Ejecutar como Administrador: powershell -ExecutionPolicy Bypass -File setup_task_scheduler.ps1

$taskName = "LCG_LinkedIn_Report_Weekly"
$description = "Envia reporte semanal de LinkedIn LCG Mexico cada lunes a las 07:00 AM"

# Ruta al proyecto
$projectPath = "C:\Users\alfre\Desktop\Claude Code\lcg-marketing"
$pythonPath = (Get-Command python).Source

# Crear la accion: ejecutar python send_report.py
$action = New-ScheduledTaskAction `
    -Execute $pythonPath `
    -Argument "send_report.py" `
    -WorkingDirectory $projectPath

# Trigger: cada lunes a las 07:00
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 7:00AM

# Configuracion: ejecutar aunque no haya sesion iniciada, despertar PC si esta dormida
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -WakeToRun `
    -StartWhenAvailable

# Eliminar tarea anterior si existe
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue

# Registrar la nueva tarea
Register-ScheduledTask `
    -TaskName $taskName `
    -Description $description `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -RunLevel Highest

Write-Host ""
Write-Host "Tarea programada creada exitosamente!" -ForegroundColor Green
Write-Host "  Nombre: $taskName" -ForegroundColor Cyan
Write-Host "  Horario: Cada lunes a las 07:00 AM" -ForegroundColor Cyan
Write-Host "  Accion: python send_report.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para verificar, ejecuta:" -ForegroundColor Yellow
Write-Host "  Get-ScheduledTask -TaskName '$taskName'" -ForegroundColor Yellow
Write-Host ""
Write-Host "Para probar ahora:" -ForegroundColor Yellow
Write-Host "  Start-ScheduledTask -TaskName '$taskName'" -ForegroundColor Yellow
