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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/webstaurantstore/security/webstaurantstore-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/webstaurantstore-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/webstaurantstore/well-known/webstaurantstore-webstaurantstore-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webstaurantstore-webstaurantstore-security.txt
- group: auth
  href: https://artifacts.apis.io/webstaurantstore/well-known/webstaurantstore-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webstaurantstore-security.txt
- group: agent
  href: https://artifacts.apis.io/webstaurantstore/well-known/webstaurantstore-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webstaurantstore-well-known.yml
- group: other
  href: https://artifacts.apis.io/webstaurantstore/hosts/webstaurantstore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webstaurantstore-hosts.yml
- group: other
  href: https://artifacts.apis.io/webstaurantstore/vendors/webstaurantstore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/webstaurantstore-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.webstaurantstore.com/blog/
- group: auth
  href: https://artifacts.apis.io/webstaurantstore/security/webstaurantstore-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/webstaurantstore-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/webstaurantstore/security/webstaurantstore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webstaurantstore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://webstaurantstore.com/
coverage:
  checked: '2026-10-28'
  detail: The provider's website offers no public API documentation or machine‑readable spec despite having a developer‑facing site.
  evidence:
  - status: 0
    url: https://api.webstaurantstore.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: WebstaurantStore is a leading online retailer of commercial restaurant supplies, offering a vast catalog of equipment, smallwares, food and beverage items, furniture, and janitorial products. The company serves restaurants, foodservice operators, and hospitality businesses with competitive pricing, extensive product details, and a robust e‑commerce platform that includes ordering, tracking, and customer support services.
image: https://www.webstaurantstore.com/uploads/design/2014/1/webstaurantstore-logo.png
layout: provider
modified: '2026-10-28'
name: WebstaurantStore
nav: Providers
network: true
overview: 'WebstaurantStore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Restaurant Supplies, Food Service, and B2B.


  WebstaurantStore''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Webstaurantstore Domain Security
  slug: webstaurantstore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Webstaurantstore Vulnerability Disclosure
  slug: webstaurantstore-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: webstaurantstore
tags:
- Company
- E-Commerce
- Restaurant Supplies
- Food Service
- B2B
website: https://webstaurantstore.com/
---
