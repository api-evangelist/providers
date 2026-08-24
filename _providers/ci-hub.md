---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.4
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: The HTTP API a partner platform calls to embed CI HUB's DAM connectivity in its own product. A partner backend signs an RS256 JWT and exchanges it at POST /auth/exchangeToken for a CI HUB access token
  name: CI HUB Access SDK API
  slug: access-sdk
- description: The other direction of the CI HUB platform. A DAM, MAM, PIM, CMS, stock or cloud-storage vendor writes an integration that translates its own proprietary API into CI HUB's handler format using defineI
  name: CI HUB Integration SDK
  slug: integration-sdk
- description: A hosted, remote Model Context Protocol server that gives an AI client governed access to the DAM systems a user has connected through CI HUB. It exposes core system, asset and folder tools — provider
  name: CI HUB MCP Server (Bright AI Connector)
  slug: mcp
artifact_total: 10
collections:
- collection_type: open
  name: CI HUB Access SDK API
  slug: open-ci-hub-access
common:
- group: company
  title: ''
  type: Website
  url: https://ci-hub.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ci-hub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ci-hub.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ci-hub.com/access
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ci-hub.com/access/getting-started
- group: operate
  title: ''
  type: Support
  url: https://ci-hub.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.ci-hub.com/
- group: company
  title: ''
  type: Blog
  url: https://ci-hub.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CI-HUB-GmbH
- group: commercial
  title: ''
  type: Pricing
  url: https://ci-hub.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/ci-hub-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://ci-hub.com/start-free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ci-hub.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ci-hub.com/legal/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/ci-hub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ci-hub-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ci-hub-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ci-hub-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ci-hub-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ci-hub-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ci-hub-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ci-hub-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ci-hub-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'CI HUB (CI HUB GmbH, Berlin) builds the connector layer between digital asset repositories and the applications creative and marketing teams actually work in. Its Connector plugs Adobe Creative Cloud, Microsoft 365, Google Workspace, Figma, Sketch, Canva, WordPress, SharePoint, Salesforce and Asana into more than 60 DAM, MAM, PIM, CMS, stock and cloud-storage systems through one uniform panel, so an asset is placed, relinked and version-checked without leaving the design or document. For developers CI HUB publishes two SDKs at developer.ci-hub.com. The Access SDK is an HTTP API under /api/v1 that lets a partner platform embed that same connectivity: a partner backend signs an RS256 JWT, exchanges it for a CI HUB session, connects an end user to a DAM provider, then browses, searches and reads assets over one contract regardless of which DAM is behind it. The Integration SDK runs the other direction, letting a DAM, PIM or storage vendor translate its own API into CI HUB''s handler
  format and appear in every CI HUB connector. CI HUB also operates a hosted MCP server (mcp.ci-hub.com, marketed as the Bright AI Connector) that exposes governed, permission-mapped DAM search and asset operations to ChatGPT, Claude, Gemini, Microsoft Copilot and any other MCP-compatible client.'
image: https://ci-hub.com/hubfs/CI-HUB_logo-new.svg
layout: provider
mcp_servers:
- description: A hosted, remote MCP server that gives an AI client governed access to whichever DAM, PIM, CMS or cloud-storage systems the end user has connected through CI HUB. The pitch is a governance layer rathe
  name: CI HUB MCP Server
  slug: ci-hub-mcp-server
modified: '2026-08-12'
name: CI HUB
nav: Providers
network: true
overview: 'CI HUB publishes 1 API on the [APIs.io](https://apis.io/) network: Access SDK API. Tagged areas include Company, Digital Asset Management, Content Management, Product Information Management, and Integration.


  CI HUB''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Ci Hub Plans Pricing
  plan_count: 12
  slug: ci-hub-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Ci Hub Rate Limits
  slug: ci-hub-rate-limits
scopes:
- name: Ci Hub Scopes
  scope_count: 0
  slug: ci-hub-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.3
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 30.3
    contract_quality: 59.3
    developer_ergonomics: 61.3
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 23.7
  previous_composite: 58.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ci-hub/refs/heads/main/screenshots/ci-hub-2026-08-17T080817.png
security:
- kind: authentication
  name: Ci Hub Authentication
  slug: ci-hub-authentication
  summary_line: http/apiKey/oauth2 · 0 schemes
- kind: domain-security
  name: Ci Hub Domain Security
  slug: ci-hub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ci-hub
tags:
- Company
- Digital Asset Management
- Content Management
- Product Information Management
- Integration
- Connectors
- Creative Tools
- Marketing
- Brand Management
- MCP
- Cloud Storage
- Germany
website: https://ci-hub.com/
---
