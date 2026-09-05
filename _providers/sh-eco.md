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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sh-eco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sh-eco.com.cn
created: '2026-07-17'
description: SH-ECO (翊科聚合物 / Yike Polymer) is a Chinese medical-device materials manufacturer specializing in the research, production, and customized fabrication of medical catheters and membrane materials. Its product range spans single-lumen tubing, multi-lumen tubing, composite/multi-layer tubing, and injection-molded components serving healthcare and multiple industrial applications. The company is a portfolio company of Qiming Venture Partners and was added to the API Evangelist network as a company profile. It publishes a corporate marketing website but exposes no public developer or API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sh-eco.png
layout: provider
modified: '2026-07-21'
name: sh-eco
nav: Providers
network: true
overview: sh-eco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Materials, Manufacturing, and Healthcare.
random_paper: 8
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sh-eco/refs/heads/main/screenshots/sh-eco-2026-09-02T155054.png
security:
- kind: domain-security
  name: Sh Eco Domain Security
  slug: sh-eco-domain-security
  summary_line: no transport/DNS hardening detected
slug: sh-eco
tags:
- Company
- Medical Devices
- Materials
- Manufacturing
- Healthcare
- Catheters
- Polymers
- China
website: https://sh-eco.com.cn
---
