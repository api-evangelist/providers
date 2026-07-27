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
- acting_count: 2
  human_in_the_loop: 0
  name: Marginalia Search Agentic Access
  operation_count: 5
  slug: marginalia-search-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 2
apis:
- description: Manage named search filters (new API only).
  name: Marginalia Search Filters API
  slug: marginalia-search-filters-api
- description: Search the Marginalia index.
  name: Marginalia Search Search API
  slug: marginalia-search-search-api
artifact_total: 9
collections:
- collection_type: open
  name: Marginalia Search API
  slug: open-marginalia-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marginalia-search-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marginalia-search-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marginalia-search-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://marginalia-search.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MarginaliaSearch
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@marginalia-search.com
created: '2025-02-06'
description: Marginalia Search is an independent search engine focused on non-commercial content. Its API is accessible through api2.marginalia-search.com (current) and the legacy api.marginalia.nu / api.marginalia-search.com endpoints, and allows developers to perform web searches against the Marginalia index.
finops:
- name: Marginalia Search Finops
  service_category: API
  slug: marginalia-search-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marginalia-search.png
layout: provider
modified: '2026-05-19'
name: Marginalia Search
nav: Providers
network: true
overview: 'Marginalia Search publishes 2 APIs on the [APIs.io](https://apis.io/) network: Filters API and Search API. Tagged areas include Open Source, Search, and Web Search.


  Marginalia Search''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Marginalia Search Plans Pricing
  plan_count: 3
  slug: marginalia-search-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Marginalia Search Rate Limits
  slug: marginalia-search-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marginalia-search/refs/heads/main/screenshots/marginalia-search-2026-06-20T184938.png
security:
- kind: authentication
  name: Marginalia Search Authentication
  slug: marginalia-search-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marginalia Search Domain Security
  slug: marginalia-search-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: marginalia-search
tags:
- Open Source
- Search
- Web Search
website: https://marginalia-search.com/
---
