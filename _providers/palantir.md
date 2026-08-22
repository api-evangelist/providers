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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Palantir Foundry API v2 Admin - Groups API
  slug: open-palantir-admin-groups-api
- collection_type: open
  name: Palantir Foundry API v2 Admin - Groups Admin - Users API
  slug: open-palantir-admin-users-api
- collection_type: open
  name: Palantir Foundry API v2 Admin - Groups Datasets API
  slug: open-palantir-datasets-api
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
random_paper: 19
rate_limits:
- limit_count: 5
  name: Palantir Rate Limits
  slug: palantir-rate-limits
score:
  band: thin
  composite: 28.0
  delta: -9.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 11.9
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 33.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
