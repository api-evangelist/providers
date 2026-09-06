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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Gooddata Agentic Access
  operation_count: 30
  slug: gooddata-agentic-access
  summary_line: 30 operations · 16 acting
api_count: 1
apis:
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Dashboards API from GoodData — 1 operation(s) for dashboards.
  name: GoodData Dashboards API
  slug: gooddata-dashboards-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Data Sources API from GoodData — 3 operation(s) for data sources.
  name: GoodData Data Sources API
  slug: gooddata-data-sources-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Execution API from GoodData — 2 operation(s) for execution.
  name: GoodData Execution API
  slug: gooddata-execution-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Logical Data Model API from GoodData — 1 operation(s) for logical data model.
  name: GoodData Logical Data Model API
  slug: gooddata-logical-data-model-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Metrics API from GoodData — 2 operation(s) for metrics.
  name: GoodData Metrics API
  slug: gooddata-metrics-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Permissions API from GoodData — 1 operation(s) for permissions.
  name: GoodData Permissions API
  slug: gooddata-permissions-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Users API from GoodData — 3 operation(s) for users.
  name: GoodData Users API
  slug: gooddata-users-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Visualizations API from GoodData — 1 operation(s) for visualizations.
  name: GoodData Visualizations API
  slug: gooddata-visualizations-api
- baseURL: https://{domain}.gooddata.com/api/v1
  baseurl_source: declared
  description: The Workspaces API from GoodData — 2 operation(s) for workspaces.
  name: GoodData Workspaces API
  slug: gooddata-workspaces-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GoodData Cloud Dashboards API
  slug: open-gooddata-dashboards-api
- collection_type: open
  name: GoodData Cloud Dashboards Data Sources API
  slug: open-gooddata-data-sources-api
- collection_type: open
  name: GoodData Cloud Dashboards Execution API
  slug: open-gooddata-execution-api
- collection_type: open
  name: GoodData Cloud Dashboards Logical Data Model API
  slug: open-gooddata-logical-data-model-api
- collection_type: open
  name: GoodData Cloud Dashboards Metrics API
  slug: open-gooddata-metrics-api
- collection_type: open
  name: GoodData Cloud Dashboards Permissions API
  slug: open-gooddata-permissions-api
- collection_type: open
  name: GoodData Cloud Dashboards Users API
  slug: open-gooddata-users-api
- collection_type: open
  name: GoodData Cloud Dashboards Visualizations API
  slug: open-gooddata-visualizations-api
- collection_type: open
  name: GoodData Cloud Dashboards Workspaces API
  slug: open-gooddata-workspaces-api
- collection_type: open
  name: GoodData Cloud API
  slug: open-gooddata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gooddata-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gooddata-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gooddata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gooddata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gooddata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gooddata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gooddata
- group: company
  title: ''
  type: Website
  url: https://www.gooddata.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.gooddata.com/docs/cloud/
- group: commercial
  title: ''
  type: Plans
  url: plans/gooddata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gooddata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gooddata-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gooddata.ai/feed.xml
created: '2026-06-21'
description: GoodData is an analytics and business intelligence platform for building and embedding interactive dashboards, metrics, and self-service analytics. GoodData Cloud exposes a full REST API (Entity, Declarative, and Action APIs) for managing workspaces, data sources, the logical data model, metrics, visualizations, dashboards, AFM executions, users, and permissions, authenticated with a Bearer API token.
finops:
- name: Gooddata Finops
  service_category: Analytics
  slug: gooddata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gooddata.png
layout: provider
name: GoodData
nav: Providers
network: true
overview: 'GoodData publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Data Sources API, Execution API, and 6 more. Tagged areas include Analytics, Business Intelligence, Embedded Analytics, Dashboards, and Data.


  GoodData''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Gooddata Plans Pricing
  plan_count: 3
  slug: gooddata-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Gooddata Rate Limits
  slug: gooddata-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.6
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gooddata/refs/heads/main/screenshots/gooddata-2026-07-25T220051.png
security:
- kind: authentication
  name: Gooddata Authentication
  slug: gooddata-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gooddata Domain Security
  slug: gooddata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gooddata Vulnerability Disclosure
  slug: gooddata-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gooddata Trust Center
  slug: gooddata-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
slug: gooddata
tags:
- Analytics
- Business Intelligence
- Embedded Analytics
- Dashboards
- Data
website: https://www.gooddata.com
---
