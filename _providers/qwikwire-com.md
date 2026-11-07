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
api_count: 1
apis:
- description: Access API for payment processing and transaction monitoring.
  name: Aqwire Payments API
  slug: aqwire-payments-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://aqwire.co/
- group: other
  href: https://artifacts.apis.io/qwikwire-com/hosts/qwikwire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qwikwire-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aqwire.co/news/index.html
- group: auth
  href: https://artifacts.apis.io/qwikwire-com/security/qwikwire-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/qwikwire-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/qwikwire-com/security/qwikwire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qwikwire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aqwire.co
created: '2026-10-25'
description: Aqwire provides a seamless payments platform for enterprises and payers, offering billing, transaction monitoring, auto‑debit enrollments, and multi‑currency support worldwide. Their Access API enables secure, flexible payment processing for apps, while a robust dashboard gives real‑time insight into transactions. Aqwire’s services target large enterprises needing comprehensive payment management and integration capabilities.
layout: provider
modified: '2026-10-25'
name: Qwikwire
nav: Providers
network: true
overview: Qwikwire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, and Enterprise.
random_paper: 23
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 7.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 7.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/qwikwire-com/qwikwire-com-2026-11-03T141847.png
security:
- kind: domain-security
  name: Qwikwire Com Domain Security
  slug: qwikwire-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Qwikwire Com Trust Center
  slug: qwikwire-com-trust-center
  summary_line: PCI DSS
slug: qwikwire-com
tags:
- Company
- Payments
- Fintech
- Enterprise
website: https://aqwire.co
---
