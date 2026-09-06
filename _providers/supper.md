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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-05'
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
- description: Supper exposes a hosted, remote MCP server so any MCP-compatible AI assistant (Claude, Claude Code, etc.) can query a company's connected data in natural language, grounded in Supper's semantic model.
  name: Supper MCP Server
  slug: supper-mcp-server
modified: '2026-07-21'
name: Supper
nav: Providers
network: true
overview: 'Supper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Analytics, Artificial Intelligence, and MCP.


  Supper''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, authentication, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supper/refs/heads/main/screenshots/supper-2026-09-02T161300.png
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
