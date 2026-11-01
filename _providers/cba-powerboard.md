---
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public banking APIs provided by Commonwealth Bank, no authentication required.
  name: CommBank Public APIs
  slug: commbank-public-apis
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/cba-powerboard/conformance/cba-powerboard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cba-powerboard-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cba-powerboard/llms/cba-powerboard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cba-powerboard-llms.txt
- group: other
  href: https://artifacts.apis.io/cba-powerboard/hosts/cba-powerboard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cba-powerboard-hosts.yml
- group: other
  href: https://artifacts.apis.io/cba-powerboard/vendors/cba-powerboard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cba-powerboard-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://your-domain.com/apis/fast-payments/quick-start/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.commbank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.connectedpayments.cba.com.au/
- group: auth
  href: https://artifacts.apis.io/cba-powerboard/security/cba-powerboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cba-powerboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commbank.com.au/business/payments/take-online-payments/powerboard.html
created: '2026-10-26'
description: CBA PowerBoard is a digital platform provided by the Commonwealth Bank of Australia that enables businesses and developers to integrate banking services, manage accounts, and access financial data through APIs. The service aims to streamline financial operations, offering endpoints for account information, transaction history, and other banking functionalities, supporting secure and efficient integration for enterprise applications.
layout: provider
modified: '2026-10-26'
name: CBA PowerBoard (Commonwealth Bank)
nav: Providers
network: true
overview: 'CBA PowerBoard (Commonwealth Bank) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, API, FinTech, and Australia.


  CBA PowerBoard (Commonwealth Bank)''s developer surface includes getting-started guide, documentation, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 8.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cba Powerboard Domain Security
  slug: cba-powerboard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cba-powerboard
tags:
- Company
- Banking
- API
- FinTech
- Australia
website: https://www.commbank.com.au/business/payments/take-online-payments/powerboard.html
---
