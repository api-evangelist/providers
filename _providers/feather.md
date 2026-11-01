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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: SDK package providing programmatic access to Feather robot functions.
  name: Feather SDK API
  slug: feather-sdk-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/feather/cli/feather-cli.yml
  title: ''
  type: CLI
  url: cli/feather-cli.yml
- group: operate
  href: https://artifacts.apis.io/feather/changelog/feather-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/feather-changelog.yml
- group: design
  href: https://artifacts.apis.io/feather/lifecycle/feather-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/feather-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/feather/hosts/feather-hosts.yml
  title: ''
  type: Hosts
  url: hosts/feather-hosts.yml
- group: other
  href: https://artifacts.apis.io/feather/vendors/feather-vendors.yml
  title: ''
  type: Vendors
  url: vendors/feather-vendors.yml
- group: build
  href: https://artifacts.apis.io/feather/packages/feather-packages.yml
  title: ''
  type: SDKs
  url: packages/feather-packages.yml
- group: build
  href: https://artifacts.apis.io/feather/packages/feather-packages.yml
  title: ''
  type: Packages
  url: packages/feather-packages.yml
- group: auth
  href: https://artifacts.apis.io/feather/security/feather-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/feather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://feather.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.feather.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://feather.dev/docs/feather-spec-sheet.pdf
- group: docs
  title: ''
  type: APIReference
  url: https://docs.feather.dev/api/feathersdk.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.feather.dev/
- group: operate
  title: ''
  type: Support
  url: https://feather.dev/support
- group: commercial
  title: ''
  type: Pricing
  url: https://feather.dev/
coverage:
  checked: '2026-10-29'
  detail: No public API contract was found; attempts to fetch OpenAPI spec at https://api.feather.dev/openapi.json returned 404.
  evidence:
  - status: 404
    url: https://api.feather.dev/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Feather Robotics builds a bimanual, mobile humanoid robot platform for physical AI applications. The open‑hardware robot offers 23 degrees of freedom, hot‑swappable batteries, and an open SDK in Python and C++ for rapid development. Targeted at manufacturing, food service, and research, Feather ships ready‑to‑run units starting at $29,990, with enterprise pricing for fleets. The company provides US‑based support, extensive documentation, and a developer portal for integration.
image: https://feather.dev/icon.svg?icon=2oe1zdvz-8cn5.svg
layout: provider
modified: '2026-10-29'
name: Feather
nav: Providers
network: true
overview: 'Feather is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Hardware, AI, and Automation.


  Feather''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, pricing, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Feather Authentication
  slug: feather-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Feather Domain Security
  slug: feather-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: feather
tags:
- Company
- Robotics
- Hardware
- AI
- Automation
- Manufacturing
website: https://feather.dev/
---
