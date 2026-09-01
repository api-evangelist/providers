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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upcode-academy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upcodeacademy.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upcode-academy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/upcode-academy-well-known.yml
created: '2026-07-17'
description: UpCode Academy was a Singapore-based coding school offering short bootcamps and part-time courses (SQL, Python, Web Development with Ruby on Rails, Data Science, Computer Vision, IoT) taught by industry practitioners. Operated by 40 Tasks, a 500 Global portfolio company whose earlier product was the LOCO location-based search app at 40tasks.com. The company appears defunct - upcodeacademy.com serves a Cloudflare 522 dead-origin error (a bare default server page by December 2025) and 40tasks.com no longer resolves in DNS (domain-squatted since about 2023). No public API surface was found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upcode-academy.png
layout: provider
modified: '2026-07-21'
name: Upcode Academy
nav: Providers
network: true
overview: Upcode Academy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Coding Bootcamp, Training, and Data Science.
random_paper: 2
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Upcode Academy Domain Security
  slug: upcode-academy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: upcode-academy
tags:
- Company
- Education
- Coding Bootcamp
- Training
- Data Science
- Singapore
- Defunct
website: https://www.upcodeacademy.com
---
