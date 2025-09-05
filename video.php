<?php
// Set proper MIME type for video files
$file = $_GET['file'];
$path = '/home/courses/hcmi/media/' . $file;

if (file_exists($path)) {
    $extension = pathinfo($file, PATHINFO_EXTENSION);
    
    switch($extension) {
        case 'mp4':
            header('Content-Type: video/mp4');
            break;
        case 'webm':
            header('Content-Type: video/webm');
            break;
        case 'ogv':
            header('Content-Type: video/ogg');
            break;
        default:
            header('Content-Type: application/octet-stream');
    }
    
    header('Content-Length: ' . filesize($path));
    header('Accept-Ranges: bytes');
    
    readfile($path);
} else {
    http_response_code(404);
    echo 'File not found';
}
?>
