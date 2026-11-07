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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/cyrebro/well-known/cyrebro-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cyrebro-status-security.txt
- group: agent
  href: https://artifacts.apis.io/cyrebro/well-known/cyrebro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cyrebro-well-known.yml
- group: other
  href: https://artifacts.apis.io/cyrebro/hosts/cyrebro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyrebro-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyrebro/vendors/cyrebro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyrebro-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cyrebro.io/terms-and-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cyrebro.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyrebro.io/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cyrebro.io/media
- group: start
  title: ''
  type: Login
  url: https://partners.cyrebro.io/s/login/?language=en_US&ec=302&startURL=%2Fs%2F
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CYREBRO
- group: auth
  href: https://artifacts.apis.io/cyrebro/security/cyrebro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyrebro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cyrebro.io
coverage:
  checked: '2026-10-22'
  detail: No public developer program or API documentation is available on cyrebro.com.
  evidence:
  - status: 200
    url: https://cyrebro.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Cyrebro provides a Hyper‑SIEM autonomous security operations platform for managed service providers and MSSPs. It ingests telemetry from hundreds of vendors, auto‑triages alerts, and runs agentic investigations, delivering verdicts in seconds with minimal human interaction. The solution aims to replace legacy SIEMs with an AI‑driven, end‑to‑end SOC operating system.
layout: provider
modified: '2026-10-21'
name: Cyrebro
nav: Providers
network: true
overview: Cyrebro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, SOC, Artificial Intelligence, Managed Service, and SIEM.
random_paper: 14
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 21.1
  previous_composite: 16.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cyrebro/cyrebro-2026-11-03T125956.png
security:
- kind: domain-security
  name: Cyrebro Domain Security
  slug: cyrebro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cyrebro
tags:
- Security
- SOC
- Artificial Intelligence
- Managed Service
- SIEM
- Automation
website: https://www.cyrebro.io
---
