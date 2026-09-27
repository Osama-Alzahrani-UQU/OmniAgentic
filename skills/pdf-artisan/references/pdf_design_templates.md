# PDF Design Templates (ظ‚ظˆط§ظ„ط¨ طھطµظ…ظٹظ… ظ…ظ„ظپط§طھ ط§ظ„ظ€ PDF ط§ظ„ط¬ط§ظ‡ط²ط©)

ظ‚ظˆط§ظ„ط¨ HTML/CSS ظ…ط¬ظ‡ط²ط© ظ„ظ„ط·ط¨ط§ط¹ط© ظˆط¯ط¹ظ… ظƒط§ظ…ظ„ ظ„ظ„ط؛ط© ط§ظ„ط¹ط±ط¨ظٹط© (RTL):

---

## 1. ظ‚ط§ظ„ط¨ ظپط§طھظˆط±ط© طھط¬ط§ط±ظٹط© / ط¶ط±ظٹط¨ظٹط© (Invoice Template)

```html
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="UTF-8">
  <style>
    @page { size: A4; margin: 20mm; }
    body { font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif; color: #1e293b; direction: rtl; }
    .header { display: flex; justify-content: space-between; border-bottom: 2px solid #3b82f6; padding-bottom: 15px; }
    .title { font-size: 24px; font-weight: bold; color: #1e40af; }
    .invoice-info { text-align: left; font-size: 14px; }
    table { width: 100%; border-collapse: collapse; margin-top: 25px; }
    th { background-color: #f1f5f9; color: #475569; padding: 10px; border-bottom: 1px solid #cbd5e1; text-align: right; }
    td { padding: 10px; border-bottom: 1px solid #e2e8f0; }
    .total-box { margin-top: 20px; float: left; width: 250px; background: #f8fafc; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; }
    .total-row { display: flex; justify-content: space-between; font-weight: bold; font-size: 16px; }
  </style>
</head>
<body>
  <div class="header">
    <div class="title">ظپط§طھظˆط±ط© ظ…ط¨ظٹط¹ط§طھ</div>
    <div class="invoice-info">ط±ظ‚ظ… ط§ظ„ظپط§طھظˆط±ط©: #INV-2026-001<br>ط§ظ„طھط§ط±ظٹط®: 2026-09-20</div>
  </div>
  <table>
    <thead>
      <tr>
        <th>ط§ظ„ظˆطµظپ</th>
        <th>ط§ظ„ظƒظ…ظٹط©</th>
        <th>ط§ظ„ط³ط¹ط±</th>
        <th>ط§ظ„ط¥ط¬ظ…ط§ظ„ظٹ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ط®ط¯ظ…ط© طھط·ظˆظٹط± ظˆطھطµظ…ظٹظ… ط§ظ„ظˆط§ط¬ظ‡ط§طھ</td>
        <td>1</td>
        <td>1500 ط±.ط³</td>
        <td>1500 ط±.ط³</td>
      </tr>
    </tbody>
  </table>
  <div class="total-box">
    <div class="total-row">
      <span>ط§ظ„ظ…ط¬ظ…ظˆط¹ ط§ظ„ظƒظ„ظٹ:</span>
      <span>1500 ط±.ط³</span>
    </div>
  </div>
</body>
</html>
```

---

## 2. ظ‚ظˆط§ط¹ط¯ CSS ط§ظ„ط°ظ‡ط¨ظٹط© ظ„ط·ط¨ط§ط¹ط© PDF ظ…ظ…طھط§ط²ط©
- `page-break-inside: avoid;` (ط¶ط¹ظ‡ط§ ط¹ظ„ظ‰ ط§ظ„ط¬ط¯ط§ظˆظ„ ظˆط§ظ„ط¨ط·ط§ظ‚ط§طھ ظ„ظ…ظ†ط¹ ط§ظ†ظ‚ط³ط§ظ…ظ‡ط§ ط¨ظٹظ† طµظپط­طھظٹظ†).
- `@page { size: A4; margin: 15mm; }` ظ„ط¶ط¨ط· ط£ط¨ط¹ط§ط¯ ط§ظ„طµظپط­ط© ظˆظ‡ظˆط§ظ…ط´ظ‡ط§.
- `direction: rtl; text-align: right;` ظ„ط¶ظ…ط§ظ† ظ…ط­ط§ط°ط§ط© ظƒظ„ ط§ظ„ط¹ظ†ط§طµط± ط§ظ„ط¹ط±ط¨ظٹط© ط¨ط´ظƒظ„ ط·ط¨ظٹط¹ظٹ.
