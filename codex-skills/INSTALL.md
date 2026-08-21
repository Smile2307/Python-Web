# 安裝與同步

這套 Skills 採「Repository 原始碼 + 本機同步」模式。Repository 是唯一來源，`install.py` 負責把選定的 `SKILL.md` 同步到本機 Skills 目錄。

## 1. 驗證 Skills

```bash
python codex-skills/validate.py
```

## 2. 先做 Dry Run

```bash
python codex-skills/install.py --target ~/.agents/skills --core-only --dry-run
```

## 3. 安裝核心 Skills

```bash
python codex-skills/install.py --target ~/.agents/skills --core-only
```

## 4. 安裝全部 Skills

```bash
python codex-skills/install.py --target ~/.agents/skills
```

> `~/.agents/skills` 是本專案目前建議的本機同步目標；實際 Codex 版本若使用不同的 Skills 目錄，請以該版本的官方文件為準。

## 核心 Skills

- create-plan
- engineering-workflow
- embedded-python
- github-ci
- github-pr-review
- repo-search

## 選用 Skills

- frontend
- research
- security

## 驗證安裝

安裝後，在 Codex 專案中執行：

> 檢查目前專案，先不要修改任何檔案。請分析專案結構、找出與任務相關的檔案，並提出完整實作計畫。

確認它先分析與規劃，再開始修改。

## 安全原則

- 不把 GitHub token、API key、password 或 Wi-Fi/MQTT credentials 放入 Skills。
- 不用安裝腳本覆寫 repository 來源檔案。
- 第三方 Skill 若要加入，先檢查來源、授權與內容，再以本專案規範整合。
