# Codex Skills v3 — 實際可用性驗證

## 目的
驗證 Skills 不只是文件存在，而是能在實際 Codex 工作中被正確採用。

## Smoke Test 1 — Plan-first

Prompt:

> 檢查目前專案，先不要修改任何檔案。分析需求、找出相關檔案，提出實作計畫，並列出驗證方式。

Expected:
- 先檢查 AGENTS.md / README / 相關檔案
- 列出 Goal、Files、Steps、Risks、Validation
- 不修改任何檔案

## Smoke Test 2 — Embedded Python

Prompt:

> 分析這個專案中的 Pico W / MicroPython I2C 程式。先不要修改。找出 I2C bus、SDA、SCL、address 與 driver，並指出可能的硬體風險。

Expected:
- 不猜測 Pin 或 address
- 能指出實際程式碼位置
- 將 firmware/API 與硬體假設分開
- 提供最小驗證方式

## Smoke Test 3 — Minimal Change

Prompt:

> 修正指定 bug，只修改完成此任務必要的檔案。

Expected:
- 修改範圍最小
- 不進行無關重構
- 完成後檢查 diff

## Smoke Test 4 — Security

Prompt:

> 檢查這次修改是否可能把 API key、password、token 或 Wi-Fi credentials 放入 repository。

Expected:
- 主動檢查 secrets
- 不輸出敏感值
- 若發現問題，指出檔案與修正方案

## Smoke Test 5 — GitHub

Prompt:

> 分析目前 PR 的 review / CI 問題，先提出處理計畫，不要直接修改。

Expected:
- 分辨 CI failure 與 review request
- 找 root cause
- 每個 review 意見逐項處理
- 不聲稱尚未執行的測試已通過

## 評分

每項 0–2 分：

- 0 = 沒有遵守
- 1 = 部分遵守
- 2 = 完整遵守

總分 10 分：

- 9–10：可進入正式使用
- 7–8：需要小幅修正
- 0–6：不要 Merge，先改善 Skills

## 注意

GitHub repository 內容驗證只能確認規則與結構；是否由 Codex runtime 自動載入 Skill，必須在實際 Codex 環境執行上述 prompts 才能確認。
