---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Open Webui Agentic Access
  operation_count: 5
  slug: open-webui-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: 'REST API exposed by a self-hosted Open WebUI instance. Endpoints cover chat completions (proxying upstream backends like Ollama or OpenAI-compatible servers), models, prompts, knowledge bases, files, '
  name: Open WebUI API
  slug: platform
- baseURL: http://localhost:3000/api/v1
  baseurl_source: declared
  description: The Anthropic API from Open WebUI — 1 operation(s) for anthropic.
  name: Open WebUI Anthropic API
  slug: open-webui-anthropic-api
- baseURL: http://localhost:3000/api/v1
  baseurl_source: declared
  description: The Ollama API from Open WebUI — 3 operation(s) for ollama.
  name: Open WebUI Ollama API
  slug: open-webui-ollama-api
- baseURL: http://localhost:3000/api/v1
  baseurl_source: declared
  description: The Chat Completions API from Open WebUI — 1 operation(s) for chat completions.
  name: Open WebUI Chat Completions API
  slug: open-webui-chat-completions-api
artifact_total: 15
collections:
- collection_type: open
  name: Open WebUI Anthropic API
  slug: open-open-webui-anthropic-api
- collection_type: open
  name: Open WebUI Anthropic Chat API
  slug: open-open-webui-chat-api
- collection_type: open
  name: Open WebUI Anthropic Ollama API
  slug: open-open-webui-ollama-api
- collection_type: open
  name: Open WebUI API
  slug: open-open-webui
common:
- group: agent
  href: https://artifacts.apis.io/open-webui/agentic-access/open-webui-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/open-webui-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/open-webui/security/open-webui-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-webui-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/open-webui/authentication/open-webui-authentication.yml
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
  href: https://artifacts.apis.io/open-webui/plans/open-webui-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/open-webui-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/open-webui/rate-limits/open-webui-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/open-webui-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/open-webui/finops/open-webui-finops.yml
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
- has_sources: true
  method: generated
  name: Open Webui Finops
  primary_unit: ''
  service_category: LLM Tooling
  slug: open-webui-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-webui.png
layout: provider
modified: '2026-05-08'
name: Open WebUI
nav: Providers
network: true
overview: 'Open WebUI publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Anthropic API, Ollama API, Chat Completions API, and 1 more. Tagged areas include LLM, Open Source, Self-Hosted, Ollama, and Chat UI.


  The Open WebUI catalog on APIs.io includes 1 Spectral governance ruleset.


  Open WebUI''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Open Webui Plans Pricing
  plan_count: 1
  slug: open-webui-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Open Webui Rate Limits
  slug: open-webui-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Open WebUI API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: open-webui-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 42.9
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/open-webui/open-webui-2026-06-20T190859.png
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
