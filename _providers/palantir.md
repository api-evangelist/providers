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
- acting_count: 1
  human_in_the_loop: 0
  name: Palantir Agentic Access
  operation_count: 3
  slug: palantir-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 4
apis:
- description: Palantir Foundry API provides programmatic access to data integration, transformation, and analysis workflows within the Palantir Foundry platform. The v2 API uses OAuth 2.0 and JSON, with endpoints o
  name: Palantir Foundry API
  slug: palantir-foundry-api
- description: The Admin - Groups API from Palantir — 1 operation(s) for admin - groups.
  name: Palantir Admin - Groups API
  slug: palantir-admin-groups-api
- description: The Admin - Users API from Palantir — 1 operation(s) for admin - users.
  name: Palantir Admin - Users API
  slug: palantir-admin-users-api
- description: The Datasets API from Palantir — 1 operation(s) for datasets.
  name: Palantir Datasets API
  slug: palantir-datasets-api
artifact_total: 12
collections:
- collection_type: open
  name: Palantir Foundry API v2
  slug: open-palantir
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/palantir-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/palantir-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palantir-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/palantir-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/palantir
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/palantir-technologies
- group: start
  title: ''
  type: Portal
  url: https://www.palantir.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.palantir.com/docs/foundry/
- group: company
  title: ''
  type: Website
  url: https://www.palantir.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.palantir.com/privacy-and-security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.palantir.com/terms-of-service/
- group: company
  title: ''
  type: Blog
  url: https://blog.palantir.com/feed
created: '2025-03-01'
description: Palantir is a data analytics company providing software platforms for organizations to integrate, analyze, and visualize data. Palantir Foundry and AIP provide REST APIs for data workflows, AI operations, ontology management, orchestration, and decision-making across enterprise and government use cases.
finops:
- name: Palantir Finops
  service_category: API
  slug: palantir-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/palantir.png
layout: provider
modified: '2026-04-28'
name: Palantir
nav: Providers
network: true
overview: 'Palantir publishes 3 APIs on the [APIs.io](https://apis.io/) network: Admin - Groups API, Admin - Users API, and Datasets API. Tagged areas include AI Platform, Data Analytics, Enterprise, and Government.


  Palantir''s developer surface includes authentication, developer portal, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Palantir Plans Pricing
  plan_count: 3
  slug: palantir-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Palantir Rate Limits
  slug: palantir-rate-limits
score:
  band: developing
  composite: 47.2
  delta: 1.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 30.4
    discoverability: 75.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.5
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 56.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/palantir/refs/heads/main/screenshots/palantir-2026-06-20T191326.png
security:
- kind: authentication
  name: Palantir Authentication
  slug: palantir-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Palantir Domain Security
  slug: palantir-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Palantir Vulnerability Disclosure
  slug: palantir-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: palantir
tags:
- AI Platform
- Data Analytics
- Enterprise
- Government
website: https://www.palantir.com/
---
