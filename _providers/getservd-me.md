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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Servd MCP (Machine Control Protocol) API for managing venues and AI ordering.
  name: Servd MCP
  slug: servd-mcp
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/getservd-me/cli/getservd-me-cli.yml
  title: ''
  type: CLI
  url: cli/getservd-me-cli.yml
- group: operate
  href: https://artifacts.apis.io/getservd-me/changelog/getservd-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getservd-me-changelog.yml
- group: design
  href: https://artifacts.apis.io/getservd-me/conformance/getservd-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getservd-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getservd-me/llms/getservd-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getservd-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/getservd-me/well-known/getservd-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getservd-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/getservd-me/hosts/getservd-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getservd-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/getservd-me/vendors/getservd-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getservd-me-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://getservd.me/en/changelog
- group: auth
  href: https://artifacts.apis.io/getservd-me/security/getservd-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getservd-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getservd.me/
- group: docs
  title: ''
  type: Documentation
  url: https://getservd.me/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.getservd.me/
- group: docs
  title: ''
  type: APIReference
  url: https://getservd.me/en/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://getservd.me/en/why-servd
- group: operate
  title: ''
  type: Support
  url: https://getservd.me/en/help
- group: company
  title: ''
  type: Blog
  url: https://getservd.me/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getservd.me/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getservd.me/en/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.getservd.me/signup
coverage:
  checked: '2026-10-30'
  detail: The MCP API reference page provides HTML documentation but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://getservd.me/en/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Servd (getservd.me) is a food commerce platform that enables restaurants and food businesses to create online ordering pages, manage menus, process payments, and integrate with various sales channels. The service offers tools for quick setup, menu bulk uploads, AI ordering, and a unified dashboard for operations, payments, and analytics. It targets small cafés to multi-location groups, providing a single platform to replace multiple subscriptions.
image: https://getservd.me/og-en.png
layout: provider
modified: '2026-10-30'
name: getservd-me
nav: Providers
network: true
overview: 'getservd-me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FoodTech, Commerce, SaaS, and Restaurants.


  getservd-me''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getservd Me Domain Security
  slug: getservd-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getservd-me
tags:
- Company
- FoodTech
- Commerce
- SaaS
- Restaurants
website: https://getservd.me/
---
