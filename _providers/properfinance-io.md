---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
api_count: 1
apis:
- description: Automated Reconciliation and Financial Operations Platform
  name: Proper API
  slug: properfinance-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/properfinance-io/hosts/properfinance-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/properfinance-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/properfinance-io/vendors/properfinance-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/properfinance-io-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.properfinance.io/
- group: auth
  href: https://artifacts.apis.io/properfinance-io/security/properfinance-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/properfinance-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.properfinance.io/
- group: company
  title: ''
  type: Blog
  url: https://www.properfinance.io/blog
- group: auth
  title: ''
  type: Security
  url: https://www.properfinance.io/platform/security
- group: start
  title: ''
  type: GettingStarted
  url: https://www.properfinance.io/platform/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://www.properfinance.io/platform/security
- group: other
  title: ''
  type: SignIn
  url: https://app.properfinance.io
coverage:
  checked: '2026-10-29'
  detail: The provider's website offers no public API documentation or machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.properfinance.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Proper provides a modern financial data platform that automates reconciliation, streamlines accounting processes, and offers a suite of products including Reconciliation, Exception Management, Connections, Financial Data Platform, and Ledgers. The platform simplifies financial data integration for businesses and offers product guides and API reference for developers.
image: https://cdn.prod.website-files.com/61b259caf730d7d8455895a1/642db0ee5fe941124de69405_home%20open%20graph%201.png
layout: provider
modified: '2026-10-28'
name: Proper
nav: Providers
network: true
overview: 'Proper is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Reconciliation, Platform, and Software-as-a-Service.


  Proper''s developer surface includes documentation, engineering blog, getting-started guide, support, and 6 more developer resources.'
random_paper: 17
scopes:
- name: Properfinance Io Scopes
  scope_count: 0
  slug: properfinance-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/properfinance-io/properfinance-io-2026-11-03T141628.png
security:
- kind: authentication
  name: Properfinance Io Authentication
  slug: properfinance-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Properfinance Io Domain Security
  slug: properfinance-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: properfinance-io
tags:
- Finance
- Reconciliation
- Platform
- Software-as-a-Service
website: https://www.properfinance.io/
---
