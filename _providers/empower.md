---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer portal for Empower's financial platform APIs.
  name: Empower API
  slug: empower-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/empower/refs/heads/main/authentication/empower-authentication.yml
  title: ''
  type: Authentication
  url: authentication/empower-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/empower/refs/heads/main/conformance/empower-conformance.yml
  title: ''
  type: Conformance
  url: conformance/empower-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/empower/refs/heads/main/hosts/empower-hosts.yml
  title: ''
  type: Hosts
  url: hosts/empower-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/empower/refs/heads/main/vendors/empower-vendors.yml
  title: ''
  type: Vendors
  url: vendors/empower-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.empower.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.empower.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.empower.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.empower.com/the-currency/money/price-check-research
- group: company
  title: ''
  type: Newsroom
  url: https://www.empower.com/investments/news
- group: other
  title: ''
  type: Leadership
  url: https://www.empower.com/management
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.empower.com/docs/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.empower.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/empower/refs/heads/main/security/empower-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/empower-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.empower.com
coverage:
  checked: '2026-10-14'
  detail: OpenAPI spec endpoints on api.empower.com return 403, and no machine-readable contract was found.
  evidence:
  - status: 403
    url: https://api.empower.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Empower provides a modern financial platform offering personal investing, workplace retirement, and tools for financial professionals. It delivers a suite of services including investment accounts, IRAs, cash management, and financial planning tools, aiming to help individuals and organizations make better money decisions throughout their lives.
layout: provider
modified: '2026-10-14'
name: Empower
nav: Providers
network: true
overview: 'Empower is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Investment, Retirement, and Financial-Tools.


  Empower''s developer surface includes authentication, signup flow, pricing, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Empower Authentication
  slug: empower-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Empower Domain Security
  slug: empower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: empower
tags:
- Company
- Finance
- Investment
- Retirement
- Financial-Tools
website: https://www.empower.com
---
