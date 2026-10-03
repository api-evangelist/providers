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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autobooks/refs/heads/main/well-known/autobooks-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autobooks-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autobooks/refs/heads/main/well-known/autobooks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autobooks-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autobooks/refs/heads/main/hosts/autobooks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autobooks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autobooks/refs/heads/main/vendors/autobooks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autobooks-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/autobooks/refs/heads/main/packages/autobooks-packages.yml
  title: ''
  type: SDKs
  url: packages/autobooks-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/autobooks/refs/heads/main/packages/autobooks-packages.yml
  title: ''
  type: Packages
  url: packages/autobooks-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.autobooks.co/knowledge
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autobooks.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.autobooks.co/pricing-calculator
- group: start
  title: ''
  type: Login
  url: https://www.autobooks.co/login
- group: company
  title: ''
  type: Blog
  url: https://blog.autobooks.co/?hsLang=en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://help.autobooks.co/knowledge/optimize-your-invoice-tool-setup
- group: docs
  title: ''
  type: Documentation
  url: https://dev.autobooks.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autobooks
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autobooks/refs/heads/main/security/autobooks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autobooks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autobooks.co/
coverage:
  checked: '2026-09-26'
  detail: Autobooks provides public documentation but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://www.autobooks.co/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Autobooks provides a connected banking platform for small businesses, offering invoicing, payment links, checkout pages, tap‑to‑pay, bill payment, accounting, lending and cash‑balance tools. It integrates receivables, payables and financial reporting into digital banking, enabling businesses and their banks to see real‑time financial activity.
layout: provider
modified: '2026-09-26'
name: Autobooks
nav: Providers
network: true
overview: 'Autobooks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Banking, Payments, Small Business, and Accounting.


  Autobooks'' developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 44.6
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autobooks Domain Security
  slug: autobooks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: autobooks
tags:
- Fintech
- Banking
- Payments
- Small Business
- Accounting
- Lending
website: https://www.autobooks.co/
---
