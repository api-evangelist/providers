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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference not publicly available; site renders JavaScript shell with no machine‑readable docs.
  name: FTN Network API
  slug: ftn-network-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ftnnetwork-com/hosts/ftnnetwork-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ftnnetwork-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ftnnetwork-com/security/ftnnetwork-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ftnnetwork-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ftnnetwork.com/
coverage:
  checked: '2026-10-29'
  detail: Landing page renders a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://ftnnetwork.com/lander
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: FTN Network is a technology company focused on providing secure, high‑performance networking solutions for enterprises and service providers. Founded with backing from Techstars, the company offers a suite of APIs that enable customers to manage network devices, monitor traffic, and integrate with third‑party services. Their platform emphasizes scalability, reliability, and compliance with industry standards, aiming to simplify complex network operations for developers and IT teams.
layout: provider
modified: '2026-10-29'
name: FTN Network
nav: Providers
network: true
overview: FTN Network is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Networking, Enterprise, and Security.
random_paper: 6
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 4.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ftnnetwork Com Domain Security
  slug: ftnnetwork-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ftnnetwork-com
tags:
- Company
- Technology
- Networking
- Enterprise
- Security
website: https://ftnnetwork.com/
---
