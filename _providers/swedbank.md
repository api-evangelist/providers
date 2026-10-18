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
- description: Swedbank developer portal provides API documentation and access.
  name: Swedbank API
  slug: swedbank-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/well-known/swedbank-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swedbank-www-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/well-known/swedbank-swedbank-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swedbank-swedbank-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.swedbank.se/om-oss/sakerhet/report-a-security-flaw.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/well-known/swedbank-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swedbank-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/well-known/swedbank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swedbank-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/hosts/swedbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swedbank-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/vendors/swedbank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swedbank-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.swedbank.com/newsroom/logotype.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.swedbank.com/admin/app/home
- group: docs
  title: ''
  type: Documentation
  url: https://developer.swedbank.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/security/swedbank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/swedbank-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swedbank/refs/heads/main/security/swedbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swedbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swedbank.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://swedbank.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Swedbank Group is a modern bank rooted in Sweden’s savings banks and cooperative agricultural banking tradition. It serves 7.3 million private customers and 548,000 corporate customers across the Nordics, offering services such as cash management, trade finance, asset management, and sustainable banking. The bank emphasizes responsible business, environmental stewardship, and anti‑money‑laundering efforts, with extensive investor relations and corporate governance information publicly available on its website.
layout: provider
modified: '2026-10-14'
name: Swedbank
nav: Providers
network: true
overview: 'Swedbank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Nordic, Corporate Banking, and Sustainable Banking.


  Swedbank''s developer surface includes documentation and 12 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Swedbank Domain Security
  slug: swedbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Swedbank Vulnerability Disclosure
  slug: swedbank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swedbank
tags:
- Banking
- Financial Services
- Nordic
- Corporate Banking
- Sustainable Banking
website: https://swedbank.com/
---
