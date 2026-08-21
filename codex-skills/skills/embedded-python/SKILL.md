# embedded-python

## 目的
安全地處理 Python / MicroPython 與 Raspberry Pi、Pico W/RP2040、ESP32、ESP8266、ESP01S 等嵌入式專案。

## 修改前必查
- MCU / board 型號
- Python 或 MicroPython 版本與可用 API
- GPIO / Pin mapping
- I2C bus、SDA、SCL、frequency、device address
- SPI bus、SCK、MOSI、MISO、CS
- UART TX/RX、baud rate
- ADC channel、參考電壓與量測範圍
- PWM frequency / duty
- 電源電壓與邏輯電位
- 共用匯流排上的其他裝置
- 外部 library / driver 是否真的存在

## 保護規則
1. 不可在未確認的情況下更換既有 GPIO、I2C bus 或裝置位址。
2. 不可把 MicroPython API 當成 CPython API 使用。
3. 遇到 `ENODEV`、`No I2C devices found` 等錯誤，先檢查 wiring、電源、位址、bus 與時序，再修改程式。
4. 修改 driver 前先確認模組 datasheet 或專案既有 driver 的介面。
5. 對 DS18B20、SSD1306、MCP3008、ADS1115、MCP23017、MAX98357A、MQTT 等裝置，優先沿用專案已驗證的介面。
6. 不可把數位感測器錯當成 ADC 類比輸入；若架構要求經由 ADC，必須先確認硬體訊號路徑。
7. 每次修改後提供硬體接線檢查項目與最小測試程式。

## 建議診斷順序
```text
程式錯誤
 ↓
確認 board / firmware
 ↓
確認 wiring / power
 ↓
確認 bus / pin / address
 ↓
最小化測試
 ↓
確認 driver API
 ↓
再修改主程式
```

## Raspberry Pi 規則
涉及 GPIO、I2C、SPI、UART、MQTT、PostgreSQL 或 Node-RED 時，先確認服務狀態、port、權限與設定檔，再做修改。

## 完成條件
程式碼、硬體假設、測試方式三者必須一致；若無法實際連接硬體，必須明確標示哪些驗證尚未完成。
