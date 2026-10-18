---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: ProsperOps provides autonomous cloud cost optimization through AI-driven management of AWS Reserved Instances and Savings Plans, maximizing discount coverage while minimizing commitment risk.
  name: ProsperOps
  slug: prosperops
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/prosperops/refs/heads/main/plans/prosperops-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prosperops-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/prosperops/refs/heads/main/rate-limits/prosperops-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prosperops-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/prosperops/refs/heads/main/finops/prosperops-finops.yml
  title: ''
  type: FinOps
  url: finops/prosperops-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prosperops/refs/heads/main/security/prosperops-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prosperops-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prosperops/refs/heads/main/security/prosperops-domain-security.yml
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
  primary_unit: ''
  service_category: API
  slug: prosperops-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prosperops.png
layout: provider
modified: '2026-04-28'
name: ProsperOps
nav: Providers
network: true
overview: 'ProsperOps is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Cost Optimization and FinOps.


  ProsperOps'' developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Prosperops Plans Pricing
  plan_count: 3
  slug: prosperops-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Prosperops Rate Limits
  slug: prosperops-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 7.9
  previous_composite: 13.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/prosperops/refs/heads/main/screenshots/prosperops-2026-06-20T192212.png
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
- Cloud Cost Optimization
- FinOps
website: https://www.prosperops.com/
---
