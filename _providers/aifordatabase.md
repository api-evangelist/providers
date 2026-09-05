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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-04'
api_count: 2
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
artifact_total: 19
asyncapis:
- description: ''
  name: Aifordatabase Webhooks
  slug: aifordatabase-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/aifordatabase-openapi-overlay.yaml
- group: agent
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
  title: ''
  type: Plans
  url: plans/aifordatabase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aifordatabase-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aifordatabase-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/aifordatabase-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aifordatabase-domain-security.yml
created: '2026-08-26'
description: 'AI for Database is a natural-language data layer for operational databases, built by Wavicle.tech. It connects read-only to PostgreSQL, MySQL, MariaDB, SQL Server, MongoDB, SQLite and Google Sheets, translates plain-English questions into SQL, returns the SQL alongside the answer, pins results as self-refreshing dashboards, and runs scheduled workflows that fire email, webhook or Slack alerts when a query condition becomes true. The public REST API is explicitly designed for AI agents: a scoped Bearer-auth contract (afd_ keys, nine permission scopes) documented by a live OpenAPI 3.1 spec with 80 operations, a paused-draft workflow lifecycle with a real dry-run preview and a confirmation-gated live action test, human query approval, and agent-native discovery surfaces at llms.txt, llms-full.txt and a JSON capability manifest.'
image: https://www.aifordatabase.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: AI for Database MCP Server
  slug: ai-for-database-mcp-server
modified: '2026-08-26'
name: AI for Database
nav: Providers
network: true
overview: 'AI for Database publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Connections API, Conversations API, and 9 more. Tagged areas include Artificial Intelligence, Database, Analytics, Developer Tools, and Natural Language Query.


  The AI for Database catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AI for Database''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Aifordatabase Plans Pricing
  plan_count: 3
  slug: aifordatabase-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Aifordatabase Rate Limits
  slug: aifordatabase-rate-limits
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 67.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 58.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aifordatabase/refs/heads/main/screenshots/aifordatabase-2026-09-02T144117.png
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
- Workflow-Automation
- Alerts
- agent-native
- llms-txt
- OpenAPI
- Webhook
- MCP
- PostgreSQL
- MySQL
- MongoDB
website: https://www.aifordatabase.com/for-agents/
---
