# github-pr-review

## 目的
系統性處理 PR review 意見，保留 reviewer 意圖並避免無關重構。

## 流程
1. 讀取所有 review threads 與 top-level comments。
2. 將意見分類為 bug、design、test、docs、style 或 question。
3. 對每一項判斷是否有效及其影響範圍。
4. 修改前建立最小方案。
5. 修改後執行相關測試。
6. 檢查 diff 與 CI。
7. 對每個已處理意見提供具體結果；需要人決定的事項明確標示。

## 原則
不要為了消除 comment 而改壞既有行為，也不要聲稱已驗證實際上未執行的測試。
