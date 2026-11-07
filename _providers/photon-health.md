---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.photon.health'', ''status'': 307, ''note'': ''declared website redirects to https://photonhealth.com/ — a different registrable domain (photon.health -> photonhealth.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Photon Health Agentic Access
  operation_count: 1
  slug: photon-health-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.photon.health/graphql
  baseurl_source: declared
  description: The Graph QL API from Photon Health — 1 operation(s) for graph ql.
  name: Photon Health Graph QL API
  slug: photon-health-graph-ql-api
artifact_total: 11
collections:
- collection_type: open
  name: Photon Health Clinical GraphQL API
  slug: open-photon-health-graphql-api
- collection_type: open
  name: Photon Health Clinical API
  slug: open-photon-health
common:
- group: agent
  href: https://artifacts.apis.io/photon-health/agentic-access/photon-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/photon-health-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/photon-health/security/photon-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/photon-health-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/photon-health/authentication/photon-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/photon-health-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Photon-Health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/photon-health
- group: company
  title: ''
  type: Website
  url: https://www.photon.health
- group: docs
  title: ''
  type: Documentation
  url: https://docs.photon.health
- group: commercial
  href: https://artifacts.apis.io/photon-health/plans/photon-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/photon-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/photon-health/rate-limits/photon-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/photon-health-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/photon-health/finops/photon-health-finops.yml
  title: ''
  type: FinOps
  url: finops/photon-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://photonhealth.com/blog
created: '2026-06-21'
description: Photon Health is a modern e-prescribing (eRx) platform that lets digital-health organizations create patients, write prescriptions, route orders to pharmacies, and manage fulfillment through a single GraphQL Clinical API. The platform pairs the API with embeddable Elements UI components, webhooks, and a transparent prescription marketplace for pharmacy price and fulfillment comparison.
finops:
- has_sources: true
  method: generated
  name: Photon Health Finops
  primary_unit: ''
  service_category: Healthcare and Life Sciences
  slug: photon-health-finops
  template: false
graphqls:
- description: GraphQL schema for the [Photon Health](https://www.photon.health) Clinical API — a modern
  name: Photon Health GraphQL API
  slug: photon-health-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/photon-health.png
layout: provider
modified: '2026-06-21'
name: Photon Health
nav: Providers
network: true
overview: 'Photon Health publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Health, e-Prescribing, eRx, Prescriptions, and Pharmacy.


  The Photon Health catalog on APIs.io includes 1 Spectral governance ruleset.


  Photon Health''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Photon Health Plans Pricing
  plan_count: 2
  slug: photon-health-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Photon Health Rate Limits
  slug: photon-health-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Photon Health API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: photon-health-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 55.7
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/photon-health/photon-health-2026-09-02T151156.png
security:
- kind: authentication
  name: Photon Health Authentication
  slug: photon-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Photon Health Domain Security
  slug: photon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: photon-health
tags:
- Health
- e-Prescribing
- eRx
- Prescriptions
- Pharmacy
- GraphQL
website: https://www.photon.health
---
