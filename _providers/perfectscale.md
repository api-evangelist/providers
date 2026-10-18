---
access_model:
  confidence: medium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Perfectscale Agentic Access
  operation_count: 6
  slug: perfectscale-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.app.perfectscale.io/public/v1
  baseurl_source: declared
  description: Authentication and access tokens
  name: PerfectScale Authentication API
  slug: perfectscale-authentication-api
- baseURL: https://api.app.perfectscale.io/public/v1
  baseurl_source: declared
  description: Automation audit logs
  name: PerfectScale Automation API
  slug: perfectscale-automation-api
- baseURL: https://api.app.perfectscale.io/public/v1
  baseurl_source: declared
  description: Kubernetes cluster operations
  name: PerfectScale Clusters API
  slug: perfectscale-clusters-api
- baseURL: https://api.app.perfectscale.io/public/v1
  baseurl_source: declared
  description: Workload metrics and analysis
  name: PerfectScale Workloads API
  slug: perfectscale-workloads-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PerfectScale Public Authentication API
  slug: open-perfectscale-authentication-api
- collection_type: open
  name: PerfectScale Public Authentication Automation API
  slug: open-perfectscale-automation-api
- collection_type: open
  name: PerfectScale Public Authentication Clusters API
  slug: open-perfectscale-clusters-api
- collection_type: open
  name: PerfectScale Public API
  slug: open-perfectscale-perfectscale
- collection_type: open
  name: PerfectScale Public Authentication Workloads API
  slug: open-perfectscale-workloads-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/plans/perfectscale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/perfectscale-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/rate-limits/perfectscale-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/perfectscale-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/finops/perfectscale-finops.yml
  title: ''
  type: FinOps
  url: finops/perfectscale-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.perfectscale.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.perfectscale.io/blog/feed.xml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/capabilities/perfectscale-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/perfectscale-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/agentic-access/perfectscale-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/perfectscale-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/security/perfectscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perfectscale-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/authentication/perfectscale-authentication.yml
  title: ''
  type: Authentication
  url: authentication/perfectscale-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perfectscale-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perfectscale
- group: company
  title: ''
  type: Website
  url: https://www.perfectscale.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.perfectscale.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.perfectscale.io/llms.txt
created: '2026-03-27'
description: PerfectScale is a Kubernetes cost optimization platform providing autonomous scaling and resource rightsizing.
finops:
- has_sources: false
  method: generated
  name: Perfectscale Finops
  primary_unit: ''
  service_category: API
  slug: perfectscale-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perfectscale.png
layout: provider
modified: '2026-10-06'
name: PerfectScale
nav: Providers
network: true
overview: 'PerfectScale publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Automation API, Clusters API, and 1 more. Tagged areas include FinOps, Kubernetes, and Cost Optimization.


  PerfectScale''s developer surface includes engineering blog, authentication, documentation, and 11 more developer resources.'
plans:
- name: Perfectscale Plans Pricing
  plan_count: 3
  slug: perfectscale-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Perfectscale Rate Limits
  slug: perfectscale-rate-limits
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 50.5
    developer_ergonomics: 35.7
    discoverability: 55.4
    operational_transparency: 10.5
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
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
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/screenshots/perfectscale-2026-06-20T191600.png
security:
- kind: authentication
  name: Perfectscale Authentication
  slug: perfectscale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perfectscale Domain Security
  slug: perfectscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: perfectscale
tags:
- FinOps
- Kubernetes
- Cost Optimization
website: https://www.perfectscale.io/
---
