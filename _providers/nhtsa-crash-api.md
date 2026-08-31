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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nhtsa Crash Api Agentic Access
  operation_count: 6
  slug: nhtsa-crash-api-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Case list and case detail lookups
  name: NHTSA Crash API Cases API
  slug: nhtsa-crash-api-cases-api
- description: Crash queries by location, vehicle, and occupant
  name: NHTSA Crash API Crashes API
  slug: nhtsa-crash-api-crashes-api
- description: Fatality Analysis Reporting System datasets and queries
  name: NHTSA Crash API FARS API
  slug: nhtsa-crash-api-fars-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NHTSA Crash Data Cases API
  slug: open-nhtsa-crash-api-cases-api
- collection_type: open
  name: NHTSA Crash Data Cases Crashes API
  slug: open-nhtsa-crash-api-crashes-api
- collection_type: open
  name: NHTSA Crash Data Cases FARS API
  slug: open-nhtsa-crash-api-fars-api
- collection_type: open
  name: NHTSA Crash Data API
  slug: open-nhtsa-crash-api-nhtsa-crash-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nhtsa-crash-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nhtsa-crash-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nhtsa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://crashviewer.nhtsa.dot.gov/CrashAPI
- group: operate
  title: ''
  type: Support
  url: https://www.nhtsa.gov/contact
created: '2026-03-16'
description: The NHTSA Crash Data API provides access to the National Highway Traffic Safety Administration's crash data including crash reports, vehicle information, and safety statistics collected through the Fatality Analysis Reporting System (FARS) and Crash Report Sampling System (CRSS).
finops:
- name: Nhtsa Crash Api Finops
  service_category: API
  slug: nhtsa-crash-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nhtsa-crash-api.png
layout: provider
modified: '2026-05-19'
name: NHTSA Crash API
nav: Providers
network: true
overview: 'NHTSA Crash API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cases API, Crashes API, and FARS API. Tagged areas include Crash Data, Government, NHTSA, Traffic Safety, and Transportation.


  NHTSA Crash API''s developer surface includes documentation, support, and 3 more developer resources.'
plans:
- name: Nhtsa Crash Api Plans Pricing
  plan_count: 3
  slug: nhtsa-crash-api-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Nhtsa Crash Api Rate Limits
  slug: nhtsa-crash-api-rate-limits
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 65.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nhtsa-crash-api/refs/heads/main/screenshots/nhtsa-crash-api-2026-06-20T190316.png
security:
- kind: domain-security
  name: Nhtsa Crash Api Domain Security
  slug: nhtsa-crash-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nhtsa-crash-api
tags:
- Crash Data
- Government
- NHTSA
- Traffic Safety
- Transportation
website: https://www.nhtsa.gov/
---
