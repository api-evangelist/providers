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
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Oecd Agentic Access
  operation_count: 6
  slug: oecd-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: The OECD provides programmatic access to OECD data through an application programming interface (API) based on the SDMX standard. These APIs are free of charge and are offered subject to your acceptan
  name: OECD Data API
  slug: oecd
- baseURL: https://sdmx.oecd.org/public/rest
  baseurl_source: declared
  description: The Data API from OECD — 2 operation(s) for data.
  name: OECD Data API
  slug: oecd-data-api
- baseURL: https://sdmx.oecd.org/public/rest
  baseurl_source: declared
  description: The Structure API from OECD — 4 operation(s) for structure.
  name: OECD Structure API
  slug: oecd-structure-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OECD SDMX REST Data API
  slug: open-oecd-data-api
- collection_type: open
  name: OECD SDMX REST Data Structure API
  slug: open-oecd-structure-api
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
random_paper: 12
rate_limits:
- limit_count: 5
  name: Oecd Rate Limits
  slug: oecd-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 65.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oecd/refs/heads/main/screenshots/oecd-2026-08-07T190012.png
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
