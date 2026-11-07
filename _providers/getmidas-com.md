---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
api_count: 1
apis:
- description: Midas offers investment platform APIs, but they are not publicly documented and require authentication.
  name: Midas API
  slug: midas-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/getmidas-com/llms/getmidas-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getmidas-com-llms.txt
- group: other
  href: https://artifacts.apis.io/getmidas-com/hosts/getmidas-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getmidas-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getmidas-com/vendors/getmidas-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getmidas-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getmidas
- group: auth
  href: https://artifacts.apis.io/getmidas-com/security/getmidas-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getmidas-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmidas.com/
- group: operate
  title: ''
  type: Support
  url: https://www.getmidas.com/destek/
- group: company
  title: ''
  type: Blog
  url: https://www.getmidas.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.getmidas.com/midas-akademi
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getmidas.com/ucretler/
- group: start
  title: ''
  type: SignUp
  url: https://www.getmidas.com/kayit-ol/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getmidas.com/yasal-duyurular-ve-sozlesmeler/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmidas.com/kisisel-verilerin-korunmasi-kvkk/
coverage:
  checked: '2026-10-29'
  detail: API endpoints require authentication and return 403, indicating gated access.
  evidence:
  - status: 403
    url: https://api.getmidas.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Midas, kullanıcıların Borsa İstanbul, Amerikan borsaları, Avrupa borsaları, yatırım fonları, kripto varlıklar, VİOP, opsiyon piyasası, varantlar ve emtialar gibi farklı yatırım araçlarına tek bir uygulama üzerinden erişmesini sağlayan bir yatırım platformudur. 2020 yılında kurulmuş ve İstanbul, Türkiye merkezli bir fintech şirketidir. Platform, hem bireysel hem kurumsal yatırımcılara kapsamlı piyasa verileri, alım satım hizmetleri ve eğitim içerikleri sunar.
image: https://webcdn.getmidas.com/uploads/2026/06/10161719/midas-logo.png
layout: provider
modified: '2026-10-28'
name: Midas
nav: Providers
network: true
overview: 'Midas is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investment, Trading, and Mobile App.


  Midas'' developer surface includes support, engineering blog, documentation, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Getmidas Com Plans Pricing
  plan_count: 0
  slug: getmidas-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Getmidas Com Rate Limits
  slug: getmidas-com-rate-limits
scopes:
- name: Getmidas Com Scopes
  scope_count: 0
  slug: getmidas-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getmidas-com/getmidas-com-2026-11-03T132729.png
security:
- kind: authentication
  name: Getmidas Com Authentication
  slug: getmidas-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Getmidas Com Domain Security
  slug: getmidas-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: getmidas-com
tags:
- Company
- Fintech
- Investment
- Trading
- Mobile App
- Turkey
website: https://www.getmidas.com/
---
