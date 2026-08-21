# Codex Skills Agent Guidance

這個目錄提供 Smile2307 的 Codex 工作規範。執行任務時，優先採用與需求最相關的 Skill，而不是全部載入。

## 優先順序

1. `create-plan`
2. `engineering-workflow`
3. `embedded-python`（涉及硬體、MicroPython 或 Raspberry Pi 時）
4. `github-ci` / `github-pr-review`（涉及 GitHub 時）
5. `repo-search`（大型 repository 或搜尋困難時）
6. `frontend` / `research` / `security`（依需求啟用）

## 使用者專案偏好

- 程式語言：Python / MicroPython。
- 嵌入式平台：Raspberry Pi 4、Pico W / RP2040、ESP32、ESP8266、ESP01S。
- 常見介面：GPIO、I2C、SPI、UART、ADC、PWM。
- 常見服務：MQTT、PostgreSQL、Node-RED、Streamlit。
- 回覆程式碼問題時，使用繁體中文說明，並清楚列出硬體接線與測試步驟（若適用）。

## 不可猜測

如果硬體型號、Pin、bus、address、firmware 或 library API 未知，先檢查 repository 或官方文件；無法確認時明確說明，不要自行假設。

## 最小變更

優先修改完成任務所需的最小檔案集合。不要順手重構無關程式。
