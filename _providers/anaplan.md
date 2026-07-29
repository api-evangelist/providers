---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 6
apis:
- description: RESTful bulk and transactional API for importing data, exporting results, running processes, and managing models within Anaplan workspaces.
  name: Anaplan Integration API v2.0
  slug: anaplan-integration-api-v20
- description: Manages authentication token creation and refresh for accessing all other Anaplan APIs using username/password or client certificate credentials.
  name: Anaplan Authentication Service API
  slug: anaplan-authentication-service-api
- description: Controls workflows, manages security, and supports retrieval, insertion, update, and deletion of financial data and metadata for consolidation use cases.
  name: Anaplan Financial Consolidation API
  slug: anaplan-financial-consolidation-api
- description: System for Cross-Domain Identity Management API for provisioning and managing user identities across multiple domains within the Anaplan platform.
  name: Anaplan SCIM API
  slug: anaplan-scim-api
- description: Enables creation of custom connections and integrations between Anaplan and external data sources and systems through CloudWorks.
  name: Anaplan CloudWorks API
  slug: anaplan-cloudworks-api
- description: Tracks and streams audit events and security alerts for integration with Security Information and Event Management (SIEM) services.
  name: Anaplan Audit API
  slug: anaplan-audit-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/anaplan-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anaplan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anaplan.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.anaplan.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anaplaninc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anaplan
- group: company
  title: ''
  type: Blog
  url: https://www.anaplan.com/blog/
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anaplan.com/platform/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anaplan.com/
- group: other
  title: ''
  type: X
  url: https://x.com/anaplan
- group: commercial
  title: ''
  type: Plans
  url: plans/anaplan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anaplan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/anaplan-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/anaplan-context.jsonld
created: 2026-06-12
description: Anaplan is a cloud-native connected planning platform used by enterprises for financial planning and analysis (FP&A), supply chain planning, and sales performance management. Its REST API (Integration API v2.0) allows integrators to import and export data, trigger model processes, and manage Anaplan workspaces programmatically. Beyond bulk data operations, Anaplan exposes dedicated APIs for financial consolidation, identity management via SCIM, audit event streaming, application lifecycle management, and CloudWorks custom integrations. All API access requires authentication via the Anaplan Authentication Service API, which issues tokens using username/password credentials or client certificates.
finops:
- name: Anaplan Finops
  service_category: ''
  slug: anaplan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anaplan.png
jsonld:
- class_count: 36
  name: Anaplan Context
  property_count: 2
  slug: anaplan-context
layout: provider
modified: 2026-06-12
name: Anaplan
nav: Providers
network: true
overview: 'Anaplan publishes 1 API on the [APIs.io](https://apis.io/) network: Integration API v2.0. Tagged areas include Connected Planning, Enterprise Planning, FP&A, Supply Chain, and Sales Planning.


  The Anaplan catalog on APIs.io includes 1 JSON-LD context.


  Anaplan''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Anaplan Plans Pricing
  plan_count: 3
  slug: anaplan-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 3
  name: Anaplan Rate Limits
  slug: anaplan-rate-limits
score:
  band: thin
  composite: 31.2
  delta: -3.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 34.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anaplan/refs/heads/main/screenshots/anaplan-2026-06-20T171947.png
security:
- kind: domain-security
  name: Anaplan Domain Security
  slug: anaplan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Anaplan Trust Center
  slug: anaplan-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, CSA STAR
slug: anaplan
tags:
- Connected Planning
- Enterprise Planning
- FP&A
- Supply Chain
- Sales Planning
- Financial Consolidation
- SCIM
- REST
website: https://www.anaplan.com
---
