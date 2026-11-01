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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Deferit provides bill payment services; API details are not publicly documented.
  name: Deferit API
  slug: deferit-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://deferit.com/en-au/vulnerability-disclosure-policy/
- group: auth
  href: https://artifacts.apis.io/deferit/well-known/deferit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deferit-security.txt
- group: agent
  href: https://artifacts.apis.io/deferit/well-known/deferit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deferit-well-known.yml
- group: other
  href: https://artifacts.apis.io/deferit/hosts/deferit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deferit-hosts.yml
- group: other
  href: https://artifacts.apis.io/deferit/vendors/deferit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deferit-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.deferit.com/hc/en-au
- group: company
  title: ''
  type: Newsroom
  url: https://deferit.com/en-au/media/
- group: start
  title: ''
  type: GettingStarted
  url: https://deferit.com/en-au/get-started/
- group: docs
  title: ''
  type: Documentation
  url: https://help.deferit.com/
- group: auth
  href: https://artifacts.apis.io/deferit/security/deferit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deferit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deferit/security/deferit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deferit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deferit.com/en-us/
coverage:
  checked: '2026-10-22'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 302
    url: https://help.deferit.com/hc/en-au
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Deferit is an independent bill payment service that helps consumers split their bills into four smaller, manageable installments. It offers credit‑building payments, bill‑savings negotiations, and a platform to manage and track payments online. Users can upload bills, choose payment plans, and benefit from transparent fees, aiming to improve financial health and budgeting.
layout: provider
modified: '2026-10-22'
name: Deferit
nav: Providers
network: true
overview: 'Deferit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Bill Payments, Credit Building, and Consumer Finance.


  Deferit''s developer surface includes support, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deferit Domain Security
  slug: deferit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deferit Vulnerability Disclosure
  slug: deferit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deferit
tags:
- Company
- Fintech
- Bill Payments
- Credit Building
- Consumer Finance
website: https://deferit.com/en-us/
---
