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
- description: Financial data aggregation API providing access to account, transaction, and other financial data.
  name: Sophtron API
  slug: sophtron-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/sophtron/hosts/sophtron-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sophtron-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sophtron.com/
- group: start
  title: ''
  type: SignUp
  url: https://sophtron.com/account/register
- group: auth
  title: ''
  type: Security
  url: https://sophtron.com/security
- group: company
  title: ''
  type: Blog
  url: https://blog.sophtron.com/
- group: auth
  href: https://artifacts.apis.io/sophtron/security/sophtron-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sophtron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sophtron.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sophtron.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sophtron.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sophtron.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sophtron
- group: commercial
  title: ''
  type: Pricing
  url: https://sophtron.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sophtron.com/developerAgreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sophtron.com/home/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@sophtron.com
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation site https://docs.sophtron.com/ does not publish any machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://docs.sophtron.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Sophtron provides a data aggregation platform that connects to financial institutions, enabling developers to retrieve account, transaction, and other financial data via APIs. The service supports connections to thousands of banks and credit cards across the United States and Canada, offering structured data for fintech applications, payroll, insurance, utilities, and more. Sophtron emphasizes security and compliance, offering SOC 2 certification and a developer-friendly API.
image: https://sophtron.com/_nuxt/img/Logo_White_1.f124f75.png
layout: provider
modified: '2026-10-28'
name: Sophtron
nav: Providers
network: true
overview: 'Sophtron is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Data Aggregation, Banking, and Financial Services.


  Sophtron''s developer surface includes signup flow, engineering blog, documentation, API reference, pricing, support, and 9 more developer resources.'
random_paper: 5
scopes:
- name: Sophtron Scopes
  scope_count: 0
  slug: sophtron-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 15.8
  previous_composite: 26.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sophtron/sophtron-2026-11-03T143539.png
security:
- kind: authentication
  name: Sophtron Authentication
  slug: sophtron-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sophtron Domain Security
  slug: sophtron-domain-security
  summary_line: TLSv1.3
slug: sophtron
tags:
- Fintech
- Data Aggregation
- Banking
- Financial Services
website: https://sophtron.com/
---
