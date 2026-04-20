Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile("d:\Pixalara Growth School\growth school repo\assets\images\logo.png")
$bmp = New-Object System.Drawing.Bitmap($img)
$img.Dispose()
$bmp.MakeTransparent([System.Drawing.Color]::White)
$bmp.Save("d:\Pixalara Growth School\growth school repo\assets\images\logo.png", [System.Drawing.Imaging.ImageFormat]::Png)
