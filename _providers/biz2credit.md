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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biz2credit/refs/heads/main/hosts/biz2credit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biz2credit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biz2credit/refs/heads/main/vendors/biz2credit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biz2credit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.biz2credit.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.biz2credit.com/privacy-policy.html
- group: start
  title: ''
  type: Login
  url: https://app.biz2credit.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biz2credit/refs/heads/main/security/biz2credit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biz2credit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biz2credit.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://forgeglobal.com/biz2credit_stock/
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Biz2Credit provides online business financing solutions, offering term loans, revenue‑based financing, lines of credit, and commercial real‑estate loans to small and medium‑sized enterprises. Their platform enables fast approval, a knowledge center with guides and webinars, and tools for financial calculations, helping businesses secure the capital they need to grow.
layout: provider
modified: '2026-09-28'
name: Biz2Credit
nav: Providers
network: true
overview: Biz2Credit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Lending, Small Business, Online Loans, and Credit.
random_paper: 20
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biz2Credit Domain Security
  slug: biz2credit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biz2credit
tags:
- Finance
- Lending
- Small Business
- Online Loans
- Credit
website: https://www.biz2credit.com
---
