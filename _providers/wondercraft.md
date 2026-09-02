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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Wondercraft Agentic Access
  operation_count: 7
  slug: wondercraft-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: The Account API from Wondercraft — 1 operation(s) for account.
  name: Wondercraft Account API
  slug: wondercraft-account-api
- description: The Audio Generation API from Wondercraft — 2 operation(s) for audio generation.
  name: Wondercraft Audio Generation API
  slug: wondercraft-audio-generation-api
- description: The Convo Mode API from Wondercraft — 2 operation(s) for convo mode.
  name: Wondercraft Convo Mode API
  slug: wondercraft-convo-mode-api
- description: The Jobs API from Wondercraft — 2 operation(s) for jobs.
  name: Wondercraft Jobs API
  slug: wondercraft-jobs-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wondercraft Public Account API
  slug: open-wondercraft-account-api
- collection_type: open
  name: Wondercraft Public Account Audio Generation API
  slug: open-wondercraft-audio-generation-api
- collection_type: open
  name: Wondercraft Public Account Convo Mode API
  slug: open-wondercraft-convo-mode-api
- collection_type: open
  name: Wondercraft Public Account Jobs API
  slug: open-wondercraft-jobs-api
- collection_type: open
  name: Wondercraft Public API
  slug: open-wondercraft
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wondercraft-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wondercraft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wondercraft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wondercraft-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://wondercraft.ai/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wondercraftai
- group: company
  title: ''
  type: Website
  url: https://www.wondercraft.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wondercraft.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/wondercraft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wondercraft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wondercraft-finops.yml
created: '2026-06-21'
description: Wondercraft is an AI audio creation platform for producing podcasts, audio ads, meditations, and audiobooks. Its public REST API generates audio content from an AI-written or user-supplied script, supports a two-host Convo Mode, lets callers attach platform voices and background music by ID, and exposes asynchronous jobs that are polled for status and a finished MP3 download URL.
finops:
- name: Wondercraft Finops
  service_category: AI and Machine Learning
  slug: wondercraft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wondercraft.png
layout: provider
modified: '2026-06-21'
name: Wondercraft
nav: Providers
network: true
overview: 'Wondercraft publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Audio Generation API, Convo Mode API, and 1 more. Tagged areas include Artificial Intelligence, Audio, Podcast, Text-to-Speech, and Generative Audio.


  Wondercraft''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Wondercraft Plans Pricing
  plan_count: 4
  slug: wondercraft-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Wondercraft Rate Limits
  slug: wondercraft-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Wondercraft Authentication
  slug: wondercraft-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wondercraft Domain Security
  slug: wondercraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wondercraft
tags:
- Artificial Intelligence
- Audio
- Podcast
- Text-to-Speech
- Generative Audio
website: https://www.wondercraft.ai
---
