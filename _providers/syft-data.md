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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: The Export API from Syft Data — 1 operation(s) for export.
  name: Syft Data Export API
  slug: syft-data-export-api
- description: The Lookup API from Syft Data — 1 operation(s) for lookup.
  name: Syft Data Lookup API
  slug: syft-data-lookup-api
artifact_total: 7
asyncapis:
- description: ''
  name: Syft Data Webhooks
  slug: syft-data-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.syftdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.syftdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syftdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syftdata.com/implementation/lookup-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.syftdata.com/tutorial-basics/installation
- group: operate
  title: ''
  type: Support
  url: https://www.syftdata.com/support
- group: company
  title: ''
  type: Blog
  url: https://blog.syftdata.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syftdata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.syftdata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.syftdata.com/auth/syft-signup
- group: start
  title: ''
  type: Login
  url: https://app.syftdata.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syftdata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syftdata.com/privacy.html
- group: build
  title: ''
  type: SDKs
  url: packages/syft-data-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/syft-data-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/syft-data-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syft-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/syft-data-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/syft-data-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syft-data-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syft-data-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syft-data-llms.txt
created: '2026-07-17'
description: Syft Data, Inc. is a B2B lead-intelligence platform that identifies and qualifies high-intent prospects from inbound website traffic and LinkedIn engagement. Its tracking pixel reveals anonymous visitors, enriches contacts, scores them against an Ideal Customer Profile, and triggers multi-channel outreach ("motions") into CRM, email, LinkedIn, and ad platforms. For developers Syft ships a schema-driven analytics SDK and CLI (npm @syftdata/*), a server-side Lookup and Export REST API secured with sk_live_ keys, outbound webhooks, and an official hosted MCP server so AI agents can query visitor data and build automations from chat.
image: https://www.syftdata.com/
layout: provider
mcp_servers:
- description: ''
  name: syft-data-mcp.yml
  slug: syft-data-mcpyml
modified: '2026-07-21'
name: Syft Data
nav: Providers
network: true
overview: 'Syft Data publishes 2 APIs on the [APIs.io](https://apis.io/) network: Export API and Lookup API. Tagged areas include Company, Lead Intelligence, Intent Data, Website Visitor Identification, and Sales Intelligence.


  The Syft Data catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syft Data''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 54
scopes:
- name: Syft Data Scopes
  scope_count: 0
  slug: syft-data-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 82.2
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 54.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Syft Data Authentication
  slug: syft-data-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Syft Data Domain Security
  slug: syft-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: syft-data
tags:
- Company
- Lead Intelligence
- Intent Data
- Website Visitor Identification
- Sales Intelligence
- Go-To-Market
- Analytics
- MCP
website: https://www.syftdata.com/
---
