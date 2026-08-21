# Embedded Python Validation Examples

## Pico W / RP2040

確認 board 與 firmware 後，再確認 I2C bus、SDA/SCL 與 address。若專案使用 I2C0，沿用專案既有 Pin 定義，不自行換 bus。

## I2C 故障

```text
No I2C devices found / ENODEV
→ 電源
→ GND
→ SDA/SCL
→ bus
→ address
→ pull-up
→ driver/API
```

## 測試原則

先建立最小 smoke test，再整合回主程式。例如 I2C 裝置先只執行 scan/read identity，不要一開始啟動完整 MQTT/Web/UI 流程。
