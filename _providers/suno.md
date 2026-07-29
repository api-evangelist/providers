---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  human_in_the_loop: 0
  name: Suno Agentic Access
  operation_count: 3
  slug: suno-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 2
apis:
- description: Lyrics generation endpoints
  name: Suno Lyrics API
  slug: suno-lyrics-api
- description: Music generation endpoints
  name: Suno Music API
  slug: suno-music-api
artifact_total: 9
collections:
- collection_type: open
  name: Suno API (sunoapi.org)
  slug: open-suno
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/suno-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suno-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/suno-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/suno-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suno-ai
- group: company
  title: ''
  type: Website
  url: https://suno.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/suno-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/suno-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/suno-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sunoapi.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.suno.com/
created: '2026-05-08'
description: Suno is an AI music generation platform creating full songs (vocals + instrumentation) from natural language prompts. As of May 2026 Suno does NOT publish a sanctioned developer API. Public integrations are served by third-party aggregators (sunoapi.org, AIMLAPI, etc.) that wrap reverse-engineered access; some operate with formal SLAs but carry legal/operational risk and are not endorsed by Suno.
finops:
- name: Suno Finops
  service_category: AI
  slug: suno-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suno.png
layout: provider
modified: '2026-07-25'
name: Suno
nav: Providers
network: true
overview: 'Suno publishes 2 APIs on the [APIs.io](https://apis.io/) network: Lyrics API and Music API. Tagged areas include AI, Music Generation, Audio, Generative, and TTS.


  Suno''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Suno Plans Pricing
  plan_count: 2
  slug: suno-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 1
  name: Suno Rate Limits
  slug: suno-rate-limits
score:
  band: thin
  composite: 33.3
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.5
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/suno/refs/heads/main/screenshots/suno-2026-06-20T194657.png
security:
- kind: authentication
  name: Suno Authentication
  slug: suno-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Suno Domain Security
  slug: suno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: suno
tags:
- AI
- Music Generation
- Audio
- Generative
- TTS
website: https://suno.com/
---
