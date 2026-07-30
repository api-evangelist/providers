---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Bland Ai Agentic Access
  operation_count: 4
  slug: bland-ai-agentic-access
  summary_line: 4 operations · 2 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: REST API for sending and managing AI phone calls, pathways (conversation flows), voices and voice clones, personas, tools, knowledge bases, transfer lists, and analytics. Auth is bearer token; base UR
  name: Bland AI Platform API
  slug: platform
- description: Send, list, retrieve, and stop AI phone calls.
  name: Bland AI Calls API
  slug: bland-ai-calls-api
artifact_total: 10
collections:
- collection_type: open
  name: Bland AI Platform API
  slug: open-bland-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bland-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bland-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bland-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bland-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bland-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bland-ai
- group: company
  title: ''
  type: Website
  url: https://www.bland.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bland.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/bland-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bland-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bland-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bland.ai/blog
created: '2026-05-08'
description: Bland AI is an enterprise-grade conversational voice AI platform for inbound and outbound phone agents. The Bland REST API covers calls, pathways (conversation graphs), voices and voice cloning, personas, tools, knowledge bases, dynamic data, transfer lists, and webhooks.
finops:
- name: Bland Ai Finops
  service_category: AI
  slug: bland-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bland-ai.png
layout: provider
modified: '2026-05-08'
name: Bland AI
nav: Providers
network: true
overview: 'Bland AI publishes 1 API on the [APIs.io](https://apis.io/) network: Calls API. Tagged areas include AI, Voice, Agents, Phone, and Realtime.


  Bland AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Bland Ai Plans Pricing
  plan_count: 5
  slug: bland-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 9
  name: Bland Ai Rate Limits
  slug: bland-ai-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -4.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bland-ai/refs/heads/main/screenshots/bland-ai-2026-06-20T173346.png
security:
- kind: authentication
  name: Bland Ai Authentication
  slug: bland-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bland Ai Domain Security
  slug: bland-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bland Ai Vulnerability Disclosure
  slug: bland-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bland-ai
tags:
- AI
- Voice
- Agents
- Phone
- Realtime
website: https://www.bland.ai/
---
