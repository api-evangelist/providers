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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Bondaval trade credit insurance platform
  name: Trade Credit Insurance API
  slug: trade-credit-insurance-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bondaval/refs/heads/main/hosts/bondaval-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bondaval-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bondaval/refs/heads/main/security/bondaval-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bondaval-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bondaval.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.bondaval.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://bondaval.com/company/who-we-are
- group: docs
  title: ''
  type: APIReference
  url: https://bondaval.com/product/trade-credit-insurance
- group: start
  title: ''
  type: GettingStarted
  url: https://bondaval.com/product/trade-credit-insurance
- group: operate
  title: ''
  type: Support
  url: https://bondaval.com/contact
- group: company
  title: ''
  type: Blog
  url: https://bondaval.com/company/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bondaval.com/privacy-policy
coverage:
  checked: '2026-10-02'
  detail: API documentation pages return HTML shells and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://app.bondaval.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Bondaval provides technology-enabled trade credit insurance and risk management solutions. It combines market-leading credit insurance with a software platform, BondavalOS, that monitors buyer exposure, flags policy breaches, and offers dynamic risk insights. Backed by Swiss Re and an international panel of insurers, Bondaval serves businesses worldwide, helping them secure non‑cancellable, S&P AA‑rated coverage while reducing reliance on traditional collateral.
layout: provider
modified: '2026-10-02'
name: Bondaval
nav: Providers
network: true
overview: 'Bondaval publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Fintech, Trade Credit, and Risk Management.


  Bondaval''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 5 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bondaval Domain Security
  slug: bondaval-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bondaval
tags:
- Company
- Insurance
- Fintech
- Trade Credit
- Risk Management
website: https://bondaval.com
---
