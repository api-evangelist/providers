---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 42
  human_in_the_loop: 3
  name: Observeinc Agentic Access
  operation_count: 88
  slug: observeinc-agentic-access
  summary_line: 88 operations · 42 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Read-only subset of the Apache Iceberg REST Catalog protocol served under /v1/iceberg/catalog on each Observe tenant, authenticated with the same Observe API token. Implements the Apache Iceberg spec;
  name: Observe Apache Iceberg REST Catalog API
  slug: iceberg-rest-catalog
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Query monitor alerts. Learn more about [alerts](https://docs.observeinc.com/docs/work-with-alerts).
  name: Observe Alert API
  slug: observeinc-alert-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: The APM API from Observe — 3 operation(s) for apm.
  name: Observe APM API
  slug: observeinc-apm-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: The Dashboards API from Observe — 2 operation(s) for dashboards.
  name: Observe Dashboards API
  slug: observeinc-dashboards-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage datasets. Learn more about [datasets](https://docs.observeinc.com/en/latest/content/reference/ObserveKeyConcepts.html#datasets)..
  name: Observe Dataset API
  slug: observeinc-dataset-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Legacy dataset endpoints. Will be deprecated in the future.
  name: Observe Dataset Legacy API
  slug: observeinc-dataset-legacy-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage dataset query filters. Learn more about [dataset query filters](https://docs.observeinc.com/docs/dataset-query-filters).
  name: Observe Dataset Query Filter API
  slug: observeinc-dataset-query-filter-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Semantic search across Observe's built-in documentation.
  name: Observe Documentation API
  slug: observeinc-documentation-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage drop filters used to reduce ingest volume by dropping a configurable fraction of observations matching an OPAL predicate. Learn more about [drop filters](https://docs.observeinc.com/docs/drop-f
  name: Observe Drop Filters API
  slug: observeinc-drop-filters-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Export query results from Observe.
  name: Observe Export API
  slug: observeinc-export-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: The Ingest Routes API from Observe — 2 operation(s) for ingest routes.
  name: Observe Ingest Routes API
  slug: observeinc-ingest-routes-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: The Ingest Tokens API from Observe — 2 operation(s) for ingest tokens.
  name: Observe Ingest Tokens API
  slug: observeinc-ingest-tokens-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage api tokens. Learn more about [api tokens](https://docs.observeinc.com/en/latest/content/reference/ObserveAPIAuth.html).
  name: Observe Login API
  slug: observeinc-login-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: The Metrics API from Observe — 1 operation(s) for metrics.
  name: Observe Metrics API
  slug: observeinc-metrics-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage monitors. Learn more about [monitors](https://docs.observeinc.com/en/latest/content/monitors/MonitorsIntro.html).
  name: Observe Monitor API
  slug: observeinc-monitor-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage monitor mute rules. Mute rules suppress alert notifications for one or more monitors during a defined time window. Learn more about [monitor mute rules](https://docs.observeinc.com/docs/mute-a-
  name: Observe Monitor Mute API
  slug: observeinc-monitormute-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Search for object tags on objects such as dashboards, datasets, worksheets, etc.
  name: Observe Object Tags API
  slug: observeinc-objecttags-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage reference tables. Learn more about [reference tables](https://docs.observeinc.com/en/latest/content/reference/ReferenceTables.html).
  name: Observe Reference Tables API
  slug: observeinc-referencetables-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: Manage custom AI agent skills for the AI-SRE agent.
  name: Observe Skills API
  slug: observeinc-skills-api
- baseURL: https://{customerid}.observeinc.com
  baseurl_source: declared
  description: The Tags API from Observe — 1 operation(s) for tags.
  name: Observe Tags API
  slug: observeinc-tags-api
- baseURL: https://{customerid}.observeinc.com/v1/iceberg/catalog
  baseurl_source: declared
  description: Manage service accounts and api tokens. Learn more about service accounts.
  name: Observe Service Accounts API
  slug: observeinc-service-accounts-api
- baseURL: https://{customerid}.observeinc.com/v1/iceberg/catalog
  baseurl_source: declared
  description: The Tag Values API from Observe — 1 operation(s) for tag values.
  name: Observe Tag Values API
  slug: observeinc-tag-values-api
artifact_total: 37
common:
- group: commercial
  href: https://artifacts.apis.io/observeinc/finops/observeinc-finops.yml
  title: ''
  type: FinOps
  url: finops/observeinc-finops.yml
- group: auth
  href: https://artifacts.apis.io/observeinc/well-known/observeinc-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/observeinc-www-security.txt
- group: auth
  href: https://artifacts.apis.io/observeinc/well-known/observeinc-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/observeinc-status-security.txt
- group: build
  href: https://artifacts.apis.io/observeinc/integrations/observeinc-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/observeinc-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/observeinc/capabilities/observeinc-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/observeinc-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/observeinc/plans/observeinc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/observeinc-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/observeinc/lifecycle/observeinc-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/observeinc-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/observeinc/agentic-access/observeinc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/observeinc-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/observeinc/rate-limits/observeinc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/observeinc-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/observeinc/rules/observeinc-rules.yml
  title: ''
  type: Spectral
  url: rules/observeinc-rules.yml
- group: design
  href: https://artifacts.apis.io/observeinc/json-ld/observeinc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/observeinc-context.jsonld
- group: design
  href: https://artifacts.apis.io/observeinc/vocabulary/observeinc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/observeinc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/observeinc/data-model/observeinc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/observeinc-data-model.yml
- group: build
  href: https://artifacts.apis.io/observeinc/cli/observeinc-cli.yml
  title: ''
  type: CLI
  url: cli/observeinc-cli.yml
- group: operate
  href: https://artifacts.apis.io/observeinc/changelog/observeinc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/observeinc-changelog.yml
- group: design
  href: https://artifacts.apis.io/observeinc/lifecycle/observeinc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/observeinc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/observeinc/errors/observeinc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/observeinc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/observeinc/conformance/observeinc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/observeinc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/observeinc/llms/observeinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/observeinc-llms.txt
- group: agent
  href: https://artifacts.apis.io/observeinc/mcp/observeinc-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/observeinc-mcp.yml
- group: agent
  href: https://artifacts.apis.io/observeinc/well-known/observeinc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/observeinc-well-known.yml
- group: other
  href: https://artifacts.apis.io/observeinc/hosts/observeinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/observeinc-hosts.yml
- group: other
  href: https://artifacts.apis.io/observeinc/vendors/observeinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/observeinc-vendors.yml
- group: build
  href: https://artifacts.apis.io/observeinc/packages/observeinc-packages.yml
  title: ''
  type: SDKs
  url: packages/observeinc-packages.yml
- group: build
  href: https://artifacts.apis.io/observeinc/packages/observeinc-packages.yml
  title: ''
  type: Packages
  url: packages/observeinc-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.snowflake.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.snowflake.com/en/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.observeinc.com/docs/google-cloud-platform-quickstart-1
- group: auth
  href: https://artifacts.apis.io/observeinc/authentication/observeinc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/observeinc-authentication.yml
- group: auth
  href: https://artifacts.apis.io/observeinc/security/observeinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/observeinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.observeinc.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.observeinc.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.observeinc.com/reference/how-you-can-interact-with-the-observe-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.observeinc.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.snowflake.com/en/legal/privacy/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.snowflake.com/en/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.snowflake.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.snowflake.com/en/pricing-options/
- group: start
  title: ''
  type: SignUp
  url: https://signup.snowflake.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/observeinc
- group: company
  title: ''
  type: Blog
  url: https://www.snowflake.com/en/blog/product-and-technology/?tags=blog%2Fproduct-and-technology%2Fobservability
created: '2026-10-13'
description: 'Observe (Observe, Inc., now "Observe by Snowflake" following its acquisition by Snowflake; www.observeinc.com redirects to snowflake.com/en/product/observe) is an observability platform for logs, metrics, traces and APM built on a data lake and the OPAL query language. Its developer surface lives on docs.observeinc.com: a tenant-scoped REST API (https://{customerid}.observeinc.com/v1, bearer "<customerid> <token>") covering monitors, datasets, ingest and API tokens, reference tables, service accounts and query export, with date-based Observe-Api-Version response versioning; a read-only Apache Iceberg REST Catalog endpoint; a tenant MCP server; a CLI; and a Terraform provider. Snowflake''s own APIs are not credited here.'
finops:
- has_sources: true
  method: derived
  name: Observeinc Finops
  primary_unit: ''
  service_category: ''
  slug: observeinc-finops
  template: true
image: https://www.snowflake.com/content/dam/snowflake-site/general/technical/default-og-image/snowflake-social-share.png
json_schemas:
- name: AlertResource
  property_count: 17
  slug: observeinc-alert-resource
- name: DatasetQueryFilter
  property_count: 14
  slug: observeinc-dataset-query-filter-resource
- name: DatasetResource
  property_count: 40
  slug: observeinc-dataset-resource
- name: IngestFiltersObject
  property_count: 14
  slug: observeinc-ingest-filters-resource
- name: IngestRoutesObject
  property_count: 12
  slug: observeinc-ingest-routes-resource
- name: MonitorResource
  property_count: 37
  slug: observeinc-monitor-resource
jsonld:
- class_count: 120
  name: Observeinc Context
  property_count: 277
  slug: observeinc-context
layout: provider
mcp_servers:
- description: Tenant-hosted MCP server that lets AI agents investigate incidents, explore logs, metrics and traces, search Datasets, list alerts and monitors, generate OPAL queries and inspect APM service maps. OAu
  name: Observe by Snowflake MCP Server
  slug: observe-by-snowflake-mcp-server
modified: '2026-10-13'
name: Observe
nav: Providers
network: true
overview: 'Observe publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alert API, APM API, Dashboards API, and 19 more. Tagged areas include Company, Observability, Monitoring, Logs, and Metrics.


  The Observe catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Observe''s developer surface includes CLI, changelog, getting-started guide, authentication, documentation, API reference, support, and 34 more developer resources.'
plans:
- name: Observeinc Plans Pricing
  plan_count: 4
  slug: observeinc-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Observeinc Rate Limits
  slug: observeinc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Observe API Rules
  rule_count: 65
  severity_counts:
    error: 42
    hint: 0
    info: 8
    warn: 15
  slug: observeinc-rules
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 40.5
    discoverability: 75.8
    operational_transparency: 76.3
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/observeinc/observeinc-2026-11-03T140414.png
security:
- kind: authentication
  name: Observeinc Authentication
  slug: observeinc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Observeinc Domain Security
  slug: observeinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: observeinc
tags:
- Company
- Observability
- Monitoring
- Logs
- Metrics
- Traces
- APM
- Snowflake
website: https://www.observeinc.com
---
