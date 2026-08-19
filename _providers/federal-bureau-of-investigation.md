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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FBI Most Wanted List API
  slug: open-federal-bureau-of-investigation-list-api
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
random_paper: 147
rate_limits:
- limit_count: 5
  name: Federal Bureau Of Investigation Rate Limits
  slug: federal-bureau-of-investigation-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -3.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 23.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
