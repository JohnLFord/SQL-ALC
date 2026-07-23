param(
    [Parameter(Mandatory = $true)]
    [string]$Message
)

$ErrorActionPreference = "Stop"

git status --short
git add .
git commit -m $Message
git push