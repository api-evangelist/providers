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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Workspace-scoped REST API for embedding Improvado's data extraction, transformation, and load pipeline into agency and platform products. Manages data sources, connections, accounts, extraction templa
  name: Improvado Embedded API v3
  slug: improvado-embedded-api-v3
- description: Hosted, remote Model Context Protocol server exposing Improvado's marketing data platform to any MCP client (Claude, ChatGPT/Codex, Gemini CLI, Antigravity, Cursor) as 83 published tools across twelve
  name: Improvado Customer MCP
  slug: improvado-customer-mcp
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Manage connection accounts from which data is extracted. Accounts represent specific accounts within a data source platform. Each account is associated with a connection and can have multiple extracts
  name: Improvado Accounts API
  slug: improvado-accounts-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Authentication and authorization endpoints for the Improvado Embedded API. Authentication supports Basic Auth (username:password) for initial token creation, then Bearer tokens for workspace-scoped op
  name: Improvado Authentication API
  slug: improvado-authentication-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Deploy and operate automated recipes through the v3.1 API. An automated recipe turns a template into a SQL view in your workspace destination, built from the extractions the template needs. **Deployin
  name: Improvado Automated Recipes API
  slug: improvado-automated-recipes-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Manage connections to data sources for authentication and data access. Connections handle authentication with data sources and maintain the credentials needed for data extraction. Connections are typi
  name: Improvado Data source connections API
  slug: improvado-data-source-connections-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Browse and configure available data sources for extraction. Data sources represent the marketing platforms, advertising networks, analytics tools, and other systems from which Improvado can extract da
  name: Improvado Data sources API
  slug: improvado-data-sources-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Manage data tables where extracted data is stored and organized. Data tables serve as centralized storage for extracted data. All extractions created from the same extract template are stored in the s
  name: Improvado Data tables API
  slug: improvado-data-tables-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: 'Configure and manage connections to destinations for data loading. Destination connections define how and where data should be loaded within a destination system. They include: - Authentication creden'
  name: Improvado Destination connections API
  slug: improvado-destination-connections-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: 'Manage available destination options where Improvado can load your data. Destinations represent the target systems where extracted and transformed data is loaded, including: - Data warehouses (Snowfla'
  name: Improvado Destinations API
  slug: improvado-destinations-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: 'Work with predefined templates that define what data to extract from a data source. Extract templates are blueprints that specify: - Available fields from a data source - Default extraction settings a'
  name: Improvado Extraction templates API
  slug: improvado-extraction-templates-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: 'Create and manage data extraction orders that pull data from connected sources. An extract represents a configured instance of data extraction with specific settings: - Which connection and account to'
  name: Improvado Extracts API
  slug: improvado-extracts-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: 'Generate secure iframe URLs for embedded UI components. iframe endpoints provide secure, embeddable UI components for: - Creating and managing data source connections (OAuth flows, credential input) -'
  name: Improvado Iframe API
  slug: improvado-iframe-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Configure and manage data loading from data tables to destinations. Load orders define the rules and settings for how data moves from Improvado's data tables to your destination systems. This includes
  name: Improvado Loads API
  slug: improvado-loads-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: 'Work with pre-built recipes that automate common data pipeline workflows. Recipes are templated workflows that combine multiple API operations into reusable patterns. They simplify common tasks like: '
  name: Improvado Recipes API
  slug: improvado-recipes-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Manage custom workspace roles and inspect the available permission catalog. Each agency ships with a fixed set of system roles (Workspace Admin, Editor, Viewer, Data Manager, Data Load Manager, Data A
  name: Improvado Roles API
  slug: improvado-roles-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Manage webhook endpoints that receive event notifications from Improvado. Webhooks let your application react to platform events (extraction completion, load completion, etc.) in near real time, witho
  name: Improvado Webhooks API
  slug: improvado-webhooks-api
- baseURL: https://embedded.improvado.io
  baseurl_source: declared
  description: Manage workspaces that provide isolated environments for organizing resources. Workspaces are fundamental to multi-tenancy in Improvado's Embedded API. Each workspace provides complete isolation of re
  name: Improvado Workspaces API
  slug: improvado-workspaces-api
artifact_total: 32
asyncapis:
- description: ''
  name: Improvado Webhooks
  slug: improvado-webhooks
common:
- group: other
  href: https://artifacts.apis.io/improvado/capabilities/improvado-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/improvado-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://improvado.io/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://improvado.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.improvado.io/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.improvado.io/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.improvado.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.improvado.io/introduction
- group: company
  title: ''
  type: Blog
  url: https://improvado.io/blog
- group: operate
  title: ''
  type: Support
  url: https://improvado.io/help
- group: commercial
  title: ''
  type: Pricing
  url: https://improvado.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://improvado.io/register/talk-to-an-expert
- group: start
  title: ''
  type: Login
  url: https://report.improvado.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://improvado.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://improvado.io/company-legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.improvado.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.improvado.io/changelog
- group: auth
  href: https://artifacts.apis.io/improvado/security/improvado-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/improvado-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.improvado.io
- group: agent
  href: https://artifacts.apis.io/improvado/llms/improvado-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/improvado-llms.txt
- group: agent
  href: https://artifacts.apis.io/improvado/well-known/improvado-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/improvado-well-known.yml
- group: auth
  href: https://artifacts.apis.io/improvado/well-known/improvado-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/improvado-security.txt
- group: auth
  href: https://artifacts.apis.io/improvado/security/improvado-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/improvado-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/improvado/security/improvado-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/improvado-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://improvado.io/company-legal/responsible-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/improvado/authentication/improvado-authentication.yml
  title: ''
  type: Authentication
  url: authentication/improvado-authentication.yml
- group: design
  href: https://artifacts.apis.io/improvado/conventions/improvado-conventions.yml
  title: ''
  type: Conventions
  url: conventions/improvado-conventions.yml
- group: design
  href: https://artifacts.apis.io/improvado/conventions/improvado-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/improvado-conventions.yml
- group: design
  href: https://artifacts.apis.io/improvado/asyncapi/improvado-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/improvado-webhooks.yml
- group: design
  href: https://artifacts.apis.io/improvado/lifecycle/improvado-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/improvado-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/improvado/conformance/improvado-conformance.yml
  title: ''
  type: Conformance
  url: conformance/improvado-conformance.yml
- group: design
  href: https://artifacts.apis.io/improvado/errors/improvado-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/improvado-error-codes.yml
- group: design
  href: https://artifacts.apis.io/improvado/data-model/improvado-data-model.yml
  title: ''
  type: DataModel
  url: data-model/improvado-data-model.yml
- group: agent
  href: https://artifacts.apis.io/improvado/mcp/improvado-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/improvado-mcp.yml
- group: agent
  href: https://artifacts.apis.io/improvado/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/improvado/openapi/_original/improvado-agent-ask-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/improvado-agent-ask-openapi.json
- group: other
  href: https://artifacts.apis.io/improvado/overlays/improvado-agent-ask-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/improvado-agent-ask-overlay.yaml
- group: build
  href: https://artifacts.apis.io/improvado/mcp/improvado-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/improvado-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/improvado/scopes/improvado-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/improvado-scopes.yml
- group: build
  href: https://artifacts.apis.io/improvado/packages/improvado-packages.yml
  title: ''
  type: Packages
  url: packages/improvado-packages.yml
- group: build
  href: https://artifacts.apis.io/improvado/packages/improvado-packages.yml
  title: ''
  type: SDKs
  url: packages/improvado-packages.yml
- group: commercial
  href: https://artifacts.apis.io/improvado/plans/improvado-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/improvado-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/improvado/rate-limits/improvado-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/improvado-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/improvado/components/improvado-components.yml
  title: ''
  type: Components
  url: components/improvado-components.yml
- group: agent
  href: https://artifacts.apis.io/improvado/llms/improvado-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/improvado-site-llms.txt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tekliner/improvado-agentic-frameworks-and-skills
created: '2026-07-17'
description: Improvado is a marketing intelligence and AI-agent platform that connects, extracts, transforms, and loads data from 876+ marketing, advertising, sales, and analytics sources into governed data pipelines, warehouses, and BI tools. Its Embedded API v3 (base https://embedded.improvado.io, all paths under /api/v3/) gives agencies and platforms programmatic, workspace-scoped control over data sources, connections and accounts, extraction templates and extracts, destinations, data tables, loads, automated recipes, custom roles, and webhook endpoints for load, transformation, and extraction lifecycle events. Authentication is HTTP Basic for workspace management and short-lived Bearer tokens for workspace-scoped resources. The platform maintains a SOC 2 / HIPAA / GDPR trust center, a public status page, a dated API changelog, and a responsible-disclosure security program.
finops:
- has_sources: true
  method: derived
  name: Improvado Finops
  primary_unit: workspace
  service_category: ''
  slug: improvado-finops
  template: false
image: https://improvado.io/-/astro/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP; 83 tools listed.
  name: Improvado MCP Server
  slug: improvado-customer
modified: '2026-10-06'
name: Improvado
nav: Providers
network: true
overview: 'Improvado publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Automated Recipes API, and 15 more. Tagged areas include Company, Marketing, Marketing Intelligence, Marketing Analytics, and Data Pipeline.


  The Improvado catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Improvado''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 38 more developer resources.'
plans:
- name: Improvado Plans Pricing
  plan_count: 6
  slug: improvado-plans-pricing
- name: Improvado Price Estimates
  plan_count: 0
  slug: improvado-price-estimates
random_paper: 17
rate_limits:
- limit_count: 0
  name: Improvado Rate Limits
  slug: improvado-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Improvado API Rules
  rule_count: 64
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 12
  slug: improvado-rules
scopes:
- name: Improvado Scopes
  scope_count: 3
  slug: improvado-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 67.7
    developer_ergonomics: 71.4
    discoverability: 73.2
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 71.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 88.9
      total: 18
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/improvado/improvado-2026-07-25T222205.png
security:
- kind: authentication
  name: Improvado Authentication
  slug: improvado-authentication
  summary_line: http/oauth2/none · 5 schemes
- kind: domain-security
  name: Improvado Domain Security
  slug: improvado-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Improvado Vulnerability Disclosure
  slug: improvado-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Improvado Trust Center
  slug: improvado-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 2
skills:
- name: Connect a data source and run an extract
  slug: improvado-connect-and-extract
- name: Register and verify a webhook endpoint
  slug: improvado-register-webhook
slug: improvado
tags:
- Company
- Marketing
- Marketing Intelligence
- Marketing Analytics
- Data Pipeline
- ETL
- Advertising Data
- Business Intelligence
- Data Integration
- AI Agents
- MCP
- Agent Readiness
website: https://improvado.io
---
