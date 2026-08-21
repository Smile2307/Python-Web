# security

## 目的
在 Coding Agent 修改程式時建立基本安全檢查。

## 檢查項目
- secrets、API keys、tokens、passwords 不得寫入 repository。
- 不要在 logs、README、測試資料中暴露敏感資訊。
- 網路服務確認 authentication、authorization、port 與 bind address。
- MQTT、PostgreSQL、Web server 等服務避免預設公開暴露。
- 對輸入、檔案路徑、SQL、shell command 做基本 injection 檢查。
- 不為通過 CI 而關閉安全檢查。

## 嵌入式補充
確認 Wi-Fi credentials、MQTT credentials 與裝置 API keys 不進入版本控制；必要時使用環境變數或裝置本地設定。
