---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.supper.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supper.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.supper.co/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.supper.co/pricing-2
- group: start
  title: ''
  type: SignUp
  url: https://app.supper.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.supper.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.supper.co/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.supper.co/resources
- group: agent
  title: ''
  type: MCPServer
  url: mcp/supper-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supper-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supper-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/supper-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supper-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.supper.co/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/supper-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supper-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supper-llms.txt
created: '2026-07-17'
description: Supper is an AI data agent for high-growth companies that connects a company's data, cleans it, and maps its business language so teams can answer critical questions in plain English within minutes. Supper reads from the customer's warehouse (Snowflake, BigQuery, Postgres, Redshift) and SaaS tools (CRM, ERP, marketing, product, payments) over a read-only connection, builds a verified semantic model, and exposes a hosted, OAuth-secured MCP server so any MCP-compatible AI assistant such as Claude can query that data via natural language and return dashboards and answers grounded in that model.
image: https://cdn.prod.website-files.com/6878f348cb0839fd6dc7599d/6892361798f9bef9d3c1a4a1_supper-open-graph%20(1).jpg
layout: provider
mcp_servers:
- description: ''
  name: supper-mcp.yml
  slug: supper-mcpyml
modified: '2026-07-21'
name: Supper
nav: Providers
network: true
overview: 'Supper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Analytics, Artificial Intelligence, and MCP.


  Supper''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, authentication, and 11 more developer resources.'
random_paper: 91
score:
  band: emerging
  composite: 27.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 27.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Supper Authentication
  slug: supper-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Supper Domain Security
  slug: supper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Supper Trust Center
  slug: supper-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: supper
tags:
- Company
- Data
- Analytics
- Artificial Intelligence
- MCP
- Business Intelligence
- Semantic Layer
- Data Agent
website: https://www.supper.co
---
