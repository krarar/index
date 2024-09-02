  GNU nano 8.0           server.js
const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 3000;

// تقديم ملفات من مجلد 'public'
app.use(express.static('public'));

// مسار لجلب الأجهزة المتصلة بالشبكة مع معلوماتها
app.get('/scan', async (req, res) => {
    exec('arp-scan -l', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing arp-scan: ${>
            return res.status(500).json({ error: 'Error>
        }
        if (stderr) {
            console.error(`arp-scan stderr: ${stderr}`);
            return res.status(500).json({ error: 'arp-s>
        }

        const devices = [];
        const lines = stdout.split('\n');

        lines.forEach(line => {
            const match = line.match(/^(\d{1,3}\.\d{1,3>
            if (match) {
                devices.push({
                    ip: match[1],
                    mac: match[2],