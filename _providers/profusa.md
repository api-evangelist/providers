---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/profusa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profusa.com/
- group: company
  title: ''
  type: About
  url: https://profusa.com/about-profusa/
- group: operate
  title: ''
  type: Support
  url: https://profusa.com/contact-profusa/
- group: company
  title: ''
  type: Blog
  url: https://investors.profusa.com/press-releases
- group: company
  title: ''
  type: BlogRSS
  url: https://profusa.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://profusa.com/careers-profusa/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.profusa.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/profusa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/profusa-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Profusa ships a clinical Data Platform and a phone app for its Lumee biosensors but publishes nothing for developers — profusa.com is a WordPress marketing site whose only machine-readable surface is the generic WordPress core REST discovery document at /wp-json/, and every developer path (/developers, /api, /docs, /openapi.json, /llms.txt, /.well-known/*) returns 404, while investors.profusa.com answers 200 with an SPA shell for every path including /.well-known/agent-card.json.
  evidence:
  - status: 404
    url: https://profusa.com/developers
  - status: 404
    url: https://profusa.com/openapi.json
  - status: 404
    url: https://profusa.com/llms.txt
  - status: 404
    url: https://profusa.com/.well-known/agent-card.json
  - status: 200
    url: https://profusa.com/wp-json/
  - status: 200
    url: https://investors.profusa.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Profusa, Inc. (Nasdaq: PFSA) is a South San Francisco digital-health and medical-device company that builds tissue-integrated biosensors — injectable, biologically compatible hydrogel microsensors smaller than a grain of rice — for continuous, real-time monitoring of body chemistry. Its Lumee Oxygen Platform reports tissue oxygen for peripheral artery disease, chronic wounds and reconstructive surgery, and a long-duration Lumee glucose sensor is in development. A companion Data Platform turns raw sensor readings into clinical intelligence for clinicians, with EMR integration described as planned rather than shipped. Profusa has received more than USD 23M in NIH and DARPA funding and became publicly traded in July 2025 through a business combination with NorthView Acquisition Corporation. As of this profiling pass the company publishes no developer program, no public API documentation and no machine-readable API contract.'
image: https://profusa.com/wp-content/uploads/2015/12/cropped-profusa-logo-1-270x270.png
layout: provider
modified: '2026-08-26'
name: Profusa
nav: Providers
network: true
overview: 'Profusa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Medical Devices, Biosensors, and Digital Health.


  Profusa''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/profusa/refs/heads/main/screenshots/profusa-2026-09-02T152124.png
security:
- kind: domain-security
  name: Profusa Domain Security
  slug: profusa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: profusa
tags:
- Company
- Health
- Medical Devices
- Biosensors
- Digital Health
- Continuous Monitoring
- Diagnostics
- Life Sciences
website: https://profusa.com/
---
