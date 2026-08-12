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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/docsend-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/docsend-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docsend-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/docsend-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/docsend-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/docsend-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/docsend-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docsend-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docsend-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.docsend.com
created: '2026-07-17'
description: DocSend is a secure document sharing and analytics platform, now part of Dropbox, used by sales, marketing, and fundraising teams to share pitch decks, sales collateral, and confidential documents through trackable links. It provides page-by-page viewer analytics, granular access controls (email verification, passcodes, expiration, watermarking), virtual data rooms, and e-signature. DocSend was surfaced as a portfolio company of Cowboy Ventures, DCM Ventures, and Uncork Capital and enriched by the API Evangelist pipeline. Enrichment confirmed a live, OAuth-secured hosted Model Context Protocol (MCP) server at mcp.docsend.com backed by RFC 8414 authorization-server discovery, dynamic client registration (RFC 7591), and PKCE.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docsend.png
layout: provider
mcp_servers:
- description: ''
  name: docsend-mcp.yml
  slug: docsend-mcpyml
modified: '2026-07-18'
name: DocSend
nav: Providers
network: true
overview: 'DocSend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Document Sharing, Sales Enablement, and Analytics.


  DocSend''s developer surface includes authentication and 9 more developer resources.'
random_paper: 40
scopes:
- name: Docsend Scopes
  scope_count: 2
  slug: docsend-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 15.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 15.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Docsend Authentication
  slug: docsend-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Docsend Domain Security
  slug: docsend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Docsend Trust Center
  slug: docsend-trust-center
  summary_line: PCI DSS, GDPR
slug: docsend
tags:
- Company
- Enterprise
- Document Sharing
- Sales Enablement
- Analytics
- Data Room
- E-Signature
- MCP
- Dropbox
website: https://www.docsend.com
---
