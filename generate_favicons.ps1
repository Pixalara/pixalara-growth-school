Add-Type -AssemblyName System.Drawing

$sourcePath = "d:\Pixalara Growth School\growth school repo\assets\images\logo.png"
$img = [System.Drawing.Image]::FromFile($sourcePath)

function Save-ResizedImage {
    param([int]$size, [string]$outPath, [bool]$isIco)
    
    $bmp = New-Object System.Drawing.Bitmap($size, $size)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.Clear([System.Drawing.Color]::Transparent)
    
    # Calculate scale to fit within the square
    $scale = [math]::Min($size / $img.Width, $size / $img.Height)
    $newWidth = [int]($img.Width * $scale)
    $newHeight = [int]($img.Height * $scale)
    
    # Center the image
    $x = ($size - $newWidth) / 2
    $y = ($size - $newHeight) / 2
    
    $g.DrawImage($img, $x, $y, $newWidth, $newHeight)
    
    if ($isIco) {
        # Browsers accept PNG content named as .ico
        $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
    } else {
        $bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
    }
    
    $g.Dispose()
    $bmp.Dispose()
}

$repoPath = "d:\Pixalara Growth School\growth school repo"

Save-ResizedImage -size 180 -outPath "$repoPath\assets\images\apple-touch-icon.png" -isIco $false
Save-ResizedImage -size 32 -outPath "$repoPath\assets\images\favicon-32x32.png" -isIco $false
Save-ResizedImage -size 16 -outPath "$repoPath\assets\images\favicon-16x16.png" -isIco $false
Save-ResizedImage -size 64 -outPath "$repoPath\favicon.ico" -isIco $true

$img.Dispose()
