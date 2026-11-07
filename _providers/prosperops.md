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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ProsperOps provides autonomous cloud cost optimization through AI-driven management of AWS Reserved Instances and Savings Plans, maximizing discount coverage while minimizing commitment risk.
  name: ProsperOps
  slug: prosperops
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/prosperops/plans/prosperops-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prosperops-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/prosperops/rate-limits/prosperops-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prosperops-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/prosperops/finops/prosperops-finops.yml
  title: ''
  type: FinOps
  url: finops/prosperops-finops.yml
- group: auth
  href: https://artifacts.apis.io/prosperops/security/prosperops-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prosperops-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prosperops/security/prosperops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prosperops-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prosperops
- group: company
  title: ''
  type: Website
  url: https://www.prosperops.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.prosperops.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.prosperops.com/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://prosperops.com/llms.txt
created: '2026-03-16'
description: ProsperOps is an autonomous cloud cost optimization platform that uses AI-driven algorithms to manage AWS Reserved Instances and Savings Plans, maximizing discount coverage while minimizing commitment risk.
finops:
- has_sources: false
  method: generated
  name: Prosperops Finops
  primary_unit: request
  service_category: API
  slug: prosperops-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prosperops.png
layout: provider
modified: '2026-04-28'
name: ProsperOps
nav: Providers
network: true
overview: 'ProsperOps is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Amazon Web Services, Cloud Cost Optimization, and FinOps.


  ProsperOps'' developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Prosperops Plans Pricing
  plan_count: 3
  slug: prosperops-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Prosperops Rate Limits
  slug: prosperops-rate-limits
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 18.4
  previous_composite: 13.8
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/prosperops/prosperops-2026-06-20T192212.png
security:
- kind: domain-security
  name: Prosperops Domain Security
  slug: prosperops-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Prosperops Vulnerability Disclosure
  slug: prosperops-vulnerability-disclosure
  summary_line: no policy recorded
slug: prosperops
tags:
- Amazon Web Services
- Cloud Cost Optimization
- FinOps
website: https://www.prosperops.com/
---
