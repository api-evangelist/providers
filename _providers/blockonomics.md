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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Blockonomics provides a decentralized crypto payment gateway API for merchants to accept Bitcoin and other cryptocurrencies. Documentation is available at the integrations page.
  name: Blockonomics API
  slug: blockonomics-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/blockonomics/llms/blockonomics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockonomics-llms.txt
- group: other
  href: https://artifacts.apis.io/blockonomics/hosts/blockonomics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockonomics-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockonomics/vendors/blockonomics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockonomics-vendors.yml
- group: build
  href: https://artifacts.apis.io/blockonomics/packages/blockonomics-packages.yml
  title: ''
  type: SDKs
  url: packages/blockonomics-packages.yml
- group: build
  href: https://artifacts.apis.io/blockonomics/packages/blockonomics-packages.yml
  title: ''
  type: Packages
  url: packages/blockonomics-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.blockonomics.co/support/home
- group: start
  title: ''
  type: SignUp
  url: https://www.blockonomics.co/register
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.blockonomics.co\\\
- group: docs
  title: ''
  type: APIReference
  url: https://developers.blockonomics.co/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blockonomics
- group: auth
  href: https://artifacts.apis.io/blockonomics/security/blockonomics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockonomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockonomics.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blockonomics.co/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockonomics.co/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.blockonomics.co/systemstatus
- group: docs
  title: ''
  type: Documentation
  url: https://www.blockonomics.co/integrations
- group: start
  title: ''
  type: GettingStarted
  url: https://www.blockonomics.co/merchants/demos
coverage:
  checked: '2026-10-26'
  detail: Documentation pages render via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.blockonomics.co/integrations
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Blockonomics provides a decentralized crypto payment gateway that enables merchants to accept Bitcoin and other cryptocurrencies directly to their wallets. With a focus on privacy, self‑custody, and easy integration, it offers payment widgets, invoices, and blockchain explorer tools, supporting over 150 fiat currencies and complying with global regulations.
layout: provider
modified: '2026-10-26'
name: Blockonomics
nav: Providers
network: true
overview: 'Blockonomics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cryptocurrency, Bitcoin, and Privacy.


  Blockonomics'' developer surface includes support, signup flow, API reference, pricing, documentation, getting-started guide, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blockonomics Domain Security
  slug: blockonomics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blockonomics
tags:
- Company
- Payments
- Cryptocurrency
- Bitcoin
- Privacy
website: https://www.blockonomics.co/
---
