Write-Host "Start converting formats.."

$src_path = 'raw_videos'
$dst_path = 'raw_videos_mp4'

if (-Not (Test-Path $dst_path)) {
	New-Item -ItemType Directory $dst_path
}

$total = (Get-ChildItem -Path $src_path).Count
$i = 0

foreach ($filename in Get-ChildItem -Path $src_path) {
    $i++
    $filename = $filename.ToString()
    $extension = $filename.Split('.')[-1]
    $dst_file = Join-Path $dst_path "$($filename -replace "\.$extension").mp4"

    if (Test-Path $dst_file) {
        Write-Host "$i/$total, $dst_file exists."
        continue
    }
    
    Write-Host "$i/$total, $filename"
    
    $src_file = Join-Path "$src_path" "$filename"
    if ($extension -ne "mp4") {
        ffmpeg -loglevel panic -i "$src_file" -vf pad="width=ceil(iw/2)*2:height=ceil(ih/2)*2" "$dst_file"
    } else {
        Copy-Item $src_file $dst_file
    }
}

Write-Host "Finish converting formats.."
