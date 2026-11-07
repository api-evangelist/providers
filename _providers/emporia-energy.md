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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for accessing energy data and device control
  name: Emporia Energy API
  slug: emporia-energy-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/emporia-energy/llms/emporia-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emporia-energy-llms.txt
- group: auth
  href: https://artifacts.apis.io/emporia-energy/well-known/emporia-energy-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/emporia-energy-help-security.txt
- group: agent
  href: https://artifacts.apis.io/emporia-energy/well-known/emporia-energy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/emporia-energy-well-known.yml
- group: other
  href: https://artifacts.apis.io/emporia-energy/hosts/emporia-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emporia-energy-hosts.yml
- group: other
  href: https://artifacts.apis.io/emporia-energy/vendors/emporia-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emporia-energy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.emporiaenergy.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.emporiaenergy.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emporiaenergy.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.emporiaenergy.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.emporiaenergy.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.emporiaenergy.com/en/articles/13226219-getting-started-with-the-emporia-app
- group: docs
  title: ''
  type: Documentation
  url: https://help.emporiaenergy.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emporiaenergy
- group: auth
  href: https://artifacts.apis.io/emporia-energy/security/emporia-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emporia-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.emporiaenergy.com
coverage:
  checked: '2026-10-14'
  detail: Documentation is available but no OpenAPI, GraphQL schema, or other machine‑readable contract could be retrieved.
  evidence:
  - status: 200
    url: https://shop.emporiaenergy.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Emporia Energy provides smart energy monitoring and management solutions for residential and commercial customers. Their platform offers real-time electricity usage data, device control, and insights to help users reduce consumption and save on utility bills. Through a robust API, developers can integrate energy data, control smart devices, and build applications that promote energy efficiency and sustainability across the IoT ecosystem.
image: https://www.emporiaenergy.com/assets/images/home/house.jpg.webp
layout: provider
modified: '2026-10-13'
name: Emporia Energy
nav: Providers
network: true
overview: 'Emporia Energy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Smart Home, IoT, and Monitoring.


  Emporia Energy''s developer surface includes support, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 65.2
    operational_transparency: 13.2
  previous_composite: 18.3
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
screenshot: https://apis.io/screenshots/emporia-energy/emporia-energy-2026-11-03T131505.png
security:
- kind: domain-security
  name: Emporia Energy Domain Security
  slug: emporia-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: emporia-energy
tags:
- Company
- Energy
- Smart Home
- IoT
- Monitoring
website: https://www.emporiaenergy.com
---
