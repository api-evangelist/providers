---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: Security
  url: https://balford.net/privacy-statement/
- group: agent
  href: https://artifacts.apis.io/balford-net/llms/balford-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/balford-net-llms.txt
- group: auth
  href: https://artifacts.apis.io/balford-net/well-known/balford-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/balford-net-security.txt
- group: agent
  href: https://artifacts.apis.io/balford-net/well-known/balford-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/balford-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/balford-net/hosts/balford-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/balford-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/balford-net/vendors/balford-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/balford-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://balford.net/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://balford.net/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://balford.net/news/
- group: other
  title: ''
  type: Leadership
  url: https://balford.net/team/
- group: auth
  href: https://artifacts.apis.io/balford-net/security/balford-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/balford-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/balford-net/security/balford-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/balford-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://balford.net/
- group: operate
  title: ''
  type: Support
  url: https://balford.net/support
- group: company
  title: ''
  type: Blog
  url: https://balford.net/blog
coverage:
  checked: '2026-11-02'
  detail: Balford is a manufacturing company with no public developer API.
  evidence:
  - status: 403
    url: https://balford.net/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: Balford is a China‑based manufacturer specializing in deep‑drawn metal housings and solenoid valve housings. The company offers metal stamping, CNC machining, progressive die stamping, sheet metal processing, and related engineering services. Its capabilities include precision metal stamping, CNC turning, milling, wire EDM, and PPAP‑ready production for robotics, UAVs, and industrial parts. Balford serves supplier networks and provides technical resources such as calculators, whitepapers, and engineering guides.
image: https://balford.net/media/2026/07/balford-metal-stamping-std.webp
layout: provider
modified: '2026-11-02'
name: Balford
nav: Providers
network: true
overview: 'Balford is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Metal Stamping, CNC Machining, Solenoid Housings, and China.


  Balford''s developer surface includes support, engineering blog, and 13 more developer resources.'
plans:
- name: Balford Net Plans Pricing
  plan_count: 0
  slug: balford-net-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Balford Net Rate Limits
  slug: balford-net-rate-limits
scopes:
- name: Balford Net Scopes
  scope_count: 0
  slug: balford-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 14.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Balford Net Authentication
  slug: balford-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Balford Net Domain Security
  slug: balford-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Balford Net Vulnerability Disclosure
  slug: balford-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: balford-net
tags:
- Manufacturing
- Metal Stamping
- CNC Machining
- Solenoid Housings
- China
- Engineering
website: https://balford.net/
---
