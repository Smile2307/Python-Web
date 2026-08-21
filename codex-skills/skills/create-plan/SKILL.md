# create-plan

## 目的
在修改程式碼前建立可檢查、可執行的實作計畫，避免過早編輯造成連鎖錯誤。

## 規則
1. 先閱讀專案根目錄的 `AGENTS.md`、README 與相關設定。
2. 找出真正相關的檔案、入口點、依賴與測試。
3. 明確列出：要改什麼、為什麼改、可能影響什麼、如何驗證。
4. 硬體專案必須額外列出 MCU、Pin、I2C/SPI/UART、裝置位址與電源條件。
5. 不要為了完成任務而順手重構無關程式。
6. 優先提出最小可行修改。

## Plan 格式
- Goal
- Current behavior
- Files to change
- Implementation steps
- Risks / edge cases
- Validation commands
- Expected result

## 完成條件
計畫必須讓另一位工程師可以依照步驟執行並驗證，而不需要猜測隱藏前提。
