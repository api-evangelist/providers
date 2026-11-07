---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Uptime Kuma API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Uptime Kuma API
  slug: uptime-kuma-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/uptime-kuma/rules/uptime-kuma-rules.yml
  title: ''
  type: Spectral
  url: rules/uptime-kuma-rules.yml
- group: design
  href: https://artifacts.apis.io/uptime-kuma/vocabulary/uptime-kuma-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/uptime-kuma-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/uptime-kuma/authentication/uptime-kuma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uptime-kuma-authentication.yml
- group: design
  href: https://artifacts.apis.io/uptime-kuma/conformance/uptime-kuma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uptime-kuma-conformance.yml
- group: other
  href: https://artifacts.apis.io/uptime-kuma/hosts/uptime-kuma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uptime-kuma-hosts.yml
- group: other
  href: https://artifacts.apis.io/uptime-kuma/vendors/uptime-kuma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uptime-kuma-vendors.yml
- group: build
  href: https://artifacts.apis.io/uptime-kuma/packages/uptime-kuma-packages.yml
  title: ''
  type: SDKs
  url: packages/uptime-kuma-packages.yml
- group: build
  href: https://artifacts.apis.io/uptime-kuma/packages/uptime-kuma-packages.yml
  title: ''
  type: Packages
  url: packages/uptime-kuma-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kuma.pet/
- group: auth
  href: https://artifacts.apis.io/uptime-kuma/security/uptime-kuma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uptime-kuma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uptime.kuma.pet/
- group: docs
  title: ''
  type: Documentation
  url: https://uptime.kuma.pet/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://uptime.kuma.pet/docs/How-to-Install
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/louislam/uptime-kuma
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://uptime.kuma.pet/docs/Internal-API
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Uptime Kuma is an open-source, self‑hosted monitoring tool that provides a modern dashboard for tracking the uptime of websites, services, and servers. It supports HTTP(s), TCP, ping, DNS, and Docker container monitoring, offering real‑time alerts, customizable notifications, and a responsive UI. The project is maintained by the community and can be deployed via Docker or directly on a server, making it suitable for individuals and organizations seeking a flexible, privacy‑focused monitoring solution.
layout: provider
modified: '2026-10-28'
name: Uptime Kuma
nav: Providers
network: true
overview: 'Uptime Kuma is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, Self-Hosted, Open Source, Dashboards, and Alerts.


  The Uptime Kuma catalog on APIs.io includes 1 Spectral governance ruleset.


  Uptime Kuma''s developer surface includes authentication, documentation, getting-started guide, and 11 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Uptime Kuma API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: uptime-kuma-rules
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 29.8
    discoverability: 53.6
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/uptime-kuma/uptime-kuma-2026-11-03T145518.png
security:
- kind: authentication
  name: Uptime Kuma Authentication
  slug: uptime-kuma-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Uptime Kuma Domain Security
  slug: uptime-kuma-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: uptime-kuma
tags:
- Monitoring
- Self-Hosted
- Open Source
- Dashboards
- Alerts
website: https://uptime.kuma.pet/
---
