const crypto = require('crypto');

// Şifreleme ve deşifreleme için gerekli anahtar ve iv
const algorithm = 'aes-256-cbc';
const key = crypto.randomBytes(32); // 256 bit anahtar
const iv = crypto.randomBytes(16);   // 128 bit IV

// Şifreleme fonksiyonu
function encrypt(text) {
    let cipher = crypto.createCipheriv(algorithm, Buffer.from(key), iv);
    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    return { iv: iv.toString('hex'), encryptedData: encrypted };
}

// Deşifreleme fonksiyonu
function decrypt(encryptedData, iv) {
    let decipher = crypto.createDecipheriv(algorithm, Buffer.from(key), Buffer.from(iv, 'hex'));
    let decrypted = decipher.update(encryptedData, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return decrypted;
}

// Kullanıcıdan metin alma ve şifreleme
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Şifrelenecek metni girin: ', (text) => {
    const encrypted = encrypt(text);
    console.log(`Şifreli veri: ${encrypted.encryptedData}`);
    console.log(`IV: ${encrypted.iv}`);
    
    const decrypted = decrypt(encrypted.encryptedData, encrypted.iv);
    console.log(`Deşifreli veri: ${decrypted}`);
    
    readline.close();
});

