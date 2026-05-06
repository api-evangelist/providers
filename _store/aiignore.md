---
aid: aiignore
url: https://raw.githubusercontent.com/api-evangelist/aiignore/refs/heads/main/apis.yml
name: .AIIgnore
tags:
  - AI Agents
  - Configuration
  - Developer Workflow
  - Security
  - Privacy
  - Developer Tools
  - LLM
  - Secrets Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-19'
position: Consumer
description: The .aiignore file is a configuration specification that tells AI coding agents and LLM-powered developer tools which files, directories, and content should not be read, processed, or modified. Modeled after .gitignore syntax, .aiignore files protect sensitive data, proprietary code, and personal information from being exposed to AI models during development workflows. Supported by JetBrains AI Assistant, Cursor, GitHub Copilot, Claude Code, Gemini Code Assist, and other AI coding tools.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: aiignore:aiignore-cli
    name: AIIgnore CLI
    tags:
      - CLI
      - Security
      - Developer Tools
      - TypeScript
      - Node.js
      - Secrets Management
    humanURL: https://github.com/yjcho9317/aiignore-cli
    description: Command-line tool that generates .aiignore configuration files to protect secrets from AI coding tools including JetBrains AI, Cursor, GitHub Copilot, Claude Code, Codeium, and Windsurf with a single command.
    properties:
      - url: https://github.com/yjcho9317/aiignore-cli
        type: GitHubRepository
      - url: https://www.npmjs.com/package/aiignore-cli
        type: SDK
        title: npm Package
common:
  - name: AIIgnore CLI GitHub
    url: https://github.com/yjcho9317/aiignore-cli
    type: GitHubRepository
    description: CLI tool for generating .aiignore files across multiple AI coding tools.
  - name: JetBrains AI Assistant
    url: https://www.jetbrains.com/ai/
    type: Portal
    description: JetBrains AI Assistant which respects .aiignore files in project roots.
  - name: 'GitHub Topics: aiignore'
    url: https://github.com/topics/aiignore
    type: GitHubRepository
    description: GitHub topic page collecting .aiignore-related repositories and tools.
  - name: Cursor AI Rules
    url: https://docs.cursor.com/context/rules
    type: Documentation
    description: Cursor AI editor rules documentation for context exclusion (.cursorignore).
  - name: Claude Code Ignore
    url: https://docs.anthropic.com/en/claude-code/
    type: Documentation
    description: Claude Code documentation for .claudeignore file support.
  - type: Features
    data:
      - name: .gitignore-Compatible Syntax
        description: Uses familiar glob pattern syntax from .gitignore so developers can immediately define exclusion rules.
      - name: Secrets Protection
        description: Prevents AI models from reading .env files, credential files, API keys, private keys, and other sensitive data.
      - name: Multi-Tool Support
        description: Single .aiignore file works across JetBrains AI, Cursor, GitHub Copilot, Claude Code, Codeium, and Windsurf.
      - name: Directory-Level Exclusion
        description: Exclude entire directories from AI context with simple pattern rules (e.g., vendor/, node_modules/).
      - name: File Pattern Matching
        description: Match files by extension, name, or path pattern to control AI model access granularly.
      - name: Project-Root Placement
        description: Single file in project root applies rules across the entire project tree.
      - name: Proprietary Code Protection
        description: Prevent proprietary algorithms, business logic, or licensed code from being sent to external AI APIs.
      - name: CLI Generation Tool
        description: aiignore-cli generates boilerplate .aiignore files with one command, covering common secrets patterns automatically.
  - type: UseCases
    data:
      - name: API Key Protection
        description: Exclude .env and config files containing API keys, tokens, and credentials from AI coding tool context.
      - name: Proprietary Algorithm Protection
        description: Protect trade secrets and proprietary algorithms from being processed by AI models hosted on third-party infrastructure.
      - name: Compliance and Data Privacy
        description: Ensure regulated data (PII, healthcare records, financial data) is not sent to external AI APIs.
      - name: Large File Exclusion
        description: Exclude large binary files, build artifacts, and generated files that would waste AI context window.
      - name: Third-Party Code Exclusion
        description: Prevent licensed third-party code and vendor directories from being included in AI context.
  - type: Integrations
    data:
      - name: JetBrains AI Assistant
        description: JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.) AI Assistant respects .aiignore in project root.
      - name: Cursor AI Editor
        description: Cursor IDE supports .cursorignore (similar concept) for controlling AI context access.
      - name: GitHub Copilot
        description: GitHub Copilot supports content exclusion via repository settings and .copilotignore patterns.
      - name: Claude Code
        description: Anthropic Claude Code CLI supports .claudeignore file for excluding files from AI context.
      - name: Codeium
        description: Codeium AI coding assistant with configurable file exclusion patterns.
      - name: Windsurf
        description: Codeium Windsurf AI editor with .windsurfignore support for context control.
      - name: Gemini Code Assist
        description: Google Gemini Code Assist with project-level context exclusion configuration.
---
