---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Celigo Agentic Access
  operation_count: 37
  slug: celigo-agentic-access
  summary_line: 37 operations · 21 acting
api_count: 1
apis:
- description: 'The integrator.io Platform API is a RESTful JSON API secured by Bearer Tokens. It provides programmatic access to integrations, connections, flows, imports, exports, iClients, and other integrator.io '
  name: Celigo integrator.io Platform API
  slug: celigo-integrator-io-api
- description: Celigo supports OAuth 2.0 and OAuth 1.0 authentication for HTTP connections, configured through iClient resources for reusable OAuth client credentials across integrations.
  name: Celigo OAuth Authentication
  slug: celigo-oauth-api
- description: Celigo API Management allows organizations to build, publish, and govern APIs on top of Celigo-managed integrations and third-party systems with a dedicated API Management console.
  name: Celigo API Management
  slug: celigo-api-management
- description: Inbound webhook listeners exposed by integrator.io. Each listener provides an auto-generated public HTTPS URL that accepts HTTP POST or PUT requests from a source application to trigger a real-time fl
  name: Celigo integrator.io Webhook Listeners
  slug: celigo-webhook-listeners
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The Connections API from Celigo — 3 operation(s) for connections.
  name: Celigo Connections API
  slug: celigo-connections-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The Exports API from Celigo — 2 operation(s) for exports.
  name: Celigo Exports API
  slug: celigo-exports-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The Flows API from Celigo — 3 operation(s) for flows.
  name: Celigo Flows API
  slug: celigo-flows-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The iClients API from Celigo — 1 operation(s) for iclients.
  name: Celigo iClients API
  slug: celigo-iclients-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The Imports API from Celigo — 2 operation(s) for imports.
  name: Celigo Imports API
  slug: celigo-imports-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The Integrations API from Celigo — 2 operation(s) for integrations.
  name: Celigo Integrations API
  slug: celigo-integrations-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The Jobs API from Celigo — 2 operation(s) for jobs.
  name: Celigo Jobs API
  slug: celigo-jobs-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The Licenses API from Celigo — 1 operation(s) for licenses.
  name: Celigo Licenses API
  slug: celigo-licenses-api
- baseURL: https://api.integrator.io/v1
  baseurl_source: spec
  description: The State API from Celigo — 2 operation(s) for state.
  name: Celigo State API
  slug: celigo-state-api
artifact_total: 46
asyncapis:
- description: AsyncAPI description of Celigo integrator.io's inbound webhook surface. integrator.io exposes "webhook listeners" that receive HTTP POST or PUT requests from third-party source applications. Each list
  name: Celigo integrator.io Webhook Listeners
  slug: celigo-webhook-listeners-asyncapi
collections:
- collection_type: open
  name: Celigo integrator.io Platform REST Connections API
  slug: open-celigo-connections-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections Exports API
  slug: open-celigo-exports-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections Flows API
  slug: open-celigo-flows-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections iClients API
  slug: open-celigo-iclients-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections Imports API
  slug: open-celigo-imports-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections Integrations API
  slug: open-celigo-integrations-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections Jobs API
  slug: open-celigo-jobs-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections Licenses API
  slug: open-celigo-licenses-api
- collection_type: open
  name: Celigo integrator.io Platform REST Connections State API
  slug: open-celigo-state-api
- collection_type: open
  name: Celigo integrator.io Platform REST API
  slug: open-celigo
common:
- group: commercial
  href: https://artifacts.apis.io/celigo/plans/celigo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/celigo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/celigo/rate-limits/celigo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/celigo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/celigo/finops/celigo-finops.yml
  title: ''
  type: FinOps
  url: finops/celigo-finops.yml
- group: agent
  href: https://artifacts.apis.io/celigo/agentic-access/celigo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/celigo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/celigo/security/celigo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/celigo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/celigo/security/celigo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celigo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/celigo/authentication/celigo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/celigo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/celigo-inc
- group: company
  title: ''
  type: Website
  url: https://celigo.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.celigo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.celigo.com/hc/en-us/categories/360001519091-Platform-API
- group: docs
  title: ''
  type: Reference
  url: https://github.com/celigo/integrator-api-docs
- group: company
  title: ''
  type: Blog
  url: https://www.celigo.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.celigo.com/hc/en-us/articles/360042281231-Getting-started-with-standard-REST-API
- group: auth
  title: ''
  type: Authentication
  url: https://docs.celigo.com/hc/en-us/articles/360039586072-Set-up-an-OAuth-2-0-HTTP-connection
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celigo.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://celigo.com/terms-of-service/
created: '2026-03-16'
description: Celigo is an intelligent automation platform (iPaaS) that enables organizations to integrate applications, automate business processes, and connect data across their technology stack with low-code tooling. Celigo offers a REST-based integrator.io Platform API, an API Management console, OAuth 2.0 and Bearer Token authentication, and more than one thousand pre-built connectors and integration applications.
finops:
- has_sources: true
  method: derived
  name: Celigo Finops
  primary_unit: ''
  service_category: ''
  slug: celigo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celigo.png
json_schemas:
- name: Connection
  property_count: 8
  slug: celigo-connection
- name: Export
  property_count: 5
  slug: celigo-export
- name: Flow
  property_count: 6
  slug: celigo-flow
- name: Import
  property_count: 5
  slug: celigo-import
- name: Integration
  property_count: 5
  slug: celigo-integration
jsonld:
- class_count: 5
  name: Celigo Context
  property_count: 18
  slug: celigo-context
layout: provider
mcp_servers:
- description: Remote MCP server at developer.celigo.com over HTTP.
  name: Celigo MCP Server
  slug: celigo
- description: Remote MCP server at developer.celigo.com over HTTP.
  name: Celigo MCP Server
  slug: celigo-2
- description: Remote MCP server at www.celigo.com over HTTP.
  name: Celigo MCP Server
  slug: celigo-3
modified: '2026-05-30'
name: Celigo
nav: Providers
network: true
overview: 'Celigo publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including integrator.io Webhook Listeners, Connections API, Exports API, and 10 more. Tagged areas include API Management, Automation, Data Integration, Integration, and iPaaS.


  The Celigo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Celigo''s developer surface includes authentication, developer portal, documentation, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Celigo Plans Pricing
  plan_count: 3
  slug: celigo-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Celigo Rate Limits
  slug: celigo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Celigo — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: celigo-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Celigo API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: celigo-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.5
    catalog_earned_first_party: 12.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 63.5
    developer_ergonomics: 42.9
    discoverability: 66.7
    operational_transparency: 18.4
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/celigo/celigo-2026-06-20T174113.png
security:
- kind: authentication
  name: Celigo Authentication
  slug: celigo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Celigo Domain Security
  slug: celigo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Celigo Trust Center
  slug: celigo-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 4
skills:
- name: celigo-create-and-test-connection
  slug: celigo-create-and-test-connection
- name: celigo-create-import
  slug: celigo-create-import
- name: celigo-exports-crud
  slug: celigo-exports-crud
- name: celigo-manage-integrations
  slug: celigo-manage-integrations
slug: celigo
tags:
- API Management
- Automation
- Data Integration
- Integration
- iPaaS
- Workflows
website: https://celigo.com/
---
