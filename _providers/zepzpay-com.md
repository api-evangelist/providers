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
  href: https://artifacts.apis.io/zepzpay-com/hosts/zepzpay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zepzpay-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/zepzpay-com/security/zepzpay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zepzpay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zepzpay.com/
- group: company
  title: ''
  type: Blog
  url: https://zepz.io/news-and-insights/
coverage:
  checked: '2026-10-22'
  detail: No machine‑readable API specification was found on the provider's documented developer portal.
  evidence:
  - status: 404
    url: https://zepz.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Zepz provides a modern payments platform that enables businesses to embed banking, card issuing, and money movement capabilities directly into their products. The company offers APIs for account creation, transfers, payouts, and compliance, supporting both B2B and B2C use cases. Backed by Accel and other investors, Zepz aims to simplify financial services integration, reduce friction, and accelerate time‑to‑market for fintech innovators worldwide.
layout: provider
modified: '2026-10-21'
name: Zepz
nav: Providers
network: true
overview: 'Zepz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, and Banking.


  Zepz''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 1.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 2.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zepzpay-com/zepzpay-com-2026-11-03T150505.png
security:
- kind: domain-security
  name: Zepzpay Com Domain Security
  slug: zepzpay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zepzpay-com
tags:
- Company
- Payments
- Fintech
- Banking
website: https://zepzpay.com/
---
