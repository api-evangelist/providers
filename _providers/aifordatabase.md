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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Send natural-language messages and receive AI-generated SQL and insights
  name: AI for Database Chat API
  slug: aifordatabase-chat-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Manage database connections, schemas, annotations, and execute SQL queries
  name: AI for Database Connections API
  slug: aifordatabase-connections-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Manage chat conversation history
  name: AI for Database Conversations API
  slug: aifordatabase-conversations-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Create and manage dashboards and their widgets
  name: AI for Database Dashboards API
  slug: aifordatabase-dashboards-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Manage platform API keys
  name: AI for Database Keys API
  slug: aifordatabase-keys-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Define and evaluate metric formulas against connections
  name: AI for Database Metrics API
  slug: aifordatabase-metrics-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Submit queries for human approval before execution
  name: AI for Database Query Approval API
  slug: aifordatabase-query-approval-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Store, parameterize, and execute reusable SQL queries
  name: AI for Database Saved Queries API
  slug: aifordatabase-saved-queries-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: View usage records and budget information
  name: AI for Database Usage API
  slug: aifordatabase-usage-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Manage webhook endpoints, deliveries, and test events
  name: AI for Database Webhooks API
  slug: aifordatabase-webhooks-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Manage encrypted, destination-bound credentials for workflow actions
  name: AI for Database Workflow Credentials API
  slug: aifordatabase-workflow-credentials-api
- baseURL: https://app.aifordatabase.com/api/v1
  baseurl_source: declared
  description: Build and run scheduled or manual multi-step workflows
  name: AI for Database Workflows API
  slug: aifordatabase-workflows-api
artifact_total: 26
asyncapis:
- description: ''
  name: Aifordatabase Webhooks
  slug: aifordatabase-webhooks
common:
- group: other
  href: https://artifacts.apis.io/aifordatabase/capabilities/aifordatabase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aifordatabase-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.aifordatabase.com/
- group: other
  href: https://artifacts.apis.io/aifordatabase/overlays/aifordatabase-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aifordatabase-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/aifordatabase/mcp/aifordatabase-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aifordatabase-mcp.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aifordatabase.com/for-agents/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aifordatabase.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.aifordatabase.com/docs/endpoints/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aifordatabase.com/docs/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://www.aifordatabase.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.aifordatabase.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aifordatabase.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.aifordatabase.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.aifordatabase.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aifordatabase.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aifordatabase.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.aifordatabase.com/trust/
- group: commercial
  href: https://artifacts.apis.io/aifordatabase/plans/aifordatabase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aifordatabase-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aifordatabase/rate-limits/aifordatabase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aifordatabase-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/aifordatabase/sandbox/aifordatabase-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aifordatabase-sandbox.yml
- group: build
  href: https://artifacts.apis.io/aifordatabase/packages/aifordatabase-packages.yml
  title: ''
  type: Packages
  url: packages/aifordatabase-packages.yml
- group: agent
  href: https://artifacts.apis.io/aifordatabase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/aifordatabase/security/aifordatabase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aifordatabase-domain-security.yml
created: '2026-08-26'
description: 'AI for Database is a natural-language data layer for operational databases, built by Wavicle.tech. It connects read-only to PostgreSQL, MySQL, MariaDB, SQL Server, MongoDB, SQLite and Google Sheets, translates plain-English questions into SQL, returns the SQL alongside the answer, pins results as self-refreshing dashboards, and runs scheduled workflows that fire email, webhook or Slack alerts when a query condition becomes true. The public REST API is explicitly designed for AI agents: a scoped Bearer-auth contract (afd_ keys, nine permission scopes) documented by a live OpenAPI 3.1 spec with 80 operations, a paused-draft workflow lifecycle with a real dry-run preview and a confirmation-gated live action test, human query approval, and agent-native discovery surfaces at llms.txt, llms-full.txt and a JSON capability manifest.'
finops:
- has_sources: true
  method: derived
  name: Aifordatabase Finops
  primary_unit: user
  service_category: ''
  slug: aifordatabase-finops
  template: false
image: https://www.aifordatabase.com/logo.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server requiring an API key; 9 tools listed.
  name: AI for Database MCP Server
  slug: aifordatabase-mcp
modified: '2026-08-26'
name: AI for Database
nav: Providers
network: true
overview: 'AI for Database publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chat API, Connections API, Conversations API, and 9 more. Tagged areas include Artificial Intelligence, Database, Analytics, Developer Tools, and Natural Language Query.


  The AI for Database catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AI for Database''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Aifordatabase Plans Pricing
  plan_count: 3
  slug: aifordatabase-plans-pricing
- name: Aifordatabase Price Estimates
  plan_count: 0
  slug: aifordatabase-price-estimates
random_paper: 6
rate_limits:
- limit_count: 6
  name: Aifordatabase Rate Limits
  slug: aifordatabase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: AI for Database API Rules
  rule_count: 58
  severity_counts:
    error: 48
    hint: 0
    info: 4
    warn: 6
  slug: aifordatabase-rules
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 67.0
    developer_ergonomics: 66.1
    discoverability: 71.7
    operational_transparency: 39.5
  previous_composite: 63.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/aifordatabase/aifordatabase-2026-09-02T144117.png
security:
- kind: authentication
  name: Aifordatabase Authentication
  slug: aifordatabase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aifordatabase Domain Security
  slug: aifordatabase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aifordatabase Trust Center
  slug: aifordatabase-trust-center
  summary_line: SOC 2, GDPR
skill_count: 4
skills:
- name: aifordatabase-answer-a-database-question
  slug: aifordatabase-answer-a-database-question
- name: aifordatabase-govern-query-approval
  slug: aifordatabase-govern-query-approval
- name: aifordatabase-ship-a-scheduled-alert
  slug: aifordatabase-ship-a-scheduled-alert
- name: aifordatabase-subscribe-to-events
  slug: aifordatabase-subscribe-to-events
slug: aifordatabase
tags:
- Artificial Intelligence
- Database
- Analytics
- Developer Tools
- Natural Language Query
- Text-to-SQL
- Dashboards
- Business Intelligence
- Workflow Automation
- Alerts
- Agent-Native
- Llms.txt
- OpenAPI
- Webhook
- MCP
- PostgreSQL
- MySQL
- MongoDB
website: https://www.aifordatabase.com/
---
