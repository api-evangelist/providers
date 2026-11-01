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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://vrmapi.victronenergy.com/v2
  baseurl_source: declared
  description: API for Victron Energy's VRM platform providing system monitoring and management endpoints.
  name: VRM API
  slug: vrm-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/victron-energy/security/victron-energy-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/victron-energy-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/victron-energy/conformance/victron-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/victron-energy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/victron-energy/llms/victron-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/victron-energy-llms.txt
- group: auth
  href: https://artifacts.apis.io/victron-energy/well-known/victron-energy-victronenergy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/victron-energy-victronenergy-security.txt
- group: auth
  href: https://artifacts.apis.io/victron-energy/well-known/victron-energy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/victron-energy-security.txt
- group: agent
  href: https://artifacts.apis.io/victron-energy/well-known/victron-energy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/victron-energy-well-known.yml
- group: other
  href: https://artifacts.apis.io/victron-energy/hosts/victron-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/victron-energy-hosts.yml
- group: build
  href: https://artifacts.apis.io/victron-energy/packages/victron-energy-packages.yml
  title: ''
  type: SDKs
  url: packages/victron-energy-packages.yml
- group: build
  href: https://artifacts.apis.io/victron-energy/packages/victron-energy-packages.yml
  title: ''
  type: Packages
  url: packages/victron-energy-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.victronenergy.com/p/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.victronenergy.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.victronenergy.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://vrm-api-docs.victronenergy.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/victronenergy
- group: auth
  href: https://artifacts.apis.io/victron-energy/security/victron-energy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/victron-energy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/victron-energy/security/victron-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/victron-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://victronenergy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.victronenergy.com/support-and-downloads/software
- group: start
  title: ''
  type: GettingStarted
  url: https://www.victronenergy.com/this-is-victron
- group: operate
  title: ''
  type: Support
  url: https://www.victronenergy.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.victronenergy.com/blog
created: '2026-10-28'
description: Victron Energy designs and manufactures power conversion and storage solutions for off‑grid, marine, recreational, and professional applications. Their product range includes inverters, battery monitors, solar chargers, and remote monitoring platforms, enabling reliable energy systems worldwide. The company also offers the VRM portal for system monitoring and management, supporting a broad ecosystem of renewable energy installations.
layout: provider
modified: '2026-10-28'
name: Victron Energy (VRM)
nav: Providers
network: true
overview: 'Victron Energy (VRM) is listed with 1 API on the [APIs.io](https://apis.io/) network: VRM API. Tagged areas include Company, Energy, Renewable, Off-grid, and Monitoring.


  Victron Energy (VRM)''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, and 16 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 34.4
    developer_ergonomics: 42.9
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Victron Energy Domain Security
  slug: victron-energy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Victron Energy Vulnerability Disclosure
  slug: victron-energy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: victron-energy
tags:
- Company
- Energy
- Renewable
- Off-grid
- Monitoring
website: https://victronenergy.com/
---
