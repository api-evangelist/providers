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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Payment APIs for merchants to accept payments, manage transactions, and access financial data.
  name: Bambora API
  slug: bambora-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bambora/refs/heads/main/hosts/bambora-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bambora-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bambora/refs/heads/main/vendors/bambora-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bambora-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bambora/refs/heads/main/packages/bambora-packages.yml
  title: ''
  type: SDKs
  url: packages/bambora-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bambora/refs/heads/main/packages/bambora-packages.yml
  title: ''
  type: Packages
  url: packages/bambora-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worldline.com/sv-se/compliancy/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://worldline.com/sv-se/compliancy/privacy
- group: start
  title: ''
  type: Login
  url: https://worldline.com/sv-se/home/top-navigation/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bambora
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bambora/refs/heads/main/security/bambora-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bambora-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bambora.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bambora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bambora.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bambora.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.bambora.com/contact
coverage:
  checked: '2026-10-15'
  detail: Developer portal returns HTML for typical OpenAPI URLs, providing no machine‑readable contract.
  evidence:
  - status: 200
    url: https://developer.bambora.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Bambora, now part of Worldline, provides payment solutions for businesses, including card acquiring, online checkout, invoicing, and open banking services. The company offers a unified platform for merchants to accept payments across channels, manage transactions, and access financial data APIs. With a focus on security and compliance, Bambora serves retailers, e‑commerce, and enterprises in Europe and beyond.
layout: provider
modified: '2026-10-15'
name: Bambora
nav: Providers
network: true
overview: 'Bambora is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, and Europe.


  Bambora''s developer surface includes documentation, API reference, support, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bambora Domain Security
  slug: bambora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bambora
tags:
- Company
- Payments
- Fintech
- Europe
website: https://bambora.com/
---
