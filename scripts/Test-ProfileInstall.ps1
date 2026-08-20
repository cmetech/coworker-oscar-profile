[CmdletBinding()]
param(
    [Parameter()]
    [string]$Source = "github.com/cmetech/coworker-oscar-profile"
)

$ErrorActionPreference = "Stop"
$profileName = "oscar-install-smoke"
$installedByThisRun = $false

function Invoke-Loop24 {
    param([Parameter(Mandatory = $true)][string[]]$Arguments)

    & loop24 @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "loop24 $($Arguments -join ' ') failed with exit code $LASTEXITCODE"
    }
}

Get-Command git -ErrorAction Stop | Out-Null
Get-Command loop24 -ErrorAction Stop | Out-Null

& loop24 profile info $profileName *> $null
if ($LASTEXITCODE -eq 0) {
    throw "Disposable profile '$profileName' already exists. Remove or rename it manually before running this smoke test; this script will not delete a pre-existing profile."
}

try {
    Write-Host "Installing '$Source' as disposable profile '$profileName'..."
    Invoke-Loop24 -Arguments @(
        "profile", "install", $Source,
        "--name", $profileName,
        "--yes"
    )
    $installedByThisRun = $true

    $info = (& loop24 profile info $profileName 2>&1 | Out-String)
    if ($LASTEXITCODE -ne 0) {
        throw "Installed profile could not be inspected. Output:`n$info"
    }
    if ($info -notmatch "0\.1\.0") {
        throw "Installed profile did not report distribution version 0.1.0. Output:`n$info"
    }

    Write-Host "Install and profile-info verification passed."
}
finally {
    if ($installedByThisRun) {
        Write-Host "Deleting disposable profile '$profileName'..."
        Invoke-Loop24 -Arguments @("profile", "delete", $profileName, "--yes")

        & loop24 profile info $profileName *> $null
        if ($LASTEXITCODE -eq 0) {
            throw "Disposable profile '$profileName' still exists after deletion."
        }
        Write-Host "Removal verification passed."
    }
}
