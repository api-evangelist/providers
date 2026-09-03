---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: The Wasabi S3 API is a 100% bit-compatible implementation of the Amazon S3 REST API for creating and managing buckets, uploading and retrieving objects, controlling access, and managing lifecycle poli
  name: Wasabi S3 API
  slug: wasabi-s3-api
- description: The Wasabi Account Control Management API provides programmatic access to account management, user and sub-account provisioning, IAM policy management, access key management, and account utilization d
  name: Wasabi Account Control Management (WACM) API
  slug: wasabi-account-control-api
- description: The Wasabi Stats API provides access to utilization analytics and storage statistics for accounts, including storage usage, bandwidth metrics, and cost utilization data for reporting and FinOps purpos
  name: Wasabi Stats API
  slug: wasabi-stats-api
- description: The Wasabi AiR (AI Ready) API provides AI-powered media intelligence capabilities for objects stored in Wasabi, enabling content analysis, tagging, and search across media assets stored in Wasabi buck
  name: Wasabi AiR API
  slug: wasabi-air-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/wasabi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wasabi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wasabi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wasabi.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wasabi-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wasabitechnologies/
- group: company
  title: ''
  type: Blog
  url: https://wasabi.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://wasabi.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wasabi.com
- group: other
  title: ''
  type: X
  url: https://x.com/wasabi_cloud
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/wasabi-dev
- group: commercial
  title: ''
  type: Plans
  url: plans/wasabi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wasabi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wasabi-finops.yml
created: 2026-06-13
description: Wasabi Hot Cloud Storage is an S3-compatible object storage service offering a REST API that mirrors the Amazon S3 API for storing, retrieving, and managing objects and buckets. Wasabi provides always-consistent storage at lower cost than hyperscale providers, with no egress fees, no API request fees, and enterprise-grade performance across multiple global regions.
finops:
- name: Wasabi Finops
  service_category: ''
  slug: wasabi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wasabi.png
jsonld:
- class_count: 0
  name: Wasabi Context
  property_count: 0
  slug: wasabi-context
layout: provider
modified: 2026-06-13
name: Wasabi
nav: Providers
network: true
overview: 'Wasabi publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Storage, Object Storage, S3 Compatible, REST API, and Hot Storage.


  The Wasabi catalog on APIs.io includes 1 JSON-LD context.


  Wasabi''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Wasabi Plans Pricing
  plan_count: 2
  slug: wasabi-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Wasabi Rate Limits
  slug: wasabi-rate-limits
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 47.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 31.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wasabi/refs/heads/main/screenshots/wasabi-2026-06-20T201235.png
security:
- kind: domain-security
  name: Wasabi Domain Security
  slug: wasabi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wasabi Trust Center
  slug: wasabi-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: wasabi
tags:
- Cloud Storage
- Object Storage
- S3 Compatible
- REST API
- Hot Storage
- Buckets
- Objects
- Media Storage
- Backup
- Enterprise Storage
website: https://wasabi.com
---
