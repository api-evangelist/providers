---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Access to Dynamik Orbits developer agents.
  name: Dynamik Orbits API
  slug: dynamik-orbits-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dynamikorbits-com/plans/dynamikorbits-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynamikorbits-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dynamikorbits-com/llms/dynamikorbits-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynamikorbits-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dynamikorbits-com/well-known/dynamikorbits-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dynamikorbits-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dynamikorbits-com/hosts/dynamikorbits-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynamikorbits-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynamikorbits.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynamikorbits.com/privacy
- group: auth
  href: https://artifacts.apis.io/dynamikorbits-com/security/dynamikorbits-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamikorbits-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dynamikorbits.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dynamikorbits.com/pricing
- group: other
  title: ''
  type: Data
  url: https://www.dynamikorbits.com/data
- group: other
  title: ''
  type: Research
  url: https://www.dynamikorbits.com/research
- group: company
  title: ''
  type: About
  url: https://www.dynamikorbits.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://www.dynamikorbits.com/developers/agents
- group: agent
  title: ''
  type: LLMs
  url: https://www.dynamikorbits.com/llms.txt
coverage:
  checked: '2026-11-06'
  detail: Developer portal provides HTML docs but no machine‑readable OpenAPI, GraphQL or AsyncAPI specifications.
  evidence:
  - status: 200
    url: https://www.dynamikorbits.com/developers/agents
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Dynamik Orbits provides a platform for visualizing and analyzing space systems. It offers ground stations on real terrain, integrates data from every active satellite via CelesTrak, supports constellation modeling, cloud cover analysis, and FCC beam footprints. The service is free to start and targets engineers building space applications.
image: https://www.dynamikorbits.com/og-image.png
layout: provider
modified: '2026-11-06'
name: Dynamik Orbits
nav: Providers
network: true
overview: 'Dynamik Orbits is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Space, Satellite, Ground Station, Visualization, and Engineering.


  Dynamik Orbits'' developer surface includes pricing, API reference, and 12 more developer resources.'
plans:
- name: Dynamikorbits Com Plans Pricing
  plan_count: 2
  slug: dynamikorbits-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dynamikorbits Com Domain Security
  slug: dynamikorbits-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dynamikorbits-com
tags:
- Space
- Satellite
- Ground Station
- Visualization
- Engineering
website: https://www.dynamikorbits.com/
---
