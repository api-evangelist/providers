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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Census Ci Agentic Access
  operation_count: 28
  slug: census-ci-agentic-access
  summary_line: 28 operations · 10 acting
api_count: 1
apis:
- description: The Connectors API from Census — 2 operation(s) for connectors.
  name: Census Connectors API
  slug: census-ci-connectors-api
- description: The Datasets and Models API from Census — 3 operation(s) for datasets and models.
  name: Census Datasets and Models API
  slug: census-ci-datasets-and-models-api
- description: The Destinations API from Census — 3 operation(s) for destinations.
  name: Census Destinations API
  slug: census-ci-destinations-api
- description: The Segments API from Census — 2 operation(s) for segments.
  name: Census Segments API
  slug: census-ci-segments-api
- description: The Sources API from Census — 3 operation(s) for sources.
  name: Census Sources API
  slug: census-ci-sources-api
- description: The Sync Runs API from Census — 3 operation(s) for sync runs.
  name: Census Sync Runs API
  slug: census-ci-sync-runs-api
- description: The Syncs API from Census — 3 operation(s) for syncs.
  name: Census Syncs API
  slug: census-ci-syncs-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Census Management Connectors API
  slug: open-census-ci-connectors-api
- collection_type: open
  name: Census Management Connectors Datasets and Models API
  slug: open-census-ci-datasets-and-models-api
- collection_type: open
  name: Census Management Connectors Destinations API
  slug: open-census-ci-destinations-api
- collection_type: open
  name: Census Management Connectors Segments API
  slug: open-census-ci-segments-api
- collection_type: open
  name: Census Management Connectors Sources API
  slug: open-census-ci-sources-api
- collection_type: open
  name: Census Management Connectors Sync Runs API
  slug: open-census-ci-sync-runs-api
- collection_type: open
  name: Census Management Connectors Syncs API
  slug: open-census-ci-syncs-api
- collection_type: open
  name: Census Management API
  slug: open-census-ci
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/census-ci-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/census-ci-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/census-ci-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/census-ci-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sutrolabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getcensus
- group: company
  title: ''
  type: Website
  url: https://www.getcensus.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getcensus.com
- group: commercial
  title: ''
  type: Plans
  url: plans/census-ci-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/census-ci-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/census-ci-finops.yml
created: '2026-07-01'
description: Census is a reverse ETL and data activation platform that syncs modeled data out of the cloud data warehouse into 200+ business tools (CRM, ads, marketing, support, and analytics), plus an Audience Hub for building and activating segments. The Census Management API (base https://app.getcensus.com/api/v1, Bearer workspace token) lets teams manage sources, destinations, syncs, sync runs, datasets/models, connections, and segments/audiences programmatically.
finops:
- name: Census Ci Finops
  service_category: Data Integration and Activation
  slug: census-ci-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/census-ci.png
layout: provider
modified: '2026-07-01'
name: Census
nav: Providers
network: true
overview: 'Census publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Connectors API, Datasets and Models API, Destinations API, and 4 more. Tagged areas include Reverse ETL, Data Activation, Data Warehouse, Syncs, and Audience Hub.


  Census'' developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Census Ci Plans Pricing
  plan_count: 3
  slug: census-ci-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Census Ci Rate Limits
  slug: census-ci-rate-limits
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/census-ci/refs/heads/main/screenshots/census-ci-2026-07-25T204919.png
security:
- kind: authentication
  name: Census Ci Authentication
  slug: census-ci-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Census Ci Domain Security
  slug: census-ci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Census Ci Trust Center
  slug: census-ci-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: census-ci
tags:
- Reverse ETL
- Data Activation
- Data Warehouse
- Syncs
- Audience Hub
- Data Marketing
website: https://www.getcensus.com
---
