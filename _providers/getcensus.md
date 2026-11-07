---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-11-06'
api_count: 7
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
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: declared
  description: Destination connections to operational systems
  name: Census Destinations API
  slug: getcensus-destinations-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: declared
  description: Modeled queries that drive activations
  name: Census Models API
  slug: getcensus-models-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: declared
  description: Audience segments
  name: Census Segments API
  slug: getcensus-segments-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: declared
  description: Source connections to data warehouses
  name: Census Sources API
  slug: getcensus-sources-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: declared
  description: Sync executions
  name: Census Sync Runs API
  slug: getcensus-syncruns-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: declared
  description: Sync configurations
  name: Census Syncs API
  slug: getcensus-syncs-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: declared
  description: Organization-level workspace management
  name: Census Workspaces API
  slug: getcensus-workspaces-api
artifact_total: 27
asyncapis:
- description: ''
  name: Getcensus Sync Lifecycle Webhooks
  slug: getcensus-sync-lifecycle-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/getcensus/security/getcensus-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getcensus-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/getcensus/security/getcensus-domain-security.yml
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
  href: https://artifacts.apis.io/getcensus/plans/getcensus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getcensus-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/getcensus/rate-limits/getcensus-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getcensus-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/getcensus/finops/getcensus-finops.yml
  title: ''
  type: FinOps
  url: finops/getcensus-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://whatsnew.getcensus.com/
- group: operate
  href: https://artifacts.apis.io/getcensus/changelog/getcensus-changelog.yml
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
  href: https://artifacts.apis.io/getcensus/authentication/getcensus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getcensus-authentication.yml
- group: design
  href: https://artifacts.apis.io/getcensus/conventions/getcensus-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getcensus-conventions.yml
- group: design
  href: https://artifacts.apis.io/getcensus/conformance/getcensus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getcensus-conformance.yml
- group: design
  href: https://artifacts.apis.io/getcensus/data-model/getcensus-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getcensus-data-model.yml
- group: design
  href: https://artifacts.apis.io/getcensus/lifecycle/getcensus-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getcensus-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/getcensus/asyncapi/getcensus-sync-lifecycle-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/getcensus-sync-lifecycle-webhooks.yml
- group: build
  href: https://artifacts.apis.io/getcensus/packages/getcensus-packages.yml
  title: ''
  type: Packages
  url: packages/getcensus-packages.yml
- group: build
  href: https://artifacts.apis.io/getcensus/packages/getcensus-packages.yml
  title: ''
  type: SDKs
  url: packages/getcensus-packages.yml
- group: design
  href: https://artifacts.apis.io/getcensus/components/getcensus-components.yml
  title: ''
  type: Components
  url: components/getcensus-components.yml
- group: agent
  href: https://artifacts.apis.io/getcensus/llms/getcensus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getcensus-llms.txt
created: '2026-06-13'
description: Census (now Fivetran Activations) is a reverse ETL platform that syncs data from data warehouses to CRM, marketing, advertising, and other business destinations. It enables data teams to define SQL-based models and segments, then automatically activate that data to over 200 destinations including Salesforce, HubSpot, Facebook Ads, and Google Ads without writing custom integrations.
finops:
- has_sources: true
  method: derived
  name: Getcensus Finops
  primary_unit: model run
  service_category: ''
  slug: getcensus-finops
  template: false
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
overview: 'Census publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Management API, Destinations API, Models API, and 15 more. Tagged areas include Sync, Census, Reverse ETL, Data Activation, and Data Warehouse.


  The Census catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Census'' developer surface includes documentation, engineering blog, pricing, changelog, API reference, support, signup flow, and 27 more developer resources.'
plans:
- name: Getcensus Plans Pricing
  plan_count: 9
  slug: getcensus-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Getcensus Rate Limits
  slug: getcensus-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Census API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: getcensus-rules
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.5
    catalog_earned_first_party: 20.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 56.1
    developer_ergonomics: 66.7
    discoverability: 62.5
    operational_transparency: 65.8
  previous_composite: 64.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/getcensus/getcensus-2026-06-20T181807.png
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
- Sync
- Census
- Reverse ETL
- Data Activation
- Data Warehouse
- CRM
- Marketing Automation
- Segments
- SQL
website: https://www.getcensus.com/
---
