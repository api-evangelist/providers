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
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'REST/JSON API for the Iru (formerly Kandji) endpoint management platform: read fleet data and run device actions, manage apps, Library items, Library uploads, Blueprints, tenant activity, and Automate'
  name: Iru Endpoint Management API
  slug: iru-endpoint-management-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://iru.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iru.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iru.com
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.iru.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iru.com/en/endpoint/api/iru-api-overview.md
- group: operate
  title: ''
  type: Support
  url: https://support.kandji.io
- group: company
  title: ''
  type: Blog
  url: https://iru.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://iru.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://iru.com/request-demo
- group: start
  title: ''
  type: Login
  url: https://iru.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iru.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iru.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kandji-inc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iru.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/iru-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iru-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iru-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iru-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/iru-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/iru-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/iru-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/iru-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iru-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/iru-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/iru-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iru-domain-security.yml
created: '2026-07-17'
description: Iru (formerly Kandji) is an enterprise IT and security company that unifies device management, endpoint security, workforce identity, and compliance automation into a single AI-powered platform, trusted by 6,000+ organizations including Airbus, Plaid, and Vercel. Its three core products are Endpoint (Apple, Windows, and Android device management, threat detection and response, and vulnerability scanning via a single lightweight agent), Identity (passwordless, device-bound workforce access), and Compliance (AI-driven, audit-ready compliance monitoring with a public Trust Center). For developers, Iru exposes the Iru Endpoint Management REST API (tenant-scoped bearer tokens, 10,000 requests/hour/tenant, US and EU regions), an official hosted MCP server for AI assistants, first-party Python tooling (iructl, irupkg), and a Postman collection.
image: https://www.iru.com/hubfs/assets/favicons/og-image.png
layout: provider
mcp_servers:
- description: 'Official Iru-hosted, remote MCP server that exposes the Iru Endpoint Management (Enterprise) API surface as MCP tools for AI assistants. Enabled per API token (the "Enable MCP" toggle when creating a '
  name: Iru MCP Server
  slug: iru-mcp-server
modified: '2026-07-19'
name: Iru
nav: Providers
network: true
overview: 'Iru publishes 1 API on the [APIs.io](https://apis.io/) network: Endpoint Management API. Tagged areas include Company, Device Management, Apple MDM, Endpoint Security, and Identity and Access Management.


  Iru''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Iru Rate Limits
  slug: iru-rate-limits
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 37.0
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iru/refs/heads/main/screenshots/iru-2026-07-25T222931.png
security:
- kind: authentication
  name: Iru Authentication
  slug: iru-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Iru Domain Security
  slug: iru-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Iru Trust Center
  slug: iru-trust-center
  summary_line: trust center published
slug: iru
tags:
- Company
- Device Management
- Apple MDM
- Endpoint Security
- Identity and Access Management
- Compliance
- Vulnerability Management
- IT Management
- Security
website: https://iru.com
---
