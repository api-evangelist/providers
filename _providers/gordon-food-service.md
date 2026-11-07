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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/gordon-food-service/well-known/gordon-food-service-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gordon-food-service-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gfs.com/
- group: design
  href: https://artifacts.apis.io/gordon-food-service/conformance/gordon-food-service-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gordon-food-service-conformance.yml
- group: other
  href: https://artifacts.apis.io/gordon-food-service/hosts/gordon-food-service-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gordon-food-service-hosts.yml
- group: other
  href: https://artifacts.apis.io/gordon-food-service/vendors/gordon-food-service-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gordon-food-service-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gfs.com/en-us/terms-of-use-agreement/
- group: start
  title: ''
  type: SignUp
  url: https://signup.gfs.com/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gfs.com/en-us/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://gfs.com/en-us/ideas/pricing-your-restaurant-menu-profitably/
- group: company
  title: ''
  type: Newsroom
  url: https://gfs.com/ideas/category/newsroom/
- group: start
  title: ''
  type: GettingStarted
  url: https://gfs.com/en-us/quick-start/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.gfs.com/
- group: auth
  href: https://artifacts.apis.io/gordon-food-service/security/gordon-food-service-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gordon-food-service-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gordon-food-service/security/gordon-food-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gordon-food-service-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gfs.com/
coverage:
  checked: '2026-10-28'
  detail: Provider documentation is HTML only with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract discovered.
  evidence:
  - status: 200
    url: https://dev.gfs.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Gordon Food Service (GFS) is North America’s largest family‑operated foodservice distributor, supplying a broad range of food, beverage and related products to restaurants, healthcare facilities, schools and other institutions. With over 125 years of experience, GFS operates a network of distribution centers and offers services such as menu planning, culinary expertise, and technology solutions to help customers manage their operations efficiently.
image: https://gfs.com/wp-content/uploads/2023/02/GordonFoodService_Logo_RGB.png
layout: provider
modified: '2026-10-28'
name: Gordon Food Service
nav: Providers
network: true
overview: 'Gordon Food Service is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Distribution, B2B, Logistics, and North America.


  Gordon Food Service''s developer surface includes signup flow, pricing, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 24.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gordon-food-service/gordon-food-service-2026-11-03T132944.png
security:
- kind: domain-security
  name: Gordon Food Service Domain Security
  slug: gordon-food-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gordon Food Service Trust Center
  slug: gordon-food-service-trust-center
  summary_line: PCI DSS
slug: gordon-food-service
tags:
- Company
- Food Distribution
- B2B
- Logistics
- North America
website: https://gfs.com/
---
