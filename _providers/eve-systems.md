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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/eve-systems/hosts/eve-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eve-systems-hosts.yml
- group: other
  href: https://artifacts.apis.io/eve-systems/vendors/eve-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eve-systems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evehome.com/en/installationsservice/terms
- group: auth
  title: ''
  type: Security
  url: https://www.evehome.com/en/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.evehome.com/en/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evehome
- group: auth
  href: https://artifacts.apis.io/eve-systems/security/eve-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eve-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evehome.com/
- group: company
  title: ''
  type: Blog
  url: https://www.evehome.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://www.evehome.com/en/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evehome.com/en/privacy
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: failed
    url: https://api.evehome.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Eve Systems designs and manufactures smart home devices that integrate with Apple HomeKit, providing users with intuitive control over heating, lighting, and energy consumption. Their product line includes smart thermostats, radiator valves, smart plugs, and sensors, all managed through the Eve app and supporting Matter standards. The company emphasizes energy efficiency, user-friendly design, and seamless automation across a connected home ecosystem.
image: https://www.evehome.com/sites/default/files/social_media/Open_Graph_Eve.jpg
layout: provider
modified: '2026-10-28'
name: Eve Systems
nav: Providers
network: true
overview: 'Eve Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, HomeKit, IoT, and Energy.


  Eve Systems'' developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 49.1
    operational_transparency: 7.9
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/eve-systems/eve-systems-2026-11-03T131652.png
security:
- kind: domain-security
  name: Eve Systems Domain Security
  slug: eve-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eve-systems
tags:
- Company
- Smart Home
- HomeKit
- IoT
- Energy
- Automation
website: https://evehome.com/
---
