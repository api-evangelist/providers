---
access_model:
  confidence: high
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
  - rate-limits
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Gcore Agentic Access
  operation_count: 31
  slug: gcore-agentic-access
  summary_line: 31 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Content delivery network resources, rules, origin groups, and purge.
  name: Gcore CDN API
  slug: gcore-cdn-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Virtual machine instances, networks, and volumes.
  name: Gcore Cloud API
  slug: gcore-cloud-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Managed authoritative DNS zones and RRSets.
  name: Gcore DNS API
  slug: gcore-dns-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Serverless edge functions and applications.
  name: Gcore FastEdge API
  slug: gcore-fastedge-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Everywhere Inference edge AI model deployments.
  name: Gcore Inference API
  slug: gcore-inference-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: S3-compatible and SFTP object storage.
  name: Gcore Storage API
  slug: gcore-storage-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Video hosting (VOD) and live streaming.
  name: Gcore Streaming API
  slug: gcore-streaming-api
- baseURL: https://api.gcore.com/cdn
  baseurl_source: declared
  description: Web Application and API Protection domains.
  name: Gcore WAAP API
  slug: gcore-waap-api
artifact_total: 25
collections:
- collection_type: open
  name: Gcore CDN API
  slug: open-gcore-cdn-api
- collection_type: open
  name: Gcore CDN Cloud API
  slug: open-gcore-cloud-api
- collection_type: open
  name: Gcore CDN DNS API
  slug: open-gcore-dns-api
- collection_type: open
  name: Gcore CDN FastEdge API
  slug: open-gcore-fastedge-api
- collection_type: open
  name: Gcore CDN Inference API
  slug: open-gcore-inference-api
- collection_type: open
  name: Gcore CDN Storage API
  slug: open-gcore-storage-api
- collection_type: open
  name: Gcore CDN Streaming API
  slug: open-gcore-streaming-api
- collection_type: open
  name: Gcore CDN WAAP API
  slug: open-gcore-waap-api
- collection_type: open
  name: Gcore API
  slug: open-gcore
common:
- group: company
  title: ''
  type: Blog
  url: https://gcore.com/blog
- group: other
  href: https://artifacts.apis.io/gcore/vendor-facets/gcore-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/gcore-vendor-facets.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://gcore.com/pricing/edge-network
- group: other
  href: https://artifacts.apis.io/gcore/capabilities/gcore-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gcore-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gcore/agentic-access/gcore-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gcore-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gcore/security/gcore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gcore-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gcore/authentication/gcore-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gcore-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/G-Core
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gcore
- group: company
  title: ''
  type: Website
  url: https://gcore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gcore.com/docs/api-reference/overview
- group: commercial
  href: https://artifacts.apis.io/gcore/plans/gcore-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gcore-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gcore/rate-limits/gcore-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gcore-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gcore/finops/gcore-finops.yml
  title: ''
  type: FinOps
  url: finops/gcore-finops.yml
created: '2026-06-20'
description: Gcore is a global edge cloud, CDN, streaming, and AI infrastructure provider operating 210+ points of presence. A single REST platform at https://api.gcore.com (APIKey auth) spans content delivery, GPU cloud and bare-metal compute, S3-compatible object storage, managed DNS, video streaming and live, Everywhere Inference (edge AI), WAAP/DDoS security, and FastEdge serverless functions.
finops:
- has_sources: true
  method: generated
  name: Gcore Finops
  primary_unit: ''
  service_category: Compute and Networking
  slug: gcore-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gcore.png
layout: provider
modified: '2026-10-06'
name: Gcore
nav: Providers
network: true
overview: 'Gcore publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including CDN API, Cloud API, DNS API, and 5 more. Tagged areas include Edge Cloud, CDN, Streaming, Edge AI, and Infrastructure.


  The Gcore catalog on APIs.io includes 1 Spectral governance ruleset.


  Gcore''s developer surface includes engineering blog, pricing, authentication, documentation, and 10 more developer resources.'
plans:
- name: Gcore Plans Pricing
  plan_count: 10
  slug: gcore-plans-pricing
- name: Gcore Price Estimates
  plan_count: 0
  slug: gcore-price-estimates
random_paper: 0
rate_limits:
- limit_count: 0
  name: Gcore Rate Limits
  slug: gcore-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Gcore API Rules
  rule_count: 62
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 14
  slug: gcore-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 28.7
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 30.9
      derived: 0
      marker_coverage: 14.5
      total: 55
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
    score: 33.3
screenshot: https://apis.io/screenshots/gcore/gcore-2026-06-20T181710.png
security:
- kind: authentication
  name: Gcore Authentication
  slug: gcore-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gcore Domain Security
  slug: gcore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gcore
tags:
- Edge Cloud
- CDN
- Streaming
- Edge AI
- Infrastructure
website: https://gcore.com/
---
