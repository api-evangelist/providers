---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Bureau Of Investigation Agentic Access
  operation_count: 1
  slug: federal-bureau-of-investigation-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: The FBI Crime Data Explorer (CDE) provides public access to Uniform Crime Reporting (UCR) data through a JSON API. The API exposes summary statistics, agency-level participation, offense and arrest co
  name: FBI Crime Data Explorer
  slug: crime-data-explorer
- description: The List API from Federal Bureau of Investigation — 1 operation(s) for list.
  name: Federal Bureau of Investigation List API
  slug: federal-bureau-of-investigation-list-api
artifact_total: 8
collections:
- collection_type: open
  name: FBI Most Wanted
  slug: open-most-wanted-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-bureau-of-investigation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-bureau-of-investigation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fbi-cde
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fbi
- group: company
  title: ''
  type: Website
  url: https://www.fbi.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fbi.gov/services
created: '2024-10-18'
description: The Federal Bureau of Investigation (FBI) is the domestic intelligence and security service of the United States and its principal federal law enforcement agency. The FBI publishes public APIs covering its Most Wanted program and Uniform Crime Reporting (UCR) data through the Crime Data Explorer.
finops:
- name: Federal Bureau Of Investigation Finops
  service_category: API
  slug: federal-bureau-of-investigation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-bureau-of-investigation.png
layout: provider
modified: '2026-05-19'
name: Federal Bureau of Investigation
nav: Providers
network: true
overview: 'Federal Bureau of Investigation publishes 1 API on the [APIs.io](https://apis.io/) network: List API. Tagged areas include FBI and Federal Government.


  Federal Bureau of Investigation''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Federal Bureau Of Investigation Plans Pricing
  plan_count: 3
  slug: federal-bureau-of-investigation-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Federal Bureau Of Investigation Rate Limits
  slug: federal-bureau-of-investigation-rate-limits
score:
  band: thin
  composite: 30.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 46.9
    developer_ergonomics: 8.7
    discoverability: 47.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-bureau-of-investigation/refs/heads/main/screenshots/federal-bureau-of-investigation-2026-06-20T181110.png
security:
- kind: domain-security
  name: Federal Bureau Of Investigation Domain Security
  slug: federal-bureau-of-investigation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-bureau-of-investigation
tags:
- FBI
- Federal Government
website: https://www.fbi.gov/
---
