# Silent Installation Flags Reference

ظ…ط±ط¬ط¹ ط±ط§ظٹط§طھ ط§ظ„طھط«ط¨ظٹطھ ط§ظ„طµط§ظ…طھ ط؛ظٹط± ط§ظ„طھظپط§ط¹ظ„ظٹ ط¹ظ„ظ‰ ظ†ط¸ط§ظ… Windows:

| ظ†ظˆط¹ ط§ظ„ظ€ Installer | ط§ظ„ط±ط§ظٹط§طھ ط§ظ„طµط§ظ…طھط© (Silent Flags) | ظ…ظ„ط§ط­ط¸ط§طھ |
| :--- | :--- | :--- |
| **Windows Package Manager** | `winget install <id> --silent --accept-package-agreements --accept-source-agreements` | ط§ظ„ط®ظٹط§ط± ط§ظ„ط£ظپط¶ظ„ ظˆط§ظ„ط£ظƒط«ط± ط£ظ…ط§ظ†ط§ظ‹ ظˆظ…ظˆط«ظˆظ‚ظٹط© |
| **Microsoft Installer (MSI)** | `msiexec.exe /i package.msi /qn /norestart` | `/qn` طھط¹ظ†ظٹ No UIطŒ `/norestart` طھظ…ظ†ط¹ ط¥ط¹ط§ط¯ط© ط§ظ„طھط´ط؛ظٹظ„ ط§ظ„ظپط¬ط§ط¦ظٹط© |
| **Inno Setup** | `installer.exe /VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP-` | ظˆط§ط³ط¹ ط§ظ„ط§ظ†طھط´ط§ط± ظپظٹ ط¨ط±ط§ظ…ط¬ ط§ظ„ظˆظٹظ†ط¯ظˆط² |
| **NSIS (Nullsoft)** | `installer.exe /S` | ط§ظ„ط­ط±ظپ `/S` ط­ط³ط§ط³ ظ„ط­ط§ظ„ط© ط§ظ„ط£ط­ط±ظپ (ظƒط¨ظٹط±) |
| **InstallShield** | `installer.exe /s /v"/qn"` | ظٹظ…ط±ط± `/qn` ط¥ظ„ظ‰ ظ…ط­ط±ظƒ MSI ط§ظ„ط¯ط§ط®ظ„ظٹ |
| **Advanced Installer** | `installer.exe /exenoui /qn` | طھط´ط؛ظٹظ„ طµط§ظ…طھ ظƒط§ظ…ظ„ |
