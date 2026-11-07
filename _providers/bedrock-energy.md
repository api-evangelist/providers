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
  href: https://artifacts.apis.io/bedrock-energy/hosts/bedrock-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bedrock-energy-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bedrockenergy.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/bedrock-energy/security/bedrock-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bedrock-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bedrockenergy.com
coverage:
  checked: '2026-09-27'
  detail: OpenAPI spec endpoints returned 404 on both primary hosts.
  evidence:
  - status: 404
    url: https://bedrockenergy.com/openapi.json
  - status: 404
    url: https://api.bedrockenergy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bedrock Energy provides innovative geothermal heating and cooling solutions for residential and commercial properties. Leveraging proprietary drilling technology and advanced data algorithms, the company enables fast, cost-effective borehole installations that deliver high-efficiency, resilient energy performance. Their mission is to make geothermal energy affordable and accessible, reducing energy costs and environmental impact for building owners across the United States.
layout: provider
modified: '2026-09-27'
name: Bedrock Energy
nav: Providers
network: true
overview: Bedrock Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geothermal, Energy, HVAC, and Cleantech.
random_paper: 9
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 5.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bedrock-energy/bedrock-energy-2026-10-11T101725.png
security:
- kind: domain-security
  name: Bedrock Energy Domain Security
  slug: bedrock-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bedrock-energy
tags:
- Company
- Geothermal
- Energy
- HVAC
- Cleantech
website: https://bedrockenergy.com
---
