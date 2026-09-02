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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The my.anydesk I REST API automates retrieval and management of AnyDesk account data from the my.anydesk management console: license and account details, registered clients and their aliases/online st'
  name: AnyDesk REST API
  slug: anydesk-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://anydesk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.anydesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.anydesk.com/
- group: docs
  title: ''
  type: APIReference
  url: https://support.anydesk.com/docs/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://support.anydesk.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.anydesk.com/docs/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anydesk
- group: start
  title: ''
  type: SignUp
  url: https://my.anydesk.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://anydesk.com/en/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anydesk.com/en/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://support.anydesk.com/docs/gdpr-compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anydesk-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/anydesk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anydesk-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anydesk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anydesk-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anydesk-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anydesk-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anydesk-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anydesk-mcp.yml
created: '2026-07-17'
description: AnyDesk is a German remote desktop and remote access software company whose clients provide cross-platform remote control, unattended access, remote support and file transfer for Windows, macOS, Linux, Android and iOS. For administrators, the my.anydesk management console centralizes license, client, address book and session management, and exposes a JSON-over-HTTPS REST API (my.anydesk I REST API, v1.1.1) that automates retrieval and management of account data — license and account details, registered clients, session history and comments, aliases and address books — so teams can integrate AnyDesk with billing, ticketing and session-logging systems. AnyDesk ships an official open-source Python library for the API and supports SSO/SAML for console access.
image: https://anydesk.com/favicon.ico
layout: provider
mcp_servers:
- description: Candidate MCP server tool list derived from the documented my.anydesk I REST API command set. AnyDesk publishes no official hosted or remote MCP server; these tools are a proposed one-tool-per-documen
  name: AnyDesk MCP Server
  slug: anydesk-mcp-server
modified: '2026-07-17'
name: AnyDesk
nav: Providers
network: true
overview: 'AnyDesk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Remote Work, Remote Desktop, Remote Access, and Remote Support.


  AnyDesk''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, authentication, and 13 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 30.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anydesk/refs/heads/main/screenshots/anydesk-2026-07-25T200502.png
security:
- kind: authentication
  name: Anydesk Authentication
  slug: anydesk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anydesk Domain Security
  slug: anydesk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anydesk
tags:
- Company
- Remote Work
- Remote Desktop
- Remote Access
- Remote Support
- IT Management
- REST API
- Security
website: https://anydesk.com/
---
