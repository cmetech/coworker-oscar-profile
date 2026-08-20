[CmdletBinding()]
param(
    [Parameter()]
    [string]$Source = "github.com/cmetech/coworker-oscar-profile"
)

$ErrorActionPreference = "Stop"
$profileName = "oscar-install-smoke"
$installedByThisRun = $false

function Invoke-Hermes {
    param([Parameter(Mandatory = $true)][string[]]$Arguments)

    & hermes @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "hermes $($Arguments -join ' ') failed with exit code $LASTEXITCODE"
    }
}

Get-Command git -ErrorAction Stop | Out-Null
Get-Command hermes -ErrorAction Stop | Out-Null

& hermes profile info $profileName *> $null
if ($LASTEXITCODE -eq 0) {
    throw "Disposable profile '$profileName' already exists. Remove or rename it manually before running this smoke test; this script will not delete a pre-existing profile."
}

try {
    Write-Host "Installing '$Source' as disposable profile '$profileName'..."
    Invoke-Hermes -Arguments @(
        "profile", "install", $Source,
        "--name", $profileName,
        "--yes"
    )
    $installedByThisRun = $true

    $info = (& hermes profile info $profileName 2>&1 | Out-String)
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
        Invoke-Hermes -Arguments @("profile", "delete", $profileName, "--yes")

        & hermes profile info $profileName *> $null
        if ($LASTEXITCODE -eq 0) {
            throw "Disposable profile '$profileName' still exists after deletion."
        }
        Write-Host "Removal verification passed."
    }
}
