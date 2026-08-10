---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 35
  human_in_the_loop: 35
  name: Novelai Agentic Access
  operation_count: 52
  slug: novelai-agentic-access
  summary_line: 52 operations · 35 acting · 35 human-in-the-loop
api_count: 6
apis:
- description: NovelAI API provides programmatic access to AI image generation and text generation capabilities.
  name: NovelAI API
  slug: novelai
- description: The /ai/ API from NovelAI — 9 operation(s) for /ai/.
  name: NovelAI /ai/ API
  slug: novelai-ai-api
- description: The /ai/module/ API from NovelAI — 3 operation(s) for /ai/module/.
  name: NovelAI /ai/module/ API
  slug: novelai-ai-module-api
- description: The / API from NovelAI — 1 operation(s) for /.
  name: NovelAI / API
  slug: novelai-default-api
- description: The /user/ API from NovelAI — 28 operation(s) for /user/.
  name: NovelAI /user/ API
  slug: novelai-user-api
- description: The /user/subscription/ API from NovelAI — 2 operation(s) for /user/subscription/.
  name: NovelAI /user/subscription/ API
  slug: novelai-user-subscription-api
artifact_total: 14
collections:
- collection_type: open
  name: NovelAI Primary API
  slug: open-novelai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/novelai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/novelai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novelai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/novelai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NovelAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/novelaitechnologies
- group: company
  title: ''
  type: Website
  url: https://novelai.net/
created: '2024-07-02'
description: NovelAI is a monthly subscription service for AI-assisted image generation, storytelling, or simply a LLM powered sandbox for your imagination.
finops:
- name: Novelai Finops
  service_category: API
  slug: novelai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novelai.png
layout: provider
modified: '2026-04-28'
name: NovelAI
nav: Providers
network: true
overview: 'NovelAI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including /ai/ API, /ai/module/ API, / API, and 2 more. Tagged areas include AI, Image Generation, LLM, and Storytelling.


  NovelAI''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Novelai Plans Pricing
  plan_count: 3
  slug: novelai-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Novelai Rate Limits
  slug: novelai-rate-limits
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.6
    developer_ergonomics: 10.9
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novelai/refs/heads/main/screenshots/novelai-2026-06-20T190437.png
security:
- kind: authentication
  name: Novelai Authentication
  slug: novelai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Novelai Domain Security
  slug: novelai-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Novelai Vulnerability Disclosure
  slug: novelai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: novelai
tags:
- AI
- Image Generation
- LLM
- Storytelling
website: https://novelai.net/
---
