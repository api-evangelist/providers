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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The ION Factory OS GraphQL API. A single GraphQL endpoint for reading and writing manufacturing data in ION: Runs, Procedures, Parts, mBOM/aBOM, inventory, notifications, and webhook subscriptions. Au'
  name: ION GraphQL API
  slug: ion-graphql-api
artifact_total: 6
asyncapis:
- description: ''
  name: First Resonance Webhooks
  slug: first-resonance-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/first-resonance-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.firstresonance.io/
- group: company
  title: ''
  type: Website
  url: https://firstresonance.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://manual.firstresonance.io/api
- group: docs
  title: ''
  type: Documentation
  url: https://manual.firstresonance.io/
- group: docs
  title: ''
  type: APIReference
  url: https://manual.firstresonance.io/api/interactive-api-explorer
- group: start
  title: ''
  type: GettingStarted
  url: https://manual.firstresonance.io/api/how-to-create-an-app-with-ion
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-resonance-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.firstresonance.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.firstresonance.io/plans
- group: start
  title: ''
  type: SignUp
  url: https://app.firstresonance.io/login
- group: operate
  title: ''
  type: Support
  url: https://www.firstresonance.io/contact/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firstresonance.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firstresonance.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firstresonance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firstresonance.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.firstresonance.io/changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://manual.firstresonance.io/api/api-change-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/first-resonance-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/first-resonance-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-resonance-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-resonance-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/first-resonance-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/first-resonance-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-resonance-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/first-resonance-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/first-resonance-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-resonance-domain-security.yml
created: '2026-07-17'
description: First Resonance builds ION, a modern Factory Operating System (MES) for companies manufacturing complex hardware in aerospace, defense, robotics, medical devices, and clean energy. ION provides digital work instructions (Procedures and Runs), part and inventory traceability, mBOM/aBOM management, quality and compliance workflows, production scheduling (ION AutoPlan), and analytics. For developers, ION exposes a GraphQL API (api.buildwithion.com) secured with OAuth 2.0 client-credentials API keys, cursor-based (Relay) pagination, webhook subscriptions for realtime events, and a beta hosted MCP server so AI agents can operate the factory system. This profile was enriched from First Resonance's public developer manual.
image: https://www.firstresonance.io/favicon.ico
layout: provider
mcp_servers:
- description: First Resonance publishes an official hosted MCP (Model Context Protocol) server that lets AI agents operate ION Factory OS. It is currently in beta and available on staging only; production is not ye
  name: First Resonance MCP Server
  slug: first-resonance-mcp-server
modified: '2026-07-19'
name: First Resonance
nav: Providers
network: true
overview: 'First Resonance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Manufacturing, MES, and Factory Operating System.


  The First Resonance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  First Resonance''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 46.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-resonance/refs/heads/main/screenshots/first-resonance-2026-07-25T214610.png
security:
- kind: authentication
  name: First Resonance Authentication
  slug: first-resonance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: First Resonance Domain Security
  slug: first-resonance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: First Resonance Trust Center
  slug: first-resonance-trust-center
  summary_line: SOC 2, FedRAMP, GDPR, FIPS 140
slug: first-resonance
tags:
- Company
- Infrastructure
- Manufacturing
- MES
- Factory Operating System
- Hardware
- Aerospace
- GraphQL
- Traceability
- Supply Chain
website: https://firstresonance.io
---
