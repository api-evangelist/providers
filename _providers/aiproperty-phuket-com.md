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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aiproperty-phuket-com/llms/aiproperty-phuket-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiproperty-phuket-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aiproperty-phuket-com/well-known/aiproperty-phuket-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiproperty-phuket-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiproperty-phuket-com/hosts/aiproperty-phuket-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiproperty-phuket-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiproperty-phuket-com/vendors/aiproperty-phuket-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiproperty-phuket-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiproperty-phuket.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aiproperty-phuket.com/developers
- group: auth
  href: https://artifacts.apis.io/aiproperty-phuket-com/security/aiproperty-phuket-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiproperty-phuket-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiproperty-phuket.com/
coverage:
  checked: '2026-11-01'
  detail: Developer portal pages are rendered via Next.js JavaScript, providing no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://aiproperty-phuket.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AIProperty is a real-estate platform focused on properties in Phuket, Thailand, offering condos, villas, apartments and other residential listings for sale and rent. The site provides detailed property information, market guides, investment advice, and tools for currency conversion, catering to both local and international buyers.
image: https://aiproperty-phuket.com/og-default.jpg
layout: provider
modified: '2026-11-01'
name: AIProperty
nav: Providers
network: true
overview: AIProperty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Property Listings, Thailand, Phuket, and Real Estate Marketplace.
random_paper: 9
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - thailand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 8.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiproperty Phuket Com Domain Security
  slug: aiproperty-phuket-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aiproperty-phuket-com
tags:
- Real Estate
- Property Listings
- Thailand
- Phuket
- Real Estate Marketplace
website: https://aiproperty-phuket.com/
---
