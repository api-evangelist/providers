---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'Command-line tool that generates .aiignore configuration files to protect secrets from AI coding tools including JetBrains AI, Cursor, GitHub Copilot, Claude Code, Codeium, and Windsurf with a single '
  name: AIIgnore CLI
  slug: aiignore-cli
artifact_total: 40
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aiignore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aiignore-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yjcho9317/aiignore-cli
- group: start
  title: ''
  type: Portal
  url: https://www.jetbrains.com/ai/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/topics/aiignore
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cursor.com/context/rules
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com/en/claude-code/
created: '2025-01-01'
description: The .aiignore file is a configuration specification that tells AI coding agents and LLM-powered developer tools which files, directories, and content should not be read, processed, or modified. Modeled after .gitignore syntax, .aiignore files protect sensitive data, proprietary code, and personal information from being exposed to AI models during development workflows. Supported by JetBrains AI Assistant, Cursor, GitHub Copilot, Claude Code, Gemini Code Assist, and other AI coding tools.
examples:
- key_count: 4
  name: Aiignore Ai Ignore Config Example
  slug: aiignore-ai-ignore-config-example
- key_count: 4
  name: Aiignore Ai Ignore Rule Example
  slug: aiignore-ai-ignore-rule-example
- key_count: 5
  name: Aiignore Ai Tool Compatibility Example
  slug: aiignore-ai-tool-compatibility-example
- key_count: 3
  name: Aiignore Exclusion Pattern Example
  slug: aiignore-exclusion-pattern-example
features:
- description: Uses familiar glob pattern syntax from .gitignore so developers can immediately define exclusion rules.
  name: .gitignore-Compatible Syntax
- description: Prevents AI models from reading .env files, credential files, API keys, private keys, and other sensitive data.
  name: Secrets Protection
- description: Single .aiignore file works across JetBrains AI, Cursor, GitHub Copilot, Claude Code, Codeium, and Windsurf.
  name: Multi-Tool Support
- description: Exclude entire directories from AI context with simple pattern rules (e.g., vendor/, node_modules/).
  name: Directory-Level Exclusion
- description: Match files by extension, name, or path pattern to control AI model access granularly.
  name: File Pattern Matching
- description: Single file in project root applies rules across the entire project tree.
  name: Project-Root Placement
- description: Prevent proprietary algorithms, business logic, or licensed code from being sent to external AI APIs.
  name: Proprietary Code Protection
- description: aiignore-cli generates boilerplate .aiignore files with one command, covering common secrets patterns automatically.
  name: CLI Generation Tool
finops:
- name: Aiignore Finops
  service_category: API
  slug: aiignore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aiignore.png
integrations:
- description: JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.) AI Assistant respects .aiignore in project root.
  name: JetBrains AI Assistant
- description: Cursor IDE supports .cursorignore (similar concept) for controlling AI context access.
  name: Cursor AI Editor
- description: GitHub Copilot supports content exclusion via repository settings and .copilotignore patterns.
  name: GitHub Copilot
- description: Anthropic Claude Code CLI supports .claudeignore file for excluding files from AI context.
  name: Claude Code
- description: Codeium AI coding assistant with configurable file exclusion patterns.
  name: Codeium
- description: Codeium Windsurf AI editor with .windsurfignore support for context control.
  name: Windsurf
- description: Google Gemini Code Assist with project-level context exclusion configuration.
  name: Gemini Code Assist
json_schemas:
- name: AIIgnoreConfig
  property_count: 4
  slug: aiignore-ai-ignore-config
- name: AIIgnoreRule
  property_count: 4
  slug: aiignore-ai-ignore-rule
- name: AIToolCompatibility
  property_count: 5
  slug: aiignore-ai-tool-compatibility
- name: ExclusionPattern
  property_count: 3
  slug: aiignore-exclusion-pattern
json_structures:
- name: Aiignore Ai Ignore Config Structure
  property_count: 4
  slug: aiignore-ai-ignore-config-structure
- name: Aiignore Ai Ignore Rule Structure
  property_count: 4
  slug: aiignore-ai-ignore-rule-structure
- name: Aiignore Ai Tool Compatibility Structure
  property_count: 5
  slug: aiignore-ai-tool-compatibility-structure
- name: Aiignore Exclusion Pattern Structure
  property_count: 3
  slug: aiignore-exclusion-pattern-structure
jsonld:
- class_count: 4
  name: Aiignore Context
  property_count: 12
  slug: aiignore-context
layout: provider
modified: '2026-04-19'
name: .AIIgnore
nav: Providers
network: true
overview: '.AIIgnore publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Configuration, Developer Workflow, Security, and Privacy.


  The .AIIgnore catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  .AIIgnore''s developer surface includes developer portal, documentation, and 5 more developer resources.'
plans:
- name: Aiignore Plans Pricing
  plan_count: 3
  slug: aiignore-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Aiignore Rate Limits
  slug: aiignore-rate-limits
rules:
- name: .AIIgnore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aiignore-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 12.9
    developer_ergonomics: 17.4
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aiignore/refs/heads/main/screenshots/aiignore-2026-06-20T170859.png
security:
- kind: domain-security
  name: Aiignore Domain Security
  slug: aiignore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aiignore Vulnerability Disclosure
  slug: aiignore-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aiignore
tags:
- AI Agents
- Configuration
- Developer Workflow
- Security
- Privacy
- Developer Tools
- LLM
- Secrets Management
use_cases:
- description: Exclude .env and config files containing API keys, tokens, and credentials from AI coding tool context.
  name: API Key Protection
- description: Protect trade secrets and proprietary algorithms from being processed by AI models hosted on third-party infrastructure.
  name: Proprietary Algorithm Protection
- description: Ensure regulated data (PII, healthcare records, financial data) is not sent to external AI APIs.
  name: Compliance and Data Privacy
- description: Exclude large binary files, build artifacts, and generated files that would waste AI context window.
  name: Large File Exclusion
- description: Prevent licensed third-party code and vendor directories from being included in AI context.
  name: Third-Party Code Exclusion
website: https://www.jetbrains.com/ai/
---
