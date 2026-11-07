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
  href: https://artifacts.apis.io/bbvaapimarket/hosts/bbvaapimarket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bbvaapimarket-hosts.yml
- group: other
  href: https://artifacts.apis.io/bbvaapimarket/vendors/bbvaapimarket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bbvaapimarket-vendors.yml
- group: build
  href: https://artifacts.apis.io/bbvaapimarket/packages/bbvaapimarket-packages.yml
  title: ''
  type: SDKs
  url: packages/bbvaapimarket-packages.yml
- group: build
  href: https://artifacts.apis.io/bbvaapimarket/packages/bbvaapimarket-packages.yml
  title: ''
  type: Packages
  url: packages/bbvaapimarket-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bbvaapimarket.com/en/security/
- group: auth
  href: https://artifacts.apis.io/bbvaapimarket/security/bbvaapimarket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bbvaapimarket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bbvaapimarket.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bbvaapimarket.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bbvaapimarket.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://www.bbvaapimarket.com/en/banking-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bbvaapimarket.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.bbvaapimarket.com/en/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bbvaapimarket.com/en/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bbvaapimarket.com/en/personal-data/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://www.bbvaapimarket.com/mcp
  - status: 200
    url: https://bbvaapimarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: BBVA API_Market is the open banking platform of BBVA, offering a comprehensive suite of APIs that enable businesses to integrate financial services, create digital ecosystems, and comply with regulations such as PSD2. The platform provides APIs for treasury management, digital ecosystems, regulatory compliance, and a variety of payment services across multiple countries, fostering innovation, digital transformation, and new business models for enterprises worldwide.
layout: provider
modified: '2026-10-20'
name: BBVA
nav: Providers
network: true
overview: 'BBVA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Banking, Finance, Payments, and API Platform.


  BBVA''s developer surface includes documentation, API reference, getting-started guide, support, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 44.6
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.6
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bbvaapimarket/bbvaapimarket-2026-11-03T121617.png
security:
- kind: domain-security
  name: Bbvaapimarket Domain Security
  slug: bbvaapimarket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bbvaapimarket
tags:
- Company
- Open Banking
- Finance
- Payments
- API Platform
website: https://bbvaapimarket.com/
---
