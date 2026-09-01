---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://unamo.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unamo-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Unamo is dead — unamo.com returns NXDOMAIN with no A, NS or SOA records at all, and the pre-rebrand domain positionly.com is now a third-party WordPress rebuild of the 2017 Positionly marketing site whose own /api link 404s.
  evidence:
  - status: 0
    url: https://unamo.com
  - status: 404
    url: https://positionly.com/api
  - status: 404
    url: https://positionly.com/openapi.json
  - status: 404
    url: https://positionly.com/.well-known/agent-card.json
  - status: 200
    url: https://positionly.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: Unamo was a Warsaw, Poland based SaaS suite offering SEO monitoring, social media monitoring, and conversion rate optimization, formerly known as Positionly, and backed by Point Nine Capital. The company appears defunct as of July 2026, with unamo.com no longer resolving in DNS and the pre-rebrand positionly.com site serving stale 2017-era content whose API, signup, terms, and privacy pages return 404. No public API surface, client packages, or developer documentation remain online.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unamo.png
layout: provider
modified: '2026-08-13'
name: Unamo
nav: Providers
network: true
overview: Unamo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SEO, Social-Media, Analytics, and Monitoring.
random_paper: 19
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
slug: unamo
tags:
- Company
- SEO
- Social-Media
- Analytics
- Monitoring
- Marketing
website: https://unamo.com
---
