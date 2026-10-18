---
agent_readiness:
  band: human-only
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer portal for Espressif APIs and SDKs.
  name: Espressif Developer Portal
  slug: espressif-developer-portal
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/espressif/refs/heads/main/authentication/espressif-authentication.yml
  title: ''
  type: Authentication
  url: authentication/espressif-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/espressif/refs/heads/main/conformance/espressif-conformance.yml
  title: ''
  type: Conformance
  url: conformance/espressif-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/espressif/refs/heads/main/hosts/espressif-hosts.yml
  title: ''
  type: Hosts
  url: hosts/espressif-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/espressif/refs/heads/main/vendors/espressif-vendors.yml
  title: ''
  type: Vendors
  url: vendors/espressif-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/espressif/refs/heads/main/packages/espressif-packages.yml
  title: ''
  type: Packages
  url: packages/espressif-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.espressif.com/en/content/terms-use
- group: operate
  title: ''
  type: Support
  url: https://www.espressif.com/en/support/services
- group: operate
  title: ''
  type: StatusPage
  url: https://status.espressif.com/status/public
- group: start
  title: ''
  type: SignUp
  url: https://www.espressif.com/en/devcon/register
- group: build
  title: ''
  type: SDKs
  url: https://www.espressif.com/en/sdks/esp-zephyr
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.espressif.com/en/content/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.espressif.com/en/company/newsroom/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/espressif
- group: company
  title: ''
  type: Blog
  url: https://blog.espressif.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agents.espressif.com/docs/get-started/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://developer.espressif.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agents.espressif.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/espressif/refs/heads/main/security/espressif-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/espressif-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.espressif.com
coverage:
  checked: '2026-10-13'
  detail: Developer portal provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://developer.espressif.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Espressif Systems designs and sells wireless system‑on‑chips (SoCs), modules, development kits and related hardware for AIoT applications. It also provides software development kits, cloud services such as ESP RainMaker, and AI solutions for developers and device manufacturers building connected products.
layout: provider
modified: '2026-10-13'
name: Espressif Systems
nav: Providers
network: true
overview: 'Espressif Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SoCs, Modules, Development Kits, IoT, and AIoT.


  Espressif Systems'' developer surface includes authentication, support, signup flow, engineering blog, getting-started guide, documentation, API reference, and 12 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 55.4
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Espressif Authentication
  slug: espressif-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Espressif Domain Security
  slug: espressif-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: espressif
tags:
- SoCs
- Modules
- Development Kits
- IoT
- AIoT
- Cloud Platform
- Wireless Connectivity
- SDK
website: https://www.espressif.com
---
