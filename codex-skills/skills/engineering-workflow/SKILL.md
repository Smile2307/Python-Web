# engineering-workflow

## 工作流程

```text
需求 → Plan → Inspect → Implement → Test → Review → CI/PR
```

## Inspect
先讀取專案規範、相關檔案與現有測試；不要猜測不存在的 API、檔案或硬體。

## Implement
只修改完成任務所需的最小範圍。保持既有介面與命名，除非需求明確要求重構。

## Test
優先執行現有測試；沒有測試時建立最小可驗證案例。嵌入式專案則提供可在實機執行的 smoke test。

## Review
完成後檢查 diff：
- 是否有無關修改
- 是否有秘密、token、密碼或個資
- 是否破壞既有 API
- 是否遺漏錯誤處理
- 是否更新必要文件

## GitHub
CI 失敗時先找失敗 job 與 root cause。PR Review 意見要逐項確認，不能只用機械式回覆。
