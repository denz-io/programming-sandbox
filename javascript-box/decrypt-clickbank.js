const CryptoJS = require("crypto-js");

const decryptIpn = (secretkey, secretParams) => {

    let encrypted = CryptoJS.enc.Base64.parse(decodeURIComponent(secretParams.notification));
    let ive = CryptoJS.enc.Base64.parse(decodeURIComponent(secretParams.iv));

    let key = CryptoJS.enc.Utf8.parse(CryptoJS.SHA1(secretkey).toString().substring(0, 32));

    let decrypted = CryptoJS.AES.decrypt(
        {ciphertext: encrypted},
        key, 
        { 
            iv: ive,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }
    );

    return decrypted.toString(CryptoJS.enc.Utf8);

}

module.exports = { decryptIpn }; 
