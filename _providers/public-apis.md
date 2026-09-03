---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Public Apis Agentic Access
  operation_count: 4
  slug: public-apis-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: A collective list of free APIs organized by category including Animals, Finance, Weather, Geocoding, Government, Health, Machine Learning, Sports, and 40+ more categories for developers to discover an
  name: Public APIs Directory
  slug: public-apis-directory
- baseURL: https://api.publicapis.org
  baseurl_source: declared
  description: Endpoints for category metadata.
  name: Public APIs Categories API
  slug: public-apis-categories-api
- baseURL: https://api.publicapis.org
  baseurl_source: declared
  description: Endpoints for listing API directory entries.
  name: Public APIs Entries API
  slug: public-apis-entries-api
- baseURL: https://api.publicapis.org
  baseurl_source: declared
  description: Service health check.
  name: Public APIs Health API
  slug: public-apis-health-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Public APIs Categories API
  slug: open-public-apis-categories-api
- collection_type: open
  name: Public APIs Categories Entries API
  slug: open-public-apis-entries-api
- collection_type: open
  name: Public APIs Categories Health API
  slug: open-public-apis-health-api
- collection_type: open
  name: Public APIs API
  slug: open-public-apis
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/public-apis/public-apis/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/public-apis/public-apis/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/public-apis-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/public-apis
- group: docs
  title: ''
  type: Contributing Guide
  url: https://github.com/public-apis/public-apis/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/public-apis/public-apis/blob/master/LICENSE
created: '2026-03-26'
description: Public APIs is a community-curated collective list of over 1,400 free APIs organized across 50+ categories, maintained by contributors and the team at APILayer. It is one of the most popular open-source projects on GitHub with over 400k stars. A companion REST API (davemachado/public-api) exposes the directory data programmatically over HTTPS with no authentication.
finops:
- name: Public Apis Finops
  service_category: API
  slug: public-apis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/public-apis.png
layout: provider
modified: '2026-05-19'
name: Public APIs
nav: Providers
network: true
overview: 'Public APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Categories API, Entries API, and Health API. Tagged areas include API Aggregation, API Directory, API Discovery, Free APIs, and Open-Source.'
plans:
- name: Public Apis Plans Pricing
  plan_count: 3
  slug: public-apis-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Public Apis Rate Limits
  slug: public-apis-rate-limits
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 65.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 25.0
  previous_composite: 20.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/public-apis/refs/heads/main/screenshots/public-apis-2026-06-20T192252.png
slug: public-apis
tags:
- API Aggregation
- API Directory
- API Discovery
- Free APIs
- Open-Source
---
