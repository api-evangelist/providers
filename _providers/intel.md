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
    agentic_access: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Intel Agentic Access
  operation_count: 5
  slug: intel-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- baseURL: https://api.trustauthority.intel.com
  baseurl_source: declared
  description: Attestation verification operations
  name: intel Attestation API
  slug: intel-attestation-api
- baseURL: https://api.trustauthority.intel.com
  baseurl_source: declared
  description: Policy management operations
  name: intel Policies API
  slug: intel-policies-api
- baseURL: https://api.trustauthority.intel.com
  baseurl_source: declared
  description: Token management operations
  name: intel Tokens API
  slug: intel-tokens-api
- baseURL: https://api.trustauthority.intel.com
  baseurl_source: declared
  description: Developer tools and toolkit operations
  name: intel Tools API
  slug: intel-tools-api
artifact_total: 16
collections:
- collection_type: open
  name: Intel one Attestation API
  slug: open-intel-attestation-api
- collection_type: open
  name: Intel oneAPI
  slug: open-intel-oneapi
- collection_type: open
  name: Intel one Attestation Policies API
  slug: open-intel-policies-api
- collection_type: open
  name: Intel one Attestation Tokens API
  slug: open-intel-tokens-api
- collection_type: open
  name: Intel one Attestation Tools API
  slug: open-intel-tools-api
- collection_type: open
  name: Intel Trust Authority API
  slug: open-intel-trust-authority-api
common:
- group: commercial
  href: https://artifacts.apis.io/intel/plans/intel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/intel-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/intel/rate-limits/intel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/intel-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/intel/finops/intel-finops.yml
  title: ''
  type: FinOps
  url: finops/intel-finops.yml
- group: company
  title: ''
  type: Website
  url: https://intel.com
- group: other
  href: https://artifacts.apis.io/intel/capabilities/intel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/intel-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/intel/agentic-access/intel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/intel-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/intel/security/intel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intel-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intel-corporation
- group: company
  title: ''
  type: Blog
  url: https://newsroom.intel.com/feed
description: Discover Intel® Trust Authority, the independent attestation service for securing your confidential computing workloads.
finops:
- has_sources: true
  method: generated
  name: Intel Finops
  primary_unit: not-applicable
  service_category: Confidential Computing + Developer Tools
  slug: intel-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intel.png
layout: provider
modified: '2026-09-16'
name: Intel
nav: Providers
network: true
overview: 'Intel publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attestation API, Policies API, Tokens API, and 1 more. Tagged areas include Fortune 100.


  The Intel catalog on APIs.io includes 1 Spectral governance ruleset.


  Intel''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Intel Plans Pricing
  plan_count: 3
  slug: intel-plans-pricing
press:
- date: ''
  title: Intel Corporation (INTC) Latest Press Releases & ...
  url: https://finance.yahoo.com/quote/INTC/press-releases/
- date: ''
  title: Intel Newsroom Home
  url: https://newsroom.intel.com/
- date: ''
  title: All News - Newsroom
  url: https://newsroom.intel.com/all-news
- date: ''
  title: 'Press Releases - Investor Relations :: Intel Corporation (INTC)'
  url: https://www.intc.com/news-events/press-releases?page=10
- date: ''
  title: NVIDIA and Intel to Develop AI Infrastructure and Personal ...
  url: http://nvidianews.nvidia.com/news/nvidia-and-intel-to-develop-ai-infrastructure-and-personal-computing-products
random_paper: 12
rate_limits:
- limit_count: 2
  name: Intel Rate Limits
  slug: intel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Intel API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: intel-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 44.7
    developer_ergonomics: 11.9
    discoverability: 42.9
    operational_transparency: 7.9
  previous_composite: 21.6
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
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/intel/intel-2026-06-20T183445.png
security:
- kind: domain-security
  name: Intel Domain Security
  slug: intel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intel
tags:
- Fortune 100
website: https://intel.com
---
