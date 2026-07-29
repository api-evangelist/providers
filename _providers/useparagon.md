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
- acting_count: 6
  human_in_the_loop: 0
  name: Useparagon Agentic Access
  operation_count: 13
  slug: useparagon-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 8
apis:
- description: Prebuilt, LLM-ready actions across connected SaaS providers.
  name: Paragon ActionKit API
  slug: useparagon-actionkit-api
- description: Authenticated users and connected third-party credentials.
  name: Paragon Connect API
  slug: useparagon-connect-api
- description: Integrations enabled for a Paragon project.
  name: Paragon Integrations API
  slug: useparagon-integrations-api
- description: Normalized third-party data ingestion pipelines and records.
  name: Paragon Managed Sync API
  slug: useparagon-managed-sync-api
- description: Access control checks for ingested data.
  name: Paragon Permissions API
  slug: useparagon-permissions-api
- description: Passthrough requests to a connected user's third-party API.
  name: Paragon Proxy API
  slug: useparagon-proxy-api
- description: Authenticated user and connected integration state.
  name: Paragon Users API
  slug: useparagon-users-api
- description: Triggering workflows and checking execution status.
  name: Paragon Workflows API
  slug: useparagon-workflows-api
artifact_total: 15
collections:
- collection_type: open
  name: Paragon API
  slug: open-useparagon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/useparagon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/useparagon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/useparagon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useparagon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useparagon
- group: company
  title: ''
  type: Website
  url: https://www.useparagon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useparagon.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/useparagon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/useparagon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/useparagon-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.useparagon.com/blog
created: '2026-07-01'
description: Paragon is an embedded integration platform (embedded iPaaS) that lets B2B SaaS companies build and ship native, third-party integrations inside their own product. Developers use the Connect SDK/Portal plus a REST API (Connect API, ActionKit, and Managed Sync) to authenticate end users into 130+ SaaS providers, trigger workflows, run agentic actions, and ingest normalized third-party data.
finops:
- name: Useparagon Finops
  service_category: Integration Platform
  slug: useparagon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/useparagon.png
layout: provider
modified: '2026-07-01'
name: Paragon
nav: Providers
network: true
overview: 'Paragon publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ActionKit API, Connect API, Integrations API, and 5 more. Tagged areas include Integration, iPaaS, Embedded Integrations, Workflows, and ActionKit.


  Paragon''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Useparagon Plans Pricing
  plan_count: 4
  slug: useparagon-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 4
  name: Useparagon Rate Limits
  slug: useparagon-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Useparagon Authentication
  slug: useparagon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Useparagon Domain Security
  slug: useparagon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: useparagon
tags:
- Integration
- iPaaS
- Embedded Integrations
- Workflows
- ActionKit
- Managed Sync
- AI Agents
website: https://www.useparagon.com/
---
