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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for the Shaarli bookmarking service.
  name: Shaarli API
  slug: shaarli-api-2
- description: 'Shaarli API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Shaarli API
  slug: shaarli-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/shaarli/rules/shaarli-rules.yml
  title: ''
  type: Spectral
  url: rules/shaarli-rules.yml
- group: design
  href: https://artifacts.apis.io/shaarli/vocabulary/shaarli-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shaarli-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/shaarli/changelog/shaarli-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shaarli-changelog.yml
- group: auth
  href: https://artifacts.apis.io/shaarli/authentication/shaarli-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shaarli-authentication.yml
- group: design
  href: https://artifacts.apis.io/shaarli/errors/shaarli-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shaarli-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shaarli/conformance/shaarli-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shaarli-conformance.yml
- group: other
  href: https://artifacts.apis.io/shaarli/hosts/shaarli-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shaarli-hosts.yml
- group: other
  href: https://artifacts.apis.io/shaarli/vendors/shaarli-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shaarli-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://demo.shaarli.org/login
- group: auth
  href: https://artifacts.apis.io/shaarli/security/shaarli-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shaarli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demo.shaarli.org
- group: docs
  title: ''
  type: Documentation
  url: https://shaarli.readthedocs.io
- group: docs
  title: ''
  type: APIReference
  url: https://shaarli.readthedocs.io/en/latest/REST-API.html
- group: start
  title: ''
  type: GettingStarted
  url: https://shaarli.readthedocs.io/en/latest/Installation.html
- group: operate
  title: ''
  type: Support
  url: https://github.com/shaarli/Shaarli/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shaarli
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found; only HTML docs and API requires authentication (401) on /api/v1/info.
  evidence:
  - status: 503
    url: https://api.shaarli.org/openapi.json
  - status: 404
    url: https://demo.shaarli.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Shaarli is an open‑source, self‑hosted bookmarking service that lets users store, tag, and share web links. Designed for personal use, it is minimalist, fast, and requires no database, using flat‑file storage instead. The project provides a web interface, a public demo instance, and a REST API for programmatic access. It is written in PHP, released under the MIT license, and can be deployed via Docker or traditional web servers. The community maintains documentation on Read the Docs and offers a client library ecosystem.
image: https://raw.githubusercontent.com/shaarli/Shaarli/master/doc/md/images/doc-logo.png
layout: provider
modified: '2026-10-28'
name: Shaarli
nav: Providers
network: true
overview: 'Shaarli is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bookmarking, Self-Hosted, Open Source, PHP, and Minimalist.


  The Shaarli catalog on APIs.io includes 1 Spectral governance ruleset.


  Shaarli''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, and 10 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Shaarli API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: shaarli-rules
scopes:
- name: Shaarli Scopes
  scope_count: 0
  slug: shaarli-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.8
  provenance:
    conformance: first-party
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/shaarli/shaarli-2026-11-03T143102.png
security:
- kind: authentication
  name: Shaarli Authentication
  slug: shaarli-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shaarli Domain Security
  slug: shaarli-domain-security
  summary_line: TLSv1.3 · HSTS
slug: shaarli
tags:
- Bookmarking
- Self-Hosted
- Open Source
- PHP
- Minimalist
website: https://demo.shaarli.org
---
