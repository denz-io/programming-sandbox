<?PHP
  $token = "The quick brown fox jumps over the lazy dog.";
  $myKey = "thisisonlyme";
  $enc_key = openssl_digest($myKey, 'SHA256', TRUE);
  $cipher_method = 'aes-128-ctr';
  $enc_iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length($cipher_method));
  $crypted_token = openssl_encrypt($token, $cipher_method, $enc_key, 0, $enc_iv) . "::" . bin2hex($enc_iv);
  echo "\n";
  echo $crypted_token;
  list($crypted_token, $enc_iv) = explode("::", $crypted_token);;
  $unscrambled = openssl_decrypt($crypted_token, $cipher_method, $enc_key, 0, hex2bin($enc_iv));
  echo "\n";
  echo $unscrambled;
?>

