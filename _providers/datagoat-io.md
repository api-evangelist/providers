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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/datagoat-io/hosts/datagoat-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datagoat-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/datagoat-io/vendors/datagoat-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datagoat-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.datagoat.io/sign-in
- group: auth
  href: https://artifacts.apis.io/datagoat-io/security/datagoat-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datagoat-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datagoat.io/
coverage:
  checked: '2026-11-05'
  detail: No machine‑readable API specification was found on the provider's website.
  evidence:
  - status: 200
    url: https://www.datagoat.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Data Goat provides an AI‑augmented decision platform that learns from a company’s historical outcomes and compares them with AI predictions. It offers agents that connect to existing codebases, surface small business decisions, and deliver signed receipts for each recommendation, enabling better, auditable choices without altering the code.
layout: provider
modified: '2026-11-04'
name: Data Goat
nav: Providers
network: true
overview: Data Goat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Decisions, Software-as-a-Service, and Analytics.
random_paper: 18
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datagoat Io Domain Security
  slug: datagoat-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: datagoat-io
tags:
- Company
- Artificial Intelligence
- Decisions
- Software-as-a-Service
- Analytics
website: https://datagoat.io/
---
