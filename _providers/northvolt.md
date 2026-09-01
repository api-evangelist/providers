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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/lyten/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northvolt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://northvolt.com/
- group: company
  title: ''
  type: About
  url: https://northvolt.com/about/
- group: company
  title: ''
  type: Blog
  url: https://northvolt.com/news/
- group: company
  title: ''
  type: PressRoom
  url: https://northvolt.com/press-resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/northvolt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://northvolt.com/articles/privacy/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://northvolt.com/articles/code-of-conduct/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/northvolt_stock/
- group: build
  title: ''
  type: Packages
  url: packages/northvolt-packages.yml
- group: auth
  title: ''
  type: Security
  url: security/northvolt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/northvolt-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/northvolt-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/northvolt-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Northvolt AB filed for bankruptcy on 12 March 2025 and its Swedish, German and Polish assets were sold to Lyten during 2025; northvolt.com is now a frozen Gatsby archive whose latest news item is dated 30 January 2025, and api.northvolt.com -- the only host the company ever named that looks like an API host -- still resolves to a CloudFront distribution but returns HTTP 502 "Failed to contact the origin" on every path.
  evidence:
  - status: 502
    url: https://api.northvolt.com/openapi.json
  - status: 502
    url: https://api.northvolt.com/
  - status: 200
    url: https://northvolt.com/news/
  reason: defunct
  state: none
created: '2026-08-26'
description: Northvolt AB is a Swedish lithium-ion battery developer and manufacturer, founded in Stockholm in 2016, that built and operated the Northvolt Ett gigafactory in Skelleftea and the Northvolt Labs R&D and qualification campus in Vasteras, with further sites in Heide (Germany), Gdansk (Poland) and Montreal (Canada). Its product line covered lithium-ion, sodium-ion and lithium-metal cells, the Voltpack Core and Voltpack Mobile System battery energy storage systems, the Revolt battery recycling operation, and a Connected Battery telemetry and fleet-management service. Northvolt AB filed for bankruptcy in Sweden on 12 March 2025; through 2025 its remaining assets in Sweden, Germany and Poland were acquired by Lyten. The company never published a public developer program, API reference or machine-readable API contract; its only named developer-facing surface, api.northvolt.com, no longer has a reachable origin.
image: https://northvolt.com/icons/icon-512x512.png
layout: provider
modified: '2026-08-26'
name: Northvolt
nav: Providers
network: true
overview: 'Northvolt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Batteries, Energy Storage, Manufacturing, and Electric Vehicles.


  Northvolt''s developer surface includes engineering blog and 14 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Northvolt Domain Security
  slug: northvolt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Northvolt Vulnerability Disclosure
  slug: northvolt-vulnerability-disclosure
  summary_line: disclosure policy published
slug: northvolt
tags:
- Company
- Batteries
- Energy Storage
- Manufacturing
- Electric Vehicles
- Recycling
- Sustainability
- Industrial
- Energy
- Sweden
website: https://northvolt.com/
---
