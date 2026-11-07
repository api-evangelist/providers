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
    event_surface_described: unknown
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
  score: 6.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: STRATO HiDrive provides cloud storage and file sharing services. Documentation is available on the STRATO website but no machine‑readable API contract was found.
  name: HiDrive API
  slug: hidrive-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Security
  url: https://www.strato.de/it-security
- group: auth
  href: https://artifacts.apis.io/hidrive/well-known/hidrive-strato-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hidrive-strato-security.txt
- group: auth
  href: https://artifacts.apis.io/hidrive/well-known/hidrive-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hidrive-security.txt
- group: agent
  href: https://artifacts.apis.io/hidrive/well-known/hidrive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hidrive-well-known.yml
- group: other
  href: https://artifacts.apis.io/hidrive/hosts/hidrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hidrive-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.strato.de/server/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.strato.de/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.strato.de/faq/help/mail.php?thema=1166
- group: company
  title: ''
  type: Newsroom
  url: https://www.strato.de/press/
- group: auth
  href: https://artifacts.apis.io/hidrive/security/hidrive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hidrive-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hidrive/security/hidrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hidrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://strato.de/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.strato.de/cloud-speicher/hidrive-business/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: STRATO HiDrive is a German cloud storage service offered by STRATO, providing secure data storage, file sharing, and object storage solutions for businesses and individuals. It emphasizes data protection with AES‑256 encryption, compliance with German regulations, and integration with STRATO’s broader hosting and domain services.
image: https://www.strato.de/_assets/img/_og/de/og_startseite.png
layout: provider
modified: '2026-10-28'
name: STRATO HiDrive
nav: Providers
network: true
overview: 'STRATO HiDrive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, German, Data Protection, AES-256 Encryption, and Business.


  STRATO HiDrive''s developer surface includes support and 11 more developer resources.'
plans:
- name: Hidrive Plans Pricing
  plan_count: 0
  slug: hidrive-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Hidrive Rate Limits
  slug: hidrive-rate-limits
scopes:
- name: Hidrive Scopes
  scope_count: 0
  slug: hidrive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.0
    operational_transparency: 9.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 12.9
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hidrive/hidrive-2026-11-03T133403.png
security:
- kind: authentication
  name: Hidrive Authentication
  slug: hidrive-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hidrive Domain Security
  slug: hidrive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hidrive Vulnerability Disclosure
  slug: hidrive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hidrive
tags:
- Cloud Storage
- German
- Data Protection
- AES-256 Encryption
- Business
- Individual
website: https://strato.de/
---
