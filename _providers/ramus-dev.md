---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Ramus cloud Android emulators
  name: Ramus API
  slug: ramus-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/ramus-dev/plans/ramus-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ramus-dev-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/ramus-dev/cli/ramus-dev-cli.yml
  title: ''
  type: CLI
  url: cli/ramus-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/ramus-dev/changelog/ramus-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ramus-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/ramus-dev/authentication/ramus-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ramus-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/ramus-dev/errors/ramus-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ramus-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/ramus-dev/llms/ramus-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ramus-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/ramus-dev/well-known/ramus-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ramus-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/ramus-dev/hosts/ramus-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ramus-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ramus-dev/vendors/ramus-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ramus-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/ramus-dev/packages/ramus-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/ramus-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/ramus-dev/packages/ramus-dev-packages.yml
  title: ''
  type: Packages
  url: packages/ramus-dev-packages.yml
- group: start
  title: ''
  type: Login
  url: https://ramus.dev/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://ramus.dev/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://ramus.dev/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/ramus-dev/security/ramus-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ramus-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ramus.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://ramus.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ramus.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ramus.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ramus.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://ramus.dev/blog
coverage:
  checked: '2026-10-31'
  detail: API endpoints require authentication and return 401 without credentials.
  evidence:
  - status: 401
    url: https://api.ramus.dev/api/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Ramus provides cloud‑based Android emulators that let developers upload APKs and run them directly in the browser. The platform supports free testing, sharing live links for QA, previewing pull requests, and integrates with coding agents such as Claude Code, Cursor and Codex. It also offers iOS emulation (waitlist) and a public API at api.ramus.dev.
image: https://ramus.dev/social-card.png
layout: provider
modified: '2026-10-31'
name: ramus-dev
nav: Providers
network: true
overview: 'ramus-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Android, Emulator, Cloud, DeveloperTools, and API.


  ramus-dev''s developer surface includes CLI, changelog, authentication, getting-started guide, documentation, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Ramus Dev Plans Pricing
  plan_count: 3
  slug: ramus-dev-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ramus Dev Rate Limits
  slug: ramus-dev-rate-limits
scopes:
- name: Ramus Dev Scopes
  scope_count: 0
  slug: ramus-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ramus Dev Authentication
  slug: ramus-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ramus Dev Domain Security
  slug: ramus-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ramus-dev
tags:
- Android
- Emulator
- Cloud
- DeveloperTools
- API
website: https://ramus.dev/
---
