---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.getcensus.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.fivetran.com/ — a different registrable domain (getcensus.com -> fivetran.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
api_count: 18
apis:
- description: The Census Management REST API allows developers to programmatically manage syncs, connections, models, segments, and destinations within Census workspaces and organizations. Supports both workspace-l
  name: Census Management API
  slug: census-management-api
- description: The Census Activations REST API (formerly Census Management API) lets teams programmatically manage reverse ETL pipelines, sources, models, destinations, syncs, and sync runs. The API is region-scoped
  name: Census Activations REST API
  slug: census-activations-api
- description: 'Custom Destinations API lets partners declare the type of data a destination can process, the operations allowed on that data, and the loading mechanism so that Activations can orchestrate loads into '
  name: Census Custom Destinations API
  slug: census-custom-destinations-api
- description: Connect Links enable embedded Activations flows for Powered by Fivetran partners, letting end users configure destinations and syncs from within a host application via hosted URLs.
  name: Census Connect Links (Powered by Fivetran)
  slug: census-connect-links-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Destination connections to operational systems
  name: Census Destinations API
  slug: census-destinations-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Modeled queries that drive activations
  name: Census Models API
  slug: census-models-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Audience segments
  name: Census Segments API
  slug: census-segments-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Source connections to data warehouses
  name: Census Sources API
  slug: census-sources-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Sync executions
  name: Census SyncRuns API
  slug: census-syncruns-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Sync configurations
  name: Census Syncs API
  slug: census-syncs-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Organization-level workspace management
  name: Census Workspaces API
  slug: census-workspaces-api
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
artifact_total: 26
asyncapis:
- description: ''
  name: Getcensus Sync Lifecycle Webhooks
  slug: getcensus-sync-lifecycle-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/getcensus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getcensus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcensus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fivetran.com/docs/activations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sutrolabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getcensus
- group: company
  title: ''
  type: Blog
  url: https://www.getcensus.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fivetran.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getcensus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getcensus
- group: commercial
  title: ''
  type: Plans
  url: plans/getcensus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getcensus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/getcensus-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://whatsnew.getcensus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/getcensus-changelog.yml
- group: other
  title: ''
  type: Terraform
  url: https://fivetran.com/docs/activations/rest-api/terraform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fivetran.com/docs/activations/rest-api
- group: docs
  title: ''
  type: APIReference
  url: https://fivetran.com/docs/activations/rest-api/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://support.fivetran.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.getcensus.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fivetran.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fivetran.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/getcensus/workspace/census-api/overview
- group: auth
  title: ''
  type: Compliance
  url: https://www.fivetran.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/getcensus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getcensus-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/getcensus-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getcensus-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getcensus-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/getcensus-sync-lifecycle-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/getcensus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/getcensus-packages.yml
- group: design
  title: ''
  type: Components
  url: components/getcensus-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getcensus-llms.txt
created: '2026-06-13'
description: Census (now Fivetran Activations) is a reverse ETL platform that syncs data from data warehouses to CRM, marketing, advertising, and other business destinations. It enables data teams to define SQL-based models and segments, then automatically activate that data to over 200 destinations including Salesforce, HubSpot, Facebook Ads, and Google Ads without writing custom integrations.
finops:
- name: Getcensus Finops
  service_category: ''
  slug: getcensus-finops
graphqls:
- description: Census (now Fivetran Activations) is a reverse ETL and data activation platform that syncs data from cloud data warehouses such as Snowflake, BigQuery, Databricks, and Redshift into operational SaaS a
  name: Census GraphQL API
  slug: census-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getcensus.png
layout: provider
modified: '2026-08-13'
name: Census
nav: Providers
network: true
overview: 'Census publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Management API, Destinations API, Models API, and 5 more. Tagged areas include Reverse ETL, Data Activation, Data Warehouse, CRM, and Marketing Automation.


  The Census catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Census'' developer surface includes documentation, engineering blog, pricing, changelog, API reference, support, signup flow, and 27 more developer resources.'
plans:
- name: Getcensus Plans Pricing
  plan_count: 4
  slug: getcensus-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Getcensus Rate Limits
  slug: getcensus-rate-limits
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 58.0
    catalog_earned_first_party: 20.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 11.4
    developer_ergonomics: 66.7
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 55.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/getcensus/refs/heads/main/screenshots/getcensus-2026-06-20T181807.png
security:
- kind: authentication
  name: Getcensus Authentication
  slug: getcensus-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Getcensus Domain Security
  slug: getcensus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getcensus Trust Center
  slug: getcensus-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: getcensus
tags:
- Reverse ETL
- Data Activation
- Data Warehouse
- CRM
- Marketing Automation
- Segments
- Syncs
- SQL
website: https://www.getcensus.com/
---
