---
access_model:
  confidence: low
  gated: private
  gated_source:
  - x-api-posture
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digitaliron.com/
- group: commercial
  href: https://artifacts.apis.io/digital-iron/plans/digital-iron-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digital-iron-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.digitaliron.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.digitaliron.com/
- group: operate
  title: ''
  type: Support
  url: https://www.digitaliron.com/contact/
- group: start
  title: ''
  type: Login
  url: https://platform.digitaliron.ai/login
- group: agent
  href: https://artifacts.apis.io/digital-iron/llms/digital-iron-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digital-iron-llms.txt
- group: auth
  href: https://artifacts.apis.io/digital-iron/security/digital-iron-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digital-iron-domain-security.yml
created: '2026-07-17'
description: Digital Iron is an AI platform delivering aftersales intelligence for heavy machinery. It helps equipment dealers and OEMs turn scattered service data — machine history, product documentation, customer records, bills of materials, work orders, and technician notes — into faster troubleshooting, accurate parts identification, and reliable job quoting. The platform surfaces recurring failure patterns across fleets (excavators, crushers, compaction rollers, and similar equipment) to improve first-time fix rates. Digital Iron is backed by Seedcamp and tracked in the API Evangelist network as a portfolio company; the product is delivered as a hosted web application and no public API has been identified to date.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digital-iron.png
layout: provider
modified: '2026-10-06'
name: Digital Iron
nav: Providers
network: true
overview: 'Digital Iron is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Heavy Machinery, Aftersales, and Field Service Management.


  Digital Iron''s developer surface includes pricing, support, and 6 more developer resources.'
plans:
- name: Digital Iron Plans Pricing
  plan_count: 1
  slug: digital-iron-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/digital-iron/digital-iron-2026-07-25T212015.png
security:
- kind: domain-security
  name: Digital Iron Domain Security
  slug: digital-iron-domain-security
  summary_line: TLSv1.3 · DMARC
slug: digital-iron
tags:
- Company
- Artificial Intelligence
- Heavy Machinery
- Aftersales
- Field Service Management
- Equipment Dealers
- OEM
- Service Data
website: https://www.digitaliron.com/
---
