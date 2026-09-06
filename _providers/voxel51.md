---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://docs.voxel51.com
  baseurl_source: spec
  description: The open-source FiftyOne Python SDK is the primary interface for building and curating visual AI datasets - creating Datasets and Samples, slicing data with Views and aggregations, computing embedding
  name: FiftyOne SDK (Python)
  slug: fiftyone-sdk-python
- baseURL: https://docs.voxel51.com
  baseurl_source: spec
  description: FiftyOne Enterprise (formerly Teams) adds the fiftyone.management Python module for administering users, service accounts, API keys, dataset permissions, user groups, and cloud credentials. It operate
  name: FiftyOne Enterprise Management SDK / API
  slug: fiftyone-enterprise-management-sdk
- baseURL: https://docs.voxel51.com
  baseurl_source: spec
  description: The plugin and operator framework extends FiftyOne with custom Python (and JavaScript/React) functionality - new App panels, operators, and integrations that run inside the FiftyOne App and SDK. Plugi
  name: FiftyOne Plugins & Operators
  slug: fiftyone-plugins-operators
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voxel51 FiftyOne
  slug: open-voxel51
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voxel51-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voxel51-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voxel51
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voxel51
- group: company
  title: ''
  type: Website
  url: https://voxel51.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.voxel51.com
- group: commercial
  title: ''
  type: Plans
  url: plans/voxel51-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voxel51-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/voxel51-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://voxel51.com/blog
created: '2026-06-21'
description: Voxel51 builds FiftyOne, the open-source toolkit for building high-quality computer-vision and multimodal datasets and models. FiftyOne's primary interface is a Python SDK (datasets, samples, views, and the FiftyOne App) rather than a broad public REST API. FiftyOne Enterprise adds a Management SDK and an authenticated API connection that lets the SDK operate over the network instead of a direct database connection.
finops:
- name: Voxel51 Finops
  service_category: AI and Machine Learning
  slug: voxel51-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voxel51.png
layout: provider
modified: '2026-06-21'
name: Voxel51
nav: Providers
network: true
overview: 'Voxel51 publishes 3 APIs on the [APIs.io](https://apis.io/) network: FiftyOne SDK (Python), FiftyOne Enterprise Management SDK / API, and FiftyOne Plugins & Operators. Tagged areas include Artificial Intelligence, Computer-Vision, Datasets, Machine-Learning, and Python SDK.


  Voxel51''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Voxel51 Plans Pricing
  plan_count: 4
  slug: voxel51-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Voxel51 Rate Limits
  slug: voxel51-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 30.6
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 33.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voxel51/refs/heads/main/screenshots/voxel51-2026-09-02T170300.png
security:
- kind: authentication
  name: Voxel51 Authentication
  slug: voxel51-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Voxel51 Domain Security
  slug: voxel51-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: voxel51
tags:
- Artificial Intelligence
- Computer-Vision
- Datasets
- Machine-Learning
- Python SDK
website: https://voxel51.com
---
