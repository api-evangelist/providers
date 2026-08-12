---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 64
  human_in_the_loop: 64
  name: Securitize Agentic Access
  operation_count: 125
  slug: securitize-agentic-access
  summary_line: 125 operations · 64 acting · 64 human-in-the-loop
api_count: 7
apis:
- description: OAuth-based identity API that lets partners add "Log in with Securitize iD" to their own application and, with investor consent, retrieve verified KYC/KYB/AML identity data — investor information, ver
  name: Securitize Connect API (Securitize iD)
  slug: securitize-connect-api-securitize-id
- description: Public, unauthenticated Model Context Protocol server ("Securitize Connector") that gives AI assistants and agents real-time, standardized access to the Securitize tokenized-asset catalog — listing as
  name: Securitize MCP Server
  slug: securitize-mcp-server
- description: The APAC API from Securitize — 4 operation(s) for apac.
  name: Securitize APAC API
  slug: securitize-apac-api
- description: The Domains API from Securitize — 74 operation(s) for domains.
  name: Securitize Domains API
  slug: securitize-domains-api
- description: The Health Check API from Securitize — 1 operation(s) for health check.
  name: Securitize Health Check API
  slug: securitize-health-check-api
- description: The Travel Rule API from Securitize — 4 operation(s) for travel rule.
  name: Securitize Travel Rule API
  slug: securitize-travel-rule-api
- description: The Webhooks API from Securitize — 4 operation(s) for webhooks.
  name: Securitize Webhooks API
  slug: securitize-webhooks-api
artifact_total: 14
asyncapis:
- description: ''
  name: Securitize Webhooks
  slug: securitize-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://securitize.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://securitize.io/apis
- group: docs
  title: ''
  type: Documentation
  url: https://domain-api-docs.securitize.io/
- group: docs
  title: ''
  type: APIReference
  url: https://public-api.sandbox.securitize.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://domain-api-docs.securitize.io/api/api-specs
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/16645978/UVsEVopd
- group: operate
  title: ''
  type: Support
  url: https://developersupport.securitize.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://securitize.io/learn/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/securitize-io
- group: start
  title: ''
  type: SignUp
  url: https://id.securitize.io/
- group: auth
  title: ''
  type: Security
  url: https://securitize.io/bug-bounty
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/securitize-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/securitize-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/securitize-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/securitize-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/securitize-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/securitize-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/securitize-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/securitize-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/securitize-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/securitize-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/securitize-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/securitize-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/securitize-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/securitize-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/securitize-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/securitize-domains-overlay.yaml
created: '2026-08-05'
description: 'Securitize is a tokenization platform and SEC-registered financial services group that issues, manages, and services digital securities representing real-world assets — tokenized U.S. Treasuries, private credit, private equity, funds, and equities — for asset managers including BlackRock (BUIDL), Apollo (ACRED), Hamilton Lane, KKR, and VanEck (VBILL). The company operates a registered transfer agent, broker-dealer (Securitize Markets), alternative trading system, fund administration business, and an EU-approved investment firm, and it publishes three developer-facing APIs: a Domain API covering the full securities lifecycle (investor onboarding, KYC/KYB, accreditation, fundraising, issuance, token wallets, blockchain transactions, snapshots, and holder records), a Connect API that acts as an OAuth provider for Securitize iD single sign-on and verified-identity sharing, and a Webhook API for real-time investor event delivery. Securitize also runs a public, unauthenticated MCP
  server that exposes its tokenized-asset catalog to AI agents.'
image: https://cdn.builder.io/api/v1/image/assets%2Fd39b51a544e84e2fbb2445f58c6c6f2c%2F0eeaf40c7ecd4ee0a05f030d32ae949e
layout: provider
mcp_servers:
- description: ''
  name: securitize-mcp.yml
  slug: securitize-mcpyml
modified: '2026-08-05'
name: Securitize
nav: Providers
network: true
overview: 'Securitize publishes 5 APIs on the [APIs.io](https://apis.io/) network, including APAC API, Domains API, Health Check API, and 2 more. Tagged areas include tokenization, digital-securities, real-world-assets, capital-markets, and fund-administration.


  The Securitize catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Securitize''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 51
scopes:
- name: Securitize Scopes
  scope_count: 3
  slug: securitize-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 45.3
  delta: 1.8
  facets:
    commercial_clarity: 13.2
    contract_quality: 50.1
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Securitize Authentication
  slug: securitize-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Securitize Domain Security
  slug: securitize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Securitize Vulnerability Disclosure
  slug: securitize-vulnerability-disclosure
  summary_line: contact published
slug: securitize
tags:
- tokenization
- digital-securities
- real-world-assets
- capital-markets
- fund-administration
- transfer-agent
- kyc
- aml
- identity-verification
- blockchain
- broker-dealer
- private-credit
- mcp
- webhooks
website: https://securitize.io/
---
