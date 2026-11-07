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
  name: North Cloud Agentic Access
  operation_count: 2
  slug: north-cloud-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.north.cloud
  baseurl_source: declared
  description: Manage and retrieve cost unit metric data.
  name: North.Cloud Cost Units API
  slug: north-cloud-cost-units-api
artifact_total: 10
collections:
- collection_type: open
  name: North.Cloud Public Cost Units API
  slug: open-north-cloud-cost-units-api
- collection_type: open
  name: North.Cloud Public API
  slug: open-north-cloud
common:
- group: commercial
  href: https://artifacts.apis.io/north-cloud/plans/north-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/north-cloud-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/north-cloud/rate-limits/north-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/north-cloud-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/north-cloud/finops/north-cloud-finops.yml
  title: ''
  type: FinOps
  url: finops/north-cloud-finops.yml
- group: other
  href: https://artifacts.apis.io/north-cloud/capabilities/north-cloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/north-cloud-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/north-cloud/agentic-access/north-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/north-cloud-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/north-cloud/security/north-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/north-cloud-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/north-cloud/authentication/north-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/north-cloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northcld
- group: company
  title: ''
  type: Website
  url: https://www.north.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.north.cloud/
- group: other
  title: ''
  type: Application
  url: https://app.north.cloud/
- group: auth
  title: ''
  type: Security
  url: https://docs.north.cloud/security
- group: company
  title: ''
  type: Blog
  url: https://www.north.cloud/blog
created: '2026-01-02'
description: North.Cloud delivers real-time savings, automated FinOps, and dynamic optimization across AWS and GCP. The platform's public API enables programmatic ingestion and retrieval of cost unit data so teams can integrate unit economics, allocation, and chargeback reporting into their own systems.
finops:
- has_sources: false
  method: generated
  name: North Cloud Finops
  primary_unit: request
  service_category: API
  slug: north-cloud-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/north-cloud.png
layout: provider
modified: '2026-05-19'
name: North.Cloud
nav: Providers
network: true
overview: 'North.Cloud publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Cost Units API. Tagged areas include FinOps, Cloud Cost Management, Amazon Web Services, GCP, and Cost Optimization.


  The North.Cloud catalog on APIs.io includes 1 Spectral governance ruleset.


  North.Cloud''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: North Cloud Plans Pricing
  plan_count: 3
  slug: north-cloud-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: North Cloud Rate Limits
  slug: north-cloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: North.Cloud API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: north-cloud-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 53.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/north-cloud/north-cloud-2026-06-20T190412.png
security:
- kind: authentication
  name: North Cloud Authentication
  slug: north-cloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: North Cloud Domain Security
  slug: north-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: north-cloud
tags:
- FinOps
- Cloud Cost Management
- Amazon Web Services
- GCP
- Cost Optimization
- Cost Units
website: https://www.north.cloud/
---
