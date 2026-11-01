---
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Opsee provides a manufacturing execution system API documented at the Reference page.
  name: Opsee API
  slug: opsee-api-2
- description: 'Opsee API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Opsee API
  slug: opsee-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/opsee/rules/opsee-rules.yml
  title: ''
  type: Spectral
  url: rules/opsee-rules.yml
- group: design
  href: https://artifacts.apis.io/opsee/vocabulary/opsee-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opsee-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/opsee/conformance/opsee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opsee-conformance.yml
- group: other
  href: https://artifacts.apis.io/opsee/hosts/opsee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opsee-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opsee.io/docs/Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opsee.io/docs/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://dev.opsee.io/
- group: auth
  href: https://artifacts.apis.io/opsee/security/opsee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opsee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opsee.io
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.opsee.io/docs/Reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Opsee provides an open, modular manufacturing execution system (MES) and industrial data platform for factories. It offers data logging, historian, analytics, OEE, quality, production order management, and AI-driven insights. The platform is container‑based, open‑source, and designed for plant‑floor operators, allowing incremental module adoption without vendor lock‑in.
image: https://opsee.io/dashboard-oee.png
layout: provider
modified: '2026-10-29'
name: Opsee
nav: Providers
network: true
overview: 'Opsee is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, MES, IndustrialIoT, OpenSource, and DataAnalytics.


  The Opsee catalog on APIs.io includes 1 Spectral governance ruleset.


  Opsee''s developer surface includes API reference, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Opsee API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: opsee-rules
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 9.4
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Opsee Domain Security
  slug: opsee-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opsee
tags:
- Manufacturing
- MES
- IndustrialIoT
- OpenSource
- DataAnalytics
website: https://opsee.io
---
