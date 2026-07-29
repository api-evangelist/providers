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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Control Plane API manages clusters (create / modify / suspend), users, roles, backups, alerts, metrics, and billing. Authentication is Bearer with a Zilliz API key.
  name: Zilliz Cloud Control Plane API
  slug: zilliz-control-plane
- description: Data Plane endpoints handle collection, vector, partition, index, and role operations on a specific cluster. Authentication accepts either a Zilliz API key or a cluster `db_admin:password` pair.
  name: Zilliz Cloud Data Plane API
  slug: zilliz-data-plane
artifact_total: 7
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
overview: 'Zilliz publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Vector Database, AI, Cloud, Milvus, and Managed.


  Zilliz''s developer surface includes developer portal, pricing, and 10 more developer resources.'
plans:
- name: Zilliz Plans Pricing
  plan_count: 1
  slug: zilliz-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 1
  name: Zilliz Rate Limits
  slug: zilliz-rate-limits
score:
  band: emerging
  composite: 23.5
  delta: -0.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 8.1
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- AI
- Cloud
- Milvus
- Managed
website: https://zilliz.com/
---
