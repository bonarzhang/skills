#!/usr/bin/env node
/**
 * NadMail Send Email Script
 * 
 * Usage: node send.js <to> <subject> <body>
 * Example: node send.js alice@nadmail.ai "Hello" "How are you?"
 */

const fs = require('fs');
const path = require('path');

const API_BASE = 'https://api.nadmail.ai';
const CONFIG_DIR = path.join(process.env.HOME, '.nadmail');
const TOKEN_FILE = path.join(CONFIG_DIR, 'token.json');
const AUDIT_FILE = path.join(CONFIG_DIR, 'audit.log');

function logAudit(action, details = {}) {
  try {
    if (!fs.existsSync(CONFIG_DIR)) return;
    const entry = {
      timestamp: new Date().toISOString(),
      action,
      to: details.to ? `${details.to.split('@')[0].slice(0, 4)}...@${details.to.split('@')[1]}` : null,
      success: details.success ?? true,
      error: details.error,
    };
    fs.appendFileSync(AUDIT_FILE, JSON.stringify(entry) + '\n', { mode: 0o600 });
  } catch (e) {
    // Silently ignore audit errors
  }
}

function getToken() {
  // 1. Environment variable
  if (process.env.NADMAIL_TOKEN) {
    return process.env.NADMAIL_TOKEN;
  }
  
  // 2. Token file
  if (!fs.existsSync(TOKEN_FILE)) {
    console.error('❌ 尚未註冊。請先執行 register.js');
    process.exit(1);
  }
  
  const data = JSON.parse(fs.readFileSync(TOKEN_FILE, 'utf8'));
  
  // Check token age (warn if > 20 hours)
  if (data.saved_at) {
    const savedAt = new Date(data.saved_at);
    const now = new Date();
    const hoursSinceSaved = (now - savedAt) / 1000 / 60 / 60;
    
    if (hoursSinceSaved > 20) {
      console.log('⚠️ Token 可能即將過期，如遇錯誤請重新執行 register.js');
    }
  }
  
  return data.token;
}

async function main() {
  const [to, subject, ...bodyParts] = process.argv.slice(2);
  const body = bodyParts.join(' ');

  if (!to || !subject) {
    console.log('📬 NadMail - 發送郵件\n');
    console.log('用法: node send.js <收件人> <主旨> <內文>');
    console.log('範例: node send.js alice@nadmail.ai "Hello" "How are you?"');
    process.exit(1);
  }

  const token = getToken();

  console.log('📧 發送郵件中...');
  console.log(`   收件人: ${to}`);
  console.log(`   主旨: ${subject}`);

  // Try multiple endpoints (as instructed in the task)
  const endpoints = ['/api/send', '/api/mail/send'];
  let success = false;
  let lastError = null;

  for (const endpoint of endpoints) {
    try {
      const res = await fetch(`${API_BASE}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ to, subject, body: body || '' }),
      });

      const data = await res.json();

      if (data.success) {
        console.log('\n✅ 發送成功！');
        console.log(`   寄件人: ${data.from}`);
        console.log(`   郵件 ID: ${data.email_id}`);
        console.log(`   使用端點: ${endpoint}`);
        logAudit('send_email', { to, success: true });
        success = true;
        break;
      } else {
        lastError = data.error || data;
        if (endpoint === endpoints[0]) {
          console.log(`⚠️ ${endpoint} 失敗，嘗試下一個端點...`);
        }
      }
    } catch (err) {
      lastError = err.message;
      if (endpoint === endpoints[0]) {
        console.log(`⚠️ ${endpoint} 失敗，嘗試下一個端點...`);
      }
    }
  }

  if (!success) {
    console.error('\n❌ 所有發送端點都失敗:', lastError);
    logAudit('send_email', { to, success: false, error: lastError });
    process.exit(1);
  }
}

main().catch(err => {
  console.error('❌ 錯誤:', err.message);
  process.exit(1);
});