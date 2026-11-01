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
api_count: 1
apis:
- description: 'Dispel API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: Dispel API
  slug: dispel-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/dispel/rules/dispel-rules.yml
  title: ''
  type: Spectral
  url: rules/dispel-rules.yml
- group: design
  href: https://artifacts.apis.io/dispel/vocabulary/dispel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dispel-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/dispel/changelog/dispel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dispel-changelog.yml
- group: design
  href: https://artifacts.apis.io/dispel/conformance/dispel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dispel-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dispel/llms/dispel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dispel-llms.txt
- group: auth
  href: https://artifacts.apis.io/dispel/well-known/dispel-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dispel-status-security.txt
- group: auth
  href: https://artifacts.apis.io/dispel/well-known/dispel-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dispel-help-security.txt
- group: agent
  href: https://artifacts.apis.io/dispel/well-known/dispel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dispel-well-known.yml
- group: other
  href: https://artifacts.apis.io/dispel/hosts/dispel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dispel-hosts.yml
- group: other
  href: https://artifacts.apis.io/dispel/vendors/dispel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dispel-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dispel.com/
- group: auth
  title: ''
  type: Security
  url: https://dispel.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.dispel.com/policies/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://dispel.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dispel.com/reference/wicket-tunnel-encryption
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dispel.com/get-started/getting-started-with-dispel
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dispel
- group: auth
  href: https://artifacts.apis.io/dispel/security/dispel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dispel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dispel.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.dispel.io/en/
- group: company
  title: ''
  type: Blog
  url: https://dispel.com/blog
coverage:
  checked: '2026-10-23'
  detail: Main website renders content via JavaScript, preventing machine‑readable discovery of API specs.
  evidence:
  - status: 200
    url: https://dispel.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Dispel provides OT‑secure remote access solutions for industrial operations, enabling vendors, OEMs and operators to connect to critical systems and data without legacy complexity or delays. Their platform offers zero‑trust networking, secure remote access, data streaming, and compliance tools across manufacturing, utilities, energy, automotive, chemical, and other sectors. Trusted by industry leaders, Dispel helps organizations accelerate digital transformation while protecting operational technology from cyber threats.
image: https://framerusercontent.com/assets/fC9G6lEZJUIa7EiWlirsNYODY.png
layout: provider
modified: '2026-10-23'
name: Dispel
nav: Providers
network: true
overview: 'Dispel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OT Security, Industrial IoT, Zero Trust, Remote Access, and Data Streaming.


  The Dispel catalog on APIs.io includes 1 Spectral governance ruleset.


  Dispel''s developer surface includes changelog, API reference, getting-started guide, documentation, engineering blog, and 16 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Dispel API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dispel-rules
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 9.7
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dispel Domain Security
  slug: dispel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dispel
tags:
- OT Security
- Industrial IoT
- Zero Trust
- Remote Access
- Data Streaming
website: https://dispel.com
---
