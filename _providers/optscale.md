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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Optscale Agentic Access
  operation_count: 16
  slug: optscale-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 9
apis:
- description: User authentication and token management
  name: OptScale Authentication API
  slug: optscale-authentication-api
- description: Cloud account connections (AWS, Azure, GCP, Alibaba, Kubernetes)
  name: OptScale Cloud Accounts API
  slug: optscale-cloud-accounts-api
- description: Organization employees and roles
  name: OptScale Employees API
  slug: optscale-employees-api
- description: Cost reporting and expense breakdowns
  name: OptScale Expenses API
  slug: optscale-expenses-api
- description: Optimization checklist runs and results
  name: OptScale Optimizations API
  slug: optscale-optimizations-api
- description: Organization management
  name: OptScale Organizations API
  slug: optscale-organizations-api
- description: Budget pools and limits
  name: OptScale Pools API
  slug: optscale-pools-api
- description: Cost optimization recommendations
  name: OptScale Recommendations API
  slug: optscale-recommendations-api
- description: Cloud resources and assignment rules
  name: OptScale Resources API
  slug: optscale-resources-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OptScale REST Authentication API
  slug: open-optscale-authentication-api
- collection_type: open
  name: OptScale REST Authentication Cloud Accounts API
  slug: open-optscale-cloud-accounts-api
- collection_type: open
  name: OptScale REST Authentication Employees API
  slug: open-optscale-employees-api
- collection_type: open
  name: OptScale REST Authentication Expenses API
  slug: open-optscale-expenses-api
- collection_type: open
  name: OptScale REST Authentication Optimizations API
  slug: open-optscale-optimizations-api
- collection_type: open
  name: OptScale REST Authentication Organizations API
  slug: open-optscale-organizations-api
- collection_type: open
  name: OptScale REST Authentication Pools API
  slug: open-optscale-pools-api
- collection_type: open
  name: OptScale REST Authentication Recommendations API
  slug: open-optscale-recommendations-api
- collection_type: open
  name: OptScale REST Authentication Resources API
  slug: open-optscale-resources-api
- collection_type: open
  name: OptScale REST API
  slug: open-optscale
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/hystax/optscale/blob/integration/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optscale-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hystax.com/optscale/
- group: docs
  title: ''
  type: Documentation
  url: https://hystax.com/documentation/optscale/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hystax
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hystax/optscale
- group: agent
  title: ''
  type: LlmsText
  url: https://my.optscale.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://hystax.com/feed/
created: '2026-03-27'
description: OptScale is an open-source FinOps and cloud cost optimization platform by Hystax supporting AWS, Azure, GCP, Alibaba Cloud, and Kubernetes.
finops:
- name: Optscale Finops
  service_category: API
  slug: optscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optscale.png
layout: provider
modified: '2026-05-19'
name: OptScale
nav: Providers
network: true
overview: 'OptScale publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Cloud Accounts API, Employees API, and 6 more. Tagged areas include FinOps, Cost Optimization, Cloud, Kubernetes, and Open Source.


  OptScale''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Optscale Plans Pricing
  plan_count: 3
  slug: optscale-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 5
  name: Optscale Rate Limits
  slug: optscale-rate-limits
score:
  band: thin
  composite: 29.3
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 51.5
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optscale/refs/heads/main/screenshots/optscale-2026-06-20T191116.png
security:
- kind: authentication
  name: Optscale Authentication
  slug: optscale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Optscale Domain Security
  slug: optscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: optscale
tags:
- FinOps
- Cost Optimization
- Cloud
- Kubernetes
- Open Source
website: https://hystax.com/optscale/
---
