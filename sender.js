const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const fs = require('fs');

const client = new Client({
    authStrategy: new LocalAuth(), // QR'yi bir kere okutursun
    puppeteer: {
        headless: true,
        args: ['--no-sandbox']
    }
});

// QR kod
client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
    console.log('QR kodu okut');
});

// Giriş başarılı
client.on('ready', async () => {
    console.log('WhatsApp bağlantısı hazır');

    // numaralar.txt oku
    const numbers = fs.readFileSync('numaralar.txt', 'utf-8')
        .split('\n')
        .map(n => n.trim())
        .filter(n => n.length > 0);

    console.log(`Toplam ${numbers.length} numara bulundu`);

    for (const number of numbers) {
        const chatId = number + '@c.us';

        try {
            const isRegistered = await client.isRegisteredUser(chatId);

            if (isRegistered) {
                await client.sendMessage(chatId, 'Merhaba, bu bir otomasyon mesajıdır.');
                console.log(`Mesaj gönderildi: ${number}`);
            } else {
                console.log(`WhatsApp yok: ${number}`);
            }

            // BAN yememek için gecikme
            await delay(3000);

        } catch (err) {
            console.log(`Hata (${number}):`, err.message);
        }
    }

    console.log('Tüm mesajlar gönderildi');
});

// delay fonksiyonu
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

client.initialize();
