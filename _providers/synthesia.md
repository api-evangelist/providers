---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Synthesia Agentic Access
  operation_count: 27
  slug: synthesia-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 7
apis:
- description: The Assets API from Synthesia — 3 operation(s) for assets.
  name: Synthesia Assets API
  slug: synthesia-assets-api
- description: The AuditLogs API from Synthesia — 3 operation(s) for auditlogs.
  name: Synthesia AuditLogs API
  slug: synthesia-auditlogs-api
- description: The Dubbing API from Synthesia — 3 operation(s) for dubbing.
  name: Synthesia Dubbing API
  slug: synthesia-dubbing-api
- description: The Templates API from Synthesia — 3 operation(s) for templates.
  name: Synthesia Templates API
  slug: synthesia-templates-api
- description: The Translations API from Synthesia — 4 operation(s) for translations.
  name: Synthesia Translations API
  slug: synthesia-translations-api
- description: The Videos API from Synthesia — 5 operation(s) for videos.
  name: Synthesia Videos API
  slug: synthesia-videos-api
- description: The Webhooks API from Synthesia — 2 operation(s) for webhooks.
  name: Synthesia Webhooks API
  slug: synthesia-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Synthesia Assets API
  slug: open-synthesia-assets-api
- collection_type: open
  name: Synthesia Assets AuditLogs API
  slug: open-synthesia-auditlogs-api
- collection_type: open
  name: Synthesia Assets Dubbing API
  slug: open-synthesia-dubbing-api
- collection_type: open
  name: Synthesia Assets Templates API
  slug: open-synthesia-templates-api
- collection_type: open
  name: Synthesia Assets Translations API
  slug: open-synthesia-translations-api
- collection_type: open
  name: Synthesia Assets Videos API
  slug: open-synthesia-videos-api
- collection_type: open
  name: Synthesia Assets Webhooks API
  slug: open-synthesia-webhooks-api
- collection_type: open
  name: Synthesia API
  slug: open-synthesia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synthesia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthesia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synthesia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.synthesia.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synthesia.io
- group: company
  title: ''
  type: Blog
  url: https://www.synthesia.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synthesia.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synthesia.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synthesia.io/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/synthesiaIO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synthesia-technologies
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.synthesia.io/changelog
created: '2026-05-23'
description: Synthesia is the leading enterprise AI video platform for creating studio-quality videos from text using lifelike AI avatars and voices. Customers use Synthesia to produce training, learning and development, customer onboarding, marketing, and internal communications videos in 140+ languages without cameras, actors, or studios. The company sells tiered SaaS plans (Basic, Starter, Creator, Enterprise) with API access starting at the Creator tier and full programmatic capabilities for enterprise customers. The Synthesia API lets teams generate, translate, and dub videos at scale and embed video generation into their own applications.
finops:
- name: Synthesia Finops
  service_category: API
  slug: synthesia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synthesia.png
layout: provider
modified: '2026-05-23'
name: Synthesia
nav: Providers
network: true
overview: 'Synthesia publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, AuditLogs API, Dubbing API, and 4 more. Tagged areas include Artificial Intelligence, Generative AI, Video, Avatars, and Text-to-Video.


  Synthesia''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 7 more developer resources.'
plans:
- name: Synthesia Plans Pricing
  plan_count: 1
  slug: synthesia-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Synthesia Rate Limits
  slug: synthesia-rate-limits
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 13.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synthesia/refs/heads/main/screenshots/synthesia-2026-06-20T194840.png
security:
- kind: authentication
  name: Synthesia Authentication
  slug: synthesia-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Synthesia Domain Security
  slug: synthesia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synthesia
tags:
- Artificial Intelligence
- Generative AI
- Video
- Avatars
- Text-to-Video
- Voices
- Dubbing
- Translation
- Templates
- Enterprise
- Learning
website: https://www.synthesia.io
---
