<?php
$data = json_decode(file_get_contents("php://input"), true);
$participant_id = $data['participant_id'];
$image_data = $data['image'];

// Remove base64 prefix
$image_data = str_replace('data:image/png;base64,', '', $image_data);
$image_data = str_replace(' ', '+', $image_data);
$decoded = base64_decode($image_data);

// Ensure folder exists
$folder = __DIR__ . "/profile_pics";
if (!is_dir($folder)) {
    mkdir($folder, 0777, true);
}

// Save file
$filename = $folder . "/" . $participant_id . ".png";
file_put_contents($filename, $decoded);

echo "Saved profile picture for participant: $participant_id";
?>