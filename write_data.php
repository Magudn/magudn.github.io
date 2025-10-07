<?php
// Get POST data
$data = json_decode(file_get_contents("php://input"), true);

// Security: strip any directory paths from filename
$filename = basename($data['filename']);
$filedata = $data['filedata'];

// Ensure "db" folder exists in the same directory as this PHP file
$folder = __DIR__ . DIRECTORY_SEPARATOR . "db";
if (!is_dir($folder)) {
    mkdir($folder, 0777, true);
}

// Save CSV file
$fullpath = $folder . DIRECTORY_SEPARATOR . $filename;
if(file_put_contents($fullpath, $filedata) !== false){
    echo "Saved " . $filename;
} else {
    http_response_code(500);
    echo "Error saving file.";
}
?>

