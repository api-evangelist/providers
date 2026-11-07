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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer portal providing API information and resources for Thames Water.
  name: Developer Services
  slug: developer-services
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/thames-water/hosts/thames-water-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thames-water-hosts.yml
- group: build
  href: https://artifacts.apis.io/thames-water/packages/thames-water-packages.yml
  title: ''
  type: SDKs
  url: packages/thames-water-packages.yml
- group: build
  href: https://artifacts.apis.io/thames-water/packages/thames-water-packages.yml
  title: ''
  type: Packages
  url: packages/thames-water-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thameswater.co.uk/legal/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.thameswater.co.uk/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thameswater.co.uk/legal/privacy-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thameswater.co.uk/news/2024/jul/price-review-24-response
- group: company
  title: ''
  type: Newsroom
  url: https://www.thameswater.co.uk/news/2025/may/lsws
- group: start
  title: ''
  type: Login
  url: https://www.thameswater.co.uk/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.thameswater.co.uk/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.thameswater.co.uk/developers/nav-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThamesWater
- group: auth
  href: https://artifacts.apis.io/thames-water/security/thames-water-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thames-water-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thameswater.co.uk
coverage:
  checked: '2026-10-13'
  detail: The developer portal provides information but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.thameswater.co.uk/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Thames Water is the UK’s largest water and wastewater company, serving 16 million customers across London and the Thames Valley. It provides water supply, wastewater treatment, and related services, focusing on sustainability, community, and environmental stewardship.
layout: provider
modified: '2026-10-13'
name: Thames Water
nav: Providers
network: true
overview: 'Thames Water is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Water, Wastewater, Utilities, Billing, and Customer Service.


  Thames Water''s developer surface includes support, pricing, getting-started guide, and 11 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 54.5
    operational_transparency: 2.6
  previous_composite: 21.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thames-water/thames-water-2026-11-03T144527.png
security:
- kind: domain-security
  name: Thames Water Domain Security
  slug: thames-water-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thames-water
tags:
- Water
- Wastewater
- Utilities
- Billing
- Customer Service
- Business Services
- Property Searches
website: https://www.thameswater.co.uk
---
