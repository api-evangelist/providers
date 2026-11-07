---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides access to Netatmo smart‑home device data and settings as described in the developer portal.
  name: Netatmo API
  slug: netatmo-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/netatmo/hosts/netatmo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netatmo-hosts.yml
- group: other
  href: https://artifacts.apis.io/netatmo/vendors/netatmo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netatmo-vendors.yml
- group: build
  href: https://artifacts.apis.io/netatmo/packages/netatmo-packages.yml
  title: ''
  type: SDKs
  url: packages/netatmo-packages.yml
- group: build
  href: https://artifacts.apis.io/netatmo/packages/netatmo-packages.yml
  title: ''
  type: Packages
  url: packages/netatmo-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.netatmo.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.netatmo.com/press
- group: start
  title: ''
  type: Login
  url: https://www.netatmo.com/cs-cz/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netatmo
- group: auth
  href: https://artifacts.apis.io/netatmo/security/netatmo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netatmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netatmo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.netatmo.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.netatmo.com/
coverage:
  checked: '2026-10-28'
  detail: Developer portal provides documentation but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 404
    url: https://api.netatmo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Netatmo designs and manufactures smart home devices such as weather stations, security cameras, and smart thermostats. Their products connect to the Netatmo Connect platform, offering APIs for accessing device data, managing settings, and integrating with third‑party services. The company provides a developer portal with documentation, authentication guides, and SDKs for building applications that leverage their smart‑home ecosystem.
image: https://www.netatmo.com/_nuxt/logo-netatmo_og_padded.omDV0Q7W.jpg
layout: provider
modified: '2026-10-28'
name: Netatmo
nav: Providers
network: true
overview: 'Netatmo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, IoT, and Devices.


  Netatmo''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 58.0
    operational_transparency: 7.9
  previous_composite: 13.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/netatmo/netatmo-2026-11-03T140118.png
security:
- kind: domain-security
  name: Netatmo Domain Security
  slug: netatmo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: netatmo
tags:
- Company
- Smart Home
- IoT
- Devices
website: https://netatmo.com/
---
