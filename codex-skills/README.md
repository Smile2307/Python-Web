# Smile2307 Codex Skills v4

這套 Skills 是為 Python、MicroPython、Raspberry Pi、Pico W、ESP32/ESP8266 與 GitHub 開發流程設計的 Codex 工作框架。

## v4 架構

```text
Repository
   ↓
codex-skills/skills/*/SKILL.md
   ↓
validate.py
   ↓
install.py
   ↓
本機 Skills 目錄
   ↓
Codex
```

Repository 是唯一來源；本機安裝目錄是產物，不應手工修改後再回寫來源。

## 核心 Skills

- `create-plan` — 先分析與建立實作計畫
- `engineering-workflow` — Plan → Inspect → Implement → Test → Review
- `embedded-python` — MicroPython / Raspberry Pi / Pico W / ESP32 / ESP8266
- `github-ci` — GitHub Actions CI 診斷
- `github-pr-review` — PR Review 意見處理
- `repo-search` — 最小上下文搜尋

## 選用 Skills

- `frontend` — Streamlit / Web UI
- `research` — 官方文件與研究資料查證
- `security` — secrets、網路服務與基本安全檢查

## v4 指令

```bash
# 驗證
python codex-skills/validate.py

# 核心 Skills dry-run
python codex-skills/install.py --target ~/.agents/skills --core-only --dry-run

# 安裝核心 Skills
python codex-skills/install.py --target ~/.agents/skills --core-only

# 安裝全部 Skills
python codex-skills/install.py --target ~/.agents/skills
```

## 硬體保護

涉及 GPIO、I2C、SPI、UART、ADC、PWM、MQTT 或感測器時，Codex 必須先確認實際 board、firmware、Pin、bus、address 與 driver/API，不得猜測。

## GitHub CI

`.github/workflows/validate-codex-skills.yml` 會在 Skills 相關變更時驗證目錄結構與核心安裝 dry-run。

## 第三方內容

本專案不直接複製 Medium 文章或其他第三方 Skill 的實作內容；需要整合時，先檢查來源與授權，再依本專案工作流程重新實作。
