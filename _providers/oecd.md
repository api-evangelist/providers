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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Oecd Agentic Access
  operation_count: 6
  slug: oecd-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: The OECD provides programmatic access to OECD data through an application programming interface (API) based on the SDMX standard. These APIs are free of charge and are offered subject to your acceptan
  name: OECD Data API
  slug: oecd
- description: The Data API from OECD — 2 operation(s) for data.
  name: OECD Data API
  slug: oecd-data-api
- description: The Structure API from OECD — 4 operation(s) for structure.
  name: OECD Structure API
  slug: oecd-structure-api
artifact_total: 9
collections:
- collection_type: open
  name: OECD SDMX REST API
  slug: open-oecd
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oecd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oecd-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OECD
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oecd
- group: company
  title: ''
  type: Website
  url: https://www.oecd.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oecd.org/termsandconditions/
created: '2025-02-06'
description: The OECD provides programmatic access to OECD data through an application programming interface (API) based on the SDMX standard. These APIs are free of charge and are offered subject to your acceptance of OECD Terms and Conditions.
finops:
- name: Oecd Finops
  service_category: API
  slug: oecd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oecd.png
layout: provider
modified: '2026-04-28'
name: OECD
nav: Providers
network: true
overview: 'OECD publishes 2 APIs on the [APIs.io](https://apis.io/) network: Data API and Structure API. Tagged areas include Data, Statistics, Economics, and SDMX.'
plans:
- name: Oecd Plans Pricing
  plan_count: 3
  slug: oecd-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Oecd Rate Limits
  slug: oecd-rate-limits
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.2
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Oecd Domain Security
  slug: oecd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oecd
tags:
- Data
- Statistics
- Economics
- SDMX
website: https://www.oecd.org/
---
