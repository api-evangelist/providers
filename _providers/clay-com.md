---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Clay Com Agentic Access
  operation_count: 13
  slug: clay-com-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
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
- description: Authenticated user and workspace endpoints.
  name: Clay Me API
  slug: clay-com-me-api
- description: Routine discovery and execution endpoints.
  name: Clay Routines API
  slug: clay-com-routines-api
- description: Search creation and pagination endpoints.
  name: Clay Search API
  slug: clay-com-search-api
- description: Structured table query endpoints.
  name: Clay Tables API
  slug: clay-com-tables-api
artifact_total: 23
asyncapis:
- description: ''
  name: Clay Com Webhooks
  slug: clay-com-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/clay-com-public-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clay-com-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/clay-com-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clay-com-well-known.yml
- group: auth
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
  title: ''
  type: TrustCenter
  url: security/clay-com-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clay-com-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clay-com-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clay-com-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clay-com-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clay.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clay-com-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clay-com-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clay-com-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/clay-com-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/clay-com-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clay-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clay-com-rate-limits.yml
- group: commercial
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
  title: ''
  type: AgenticAccess
  url: agentic-access/clay-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clay-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clay-com-authentication.yml
- group: auth
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
- name: Clay Com Finops
  service_category: API
  slug: clay-com-finops
graphqls:
- description: ''
  name: Clay GraphQL API
  slug: clay-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clay-com.png
layout: provider
mcp_servers:
- description: ''
  name: Clay MCP Server
  slug: clay-mcp-server
modified: '2026-08-14'
name: Clay
nav: Providers
network: true
overview: 'Clay publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Me API, Routines API, Search API, and 1 more. Tagged areas include Prospecting, Go-To-Market, Sales, Enrichment, and Automation.


  The Clay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clay''s developer surface includes changelog, CLI, API reference, getting-started guide, support, authentication, documentation, and 39 more developer resources.'
plans:
- name: Clay Com Plans Pricing
  plan_count: 4
  slug: clay-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Clay Com Rate Limits
  slug: clay-com-rate-limits
scopes:
- name: Clay Com Scopes
  scope_count: 1
  slug: clay-com-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 64.4
  coverage:
    artifact_dirs: 26
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 4.5
    contract_quality: 63.3
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clay-com/refs/heads/main/screenshots/clay-com-2026-06-20T174453.png
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
slug: clay-com
tags:
- Prospecting
- Go-To-Market
- Sales
- Enrichment
- Automation
- Artificial Intelligence
- Webhook
website: https://www.clay.com
---
