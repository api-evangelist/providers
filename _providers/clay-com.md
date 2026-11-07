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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Clay Com Agentic Access
  operation_count: 13
  slug: clay-com-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 2
apis:
- description: Generic HTTP request column inside Clay Tables that lets users call any external REST or GraphQL endpoint with row-level variables and write the response back into Clay. Acts as Clay's universal API c
  name: Clay HTTP API Enrichment
  slug: http-api
- description: Webhook source that pushes data from any external system into a Clay Table as new rows. Used to trigger Clay workflows from CRMs, signal providers, and product events.
  name: Clay Incoming Webhooks
  slug: webhooks-incoming
- description: Action column that POSTs enriched row data to an external webhook URL, used to deliver Clay-produced data to CRMs, sequencers, Slack, and custom backends.
  name: Clay Outgoing Webhooks
  slug: webhooks-outgoing
- description: The core spreadsheet-style workspace that combines source rows, enrichment columns, conditional logic, AI agents, and write-back destinations. Tables are the unit of automation and the data plane ever
  name: Clay Tables
  slug: tables
- description: Catalog of native connectors and 150+ data providers — Salesforce, HubSpot, Pipedrive, Apollo, Clearbit, ZoomInfo, LinkedIn Sales Navigator, Smartlead, Instantly, Apollo, OpenAI, and many more — expos
  name: Clay Integrations
  slug: integrations
- description: Browser extension for scraping LinkedIn profiles and other web pages directly into Clay Tables, used to bootstrap prospect lists from manual research.
  name: Clay Chrome Extension
  slug: chrome-extension
- description: Clay's hosted remote Model Context Protocol server, letting an MCP client search companies and people, run enrichment routines and query Clay tables from natural language. Streamable HTTP at https://a
  name: Clay MCP Server
  slug: mcp
- baseURL: https://app.clay.com
  baseurl_source: declared
  description: Authenticated user and workspace endpoints.
  name: Clay Me API
  slug: clay-com-me-api
- baseURL: https://app.clay.com
  baseurl_source: declared
  description: Routine discovery and execution endpoints.
  name: Clay Routines API
  slug: clay-com-routines-api
- baseURL: https://app.clay.com
  baseurl_source: declared
  description: Search creation and pagination endpoints.
  name: Clay Search API
  slug: clay-com-search-api
- baseURL: https://app.clay.com
  baseurl_source: declared
  description: Structured table query endpoints.
  name: Clay Tables API
  slug: clay-com-tables-api
artifact_total: 46
asyncapis:
- description: ''
  name: Clay Com Webhooks
  slug: clay-com-webhooks
common:
- group: other
  href: https://artifacts.apis.io/clay-com/capabilities/clay-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clay-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/clay-com/overlays/clay-com-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clay-com-public-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/clay-com/llms/clay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clay-com-llms.txt
- group: other
  href: https://artifacts.apis.io/clay-com/a2a/clay-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clay-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/clay-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/clay-com/well-known/clay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clay-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/clay-com/well-known/clay-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clay-com-security.txt
- group: auth
  title: ''
  type: Security
  url: https://trust.clay.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.clay.com/enterprise
- group: auth
  href: https://artifacts.apis.io/clay-com/security/clay-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clay-com-trust-center.yml
- group: design
  href: https://artifacts.apis.io/clay-com/conventions/clay-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clay-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/clay-com/conformance/clay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clay-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/clay-com/errors/clay-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clay-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clay-com/lifecycle/clay-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clay-com-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clay.com
- group: operate
  href: https://artifacts.apis.io/clay-com/changelog/clay-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clay-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/clay-com/asyncapi/clay-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/clay-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/clay-com/data-model/clay-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clay-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/clay-com/packages/clay-com-packages.yml
  title: ''
  type: Packages
  url: packages/clay-com-packages.yml
- group: build
  href: https://artifacts.apis.io/clay-com/cli/clay-com-cli.yml
  title: ''
  type: CLI
  url: cli/clay-com-cli.yml
- group: commercial
  href: https://artifacts.apis.io/clay-com/plans/clay-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clay-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/clay-com/rate-limits/clay-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clay-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clay-com/finops/clay-com-finops.yml
  title: ''
  type: FinOps
  url: finops/clay-com-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.clay.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.clay.com/api-reference/me/get-the-authenticated-user
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.clay.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://community.clay.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clay-run
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.clay.com/changelog
- group: agent
  href: https://artifacts.apis.io/clay-com/agentic-access/clay-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clay-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/clay-com/security/clay-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clay-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clay-com/authentication/clay-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clay-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/clay-com/security/clay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clay.com
- group: other
  title: ''
  type: App
  url: https://app.clay.com
- group: docs
  title: ''
  type: Documentation
  url: https://university.clay.com/docs
- group: other
  title: ''
  type: University
  url: https://university.clay.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clay.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.clay.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.clay.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.clay.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clay.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clay.com/terms
- group: operate
  title: ''
  type: Slack
  url: https://www.clay.com/community
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clay-gtm
- group: company
  title: ''
  type: Twitter
  url: https://x.com/clay_gtm
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@clay_gtm
created: '2026-05-23'
description: 'Clay is an AI-native sales prospecting and GTM data orchestration platform built around Clay Tables — spreadsheet-like workspaces that combine 150+ data providers, AI research agents, and outbound automations. Clay''s developer surface is integration-oriented rather than a traditional public REST API: HTTP API enrichment columns, incoming and outgoing webhooks, a Chrome extension, and native connectors to CRMs, sequencers, and data providers. External systems push data into Clay Tables and consume enriched rows via webhooks or exports back to systems of record.'
finops:
- has_sources: true
  method: derived
  name: Clay Com Finops
  primary_unit: workspace
  service_category: ''
  slug: clay-com-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clay-com.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.clay.com over HTTP requiring OAuth.
  name: Clay MCP Server
  slug: clay
modified: '2026-08-14'
name: Clay
nav: Providers
network: true
overview: 'Clay publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Me API, Routines API, Search API, and 8 more. Tagged areas include Prospecting, Go-To-Market, Sales, Data Enrichment, and Automation.


  The Clay catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Clay''s developer surface includes changelog, CLI, API reference, getting-started guide, support, authentication, documentation, and 40 more developer resources.'
plans:
- name: Clay Com Plans Pricing
  plan_count: 6
  slug: clay-com-plans-pricing
- name: Clay Com Price Estimates
  plan_count: 0
  slug: clay-com-price-estimates
random_paper: 21
rate_limits:
- limit_count: 1
  name: Clay Com Rate Limits
  slug: clay-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: Clay API Rules
  rule_count: 70
  severity_counts:
    error: 62
    hint: 0
    info: 6
    warn: 2
  slug: clay-com-rules
scopes:
- name: Clay Com Scopes
  scope_count: 1
  slug: clay-com-scopes
  summary_line: 1 scope · authorizationCode/deviceCode/refreshToken
score:
  band: exemplar
  composite: 68.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 82.9
    contract_governance: 18.2
    contract_quality: 61.0
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 73.7
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/clay-com/clay-com-2026-06-20T174453.png
security:
- kind: authentication
  name: Clay Com Authentication
  slug: clay-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Clay Com Domain Security
  slug: clay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clay Com Vulnerability Disclosure
  slug: clay-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clay Com Trust Center
  slug: clay-com-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, CCPA
skill_count: 22
skills:
- name: audiences
  slug: clay-com-audiences
- name: clay-feedback
  slug: clay-com-clay-feedback
- name: clay
  slug: clay-com-clay
- name: Claydevelopers
  slug: clay-com-claydevelopers
- name: cli
  slug: clay-com-cli
- name: public-api
  slug: clay-com-public-api
- name: routines
  slug: clay-com-routines
- name: search
  slug: clay-com-search
- name: setup
  slug: clay-com-setup
- name: tables-analyze
  slug: clay-com-tables-analyze
- name: tables-capacity
  slug: clay-com-tables-capacity
- name: tables-error-sweep
  slug: clay-com-tables-error-sweep
- name: tables-trace
  slug: clay-com-tables-trace
- name: tables-value-trace
  slug: clay-com-tables-value-trace
- name: tables
  slug: clay-com-tables
- name: update
  slug: clay-com-update
- name: workflows-discover-actions
  slug: clay-com-workflows-discover-actions
- name: workflows-optimize-credits
  slug: clay-com-workflows-optimize-credits
- name: workflows-simplify
  slug: clay-com-workflows-simplify
- name: workflows-snapshots
  slug: clay-com-workflows-snapshots
- name: workflows-vs-tables
  slug: clay-com-workflows-vs-tables
- name: workflows
  slug: clay-com-workflows
slug: clay-com
tags:
- Prospecting
- Go-To-Market
- Sales
- Data Enrichment
- Automation
- Artificial Intelligence
- Webhook
- A2A
website: https://www.clay.com
---
