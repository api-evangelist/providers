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
overview: 'CBA PowerBoard (Commonwealth Bank) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, and Australia.


  CBA PowerBoard (Commonwealth Bank)''s developer surface includes getting-started guide, documentation, and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 60.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.9
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 8.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cba-powerboard/cba-powerboard-2026-11-03T123535.png
security:
- kind: domain-security
  name: Cba Powerboard Domain Security
  slug: cba-powerboard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cba-powerboard
tags:
- Company
- Banking
- Fintech
- Australia
website: https://www.commbank.com.au/business/payments/take-online-payments/powerboard.html
---
