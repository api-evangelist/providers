---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: An OAuth-protected Model Context Protocol endpoint served from the Vanderhall Admin Portal at https://portal.vanderhallusa.com/mcp. The endpoint is live and speaks JSON-RPC 2.0, but every method — inc
  name: Vanderhall Admin Portal MCP Server
  slug: vanderhall-admin-portal-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://vanderhallusa.com/
- group: start
  title: ''
  type: Login
  url: https://dealer.vanderhallusa.com/
- group: operate
  title: ''
  type: Support
  url: https://dealer.vanderhallusa.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vanderhallusa.com/privacy-policy-2023/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vanderhall
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vanderhall-motor-works-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vanderhall-motor-works-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vanderhall-motor-works-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vanderhall-motor-works-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vanderhall-motor-works-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vanderhall-motor-works-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vanderhall-motor-works-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vanderhall-motor-works-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vanderhall-motor-works-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vanderhall-motor-works-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/vanderhall-motor-works-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vanderhall-motor-works-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vanderhall-motor-works-domain-security.yml
created: '2026-09-02'
description: 'Vanderhall Motor Works is a privately held American vehicle manufacturer founded in 2010 by Steve Hall and headquartered in Provo, Utah. The company hand-builds three-wheeled autocycles — the Laguna, Venice, Venice Speedster, Carmel and Santarosa — alongside the all-electric Edison and the quad-motor Brawley off-road UTV, selling through an independent dealer network rather than direct to consumers. Its software footprint is internal rather than commercial: Vanderhall runs a dealer portal, an admin portal and a parts/accessory shop on its own domain, and the admin portal publishes an OAuth-protected Model Context Protocol (MCP) endpoint at https://portal.vanderhallusa.com/mcp with RFC 8414 authorization-server metadata, RFC 9728 protected-resource metadata and RFC 7591 dynamic client registration. There is no public developer program, no published OpenAPI, and no public API reference.'
image: https://dealer.vanderhallusa.com/android-icon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Vanderhall Admin Portal MCP Server
  slug: vanderhall-admin-portal-mcp-server
modified: '2026-09-02'
name: Vanderhall Motor Works
nav: Providers
network: true
overview: 'Vanderhall Motor Works publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Manufacturing, Electric Vehicles, and Powersports.


  Vanderhall Motor Works'' developer surface includes support, authentication, and 16 more developer resources.'
plans:
- name: Vanderhall Motor Works Plans Pricing
  plan_count: 0
  slug: vanderhall-motor-works-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Vanderhall Motor Works Rate Limits
  slug: vanderhall-motor-works-rate-limits
scopes:
- name: Vanderhall Motor Works Scopes
  scope_count: 0
  slug: vanderhall-motor-works-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Vanderhall Motor Works Authentication
  slug: vanderhall-motor-works-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vanderhall Motor Works Domain Security
  slug: vanderhall-motor-works-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vanderhall-motor-works
tags:
- Company
- Automotive
- Manufacturing
- Electric Vehicles
- Powersports
- Autocycles
- Dealer Network
- Model Context Protocol
- Utah
website: https://vanderhallusa.com/
---
