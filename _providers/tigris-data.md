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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tigris Data Agentic Access
  operation_count: 20
  slug: tigris-data-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 3
apis:
- description: S3-compatible bucket management operations.
  name: Tigris Buckets API
  slug: tigris-data-buckets-api
- description: S3-compatible multipart upload operations for large objects.
  name: Tigris Multipart API
  slug: tigris-data-multipart-api
- description: S3-compatible object CRUD, tagging, and tiering operations.
  name: Tigris Objects API
  slug: tigris-data-objects-api
artifact_total: 11
collections:
- collection_type: open
  name: Tigris Object Storage (S3-Compatible) API
  slug: open-tigris-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tigris-data-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tigris-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tigris-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tigris-data-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tigrisdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tigrisdata
- group: company
  title: ''
  type: Website
  url: https://www.tigrisdata.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.tigrisdata.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/tigris-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tigris-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tigris-data-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tigrisdata.com/blog/rss.xml
created: '2026-06-20'
description: Tigris is a globally distributed, multi-cloud, S3-compatible object storage service. Data is automatically placed close to where it is read for low latency worldwide, with no egress fees. The storage API speaks the AWS S3 protocol at https://t3.storage.dev (formerly fly.storage.tigris.dev) so existing boto3, AWS SDK, and S3 clients work unchanged, with companion IAM and CloudFront-compatible APIs for access keys and public-key signing.
finops:
- name: Tigris Data Finops
  service_category: Storage
  slug: tigris-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tigris-data.png
layout: provider
modified: '2026-06-20'
name: Tigris
nav: Providers
network: true
overview: 'Tigris publishes 3 APIs on the [APIs.io](https://apis.io/) network: Buckets API, Multipart API, and Objects API. Tagged areas include Object Storage, S3 Compatible, Storage, Multi-Cloud, and Globally Distributed.


  Tigris'' developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Tigris Data Plans Pricing
  plan_count: 3
  slug: tigris-data-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 3
  name: Tigris Data Rate Limits
  slug: tigris-data-rate-limits
score:
  band: thin
  composite: 38.9
  delta: -2.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tigris-data/refs/heads/main/screenshots/tigris-data-2026-06-20T195343.png
security:
- kind: authentication
  name: Tigris Data Authentication
  slug: tigris-data-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tigris Data Domain Security
  slug: tigris-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tigris Data Trust Center
  slug: tigris-data-trust-center
  summary_line: SOC 2
slug: tigris-data
tags:
- Object Storage
- S3 Compatible
- Storage
- Multi-Cloud
- Globally Distributed
website: https://www.tigrisdata.com
---
