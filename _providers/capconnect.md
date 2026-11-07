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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CapConnect+ provides a digital platform that simplifies fixed income primary market issuance, connecting corporate issuers, dealers, and investors.
  name: CapConnect API
  slug: capconnect-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/capconnect/well-known/capconnect-ccp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capconnect-ccp-security.txt
- group: agent
  href: https://artifacts.apis.io/capconnect/well-known/capconnect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capconnect-well-known.yml
- group: operate
  href: https://artifacts.apis.io/capconnect/changelog/capconnect-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/capconnect-changelog.yml
- group: other
  href: https://artifacts.apis.io/capconnect/hosts/capconnect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capconnect-hosts.yml
- group: other
  href: https://artifacts.apis.io/capconnect/vendors/capconnect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capconnect-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.capconnectplus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.capconnectplus.com/terms?hsLang=en
- group: operate
  title: ''
  type: Support
  url: https://www.capconnectplus.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://ccp.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://www.capconnectplus.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.capconnectplus.com/privacy?hsLang=en
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.capconnectplus.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.capconnectplus.com/en/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.capconnectplus.com/
- group: auth
  href: https://artifacts.apis.io/capconnect/security/capconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.capconnectplus.com
coverage:
  checked: '2026-10-07'
  detail: Developer portal at https://dev.capconnectplus.com renders a React SPA, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://dev.capconnectplus.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: CapConnect+ provides a digital platform that simplifies fixed income primary market issuance, connecting corporate issuers, dealers, and investors. The solution offers live book building, pricing optimization, and automated investor management, aiming to lower funding costs and increase transparency in bond and commercial paper issuance.
layout: provider
modified: '2026-10-06'
name: CapConnect
nav: Providers
network: true
overview: 'CapConnect is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Fixed Income, Digital Platform, and Issuance.


  CapConnect''s developer surface includes changelog, support, engineering blog, documentation, and 12 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 53.6
    operational_transparency: 21.1
  previous_composite: 20.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/capconnect/capconnect-2026-11-03T123204.png
security:
- kind: domain-security
  name: Capconnect Domain Security
  slug: capconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capconnect
tags:
- Company
- Fintech
- Fixed Income
- Digital Platform
- Issuance
- Investor Management
website: https://www.capconnectplus.com
---
