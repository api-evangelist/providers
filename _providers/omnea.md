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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 11.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Omnea''s documented public REST API for programmatic access to the procurement platform. The reference is served as a client-rendered docs app; the OpenAPI definition is not published at a static path '
  name: Omnea Public API
  slug: omnea-public-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.omnea.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.omnea.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.omnea.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.omnea.co/
- group: company
  title: ''
  type: Blog
  url: https://www.omnea.co/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.omnea.co/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.omnea.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.omnea.co/documents/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.omnea.co/documents/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.omnea.co/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/omnea-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/omnea-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/omnea-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/omnea-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omnea-domain-security.yml
created: '2026-07-17'
description: Omnea is an AI-native procurement platform that automates the full source-to-pay (S2P) process, unifying intake management, strategic sourcing, third-party risk management, and supplier management behind autonomous agents. Buyers raise requests conversationally through Slack, Microsoft Teams, or an OAuth-protected remote MCP (Model Context Protocol) server, and Omnea routes intelligent workflows, price-intelligence benchmarking, continuous supplier monitoring, and automated approvals. The company is backed by Accel, Insight Partners, and Point Nine, and exposes a documented public REST API plus a hosted MCP endpoint for agent integrations. Added to the API Evangelist network from VC-portfolio discovery and enriched from live probes of its public surfaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omnea.png
layout: provider
mcp_servers:
- description: Omnea operates an official remote MCP (Model Context Protocol) server at https://mcp.omnea.co, surfaced from the Omnea homepage as its primary developer/integration entry point and used to power conve
  name: Omnea MCP Server
  slug: omnea-mcp-server
modified: '2026-07-20'
name: Omnea
nav: Providers
network: true
overview: 'Omnea publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Procurement, Source-to-Pay, and Supplier Management.


  Omnea''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.5
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omnea/refs/heads/main/screenshots/omnea-2026-08-07T190143.png
security:
- kind: authentication
  name: Omnea Authentication
  slug: omnea-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Omnea Domain Security
  slug: omnea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omnea
tags:
- Company
- Artificial Intelligence
- Procurement
- Source-to-Pay
- Supplier Management
- Spend Management
- Agents
- MCP
website: https://www.omnea.co/
---
