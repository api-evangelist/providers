---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 5
apis:
- description: Open-source autonomous coding agent for VS Code. Reads/writes files, runs commands, browses the web, calls MCP tools, and connects to LLM providers (Anthropic, OpenAI, Google, OpenRouter, Ollama, etc.
  name: Cline VS Code Extension
  slug: vscode
- description: Early-access JetBrains plugin offering the same agent surfaces.
  name: Cline JetBrains Plugin
  slug: jetbrains
- description: Headless terminal version of the Cline agent.
  name: Cline CLI
  slug: cli
- description: Marketplace for MCP servers/tools that extend the Cline agent.
  name: Cline MCP Marketplace
  slug: mcp-marketplace
- description: Hosted/managed Cline product with free and paid tiers plus enterprise sales.
  name: Cline Hosted (Cline.bot)
  slug: hosted
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cline-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cline-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clinebot
- group: company
  title: ''
  type: Website
  url: https://cline.bot/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cline/cline
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cline.bot/
- group: commercial
  title: ''
  type: Plans
  url: plans/cline-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cline-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cline-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cline.bot/llms.txt
created: '2026-05-08'
description: Cline (formerly Claude Dev) is an open-source autonomous coding agent. The Cline VS Code extension has 5M+ installs; JetBrains is in early access; the Cline CLI is also available. Edits files, runs commands, uses the browser, and federates to multiple LLM providers. An MCP Marketplace extends Cline with custom tools. There is also a hosted/managed offering (Cline.bot) with free and paid tiers plus enterprise sales.
finops:
- name: Cline Finops
  service_category: AI
  slug: cline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cline.png
layout: provider
modified: '2026-05-08'
name: Cline
nav: Providers
network: true
overview: 'Cline publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Developer Tools, Agent, VS Code, and JetBrains.


  Cline''s developer surface includes GitHub presence, documentation, and 8 more developer resources.'
plans:
- name: Cline Plans Pricing
  plan_count: 1
  slug: cline-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: Cline Rate Limits
  slug: cline-rate-limits
score:
  band: emerging
  composite: 13.9
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cline/refs/heads/main/screenshots/cline-2026-06-20T174524.png
security:
- kind: domain-security
  name: Cline Domain Security
  slug: cline-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cline Vulnerability Disclosure
  slug: cline-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: cline
tags:
- AI
- Developer Tools
- Agent
- VS Code
- JetBrains
- CLI
- MCP
- Open Source
website: https://cline.bot/
---
