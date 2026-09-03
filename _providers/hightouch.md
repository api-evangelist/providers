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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Hightouch Agentic Access
  operation_count: 43
  slug: hightouch-agentic-access
  summary_line: 43 operations · 22 acting
api_count: 1
apis:
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Warehouse and database sources Hightouch reads from.
  name: Hightouch Sources API
  slug: hightouch-sources-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Model definitions (SQL, table, dbt, visual) over a source.
  name: Hightouch Models API
  slug: hightouch-models-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Destination connectors receiving synced data.
  name: Hightouch Destinations API
  slug: hightouch-destinations-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Syncs, sync runs, sync sequences and their triggers.
  name: Hightouch Syncs API
  slug: hightouch-syncs-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Trigger a campaign send to handle- or profile-based recipients and read back per-send status.
  name: Hightouch Campaigns API
  slug: hightouch-campaigns-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Decision-engine flows, their message variants, guardrails and runs.
  name: Hightouch AI Decisioning API
  slug: hightouch-ai-decisioning-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: First-party event governance — event contracts and event domains.
  name: Hightouch Events API
  slug: hightouch-events-api
- baseURL: https://api.hightouch.com/api/v1
  baseurl_source: declared
  description: Identity graph runs, reprocessing queues and run statistics.
  name: Hightouch Identity Resolution API
  slug: hightouch-identity-resolution-api
artifact_total: 25
asyncapis:
- description: ''
  name: Hightouch Webhooks
  slug: hightouch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hightouch Management Destinations API
  slug: open-hightouch-destinations-api
- collection_type: open
  name: Hightouch Management Destinations Models API
  slug: open-hightouch-models-api
- collection_type: open
  name: Hightouch Management Destinations Sources API
  slug: open-hightouch-sources-api
- collection_type: open
  name: Hightouch Management Destinations Syncs API
  slug: open-hightouch-syncs-api
- collection_type: open
  name: Hightouch Management API
  slug: open-hightouch
common:
- group: company
  title: ''
  type: Website
  url: https://hightouch.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hightouch.com/docs/developer-tools/api-guide
- group: docs
  title: ''
  type: Documentation
  url: https://hightouch.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hightouch.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://hightouch.com/docs/getting-started/welcome
- group: company
  title: ''
  type: Blog
  url: https://hightouch.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://hightouch.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.hightouch.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.hightouch.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hightouch.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hightouch.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hightouchio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hightouchio
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hightouch.io
- group: auth
  title: ''
  type: Compliance
  url: https://hightouch.com/platform/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/hightouch-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hightouch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hightouch-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hightouch-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hightouch-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hightouch-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hightouch-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/hightouch-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hightouch-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hightouch-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/hightouch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hightouch-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hightouch-cli.yml
- group: design
  title: ''
  type: Components
  url: components/hightouch-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hightouch-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hightouch-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hightouch-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hightouch-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hightouch-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/hightouch-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hightouch-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hightouch-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/hightouch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hightouch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hightouch-finops.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hightouch-api-overlay.yaml
created: '2026-03-27'
description: Hightouch is a composable Customer Data Platform (CDP) and agentic marketing platform that activates data directly from cloud warehouses and lakehouses such as Snowflake, BigQuery, Databricks and Redshift to more than 290 SaaS destinations, without copying or storing customer data. The platform covers Reverse ETL, Customer Studio audience building and journey orchestration, identity resolution, first-party event collection with SDKs for web and mobile, real-time personalization, AI Decisioning, Match Booster and an Ad Studio for advertising creative. Developers get a bearer-authenticated REST API at https://api.hightouch.com/api/v1 covering sources, models, destinations, syncs and runs, campaigns, decision-engine flows, event contracts and identity graphs, plus an `ht` CLI, Git Sync for version-controlled resource YAML, workspace environments with approval flows, a public documentation MCP server, and an A2A agent card for the Hightouch Marketing Agent.
finops:
- name: Hightouch Finops
  service_category: API
  slug: hightouch-finops
graphqls:
- description: Hightouch is a composable Customer Data Platform (CDP) and data activation platform that syncs data from cloud data warehouses such as Snowflake and BigQuery to over 300 SaaS destinations. The platfor
  name: Hightouch GraphQL API
  slug: hightouch-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hightouch.png
layout: provider
mcp_servers:
- description: ''
  name: Hightouch MCP Server
  slug: hightouch-mcp-server
modified: '2026-08-13'
name: Hightouch
nav: Providers
network: true
overview: 'Hightouch publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Sources API, Models API, Destinations API, and 5 more. Tagged areas include CDP, Data Activation, Reverse ETL, Audience Management, and Identity Resolution.


  The Hightouch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hightouch''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 35 more developer resources.'
plans:
- name: Hightouch Plans Pricing
  plan_count: 3
  slug: hightouch-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Hightouch Rate Limits
  slug: hightouch-rate-limits
scopes:
- name: Hightouch Scopes
  scope_count: 4
  slug: hightouch-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.6
  coverage:
    artifact_dirs: 29
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 71.4
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 67.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hightouch/refs/heads/main/screenshots/hightouch-2026-06-20T182738.png
security:
- kind: authentication
  name: Hightouch Authentication
  slug: hightouch-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Hightouch Domain Security
  slug: hightouch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hightouch Trust Center
  slug: hightouch-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: hightouch
tags:
- CDP
- Data Activation
- Reverse ETL
- Audience Management
- Identity Resolution
- Event Collection
- Marketing
- Advertising
- AI Agents
- Data Warehouse
website: https://hightouch.com/
---
