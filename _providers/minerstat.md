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
- acting_count: 0
  human_in_the_loop: 0
  name: Minerstat Agentic Access
  operation_count: 1
  slug: minerstat-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Mining pool data
  name: Minerstat Pools API
  slug: minerstat-pools-api
artifact_total: 8
collections:
- collection_type: open
  name: Minerstat Mining Pools API
  slug: open-minerstat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/minerstat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minerstat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/minerstat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/minerstat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/minerstatcom
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/@minerstat
created: '2025-03-01'
description: Minerstat mining pools API is a public API that allows you to obtain basic information about different mining pools that are listed on minerstat. This documentation will help you understand which data is available in the public API and how the data can be used. Before you continue with reading this documentation and using this API, please read terms and conditions carefully and follow them appropriately as by using our API you agree with the terms and conditions.
finops:
- name: Minerstat Finops
  service_category: API
  slug: minerstat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/minerstat.png
layout: provider
modified: '2026-05-19'
name: Minerstat
nav: Providers
network: true
overview: 'Minerstat publishes 1 API on the [APIs.io](https://apis.io/) network: Pools API. Tagged areas include Mining, Cryptocurrency, and Mining Pools.


  Minerstat''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Minerstat Plans Pricing
  plan_count: 3
  slug: minerstat-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Minerstat Rate Limits
  slug: minerstat-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 13.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/minerstat/refs/heads/main/screenshots/minerstat-2026-06-20T185609.png
security:
- kind: authentication
  name: Minerstat Authentication
  slug: minerstat-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Minerstat Domain Security
  slug: minerstat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: minerstat
tags:
- Mining
- Cryptocurrency
- Mining Pools
---
