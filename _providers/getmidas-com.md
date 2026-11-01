---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
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
overview: 'Midas is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Investment, Trading, and MobileApp.


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
  composite: 19.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 27.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- FinTech
- Investment
- Trading
- MobileApp
- Turkey
website: https://www.getmidas.com/
---
