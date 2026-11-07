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
- group: agent
  href: https://artifacts.apis.io/airplus/llms/airplus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airplus-llms.txt
- group: other
  href: https://artifacts.apis.io/airplus/hosts/airplus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airplus-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.airplus.com/en-de/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airplus.com/da-dk/om-airplus/lov-og-sikkerhed/privacy-notice/
- group: start
  title: ''
  type: Login
  url: https://airplus.com/en-de/log-in/
- group: company
  title: ''
  type: Blog
  url: https://comms.airplus.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airplus
- group: auth
  href: https://artifacts.apis.io/airplus/security/airplus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airplus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airplus.com/
coverage:
  checked: '2026-10-27'
  detail: The public website provides no machine‑readable API specification or developer documentation.
  evidence:
  - status: 200
    url: https://airplus.com/en-de/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: AirPlus International provides smooth, simple, and secure business payment solutions that simplify workflows, reduce complexity, and bring harmony to financial flows for corporate clients. Their platform offers virtual and physical corporate cards, expense management, and integration capabilities for enterprises.
layout: provider
modified: '2026-10-26'
name: AirPlus International
nav: Providers
network: true
overview: 'AirPlus International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Corporate Cards, Expense Management, and Fintech.


  AirPlus International''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 51.8
    operational_transparency: 2.6
  previous_composite: 10.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 7.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/airplus/airplus-2026-11-03T120534.png
security:
- kind: domain-security
  name: Airplus Domain Security
  slug: airplus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airplus
tags:
- Company
- Payments
- Corporate Cards
- Expense Management
- Fintech
website: https://www.airplus.com/
---
