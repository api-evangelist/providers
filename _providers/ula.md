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
- group: company
  title: ''
  type: Website
  url: https://ula.app
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ula-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ula-llms.txt
created: '2026-07-17'
description: Ula was a B2B wholesale commerce platform for small neighborhood retail shops (warungs), providing supply chain technology, inventory management, and credit access across Indonesia, India, and Singapore. Backed by Prosus Ventures, Ula closed its core operations in late 2023 and ula.app now hosts a retrospective of the company. No public API, developer portal, or SDKs were ever published, and no developer subdomains resolve.
image: https://ula.app/images/logo-ula-green.png
layout: provider
modified: '2026-07-21'
name: Ula
nav: Providers
network: true
overview: Ula is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, B2B, Commerce, and Retail.
random_paper: 7
score:
  band: minimal
  composite: 5.7
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ula/refs/heads/main/screenshots/ula-2026-09-02T164754.png
security:
- kind: domain-security
  name: Ula Domain Security
  slug: ula-domain-security
  summary_line: TLSv1.3
slug: ula
tags:
- Company
- Marketplace
- B2B
- Commerce
- Retail
- Indonesia
- Defunct
website: https://ula.app
---
