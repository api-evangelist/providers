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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/character-ai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/character-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/character-ai
- group: company
  title: ''
  type: Website
  url: https://character.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://book.character.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/character-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/character-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/character-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.character.ai/feed
created: '2026-05-08'
description: Character.AI is a consumer conversational-AI platform that lets users create and chat with AI personas (Characters) via web and mobile apps. Character.AI does not publish a public developer API; product surfaces are accessed through the consumer apps. Community-maintained reverse-engineered clients exist but are unofficial and unsupported.
finops:
- name: Character Ai Finops
  service_category: AI and Machine Learning
  slug: character-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/character-ai.png
layout: provider
modified: '2026-07-25'
name: Character.AI
nav: Providers
network: true
overview: 'Character.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, LLM, Chatbots, Personas, and Generative AI.


  Character.AI''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Character Ai Plans Pricing
  plan_count: 3
  slug: character-ai-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 3
  name: Character Ai Rate Limits
  slug: character-ai-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 19.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/character-ai/refs/heads/main/screenshots/character-ai-2026-06-20T174219.png
security:
- kind: domain-security
  name: Character Ai Domain Security
  slug: character-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: character-ai
tags:
- AI
- LLM
- Chatbots
- Personas
- Generative AI
- Consumer
website: https://character.ai/
---
