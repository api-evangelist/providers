---
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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adagiomedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adagiomedical.com/
- group: operate
  title: ''
  type: Support
  url: https://adagiomedical.com/us/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adagiomedical.com/us/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adagiomedical.com/us/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://adagiomedical.com/us/product-security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adagiomedical-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adagiomedical-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Adagio Medical is a NASDAQ-listed cardiac-ablation device manufacturer whose entire public web presence is 18 marketing, clinical-evidence and careers pages across /us and /eu; the only /api path on the site is the Next.js internal route that its own robots.txt disallows, and every contract-discovery probe (openapi.json, swagger.json, apis.json, llms.txt, agent-card, OAuth/OIDC discovery) returned 404 on every host.
  evidence:
  - status: 200
    url: https://adagiomedical.com/us/sitemap.xml
  - status: 404
    url: https://adagiomedical.com/openapi.json
  - status: 404
    url: https://adagiomedical.com/.well-known/agent-card.json
  - status: 404
    url: https://adagiomedical.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/adagiomedical
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'Adagio Medical, Inc. is a Laguna Hills, California medical device company and an operating subsidiary of Adagio Medical Holdings, Inc. (NASDAQ: ADGM). It develops catheter-based cardiac ablation systems built on its proprietary Ultra-Low Temperature Cryoablation (ULTC) platform and an emerging Pulsed Field Cryoablation (PFCA) platform, designed to create large, durable, transmural lesions for the treatment of ventricular tachycardia, atrial fibrillation and atrial flutter. Its CE-marked vCLAS Cryoablation System holds FDA Breakthrough Device Designation and is under U.S. evaluation in the FULCRUM-VT pivotal IDE study. Adagio Medical sells regulated physical devices to hospitals and electrophysiology labs; it publishes no public API, developer portal, SDK or machine-readable contract. It does publish a coordinated product-security vulnerability disclosure policy.'
image: https://adagiomedical.com/adagio-logo.svg
layout: provider
modified: '2026-09-06'
name: Adagio Medical
nav: Providers
network: true
overview: 'Adagio Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Cardiology, and Medical Technology.


  Adagio Medical''s developer surface includes support and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adagiomedical Domain Security
  slug: adagiomedical-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Adagiomedical Vulnerability Disclosure
  slug: adagiomedical-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: adagiomedical
tags:
- Company
- Medical Devices
- Health
- Cardiology
- Medical Technology
- Cryoablation
- Electrophysiology
website: https://adagiomedical.com/
---
