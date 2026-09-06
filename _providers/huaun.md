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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huaun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.huaun.com/
created: '2026-07-17'
description: 'Huaun (华云安, Huayun''an) is a Beijing-based cybersecurity company specializing in attack surface management, vulnerability research, and adversarial (offensive/defensive) security. Its product line centers on three AI-driven systems: Ai·Vul (灵洞), an adaptive threat and vulnerability management platform that discovers and inventories host, web, IoT, and container-cluster assets along with eighteen classes of digital exposure including APIs; Ai·Radar (灵知), a threat-intelligence engine built on natural-language processing and knowledge graphs across thirty-plus data sources; and Ai·Bot (灵刃), an intelligent penetration-testing and attack-simulation system backed by a library of over 160,000 vulnerabilities and 2,000+ proof-of-concept exploits. Backed by DCM Ventures and other investors, Huaun helps enterprises continuously discover and validate their external and internal attack surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huaun.png
layout: provider
modified: '2026-07-19'
name: Huaun
nav: Providers
network: true
overview: Huaun is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Cybersecurity, Attack Surface Management, and Vulnerability Management.
random_paper: 20
score:
  band: minimal
  composite: 5.0
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huaun/refs/heads/main/screenshots/huaun-2026-07-25T221559.png
security:
- kind: domain-security
  name: Huaun Domain Security
  slug: huaun-domain-security
  summary_line: TLSv1.2 · HSTS
slug: huaun
tags:
- Company
- Enterprise
- Cybersecurity
- Attack Surface Management
- Vulnerability Management
- Threat Intelligence
- Penetration Testing
- Security
website: https://www.huaun.com/
---
