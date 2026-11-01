---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 159
  human_in_the_loop: 7
  name: Robosystems Ai Agentic Access
  operation_count: 231
  slug: robosystems-ai-agentic-access
  summary_line: 231 operations · 159 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🔐 Authentication - Register, sign in, manage the session, verify email, and reset passwords
  name: robosystems-ai Auth API
  slug: robosystems-ai-auth-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🛡️ Multi-factor auth - Assertion options, verification, status, and recovery codes
  name: 'robosystems-ai Auth: MFA API'
  slug: robosystems-ai-auth-mfa-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🔑 Passkeys - WebAuthn registration, passwordless login, and re-authentication
  name: 'robosystems-ai Auth: Passkeys API'
  slug: robosystems-ai-auth-passkeys-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🎫 Single sign-on - Cross-app token exchange, and enterprise OIDC where enabled
  name: 'robosystems-ai Auth: SSO API'
  slug: robosystems-ai-auth-sso-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 💾 Backup - List, download, and inspect graph backups
  name: robosystems-ai Backup API
  slug: robosystems-ai-backup-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🛒 Billing - Create and manage billing checkout sessions
  name: robosystems-ai Billing API
  slug: robosystems-ai-billing-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🔗 Connection management — Manage external data source integrations
  name: robosystems-ai Connections API
  slug: robosystems-ai-connections-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: ✍️ Content operations - Write content across memory, documents, and files
  name: robosystems-ai Content Operations API
  slug: robosystems-ai-content-operations-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🪙 Credits - Manage credit-based usage and allocation
  name: robosystems-ai Credits API
  slug: robosystems-ai-credits-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📑 Documents - List documents for search and analysis
  name: robosystems-ai Documents API
  slug: robosystems-ai-documents-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📄 File management - List stored data files for generic graphs
  name: robosystems-ai Files API
  slug: robosystems-ai-files-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📜 Graph audit - Every change made to a graph, from the REST API, MCP clients, and AI operators
  name: robosystems-ai Graph Audit API
  slug: robosystems-ai-graph-audit-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🩺 Graph health - Database health and performance metrics
  name: robosystems-ai Graph Health API
  slug: robosystems-ai-graph-health-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: ℹ️ Graph info - Database metadata and statistics
  name: robosystems-ai Graph Info API
  slug: robosystems-ai-graph-info-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📏 Graph limits - Storage usage, operation limits, and tier configuration
  name: robosystems-ai Graph Limits API
  slug: robosystems-ai-graph-limits-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🧑‍🤝‍🧑 Graph members - Manage per-graph member access and roles
  name: robosystems-ai Graph Members API
  slug: robosystems-ai-graph-members-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: ⚙️ Graph lifecycle — Subgraphs, backups, tier changes, and materialization
  name: robosystems-ai Graph Operations API
  slug: robosystems-ai-graph-operations-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🏗️ Graphs - Create and manage knowledge graph tenants
  name: robosystems-ai Graphs API
  slug: robosystems-ai-graphs-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🧠 Memory - Recall, list, and inspect the graph's per-graph semantic memory store
  name: robosystems-ai Memory API
  slug: robosystems-ai-memory-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: ⏱️ Operation monitoring - Track SSE stream status and progress
  name: robosystems-ai Operations API
  slug: robosystems-ai-operations-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🤖 AI Operators - AI agent orchestration and execution
  name: robosystems-ai Operator API
  slug: robosystems-ai-operator-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🏢 Organizations - Manage organizations and team collaboration
  name: robosystems-ai Org API
  slug: robosystems-ai-org-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 👥 Organization members - Manage team members, roles, and permissions
  name: robosystems-ai Org Members API
  slug: robosystems-ai-org-members-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📈 Organization usage - Track organization-wide usage, limits, and analytics
  name: robosystems-ai Org Usage API
  slug: robosystems-ai-org-usage-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🕸️ Graph queries - Execute Cypher queries on the knowledge graph
  name: robosystems-ai Query API
  slug: robosystems-ai-query-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📈 RoboInvestor operations - Named commands for portfolio management writes and analytical views
  name: robosystems-ai Robo Investor API
  slug: robosystems-ai-roboinvestor-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: '🔬 Analytical views - Read-shaped operations over the XBRL hypercube and published reports: fact grids, statements, and disclosures'
  name: 'robosystems-ai RoboLedger: Analytical Views API'
  slug: robosystems-ai-roboledger-analytical-views-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📅 Fiscal close - Close and reopen periods, and drive the schedules that feed the close
  name: 'robosystems-ai RoboLedger: Fiscal Close API'
  slug: robosystems-ai-roboledger-fiscal-close-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🧱 Information blocks - Author the units a report is built from, and compute rules, metrics and forecasts over them
  name: 'robosystems-ai RoboLedger: Information Blocks API'
  slug: robosystems-ai-roboledger-information-blocks-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📓 Ledger & events - Agents, business events, the handlers that post them to the GL, and journal entry corrections
  name: 'robosystems-ai RoboLedger: Ledger & Events API'
  slug: robosystems-ai-roboledger-ledger-events-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📬 Report distribution - Share reports, manage publish lists, and block unwanted senders
  name: 'robosystems-ai RoboLedger: Report Distribution API'
  slug: robosystems-ai-roboledger-report-distribution-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📄 Reports - Build, rebuild, and file a financial report
  name: 'robosystems-ai RoboLedger: Reports API'
  slug: robosystems-ai-roboledger-reports-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📒 Ledger setup - Initialize a ledger, seed its chart of accounts, and edit the reporting entity
  name: 'robosystems-ai RoboLedger: Setup API'
  slug: robosystems-ai-roboledger-setup-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🏷️ Taxonomy & mapping - Curate taxonomy blocks and map the chart of accounts to their elements
  name: 'robosystems-ai RoboLedger: Taxonomy & Mapping API'
  slug: robosystems-ai-roboledger-taxonomy-mapping-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📐 Schema - Inspect and export a graph's deployed schema
  name: robosystems-ai Schema API
  slug: robosystems-ai-schema-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🔎 Search - Full-text and semantic search on documents, narratives and disclosures
  name: robosystems-ai Search API
  slug: robosystems-ai-search-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🛍️ Service offerings - View available offers and pricing
  name: robosystems-ai Service Offerings API
  slug: robosystems-ai-service-offerings-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: ❤️ Service status - API status and monitoring
  name: robosystems-ai Status API
  slug: robosystems-ai-status-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🌳 Subgraphs - List and inspect subgraph databases
  name: robosystems-ai Subgraphs API
  slug: robosystems-ai-subgraphs-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 💳 Subscriptions - Shared repository subscription management
  name: robosystems-ai Subscriptions API
  slug: robosystems-ai-subscriptions-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🗃️ Staging tables - Table metadata for the staging layer
  name: robosystems-ai Tables API
  slug: robosystems-ai-tables-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 📊 Usage - Monitor usage, metrics, and system performance
  name: robosystems-ai Usage API
  slug: robosystems-ai-usage-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 👤 User management - Profile, settings, and account information
  name: robosystems-ai User API
  slug: robosystems-ai-user-api
- baseURL: https://api.robosystems.ai
  baseurl_source: declared
  description: 🧩 GraphQL endpoint - Unified GraphQL endpoint for extensions read queries
  name: robosystems-ai Graph QL API
  slug: robosystems-ai-graph-ql-api
artifact_total: 60
common:
- group: agent
  href: https://artifacts.apis.io/robosystems-ai/agentic-access/robosystems-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/robosystems-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/robosystems-ai/rules/robosystems-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/robosystems-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/robosystems-ai/json-ld/robosystems-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/robosystems-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/robosystems-ai/vocabulary/robosystems-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/robosystems-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/robosystems-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/robosystems-ai/data-model/robosystems-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/robosystems-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/robosystems-ai/conventions/robosystems-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/robosystems-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/robosystems-ai/conventions/robosystems-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/robosystems-ai-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/RoboFinSystems/robosystems/blob/main/SECURITY.md
- group: design
  href: https://artifacts.apis.io/robosystems-ai/errors/robosystems-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/robosystems-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/robosystems-ai/conformance/robosystems-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/robosystems-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/robosystems-ai/llms/robosystems-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/robosystems-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/robosystems-ai/well-known/robosystems-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/robosystems-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/robosystems-ai/well-known/robosystems-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/robosystems-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/robosystems-ai/well-known/robosystems-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/robosystems-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/robosystems-ai/hosts/robosystems-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/robosystems-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/robosystems-ai/vendors/robosystems-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/robosystems-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/robosystems-ai/packages/robosystems-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/robosystems-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/robosystems-ai/packages/robosystems-ai-packages.yml
  title: ''
  type: Packages
  url: packages/robosystems-ai-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.robosystems.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.robosystems.ai
- group: start
  title: ''
  type: Login
  url: https://robosystems.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RoboFinSystems
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.robosystems.ai</code
- group: auth
  href: https://artifacts.apis.io/robosystems-ai/authentication/robosystems-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/robosystems-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/robosystems-ai/security/robosystems-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/robosystems-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/robosystems-ai/security/robosystems-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/robosystems-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://robosystems.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://robosystems.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://robosystems.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://robosystems.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://robosystems.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://robosystems.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://robosystems.ai/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://robosystems.ai/pages/privacy
created: '2026-10-30'
description: RoboSystems is an open-source financial intelligence platform that provides a knowledge graph of company data, SEC XBRL filings, and AI-powered tools for document search, semantic analysis, and MCP integration. It enables users to build custom integrations, access a REST API, and leverage AI agents for financial analysis across public and private companies.
image: https://robosystems.ai/images/logos/robosystems-icon.png
json_schemas:
- name: CreateEntityRequest
  property_count: 27
  slug: robosystems-ai-create-entity-request
- name: CreateEventBlockRequest
  property_count: 24
  slug: robosystems-ai-create-event-block-request
- name: CreateEventHandlerRequest
  property_count: 13
  slug: robosystems-ai-create-event-handler-request
- name: CreateGraphRequest
  property_count: 6
  slug: robosystems-ai-create-graph-request
- name: UpdateEntityRequest
  property_count: 28
  slug: robosystems-ai-update-entity-request
- name: UpdateEventBlockRequest
  property_count: 12
  slug: robosystems-ai-update-event-block-request
jsonld:
- class_count: 120
  name: Robosystems Ai Context
  property_count: 458
  slug: robosystems-ai-context
layout: provider
modified: '2026-10-30'
name: robosystems-ai
nav: Providers
network: true
overview: 'robosystems-ai publishes 44 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Auth: MFA API, Auth: Passkeys API, and 41 more. Tagged areas include Finance, AI, KnowledgeGraph, OpenSource, and API.


  The robosystems-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  robosystems-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Robosystems Ai Plans Pricing
  plan_count: 6
  slug: robosystems-ai-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: robosystems-ai API Rules
  rule_count: 17
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 5
  slug: robosystems-ai-rules
score:
  band: strong
  composite: 60.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 66.0
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Robosystems Ai Authentication
  slug: robosystems-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Robosystems Ai Domain Security
  slug: robosystems-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Robosystems Ai Vulnerability Disclosure
  slug: robosystems-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: authentication
  slug: robosystems-ai-authentication
- name: passkey-management
  slug: robosystems-ai-passkey-management
- name: password-reset
  slug: robosystems-ai-password-reset
slug: robosystems-ai
tags:
- Finance
- AI
- KnowledgeGraph
- OpenSource
- API
website: https://robosystems.ai/
---
