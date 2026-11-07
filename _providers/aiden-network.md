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
api_count: 1
apis:
- description: API for AIDEN identity and reputation services
  name: AIDEN API
  slug: aiden-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/aiden-network/conventions/aiden-network-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aiden-network-conventions.yml
- group: other
  href: https://artifacts.apis.io/aiden-network/hosts/aiden-network-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiden-network-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiden-network/vendors/aiden-network-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiden-network-vendors.yml
- group: build
  href: https://artifacts.apis.io/aiden-network/packages/aiden-network-packages.yml
  title: ''
  type: SDKs
  url: packages/aiden-network-packages.yml
- group: build
  href: https://artifacts.apis.io/aiden-network/packages/aiden-network-packages.yml
  title: ''
  type: Packages
  url: packages/aiden-network-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiden.network/terms
- group: auth
  title: ''
  type: Security
  url: https://aiden.network/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiden.network/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://aiden.network/docs
- group: auth
  href: https://artifacts.apis.io/aiden-network/security/aiden-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiden-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiden.network/
coverage:
  checked: '2026-11-01'
  detail: The provider's documentation at https://aiden.network/docs contains human‑readable API information but no published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://aiden.network/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AIDEN provides identity and reputation infrastructure for AI agents on the Robinhood Chain. It implements the open ERC‑8004 standard, offering permanent on‑chain identities, score‑based reputation, and trust‑screening APIs. The platform enables developers to register agents, query reputation, and integrate trust checks into AI‑driven services, leveraging public blockchain data for transparent, auditable trust.
image: https://aiden.network/brand/og/aiden-og.png
layout: provider
modified: '2026-11-01'
name: AIDEN
nav: Providers
network: true
overview: 'AIDEN is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Artificial Intelligence, Blockchain, Trust, and ERC-8004.


  AIDEN''s developer surface includes getting-started guide and 10 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 14.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiden Network Domain Security
  slug: aiden-network-domain-security
  summary_line: TLSv1.3
slug: aiden-network
tags:
- Identity
- Artificial Intelligence
- Blockchain
- Trust
- ERC-8004
- Agents
website: https://aiden.network/
---
