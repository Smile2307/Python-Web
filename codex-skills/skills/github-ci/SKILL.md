# github-ci

## 目的
診斷 GitHub Actions 失敗，找出 root cause 後做最小修正。

## 流程
1. 確認失敗的 workflow、job 與 commit。
2. 讀取失敗 job logs，定位第一個真正錯誤，而不是只看最後一行。
3. 區分程式錯誤、依賴錯誤、環境錯誤與 flaky failure。
4. 只修改與 CI 問題直接相關的檔案。
5. 執行本地等價測試（若可行）。
6. 檢查 diff，再交由 CI 驗證。

## 禁止
- 不因 CI 失敗就大規模升級所有依賴。
- 不刪除測試來讓 CI 通過。
- 不隱藏真正錯誤。
- 不修改 secrets。
