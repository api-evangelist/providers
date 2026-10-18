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
- description: API Overview page for Seccl developers
  name: Seccl API
  slug: seccl-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seccl/refs/heads/main/security/seccl-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/seccl-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seccl/refs/heads/main/well-known/seccl-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/seccl-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seccl/refs/heads/main/well-known/seccl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seccl-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seccl/refs/heads/main/hosts/seccl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seccl-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seccl/refs/heads/main/vendors/seccl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seccl-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.seccl.tech/hc/en-gb
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seccl/refs/heads/main/security/seccl-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/seccl-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seccl/refs/heads/main/security/seccl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seccl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seccl.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://seccl.tech/developers
- group: docs
  title: ''
  type: Documentation
  url: https://seccl.tech/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://seccl.tech/about
- group: company
  title: ''
  type: Blog
  url: https://seccl.tech/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://seccl.tech/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seccl.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seccl.tech/privacy
coverage:
  checked: '2026-10-13'
  detail: Developer portal provides HTML docs but no OpenAPI or other machine-readable contract.
  evidence:
  - status: 0
    url: https://api.seccl.tech/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Seccl provides an embedded investment platform offering services such as client onboarding, portfolio management, digital pensions, custody, and payments. Their technology enables financial advisers, neobanks, and fintechs to deliver a fully digital client experience with low-cost, scalable solutions. The platform emphasizes data control, integration flexibility, and comprehensive reporting, positioning Seccl as a modern fintech infrastructure provider.
image: https://seccl.tech/assets/images/Seccl-OG.jpg
layout: provider
modified: '2026-10-13'
name: Seccl
nav: Providers
network: true
overview: 'Seccl is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Investment Platform, Embedded Banking, and B2B.


  Seccl''s developer surface includes support, documentation, getting-started guide, engineering blog, pricing, and 11 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seccl Domain Security
  slug: seccl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Seccl Vulnerability Disclosure
  slug: seccl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: seccl
tags:
- Fintech
- Investment Platform
- Embedded Banking
- B2B
website: https://seccl.tech
---
