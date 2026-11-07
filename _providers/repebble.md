---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pebble is an open platform. It's easy to develop on Pebble. Our SDK is available for free and includes iOS and Android libraries.
  name: Pebble Developer API
  slug: pebble-developer-api
artifact_total: 6
common:
- group: build
  href: https://artifacts.apis.io/repebble/cli/repebble-cli.yml
  title: ''
  type: CLI
  url: cli/repebble-cli.yml
- group: operate
  href: https://artifacts.apis.io/repebble/changelog/repebble-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/repebble-changelog.yml
- group: agent
  href: https://artifacts.apis.io/repebble/llms/repebble-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/repebble-llms.txt
- group: agent
  href: https://artifacts.apis.io/repebble/well-known/repebble-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/repebble-well-known.yml
- group: other
  href: https://artifacts.apis.io/repebble/hosts/repebble-hosts.yml
  title: ''
  type: Hosts
  url: hosts/repebble-hosts.yml
- group: other
  href: https://artifacts.apis.io/repebble/vendors/repebble-vendors.yml
  title: ''
  type: Vendors
  url: vendors/repebble-vendors.yml
- group: build
  href: https://artifacts.apis.io/repebble/packages/repebble-packages.yml
  title: ''
  type: SDKs
  url: packages/repebble-packages.yml
- group: build
  href: https://artifacts.apis.io/repebble/packages/repebble-packages.yml
  title: ''
  type: Packages
  url: packages/repebble-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.repebble.com
- group: auth
  href: https://artifacts.apis.io/repebble/security/repebble-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/repebble-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://repebble.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.repebble.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.repebble.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.repebble.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.repebble.com/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://repebble.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pebble
- group: start
  title: ''
  type: SignUp
  url: https://repebble.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://repebble.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://repebble.com/privacy
coverage:
  checked: '2026-10-29'
  detail: Developer portal provides HTML documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://developer.repebble.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Pebble smartwatch designs and sells e-paper smartwatches and a smart ring, offering long battery life, always‑on displays, and a developer ecosystem. The official store provides pre‑order options for Pebble Time 2, Pebble Round 2, and the Pebble Index 01 ring, while the developer portal offers SDKs, tutorials, and API references for building watchfaces and apps. Core Devices LLC, the company behind Pebble, maintains a blog with product updates and a terms of service and privacy policy governing user data.
image: https://repebble.com/pebble-logo-red.png
layout: provider
modified: '2026-10-28'
name: Pebble smartwatch
nav: Providers
network: true
overview: 'Pebble smartwatch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smartwatch, Wearables, IoT, and Hardware.


  Pebble smartwatch''s developer surface includes CLI, changelog, support, documentation, API reference, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Repebble Plans Pricing
  plan_count: 0
  slug: repebble-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Repebble Rate Limits
  slug: repebble-rate-limits
scopes:
- name: Repebble Scopes
  scope_count: 0
  slug: repebble-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 36.9
    discoverability: 64.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/repebble/repebble-2026-11-03T142151.png
security:
- kind: authentication
  name: Repebble Authentication
  slug: repebble-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Repebble Domain Security
  slug: repebble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: repebble
tags:
- Company
- Smartwatch
- Wearables
- IoT
- Hardware
- Consumer
website: https://repebble.com/
---
