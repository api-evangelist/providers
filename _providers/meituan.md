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
  url: security/meituan-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meituan-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.meituan.com
- group: company
  title: ''
  type: Website
  url: https://meituan.com
created: '2026-07-17'
description: Meituan (美团) is a Chinese technology-retail company operating one of the world's largest on-demand local-services and food-delivery super-apps. Its platform spans restaurant food delivery, in-store dining and group buying (Dianping), grocery and instant retail, hotel and travel booking, bike and moped sharing, and payments. Meituan runs a partner/developer cooperation center exposing merchant, delivery/logistics, and local-services integration APIs to business partners; these are partner-gated and documented in Chinese, with no public OpenAPI specification, SDK registry, or self-serve developer signup surfaced at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meituan.png
layout: provider
modified: '2026-07-20'
name: Meituan
nav: Providers
network: true
overview: Meituan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Food Delivery, Local Services, and E-Commerce.
random_paper: 20
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meituan/refs/heads/main/screenshots/meituan-2026-08-07T172447.png
security:
- kind: domain-security
  name: Meituan Domain Security
  slug: meituan-domain-security
  summary_line: TLSv1.2 · DMARC
slug: meituan
tags:
- Company
- Technology
- Food Delivery
- Local Services
- E-Commerce
- Super App
- Logistics
- China
website: https://meituan.com
---
