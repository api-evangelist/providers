---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Energy Transfer Agentic Access
  operation_count: 4
  slug: energy-transfer-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://dev.messenger.energytransfer.com
  baseurl_source: declared
  description: Manage gas pipeline nominations.
  name: Energy Transfer Nominations API
  slug: energy-transfer-nominations-api
- baseURL: https://dev.messenger.energytransfer.com
  baseurl_source: declared
  description: Retrieve pipeline information and status.
  name: Energy Transfer Pipelines API
  slug: energy-transfer-pipelines-api
- baseURL: https://dev.messenger.energytransfer.com
  baseurl_source: declared
  description: Access gas scheduling and capacity data.
  name: Energy Transfer Schedules API
  slug: energy-transfer-schedules-api
artifact_total: 14
collections:
- collection_type: open
  name: Energy Transfer Messenger+ API
  slug: open-energy-transfer-messenger-api
- collection_type: open
  name: Energy Transfer Messenger+ Nominations API
  slug: open-energy-transfer-nominations-api
- collection_type: open
  name: Energy Transfer Messenger+ Nominations Pipelines API
  slug: open-energy-transfer-pipelines-api
- collection_type: open
  name: Energy Transfer Messenger+ Nominations Schedules API
  slug: open-energy-transfer-schedules-api
common:
- group: other
  href: https://artifacts.apis.io/energy-transfer/capabilities/energy-transfer-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/energy-transfer-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/energy-transfer/plans/energy-transfer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/energy-transfer-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/energy-transfer/rate-limits/energy-transfer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/energy-transfer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/energy-transfer/finops/energy-transfer-finops.yml
  title: ''
  type: FinOps
  url: finops/energy-transfer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.energytransfer.com/news/
- group: company
  title: ''
  type: Website
  url: https://energytransfer.com
- group: agent
  href: https://artifacts.apis.io/energy-transfer/agentic-access/energy-transfer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/energy-transfer-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/energy-transfer/security/energy-transfer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/energy-transfer-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/energy-transfer/authentication/energy-transfer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/energy-transfer-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energy-transfer
created: '2026-03-21'
description: Energy Transfer is one of the largest and most diversified midstream energy companies in North America, owning and operating natural gas, crude oil, NGL, and refined products pipelines, terminals, and storage facilities.
finops:
- has_sources: true
  method: generated
  name: Energy Transfer Finops
  primary_unit: ''
  service_category: Pipeline & Midstream Services
  slug: energy-transfer-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-transfer.png
layout: provider
modified: '2026-10-06'
name: Energy Transfer
nav: Providers
network: true
overview: 'Energy Transfer publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Nominations API, Pipelines API, and Schedules API. Tagged areas include Energy, Pipelines, Midstream, Gas Scheduling, and Fortune 100.


  The Energy Transfer catalog on APIs.io includes 1 Spectral governance ruleset.


  Energy Transfer''s developer surface includes engineering blog, authentication, and 8 more developer resources.'
plans:
- name: Energy Transfer Plans Pricing
  plan_count: 1
  slug: energy-transfer-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Energy Transfer Rate Limits
  slug: energy-transfer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Energy Transfer API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: energy-transfer-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 44.7
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 24.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/energy-transfer/energy-transfer-2026-06-20T180705.png
security:
- kind: authentication
  name: Energy Transfer Authentication
  slug: energy-transfer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Energy Transfer Domain Security
  slug: energy-transfer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: energy-transfer
tags:
- Energy
- Pipelines
- Midstream
- Gas Scheduling
- Fortune 100
- Oil and Gas
website: https://energytransfer.com
---
