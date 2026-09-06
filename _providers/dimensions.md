---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dimensions Agentic Access
  operation_count: 2
  slug: dimensions-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: 'The Dimensions Analytics API provides programmatic access to the Dimensions research data platform via the Dimensions Search Language (DSL). It supports queries against publications, grants, patents, '
  name: Dimensions Analytics API
  slug: dimensions-analytics-api
- baseURL: https://app.dimensions.ai/api
  baseurl_source: declared
  description: The Authentication API from Dimensions — 1 operation(s) for authentication.
  name: Dimensions Authentication API
  slug: dimensions-authentication-api
- baseURL: https://app.dimensions.ai/api
  baseurl_source: declared
  description: The Query API from Dimensions — 1 operation(s) for query.
  name: Dimensions Query API
  slug: dimensions-query-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dimensions Analytics Authentication API
  slug: open-dimensions-authentication-api
- collection_type: open
  name: Dimensions Analytics Authentication Query API
  slug: open-dimensions-query-api
- collection_type: open
  name: Dimensions Analytics API
  slug: open-dimensions
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/digital-science/dimcli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/digital-science/dimcli/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/digital-science/dimcli/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dimensions-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dimensions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dimensions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dimensions.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dimensions.ai/dsl/
- group: operate
  title: ''
  type: Support
  url: https://plus.dimensions.ai/support/
- group: company
  title: ''
  type: Blog
  url: https://www.dimensions.ai/blog/
created: '2025-02-06'
description: Dimensions is a research data platform from Digital Science providing access to publications, grants, patents, clinical trials, datasets, and policy documents. The Dimensions Analytics API offers programmatic access to this research data via the Dimensions Search Language (DSL), enabling citation analysis, researcher discovery, organization benchmarking, and topic identification. The API is subscription-only and is not intended for bulk data extraction or to power dashboards or other derivative products.
finops:
- name: Dimensions Finops
  service_category: API
  slug: dimensions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dimensions.png
layout: provider
modified: '2026-04-28'
name: Dimensions
nav: Providers
network: true
overview: 'Dimensions publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Query API. Tagged areas include Analytics, Research, Publications, Grants, and Patents.


  Dimensions'' developer surface includes authentication, documentation, support, engineering blog, and 6 more developer resources.'
plans:
- name: Dimensions Plans Pricing
  plan_count: 3
  slug: dimensions-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Dimensions Rate Limits
  slug: dimensions-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dimensions/refs/heads/main/screenshots/dimensions-2026-06-20T180036.png
security:
- kind: authentication
  name: Dimensions Authentication
  slug: dimensions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dimensions Domain Security
  slug: dimensions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dimensions
tags:
- Analytics
- Research
- Publications
- Grants
- Patents
- Clinical Trials
- Jupyter Notebooks
website: https://www.dimensions.ai/
---
