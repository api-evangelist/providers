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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 126
  human_in_the_loop: 1
  name: Lucid Agentic Access
  operation_count: 220
  slug: lucid-agentic-access
  summary_line: 220 operations · 126 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: 'The Lucid REST API provides programmatic access to manage documents, users, folders, sharing, licensing, and audit logs across the Lucid Suite (Lucidchart, Lucidspark, and Lucidscale). 154 operations '
  name: Lucid REST API
  slug: lucid-rest-api
- description: The Lucid Data API enables external applications to create, read, update, and delete structured data linked to Lucid documents. 50 operations across data sets, data set grants and properties, data sou
  name: Lucid Data API
  slug: lucid-data-api
- description: The Lucid SCIM 2.0 API enables identity providers to automatically provision and deprovision users and groups in a Lucid account. 15 operations over /Users, /Groups, /Schemas and /ServiceProviderConfi
  name: Lucid SCIM API
  slug: lucid-scim-api
- description: 'Lucid''s remote Model Context Protocol server. Connects AI clients (ChatGPT, Claude, Microsoft Copilot, Cursor) to Lucid documents so they can be searched, retrieved, edited, summarized and created in '
  name: Lucid MCP Server
  slug: lucid-mcp-server
- description: The API behind Lucid's ChatGPT plugin — accepts Mermaid diagram source and returns a rendered image link plus, for flowcharts, an editable Lucidchart link. Described by the OpenAPI that Lucid's /.well
  name: Lucid ChatGPT Plugin API
  slug: lucid-chatgpt-plugin-api
artifact_total: 16
collections:
- collection_type: open
  name: Lucid Data API
  slug: open-lucid-data-api
- collection_type: open
  name: Lucid REST API
  slug: open-lucid-rest-api
- collection_type: open
  name: Lucid SCIM API
  slug: open-lucid-scim-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lucid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lucid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucid-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lucid-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucid-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lucid.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lucid.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lucid.co/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lucid.co/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lucid.co/docs/welcome
- group: operate
  title: ''
  type: Support
  url: https://community.lucid.co/lucid-for-developers-6
- group: company
  title: ''
  type: Blog
  url: https://lucid.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidsoftware
- group: commercial
  title: ''
  type: Pricing
  url: https://lucid.app/pricing/lucidchart
- group: start
  title: ''
  type: SignUp
  url: https://lucid.app/users/login?activate=lucidchart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lucid.co/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lucid.co/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://lucid.co/security
- group: auth
  title: ''
  type: Security
  url: https://lucid.co/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lucid-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lucid.co/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lucid-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lucid-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lucid-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lucid-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lucid-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lucid-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lucid-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucid-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/lucid-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lucid-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lucid-cli.yml
- group: design
  title: ''
  type: Components
  url: components/lucid-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucid-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lucid-mcp.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/lucid_stock/
created: '2026-08-01'
description: 'Lucid Software Inc. is the visual collaboration company behind the Lucid Suite — Lucidchart (intelligent diagramming), Lucidspark (virtual whiteboarding) and Lucidscale (cloud visualization) — plus the Lucid Cloud, Process and Enterprise Shield accelerators and airfocus. The Lucid Developer Platform at developer.lucid.co publishes three OpenAPI-described surfaces: the Lucid REST API on api.lucid.co for documents, folders, sharing, embeds, comments, teams, repositories, legal holds, licenses and audit logs; the Lucid Data API on data.lucid.app for the structured data sets, collections, schemas and data items that back data-linked diagrams; and a SCIM 2.0 API on users.lucid.app for enterprise user and group provisioning. Lucid also ships an in-editor Extension API (lucid-extension-sdk plus the lucid-package CLI), an Embed SDK, and an OAuth-gated remote MCP server at mcp.lucid.app that lets AI clients search, read, edit and create Lucid documents. Lucid is privately held and trades
  on secondary markets.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidchart.png
layout: provider
mcp_servers:
- description: ''
  name: Lucid MCP Server
  slug: lucid-mcp-server
modified: '2026-08-01'
name: Lucid
nav: Providers
network: true
overview: 'Lucid publishes 4 APIs on the [APIs.io](https://apis.io/) network, including REST API, Data API, SCIM API, and 1 more. Tagged areas include Visual Collaboration, Diagramming, Whiteboarding, Productivity, and Software-as-a-Service.


  Lucid''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 30 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 5
  name: Lucid Rate Limits
  slug: lucid-rate-limits
scopes:
- name: Lucid Scopes
  scope_count: 143
  slug: lucid-scopes
  summary_line: 143 scopes · authorizationCode
score:
  band: strong
  composite: 62.9
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 60.0
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 76.3
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucid/refs/heads/main/screenshots/lucid-2026-08-07T171817.png
security:
- kind: authentication
  name: Lucid Authentication
  slug: lucid-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lucid Domain Security
  slug: lucid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lucid Vulnerability Disclosure
  slug: lucid-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Lucid Trust Center
  slug: lucid-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001 (AI management systems), CSA STAR, PCI DSS, FedRAMP Moderate, TX-RAMP, IRAP (Australia), GDPR, CCPA
slug: lucid
tags:
- Visual Collaboration
- Diagramming
- Whiteboarding
- Productivity
- Software-as-a-Service
- Cloud Visualization
- SCIM
- Identity
- Data
- MCP
website: https://lucid.co/
---
