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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ocelot Agentic Access
  operation_count: 4
  slug: ocelot-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 4
apis:
- description: Ocelot is an open-source .NET API Gateway that provides routing, authentication, authorization, rate limiting, load balancing, caching, and service discovery for microservices architectures. It is con
  name: Ocelot API Gateway
  slug: ocelot-gateway
- description: Obtain access tokens for the Administration API
  name: Ocelot Authentication API
  slug: ocelot-authentication-api
- description: Clear output cache regions
  name: Ocelot Cache API
  slug: ocelot-cache-api
- description: Read and update the active gateway configuration
  name: Ocelot Configuration API
  slug: ocelot-configuration-api
artifact_total: 11
collections:
- collection_type: open
  name: Ocelot Administration API
  slug: open-ocelot-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ocelot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocelot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ocelot-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ocelot.readthedocs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ocelot.readthedocs.io/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ThreeMammals/Ocelot/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThreeMammals/Ocelot
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ThreeMammals/Ocelot
- group: operate
  title: ''
  type: Community
  url: https://github.com/ThreeMammals/Ocelot/discussions
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/ThreeMammals/Ocelot/issues
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Ocelot
created: '2026-03-16'
description: Ocelot is an open-source API Gateway built with .NET for microservices architectures. It provides routing, authentication, rate limiting, load balancing, and service discovery features for managing and securing APIs in .NET ecosystems.
finops:
- name: Ocelot Finops
  service_category: API
  slug: ocelot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ocelot.png
layout: provider
modified: '2026-05-19'
name: Ocelot
nav: Providers
network: true
overview: 'Ocelot publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Cache API, and Configuration API. Tagged areas include .NET, API Gateway, Microservices, and Open Source.


  Ocelot''s developer surface includes authentication, documentation, getting-started guide, changelog, and 8 more developer resources.'
plans:
- name: Ocelot Plans Pricing
  plan_count: 3
  slug: ocelot-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Ocelot Rate Limits
  slug: ocelot-rate-limits
score:
  band: developing
  composite: 43.1
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.5
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocelot/refs/heads/main/screenshots/ocelot-2026-06-20T190607.png
security:
- kind: authentication
  name: Ocelot Authentication
  slug: ocelot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ocelot Domain Security
  slug: ocelot-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ocelot
tags:
- .NET
- API Gateway
- Microservices
- Open Source
website: https://ocelot.readthedocs.io/
---
