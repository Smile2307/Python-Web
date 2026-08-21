# 安裝與同步

## 專案內使用

將本目錄納入專案後，讓 Codex 依 `codex-skills/AGENTS.md` 與各 `skills/*/SKILL.md` 執行工作規範。

## 使用者級 Skills

若目前 Codex 版本支援使用者級 Skills，可將需要的 `SKILL.md` 複製到使用者 Skills 目錄；不要整個 repository 當成單一 Skill 載入。

## 建議

第一階段只啟用：

- create-plan
- engineering-workflow
- embedded-python
- github-ci
- github-pr-review
- repo-search

frontend、research、security 依任務需要啟用。

## 驗證

安裝後先要求 Codex：

> 分析目前專案並提出修改計畫，不要修改任何檔案。

確認它能遵守 plan-first 規則後，再進行實際修改。
