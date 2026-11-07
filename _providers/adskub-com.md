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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/adskub-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/adskub-com/llms/adskub-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adskub-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adskub-com/well-known/adskub-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adskub-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adskub-com/hosts/adskub-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adskub-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adskub-com/vendors/adskub-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adskub-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adskub.com/en/phuket/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adskub.com/en/phuket/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://adskub.com/en/phuket/login
- group: docs
  title: ''
  type: Documentation
  url: https://adskub.com/en/phuket/blog/tag/guides
- group: company
  title: ''
  type: Blog
  url: https://adskub.com/en/phuket/blog
- group: auth
  href: https://artifacts.apis.io/adskub-com/security/adskub-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adskub-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adskub.com/
coverage:
  checked: '2026-11-01'
  detail: Adskub provides vehicle rental listings and does not expose a public API.
  evidence:
  - status: 200
    url: https://adskub.com/
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: AdsKub is an online classifieds platform focused on the Phuket region of Thailand, enabling users to buy, sell, and rent a wide range of items including vehicles such as cars, motorcycles, and scooters, as well as real‑estate like apartments, condos, and villas. The service provides a localized marketplace that connects buyers and sellers through a web interface, supporting multiple languages and offering image‑rich listings to facilitate transactions.
image: https://adskub.com/logo.webp
layout: provider
modified: '2026-10-31'
name: AdsKub
nav: Providers
network: true
overview: 'AdsKub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Classifieds, Marketplace, Real Estate, Vehicles, and Thailand.


  AdsKub''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Adskub Com Plans Pricing
  plan_count: 0
  slug: adskub-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Adskub Com Rate Limits
  slug: adskub-com-rate-limits
scopes:
- name: Adskub Com Scopes
  scope_count: 0
  slug: adskub-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 12.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - thailand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 17.5
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adskub Com Authentication
  slug: adskub-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adskub Com Domain Security
  slug: adskub-com-domain-security
  summary_line: TLSv1.3
slug: adskub-com
tags:
- Classifieds
- Marketplace
- Real Estate
- Vehicles
- Thailand
- Phuket
website: https://adskub.com/
---
