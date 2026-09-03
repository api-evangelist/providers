---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Control Plane API manages clusters (create / modify / suspend), users, roles, backups, alerts, metrics, and billing. Authentication is Bearer with a Zilliz API key.
  name: Zilliz Cloud Control Plane API
  slug: zilliz-control-plane
- description: Data Plane endpoints handle collection, vector, partition, index, and role operations on a specific cluster. Authentication accepts either a Zilliz API key or a cluster `db_admin:password` pair.
  name: Zilliz Cloud Data Plane API
  slug: zilliz-data-plane
- baseURL: https://api.cloud.zilliz.com/v2
  baseurl_source: declared
  description: 'Control plane: cloud and region discovery.'
  name: Zilliz Cloud Providers API
  slug: zilliz-cloud-providers-api
- baseURL: https://api.cloud.zilliz.com/v2
  baseurl_source: declared
  description: 'Control plane: cluster lifecycle management.'
  name: Zilliz Clusters API
  slug: zilliz-clusters-api
- baseURL: https://api.cloud.zilliz.com/v2
  baseurl_source: declared
  description: 'Data plane: vector collection operations.'
  name: Zilliz Collections API
  slug: zilliz-collections-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zilliz Cloud Cloud Providers API
  slug: open-zilliz-cloud-providers-api
- collection_type: open
  name: Zilliz Cloud Clusters API
  slug: open-zilliz-clusters-api
- collection_type: open
  name: Zilliz Cloud Collections API
  slug: open-zilliz-collections-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/zilliz-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zilliz-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zilliztech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zilliz
- group: company
  title: ''
  type: Website
  url: https://zilliz.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.zilliz.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://zilliz.com/pricing
- group: other
  title: Maintainer of Milvus
  type: ParentRelationship
  url: https://milvus.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/zilliz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zilliz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zilliz-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.zilliz.com/llms.txt
created: '2026-05-08'
description: Zilliz Cloud is the managed vector database service built by the Milvus maintainers. It exposes a Control Plane API for cluster management and a Data Plane API for vector operations. Offers Serverless, Dedicated, and BYOC plans.
finops:
- name: Zilliz Finops
  service_category: Vector Database
  slug: zilliz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zilliz.png
layout: provider
modified: '2026-05-08'
name: Zilliz
nav: Providers
network: true
overview: 'Zilliz publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cloud Providers API, Clusters API, and Collections API. Tagged areas include Vector Database, Artificial Intelligence, Cloud, Milvus, and Managed.


  Zilliz''s developer surface includes developer portal, pricing, and 10 more developer resources.'
plans:
- name: Zilliz Plans Pricing
  plan_count: 1
  slug: zilliz-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Zilliz Rate Limits
  slug: zilliz-rate-limits
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 34.1
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zilliz/refs/heads/main/screenshots/zilliz-2026-06-20T201901.png
security:
- kind: domain-security
  name: Zilliz Domain Security
  slug: zilliz-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Zilliz Trust Center
  slug: zilliz-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: zilliz
tags:
- Vector Database
- Artificial Intelligence
- Cloud
- Milvus
- Managed
website: https://zilliz.com/
---
