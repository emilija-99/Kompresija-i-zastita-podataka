function New-RandomFile {
    param(
        [string]$Path,
        [int]$Size,
        [int]$BlockSize = 1MB
    )

    $count = [math]::Floor($Size/$BlockSize)
    $reminder = $Size / $BlockSize

    $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
    
    try{
        $fs = [System.IO.File]::Open($Path, [System.IO.FileMode]::Create, [System.IO.FileAccess]::Write, [System.IO.FileShare]::None)
        try{
            $buffer = New-Object byte[] $BlockSize
            for ($i = 0; $i -lt $count; $i++) {
                $rng.GetBytes($buffer, 0, $BlockSize)
                $fs.Write($buffer)
            }
            if($reminder -gt 0){
                $tail = New-Object byte[] $reminder
                $rng.GetBytes($tail)
                $fs.Write($tail,0,$reminder)
            }
        } finally{
            $fs.Dispose()
        }
    }finally{
        $rng.Dispose()
    }
}

function New-TextFile{
    param(
        [Parameter(Mandatory)][string]$Path, 
        [Parameter(Mandatory)][long]$Size,
        [ValidateSet("random-b64","random-ascii","pattern-text")]
        [string]$Kind = "random-b64"
    )

    $utf8 = New-Object System.Text.UTF8Encoding($false)

    switch ($Kind) {
        "random-b64"{
            $n = [math]::Floor((($Size)/4))*3 # base 64 size
            if($n -lt 3) {
                $n = 3
            }

            $rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
            try{
                $bytes = New-Object byte[] $n 
                $rng.GetBytes($bytes)
            }finally{
                $rng.Dispose()
            }

            $b64 = [System.Convert]::ToBase64String($bytes)

            if($b64.Length -gt $Size){
                $text = $b64.Substring(0,[int]$Size)
            }
            elseif($b64.Length -lt $Size){
                $padLen = [int]($Size - $b64.Length)
                for($i = 0; $i -lt $padLen; $i++){
                    $ch = [char](Get-Random -Minimum 97 -Maximum 123)
                    $b64 = $b64 + $ch
                }
            }
            else{
                $text = $b64;
            }

            [System.IO.File]::WriteAllText($Path,$text,$utf8);
        }
        "random-ascii"{
            $alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
            $rng = New-Object System.Random
            $sb = New-Object System.Text.StringBuilder([int]$Size)
            for($i = 0; $i -lt $Size; $i++){
                [void]$sb.Append($alphabet[$rng.Next(0,$alphabet.Length)])
            }
            [System.IO.File]::WriteAllText($Path, $sb.ToString(),$utf8)
        }
        "pattern-text"{

        }
    }

}