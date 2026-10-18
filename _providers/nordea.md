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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nordea/refs/heads/main/hosts/nordea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nordea-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nordea/refs/heads/main/vendors/nordea-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nordea-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nordea.com/en/terms-and-conditions-trade
- group: operate
  title: ''
  type: Support
  url: https://www.nordea.com/en/our-services/cash-management/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nordea.com/en/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nordea.com/en/doc/price-list-for-account-holding-banks-2026.pdf
- group: company
  title: ''
  type: Newsroom
  url: https://www.nordea.com/en/media/15019
- group: start
  title: ''
  type: Login
  url: https://www.nordea.com/en/log-in
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordea/refs/heads/main/security/nordea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nordea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordea.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://nordea.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Nordea is a leading Nordic universal bank offering a wide range of financial services including retail banking, corporate banking, asset management, and investment solutions across the Nordic region. The bank focuses on digital transformation and provides various APIs for account information, payments, and financial data to enable seamless integration for developers and partners.
image: https://www.nordea.com/sites/default/files/styles/olivero_hero/public/2024-05/top-banner-test-1.jpg.webp?itok=glXlPnGU
layout: provider
modified: '2026-10-14'
name: Nordea
nav: Providers
network: true
overview: 'Nordea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Finance, and Nordic.


  Nordea''s developer surface includes support, pricing, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 41.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nordea Domain Security
  slug: nordea-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: nordea
tags:
- Company
- Banking
- Finance
- Nordic
website: https://nordea.com/
---
