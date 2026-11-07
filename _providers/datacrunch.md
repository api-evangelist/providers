---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://datacrunch.io'', ''status'': 301, ''note'': ''declared website redirects to https://verda.com/ — a different registrable domain (datacrunch.io -> verda.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Datacrunch Agentic Access
  operation_count: 39
  slug: datacrunch-agentic-access
  summary_line: 39 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Balance API from DataCrunch — 1 operation(s) for balance.
  name: DataCrunch Balance API
  slug: datacrunch-balance-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Images API from DataCrunch — 2 operation(s) for images.
  name: DataCrunch Images API
  slug: datacrunch-images-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Instance Availability API from DataCrunch — 2 operation(s) for instance availability.
  name: DataCrunch Instance Availability API
  slug: datacrunch-instance-availability-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Instance Types API from DataCrunch — 1 operation(s) for instance types.
  name: DataCrunch Instance Types API
  slug: datacrunch-instance-types-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Instances API from DataCrunch — 2 operation(s) for instances.
  name: DataCrunch Instances API
  slug: datacrunch-instances-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Locations API from DataCrunch — 1 operation(s) for locations.
  name: DataCrunch Locations API
  slug: datacrunch-locations-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Serverless Containers API from DataCrunch — 8 operation(s) for serverless containers.
  name: DataCrunch Serverless Containers API
  slug: datacrunch-serverless-containers-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The SSH Keys API from DataCrunch — 2 operation(s) for ssh keys.
  name: DataCrunch SSH Keys API
  slug: datacrunch-ssh-keys-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Startup Scripts API from DataCrunch — 2 operation(s) for startup scripts.
  name: DataCrunch Startup Scripts API
  slug: datacrunch-startup-scripts-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Volumes API from DataCrunch — 4 operation(s) for volumes.
  name: DataCrunch Volumes API
  slug: datacrunch-volumes-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Authentication API from DataCrunch — 1 operation(s) for authentication.
  name: DataCrunch Authentication API
  slug: datacrunch-authentication-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: Deploy and manage clusters. **Beta:** Clusters API is under active development and may change without notice.
  name: DataCrunch Clusters API
  slug: datacrunch-clusters-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Container Registry API from DataCrunch — 1 operation(s) for container registry.
  name: DataCrunch Container Registry API
  slug: datacrunch-container-registry-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Container Types API from DataCrunch — 1 operation(s) for container types.
  name: DataCrunch Container Types API
  slug: datacrunch-container-types-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Instance groups API from DataCrunch — 2 operation(s) for instance groups.
  name: DataCrunch Instance groups API
  slug: datacrunch-instance-groups-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: Operations related to activity journal and audit log for cloud resources. **Beta:** Journal and audit log API is under active development and may change without notice. Shows history of actions perfor
  name: DataCrunch Journal API
  slug: datacrunch-journal-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Long Term API from DataCrunch — 3 operation(s) for long term.
  name: DataCrunch Long Term API
  slug: datacrunch-long-term-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Managed Endpoints API from DataCrunch — 1 operation(s) for managed endpoints.
  name: DataCrunch Managed Endpoints API
  slug: datacrunch-managed-endpoints-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: S3-compatible object storage. Manage access keys, and buckets. Read more about our object storage support [here](https://docs.verda.com/storage/object-storage). **Beta:** Object Storage API is under a
  name: DataCrunch Object Storage API
  slug: datacrunch-object-storage-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Private Networks (internal) API from DataCrunch — 4 operation(s) for private networks (internal).
  name: DataCrunch Private Networks (internal) API
  slug: datacrunch-private-networks-internal-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Serverless Jobs API from DataCrunch — 9 operation(s) for serverless jobs.
  name: DataCrunch Serverless Jobs API
  slug: datacrunch-serverless-jobs-api
- baseURL: https://api.datacrunch.io/v1
  baseurl_source: declared
  description: The Volume Types API from DataCrunch — 1 operation(s) for volume types.
  name: DataCrunch Volume Types API
  slug: datacrunch-volume-types-api
artifact_total: 42
collections:
- collection_type: open
  name: DataCrunch Public Balance API
  slug: open-datacrunch-balance-api
- collection_type: open
  name: DataCrunch Public Balance Images API
  slug: open-datacrunch-images-api
- collection_type: open
  name: DataCrunch Public Balance Instance Availability API
  slug: open-datacrunch-instance-availability-api
- collection_type: open
  name: DataCrunch Public Balance Instance Types API
  slug: open-datacrunch-instance-types-api
- collection_type: open
  name: DataCrunch Public Balance Instances API
  slug: open-datacrunch-instances-api
- collection_type: open
  name: DataCrunch Public Balance Locations API
  slug: open-datacrunch-locations-api
- collection_type: open
  name: DataCrunch Public Balance OAuth API
  slug: open-datacrunch-oauth-api
- collection_type: open
  name: DataCrunch Public Balance Serverless Containers API
  slug: open-datacrunch-serverless-containers-api
- collection_type: open
  name: DataCrunch Public Balance SSH Keys API
  slug: open-datacrunch-ssh-keys-api
- collection_type: open
  name: DataCrunch Public Balance Startup Scripts API
  slug: open-datacrunch-startup-scripts-api
- collection_type: open
  name: DataCrunch Public Balance Volumes API
  slug: open-datacrunch-volumes-api
- collection_type: open
  name: DataCrunch Public API
  slug: open-datacrunch
common:
- group: other
  href: https://artifacts.apis.io/datacrunch/capabilities/datacrunch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/datacrunch-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/datacrunch/agentic-access/datacrunch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datacrunch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/datacrunch/security/datacrunch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datacrunch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datacrunch/security/datacrunch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datacrunch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/datacrunch/authentication/datacrunch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datacrunch-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataCrunch-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datacrunch-oy
- group: company
  title: ''
  type: Website
  url: https://datacrunch.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datacrunch.io/
- group: commercial
  href: https://artifacts.apis.io/datacrunch/plans/datacrunch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datacrunch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/datacrunch/rate-limits/datacrunch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/datacrunch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/datacrunch/finops/datacrunch-finops.yml
  title: ''
  type: FinOps
  url: finops/datacrunch-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://verda.com/blog
created: '2026-06-21'
description: DataCrunch is a European (Finland-based) GPU cloud offering on-demand and reserved NVIDIA GPU instances (H200, H100, B200, A100, L40S, V100) plus a serverless inference and container deployment platform. Its REST API at https://api.datacrunch.io/v1 uses OAuth2 client-credentials to issue Bearer tokens and exposes instances, instance types, availability, images, SSH keys, startup scripts, volumes, balance, and serverless containers, with an OpenAI-compatible inference endpoint for deployed models.
finops:
- has_sources: true
  method: generated
  name: Datacrunch Finops
  primary_unit: ''
  service_category: Compute
  slug: datacrunch-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datacrunch.png
layout: provider
modified: '2026-06-21'
name: DataCrunch
nav: Providers
network: true
overview: 'DataCrunch publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Images API, Instance Availability API, and 19 more. Tagged areas include GPU Cloud, Infrastructure, Compute, Inference, and Serverless.


  The DataCrunch catalog on APIs.io includes 1 Spectral governance ruleset.


  DataCrunch''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Datacrunch Plans Pricing
  plan_count: 4
  slug: datacrunch-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Datacrunch Rate Limits
  slug: datacrunch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: DataCrunch API Rules
  rule_count: 56
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 5
  slug: datacrunch-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 53.2
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 64.7
      total: 34
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/datacrunch/datacrunch-2026-07-25T211313.png
security:
- kind: authentication
  name: Datacrunch Authentication
  slug: datacrunch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Datacrunch Domain Security
  slug: datacrunch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datacrunch Vulnerability Disclosure
  slug: datacrunch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: datacrunch
tags:
- GPU Cloud
- Infrastructure
- Compute
- Inference
- Serverless
- Europe
website: https://datacrunch.io
---
