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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/intel-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intel-agentic-access.yml
- group: auth
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
- name: Intel Finops
  service_category: Confidential Computing + Developer Tools
  slug: intel-finops
graphqls:
- description: This conceptual GraphQL schema models the Intel developer ecosystem spanning processor architectures, heterogeneous computing via oneAPI, AI/ML acceleration with Gaudi and OpenVINO, Intel Developer Cl
  name: Intel GraphQL Schema
  slug: intel-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intel.png
layout: provider
modified: '2026-05-19'
name: Intel
nav: Providers
network: true
overview: 'Intel publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Attestation API, Policies API, Tokens API, and 1 more. Tagged areas include Fortune 100.


  Intel''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Intel Plans Pricing
  plan_count: 3
  slug: intel-plans-pricing
press:
- date: '2026-05-25'
  title: Intel Corporation (INTC) Latest Press Releases & ...
  url: https://finance.yahoo.com/quote/INTC/press-releases/
- date: '2026-05-25'
  title: Intel Newsroom Home
  url: https://newsroom.intel.com/
- date: '2026-05-25'
  title: All News - Newsroom
  url: https://newsroom.intel.com/all-news
- date: '2026-05-25'
  title: 'Press Releases - Investor Relations :: Intel Corporation (INTC)'
  url: https://www.intc.com/news-events/press-releases?page=10
- date: '2026-05-25'
  title: NVIDIA and Intel to Develop AI Infrastructure and Personal ...
  url: http://nvidianews.nvidia.com/news/nvidia-and-intel-to-develop-ai-infrastructure-and-personal-computing-products
random_paper: 15
rate_limits:
- limit_count: 2
  name: Intel Rate Limits
  slug: intel-rate-limits
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.0
    developer_ergonomics: 11.9
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intel/refs/heads/main/screenshots/intel-2026-06-20T183445.png
security:
- kind: domain-security
  name: Intel Domain Security
  slug: intel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intel
tags:
- Fortune 100
---
