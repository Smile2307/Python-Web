# Smile2307 Codex Skills

這套 Skills 是為 Python、MicroPython、Raspberry Pi、Pico W、ESP32/ESP8266 與 GitHub 開發流程設計的 Codex 工作框架。

## 設計原則

- 先分析與規劃，再修改程式。
- 硬體相關程式修改前，先確認 MCU、Pin、匯流排與裝置位址。
- 修改後必須檢查 diff，並提供可執行的測試方式。
- GitHub CI 與 PR Review 採可追蹤、最小變更原則。
- 第三方 Skills 不直接複製；本目錄以工作流程與規則為主，避免不必要的授權與維護風險。

## Skills

| Skill | 用途 | 優先級 |
|---|---|---|
| `create-plan` | 需求分析與實作計畫 | 核心 |
| `embedded-python` | MicroPython / Raspberry Pi / ESP32 硬體開發 | 核心 |
| `github-ci` | GitHub Actions / CI 診斷原則 | 核心 |
| `github-pr-review` | PR Review 意見處理 | 核心 |
| `engineering-workflow` | Plan → Implement → Test → Review | 核心 |
| `repo-search` | 大型專案搜尋與最小上下文原則 | 建議 |
| `frontend` | Streamlit / Web UI 品質規則 | 選用 |
| `research` | 技術文件與研究資料查證 | 選用 |
| `security` | 基本安全檢查與威脅建模 | 選用 |

## 建議使用流程

```text
需求
  ↓
create-plan
  ↓
檢查專案與 AGENTS.md
  ↓
確認 Python / MicroPython / 硬體環境
  ↓
Implement
  ↓
Test
  ↓
Review diff
  ↓
GitHub CI / PR
```

## 目錄

每個 Skill 使用獨立的 `SKILL.md`。這些文件可作為 Codex 專案級工作規範，也可以再依實際 Codex 安裝方式同步到使用者的 Skills 目錄。
