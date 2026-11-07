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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/paybook/hosts/paybook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paybook-hosts.yml
- group: other
  href: https://artifacts.apis.io/paybook/vendors/paybook-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paybook-vendors.yml
- group: build
  href: https://artifacts.apis.io/paybook/packages/paybook-packages.yml
  title: ''
  type: SDKs
  url: packages/paybook-packages.yml
- group: build
  href: https://artifacts.apis.io/paybook/packages/paybook-packages.yml
  title: ''
  type: Packages
  url: packages/paybook-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.paybook.com/en/article/terms-of-use-183zl4u/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.paybook.com/en/article/privacy-and-security-policy-k33bgf/
- group: docs
  title: ''
  type: Documentation
  url: https://help.paybook.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paybook
- group: auth
  href: https://artifacts.apis.io/paybook/security/paybook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paybook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paybook.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.paybook.com/en/about
- group: operate
  title: ''
  type: HelpCenter
  url: https://paybook.crisp.help/
- group: start
  title: ''
  type: Login
  url: https://www.paybook.com/w/en/paybook/login
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://api.crisp.help/mcp/v1
  - status: null
    url: https://paybook.crisp.help/mcp/v1
  - status: 200
    url: https://paybook.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Paybook provides a financial data aggregation platform that enables businesses and developers to access, normalize, and analyze banking, credit card, and other financial account information through a unified API. By connecting to thousands of financial institutions worldwide, Paybook simplifies account verification, transaction retrieval, balance checks, and categorization, supporting use cases such as personal finance apps, lending platforms, and accounting software. The service emphasizes security, compliance with banking regulations, and robust developer tooling, offering sandbox environments, detailed documentation, and SDKs for rapid integration.
image: https://www.paybook.com/assets/site-paybook/images/paybook-social.jpg
layout: provider
modified: '2026-10-21'
name: Paybook
nav: Providers
network: true
overview: 'Paybook is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Data Aggregation, and Banking.


  Paybook''s developer surface includes documentation and 12 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 39.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/paybook/paybook-2026-11-03T141014.png
security:
- kind: domain-security
  name: Paybook Domain Security
  slug: paybook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paybook
tags:
- Company
- Fintech
- Data Aggregation
- Banking
website: https://paybook.com/
---
