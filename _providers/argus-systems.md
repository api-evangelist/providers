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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/argus-systems/hosts/argus-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/argus-systems-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.argus.systems/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://argus.systems/privacy-policy
- group: auth
  href: https://artifacts.apis.io/argus-systems/security/argus-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/argus-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://argus.systems
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://argus.systems
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Argus builds AI-powered solutions for real‑world systems, delivering intelligent analytics, automation, and decision‑making tools for enterprises. Their platform integrates machine‑learning models into IoT and industrial workflows, helping customers optimize operations and unlock new value from data.
layout: provider
modified: '2026-10-26'
name: Argus
nav: Providers
network: true
overview: Argus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Analytics, Automation, and IoT.
random_paper: 15
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
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
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Argus Systems Domain Security
  slug: argus-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argus-systems
tags:
- Company
- AI
- Analytics
- Automation
- IoT
- Enterprise
website: https://argus.systems
---
