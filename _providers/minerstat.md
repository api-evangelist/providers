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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Minerstat Agentic Access
  operation_count: 1
  slug: minerstat-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.minerstat.com/v2
  baseurl_source: declared
  description: Mining pool data
  name: Minerstat Pools API
  slug: minerstat-pools-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Minerstat Mining Pools API
  slug: open-minerstat-pools-api
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
random_paper: 17
rate_limits:
- limit_count: 5
  name: Minerstat Rate Limits
  slug: minerstat-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
