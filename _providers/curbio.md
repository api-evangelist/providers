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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/curbio/hosts/curbio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curbio-hosts.yml
- group: other
  href: https://artifacts.apis.io/curbio/vendors/curbio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curbio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curbio.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curbio.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://curbio.com/curb-appeal-blog/price-reduction-alternatives/
- group: auth
  href: https://artifacts.apis.io/curbio/security/curbio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curbio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://curbio.com/how-it-works/
- group: start
  title: ''
  type: GettingStarted
  url: https://curbio.com/estimate/
- group: company
  title: ''
  type: Blog
  url: https://curbio.com/curb-appeal-blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.curbio.com/
- group: operate
  title: ''
  type: Support
  url: https://curbio.com/contact-us/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: blocked
    url: https://api.curbio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curbio is a home renovation and remodeling service that helps homeowners increase property value by managing on‑market concierge renovations. They provide a full‑service platform covering design, permits, construction, and financing, enabling sellers to showcase upgraded homes to buyers. The company operates nationwide across multiple US markets, offering services such as kitchen and bathroom remodels, exterior updates, and basic listing preparation.
image: https://curbio.com/wp-content/uploads/2025/02/Untitled-design-71.jpg
layout: provider
modified: '2026-10-12'
name: Curbio
nav: Providers
network: true
overview: 'Curbio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Home Renovation, Real Estate, Remodeling, On-Market Concierge, and USA.


  Curbio''s developer surface includes pricing, documentation, getting-started guide, engineering blog, support, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/curbio/curbio-2026-11-03T125831.png
security:
- kind: domain-security
  name: Curbio Domain Security
  slug: curbio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curbio
tags:
- Home Renovation
- Real Estate
- Remodeling
- On-Market Concierge
- USA
website: https://curbio.com/
---
