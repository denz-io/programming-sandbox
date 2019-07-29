<?php
 
$secretKey = "secret_key"; // secret key from your ClickBank account
 
// get JSON from raw body...
// Pull out the encrypted notification and the initialization vector for
// AES/CBC/PKCS5Padding decryption
$encrypted = 'message';

$iv = 'initialization vector';

// decrypt the body...
$decrypted = trim( openssl_decrypt( base64_decode($encrypted), 'AES-256-CBC', substr(sha1($secretKey), 0, 32), OPENSSL_RAW_DATA, base64_decode($iv)) , "\0..\32"); 
//error_log("Decrypted: $decrypted");
 
////UTF8 Encoding, remove escape back slashes, and convert the decrypted string to a JSON object...
$sanitizedData = utf8_encode(stripslashes($decrypted));
$order = json_decode($decrypted);
 
var_dump(base64_decode($encrypted));
var_dump(substr(sha1($secretKey), 0, 32));
var_dump(base64_decode($iv));
 
// Ready to rock and roll - If the decoding of the JSON string wasn't
// successful, then you can assume the notification wasn't encrypted
// with your secret key.
