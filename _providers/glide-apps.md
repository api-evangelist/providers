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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Glide Apps Agentic Access
  operation_count: 12
  slug: glide-apps-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.glideapps.com
  baseurl_source: declared
  description: Query a Big Table with SQL.
  name: Glide Queries API
  slug: glide-apps-queries-api
- baseURL: https://api.glideapps.com
  baseurl_source: declared
  description: List, read, add, update, and delete rows in a Big Table.
  name: Glide Rows API
  slug: glide-apps-rows-api
- baseURL: https://api.glideapps.com
  baseurl_source: declared
  description: Stage large data payloads in serial chunks for bulk loads.
  name: Glide Stashes API
  slug: glide-apps-stashes-api
- baseURL: https://api.glideapps.com
  baseurl_source: declared
  description: Create, overwrite, and list Big Tables.
  name: Glide Tables API
  slug: glide-apps-tables-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Glide Queries API
  slug: open-glide-apps-queries-api
- collection_type: open
  name: Glide Queries Rows API
  slug: open-glide-apps-rows-api
- collection_type: open
  name: Glide Queries Stashes API
  slug: open-glide-apps-stashes-api
- collection_type: open
  name: Glide Queries Tables API
  slug: open-glide-apps-tables-api
- collection_type: open
  name: Glide API
  slug: open-glide-apps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/glide-apps-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/glide-apps-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glide-apps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glide-apps-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/glideapps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glideapps
- group: company
  title: ''
  type: Website
  url: https://www.glideapps.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.glideapps.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/glide-apps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/glide-apps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/glide-apps-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.glideapps.com/blog
created: '2026-06-20'
description: Glide is a no-code platform for building custom business apps from your data. The Glide REST API (v2) lets you programmatically work with Glide Big Tables - creating tables, listing and paginating rows, adding, updating, and deleting rows, staging large batches with stashes, and querying tables with SQL - using a Bearer API token.
finops:
- name: Glide Apps Finops
  service_category: Application Development and No-Code
  slug: glide-apps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glide-apps.png
layout: provider
modified: '2026-06-20'
name: Glide
nav: Providers
network: true
overview: 'Glide publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Queries API, Rows API, Stashes API, and 1 more. Tagged areas include No-Code, App Builder, Tables, Big Tables, and Data.


  Glide''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Glide Apps Plans Pricing
  plan_count: 5
  slug: glide-apps-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Glide Apps Rate Limits
  slug: glide-apps-rate-limits
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glide-apps/refs/heads/main/screenshots/glide-apps-2026-06-20T181910.png
security:
- kind: authentication
  name: Glide Apps Authentication
  slug: glide-apps-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Glide Apps Domain Security
  slug: glide-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Glide Apps Trust Center
  slug: glide-apps-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: glide-apps
tags:
- No-Code
- App Builder
- Tables
- Big Tables
- Data
- Artificial Intelligence
website: https://www.glideapps.com
---
