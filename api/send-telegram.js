const fetch = require('node-fetch');

module.exports = async (req, res) => {
    const botToken = process.env.BOT_TOKEN; // Set in Vercel dashboard
    const chatId = process.env.CHAT_ID; // Set in Vercel dashboard
    const { message } = req.body;

    try {
        await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ chat_id: chatId, text: message })
        });
        res.status(200).json({ status: 'Message sent' });
    } catch (error) {
        res.status(500).json({ error: 'Failed to send message' });
    }
};
