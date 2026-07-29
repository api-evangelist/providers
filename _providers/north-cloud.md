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
- acting_count: 1
  human_in_the_loop: 0
  name: North Cloud Agentic Access
  operation_count: 2
  slug: north-cloud-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Manage and retrieve cost unit metric data.
  name: North.Cloud Cost Units API
  slug: north-cloud-cost-units-api
artifact_total: 8
collections:
- collection_type: open
  name: North.Cloud Public API
  slug: open-north-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/north-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/north-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/north-cloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northcld
- group: company
  title: ''
  type: Website
  url: https://www.north.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.north.cloud/
- group: other
  title: ''
  type: Application
  url: https://app.north.cloud/
- group: auth
  title: ''
  type: Security
  url: https://docs.north.cloud/security
- group: company
  title: ''
  type: Blog
  url: https://www.north.cloud/blog
created: '2026-01-02'
description: North.Cloud delivers real-time savings, automated FinOps, and dynamic optimization across AWS and GCP. The platform's public API enables programmatic ingestion and retrieval of cost unit data so teams can integrate unit economics, allocation, and chargeback reporting into their own systems.
finops:
- name: North Cloud Finops
  service_category: API
  slug: north-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/north-cloud.png
layout: provider
modified: '2026-05-19'
name: North.Cloud
nav: Providers
network: true
overview: 'North.Cloud publishes 1 API on the [APIs.io](https://apis.io/) network: Cost Units API. Tagged areas include FinOps, Cloud Cost Management, GCP, Cost Optimization, and Cost Units.


  North.Cloud''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: North Cloud Plans Pricing
  plan_count: 3
  slug: north-cloud-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: North Cloud Rate Limits
  slug: north-cloud-rate-limits
score:
  band: thin
  composite: 40.0
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/north-cloud/refs/heads/main/screenshots/north-cloud-2026-06-20T190412.png
security:
- kind: authentication
  name: North Cloud Authentication
  slug: north-cloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: North Cloud Domain Security
  slug: north-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: north-cloud
tags:
- FinOps
- Cloud Cost Management
- GCP
- Cost Optimization
- Cost Units
website: https://www.north.cloud/
---
