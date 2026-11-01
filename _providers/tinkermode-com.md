---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The MODE Platform API provides endpoints for managing users, devices, and data.
  name: MODE API
  slug: mode-api
- baseURL: https://api.tinkermode.com
  baseurl_source: declared
  description: 'Mode API as documented publicly: 239 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Mode API
  slug: tinkermode-com-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/tinkermode-com/rate-limits/tinkermode-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tinkermode-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tinkermode-com/rules/tinkermode-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tinkermode-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tinkermode-com/vocabulary/tinkermode-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tinkermode-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/tinkermode-com/authentication/tinkermode-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tinkermode-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/tinkermode-com/conformance/tinkermode-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tinkermode-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/tinkermode-com/well-known/tinkermode-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tinkermode-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/tinkermode-com/well-known/tinkermode-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tinkermode-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/tinkermode-com/hosts/tinkermode-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tinkermode-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tinkermode-com/vendors/tinkermode-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tinkermode-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://console.tinkermode.com/console/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.tinkermode.com/mode-api/reference/users
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tinkermode.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tinkermode
- group: auth
  href: https://artifacts.apis.io/tinkermode-com/security/tinkermode-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tinkermode-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tinkermode.com
coverage:
  checked: '2026-10-29'
  detail: Docs provide request examples but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://dev.tinkermode.com/mode-api/reference/users/get-all-users
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Mode BizStack turns sensors, cameras, and legacy systems into one AI-ready data layer — the foundation for AI workers across construction and industrial sites. BizStack AI workers use camera and operational data to take on the repetitive field work—reviewing what happened, then starting and tracking the right next action. Field operations rely on people to notice what happened, find the relevant information, decide who needs to act, and follow up until the work is done. That work is important—but much of it is repetitive, slow, and easy to miss.
image: https://www.tinkermode.com/assets/images/footer-logo.svg
layout: provider
modified: '2026-10-29'
name: Mode
nav: Providers
network: true
overview: 'Mode is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Data-Platform, Industrial, Construction, and Operations.


  The Mode catalog on APIs.io includes 1 Spectral governance ruleset.


  Mode''s developer surface includes authentication, sandbox, API reference, documentation, and 11 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 5
  name: Tinkermode Com Rate Limits
  slug: tinkermode-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Mode API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: tinkermode-com-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 8.9
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tinkermode Com Authentication
  slug: tinkermode-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tinkermode Com Domain Security
  slug: tinkermode-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tinkermode-com
tags:
- AI
- Data-Platform
- Industrial
- Construction
- Operations
- Company
website: https://tinkermode.com
---
