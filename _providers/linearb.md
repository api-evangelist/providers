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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Linearb Agentic Access
  operation_count: 19
  slug: linearb-agentic-access
  summary_line: 19 operations · 14 acting
api_count: 5
apis:
- description: The Deployments API from LinearB — 1 operation(s) for deployments.
  name: LinearB Deployments API
  slug: linearb-deployments-api
- description: The Incidents API from LinearB — 2 operation(s) for incidents.
  name: LinearB Incidents API
  slug: linearb-incidents-api
- description: The Measurements API from LinearB — 2 operation(s) for measurements.
  name: LinearB Measurements API
  slug: linearb-measurements-api
- description: The Services API from LinearB — 2 operation(s) for services.
  name: LinearB Services API
  slug: linearb-services-api
- description: The Teams API from LinearB — 4 operation(s) for teams.
  name: LinearB Teams API
  slug: linearb-teams-api
artifact_total: 13
collections:
- collection_type: open
  name: LinearB Public API
  slug: open-linearb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linearb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/linearb-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linearb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linearb-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linear-b
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linearb
- group: company
  title: ''
  type: Website
  url: https://linearb.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linearb.io/api-overview/
- group: commercial
  title: ''
  type: Plans
  url: plans/linearb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linearb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/linearb-finops.yml
created: '2026-06-21'
description: LinearB is a software engineering intelligence (SEI) and developer productivity platform that correlates Git, CI/CD, project management, and incident data into DORA and engineering metrics. The LinearB REST API lets teams report deployments, push incidents, export measurements, and manage teams and services programmatically.
finops:
- name: Linearb Finops
  service_category: Developer Tools
  slug: linearb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linearb.png
layout: provider
modified: '2026-06-21'
name: LinearB
nav: Providers
network: true
overview: 'LinearB publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Deployments API, Incidents API, Measurements API, and 2 more. Tagged areas include Engineering Analytics, SEI, Developer Productivity, DORA Metrics, and DevOps.


  LinearB''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Linearb Plans Pricing
  plan_count: 3
  slug: linearb-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 1
  name: Linearb Rate Limits
  slug: linearb-rate-limits
score:
  band: thin
  composite: 40.0
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 52.7
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linearb/refs/heads/main/screenshots/linearb-2026-07-25T225235.png
security:
- kind: authentication
  name: Linearb Authentication
  slug: linearb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Linearb Domain Security
  slug: linearb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Linearb Trust Center
  slug: linearb-trust-center
  summary_line: SOC 2, ISO 27001
slug: linearb
tags:
- Engineering Analytics
- SEI
- Developer Productivity
- DORA Metrics
- DevOps
website: https://linearb.io/
---
