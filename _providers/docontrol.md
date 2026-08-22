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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Docontrol Agentic Access
  operation_count: 2
  slug: docontrol-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: DoControl is a SaaS data security platform providing automated data access governance, DLP, and insider threat prevention for cloud applications.
  name: DoControl
  slug: docontrol
- description: The Authentication API from DoControl — 1 operation(s) for authentication.
  name: DoControl Authentication API
  slug: docontrol-authentication-api
- description: The GraphQL API from DoControl — 1 operation(s) for graphql.
  name: DoControl GraphQL API
  slug: docontrol-graphql-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DoControl Authentication API
  slug: open-docontrol-authentication-api
- collection_type: open
  name: DoControl Authentication GraphQL API
  slug: open-docontrol-graphql-api
- collection_type: open
  name: DoControl API
  slug: open-docontrol
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docontrol-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/docontrol-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docontrol-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docontrol-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docontrol-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/do-control
- group: company
  title: ''
  type: Website
  url: https://www.docontrol.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docontrol.io/
created: '2026-03-27'
description: DoControl is a SaaS data security platform providing automated data access governance, DLP, and insider threat prevention for cloud applications.
finops:
- name: Docontrol Finops
  service_category: API
  slug: docontrol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docontrol.png
layout: provider
modified: '2026-04-28'
name: DoControl
nav: Providers
network: true
overview: 'DoControl publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and GraphQL API. Tagged areas include Data Security and SaaS Security.


  DoControl''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Docontrol Plans Pricing
  plan_count: 3
  slug: docontrol-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Docontrol Rate Limits
  slug: docontrol-rate-limits
score:
  band: thin
  composite: 28.3
  delta: -0.9
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 21.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docontrol/refs/heads/main/screenshots/docontrol-2026-06-20T180108.png
security:
- kind: authentication
  name: Docontrol Authentication
  slug: docontrol-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Docontrol Domain Security
  slug: docontrol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Docontrol Trust Center
  slug: docontrol-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: docontrol
tags:
- Data Security
- SaaS Security
website: https://www.docontrol.io
---
