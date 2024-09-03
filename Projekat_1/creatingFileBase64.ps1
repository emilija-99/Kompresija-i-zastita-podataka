[System.Reflection.Assembly]::LoadWithPartialName("System.Web") | Out-Null
$rand = New-Object System.Security.Cryptography.RNGCryptoServiceProvider
$bytes = New-Object Byte[] 1048576
$rand.GetBytes($bytes)
$base64string = [System.Web.HttpServerUtility]::UrlTokenEncode($bytes)
$base64string | Out-File -FilePath file.txt -Encoding ascii