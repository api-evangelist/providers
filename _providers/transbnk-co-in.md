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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/transbnk-co-in/hosts/transbnk-co-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transbnk-co-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/transbnk-co-in/vendors/transbnk-co-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transbnk-co-in-vendors.yml
- group: auth
  href: https://artifacts.apis.io/transbnk-co-in/security/transbnk-co-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transbnk-co-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tbx.co.in/
coverage:
  checked: '2026-10-25'
  detail: The documentation site renders content via JavaScript, providing no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.tbx.co.in/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: TBX (formerly TransBnk) provides corporate banking infrastructure, enabling banks and enterprises to manage financial operations across treasury, payments, collections, reconciliation, APIs and banking workflows. The platform offers a suite of APIs for payments, cash management, and financial data integration, targeting corporate clients seeking streamlined treasury solutions.
image: https://www.tbx.co.in/logo-new.png
layout: provider
modified: '2026-10-25'
name: Transbnk
nav: Providers
network: true
overview: Transbnk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Treasury, Payments, and API.
random_paper: 14
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Transbnk Co In Domain Security
  slug: transbnk-co-in-domain-security
  summary_line: TLSv1.3 · DMARC
slug: transbnk-co-in
tags:
- Company
- Banking
- Treasury
- Payments
- API
website: https://www.tbx.co.in/
---
