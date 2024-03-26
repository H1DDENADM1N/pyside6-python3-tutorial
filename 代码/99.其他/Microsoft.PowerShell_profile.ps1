$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding
oh-my-posh init pwsh --config 'C:\Users\UserName\Documents\Powershell\darkblood.omp.json' | Invoke-Expression
# PSReadLine
Import-Module PSReadLine
# Enable Prediction History
Set-PSReadLineOption -PredictionSource History
# Advanced Autocompletion for arrow keys
Set-PSReadlineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward

# Shows navigable menu of all options when hitting Tab
Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete

#fzf
if(Get-Module -ListAvailable -Name "PSFzf" -ErrorAction Stop) {
    Set-PsFzfOption -PSReadlineChordProvider 'Ctrl+t' -PSReadlineChordReverseHistory 'Shift+UpArrow'
}

# fzf的主题
$ENV:FZF_DEFAULT_OPTS=@"
--layout=reverse
"@

# 类似软连接
Set-Alias touch New-Item
function ls {Color-List "-Exclude .*"}

# 取代tracert
Set-Alias -Name tracert -Value nexttrace -Option AllScope
