---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Open Webui Agentic Access
  operation_count: 5
  slug: open-webui-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 4
apis:
- description: 'REST API exposed by a self-hosted Open WebUI instance. Endpoints cover chat completions (proxying upstream backends like Ollama or OpenAI-compatible servers), models, prompts, knowledge bases, files, '
  name: Open WebUI API
  slug: platform
- description: The Anthropic API from Open WebUI — 1 operation(s) for anthropic.
  name: Open WebUI Anthropic API
  slug: open-webui-anthropic-api
- description: The Chat API from Open WebUI — 1 operation(s) for chat.
  name: Open WebUI Chat API
  slug: open-webui-chat-api
- description: The Ollama API from Open WebUI — 3 operation(s) for ollama.
  name: Open WebUI Ollama API
  slug: open-webui-ollama-api
artifact_total: 11
collections:
- collection_type: open
  name: Open WebUI API
  slug: open-open-webui
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-webui-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-webui-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-webui-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-webui
- group: company
  title: ''
  type: Website
  url: https://openwebui.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.openwebui.com/
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/open-webui/open-webui
- group: commercial
  title: ''
  type: Plans
  url: plans/open-webui-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-webui-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-webui-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://openwebui.com/blog
created: '2026-05-08'
description: Open WebUI is a self-hosted, open-source web UI for LLMs (notably Ollama and OpenAI-compatible backends). It exposes a REST API for chats, models, prompts, knowledge (RAG), users, and tools. Distributed under a modified BSD-3-Clause license; primarily run via Docker or pip on your own infrastructure.
finops:
- name: Open Webui Finops
  service_category: LLM Tooling
  slug: open-webui-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-webui.png
layout: provider
modified: '2026-05-08'
name: Open WebUI
nav: Providers
network: true
overview: 'Open WebUI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Anthropic API, Chat API, and Ollama API. Tagged areas include LLM, Open Source, Self-Hosted, Ollama, and Chat UI.


  Open WebUI''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Open Webui Plans Pricing
  plan_count: 1
  slug: open-webui-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Open Webui Rate Limits
  slug: open-webui-rate-limits
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-webui/refs/heads/main/screenshots/open-webui-2026-06-20T190859.png
security:
- kind: authentication
  name: Open Webui Authentication
  slug: open-webui-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Open Webui Domain Security
  slug: open-webui-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-webui
tags:
- LLM
- Open Source
- Self-Hosted
- Ollama
- Chat UI
- RAG
website: https://openwebui.com/
---
