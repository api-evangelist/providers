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
- acting_count: 3
  human_in_the_loop: 0
  name: Semrush Agentic Access
  operation_count: 6
  slug: semrush-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- description: The Hermes Partner API API from Semrush — 4 operation(s) for hermes partner api.
  name: Semrush Hermes Partner API API
  slug: semrush-hermes-partner-api-api
- description: The JWT Issuer API from Semrush — 1 operation(s) for jwt issuer.
  name: Semrush JWT Issuer API
  slug: semrush-jwt-issuer-api
- description: The Partner Service API from Semrush — 1 operation(s) for partner service.
  name: Semrush Partner Service API
  slug: semrush-partner-service-api
artifact_total: 11
collections:
- collection_type: open
  name: Semrush
  slug: open-semrush
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/semrush-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semrush-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/semrush-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/semrush
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semrush
created: '2024-11-14'
description: SEMrush is an all-in-one digital marketing tool that helps businesses improve their online visibility and attract more customers. This powerful software provides a range of tools and features for keyword research, website analysis, competitive analysis, and more. With SEMrush, businesses can track their online rankings, discover new keywords to target, analyze their competitors' strategies, and optimize their website for better search engine performance.
finops:
- name: Semrush Finops
  service_category: API
  slug: semrush-finops
graphqls:
- description: 'Semrush is an online marketing analytics platform. The API covers keyword research, domain analytics, backlink data, site audit, position tracking, content analysis, advertising research, and traffic '
  name: Semrush GraphQL API
  slug: semrush-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semrush.png
layout: provider
modified: '2026-05-19'
name: Semrush
nav: Providers
network: true
overview: 'Semrush publishes 3 APIs on the [APIs.io](https://apis.io/) network: Hermes Partner API API, JWT Issuer API, and Partner Service API. Tagged areas include Data and Search Engines.


  Semrush''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Semrush Plans Pricing
  plan_count: 3
  slug: semrush-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Semrush Rate Limits
  slug: semrush-rate-limits
score:
  band: thin
  composite: 34.5
  delta: -1.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.2
    developer_ergonomics: 10.9
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/screenshots/semrush-2026-06-20T193655.png
security:
- kind: authentication
  name: Semrush Authentication
  slug: semrush-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Semrush Domain Security
  slug: semrush-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: semrush
tags:
- Data
- Search Engines
---
