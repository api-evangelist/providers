---
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
    error_semantics: documented
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
  score: 29.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Scoped Bearer-auth REST API for natural-language queries, chat, connections, dashboards, workflows, webhooks, metrics, saved queries, query approval, usage, and API key management. Documented via a pu
  name: AI for Database API
  slug: ai-for-database-api
artifact_total: 8
asyncapis:
- description: ''
  name: Aifordatabase Webhooks
  slug: aifordatabase-webhooks
common:
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
- description: Local-stdio MCP server (npm aifordatabase-mcp@0.1.2, 9 tools). No hosted/remote endpoint.
  name: AI for Database MCP Server
  slug: ai-for-database-mcp-server
modified: '2026-08-26'
name: AI for Database
nav: Providers
network: true
overview: 'AI for Database publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Database, Analytics, Developer Tools, and Natural Language Query.


  The AI for Database catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AI for Database''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
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
  composite: 55.8
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 16.7
    contract_quality: 49.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- AI
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
- LLMSTxt
- OpenAPI
- Webhooks
- MCP
- PostgreSQL
- MySQL
- MongoDB
website: https://www.aifordatabase.com/for-agents/
---
