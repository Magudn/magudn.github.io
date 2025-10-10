<?php
// save_eval.php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $participant_id = $_POST['participant_id'];
    $profileID = $_POST['profileID'];
    $evaluation = $_POST['evaluation'];

    $folder = 'eval_db';
    if (!file_exists($folder)) mkdir($folder, 0777, true);

    $file = "$folder/$participant_id.csv";

    // If file doesn't exist, add header
    if (!file_exists($file)) {
        file_put_contents($file, "profileID,evaluation\n", FILE_APPEND);
    }

    // Append the evaluation
    file_put_contents($file, "$profileID,$evaluation\n", FILE_APPEND);

    echo "success";
}
?>
