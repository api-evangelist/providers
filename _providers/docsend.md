---
access_model:
  confidence: high
  label: Self-serve signup, paid plans from $30/user/month
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://www.docsend.com/pricing/
  - https://www.docsend.com/signup
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: DocSend's hosted Model Context Protocol server — the only programmatic surface DocSend publishes. An MCP client POSTs Streamable-HTTP JSON-RPC to https://docsend.com/mcp (also reachable at https://mcp
  name: DocSend MCP Server
  slug: docsend-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Docsend Events
  slug: docsend-events
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
  url: https://www.docsend.com/trust-center/compliance
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
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/docsend-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dropbox.com/
- group: build
  title: ''
  type: Packages
  url: packages/docsend-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/docsend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docsend-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/docsend-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://app.intigriti.com/programs/dropbox/dropbox-vdp
- group: company
  title: ''
  type: Website
  url: https://www.docsend.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docsend.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.docsend.com/signup
- group: start
  title: ''
  type: Login
  url: https://docsend.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docsend.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docsend.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.docsend.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.docsend.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docsend
created: '2026-07-17'
description: DocSend is a secure document sharing and analytics platform, now part of Dropbox, used by sales, marketing, and fundraising teams to share pitch decks, sales collateral, and confidential documents through trackable links. It provides page-by-page viewer analytics, granular access controls (email verification, passcodes, expiration, watermarking), virtual data rooms, and e-signature. DocSend was surfaced as a portfolio company of Cowboy Ventures, DCM Ventures, and Uncork Capital and enriched by the API Evangelist pipeline. DocSend publishes no public REST API and no OpenAPI; its only programmatic surface is a live, OAuth-secured hosted Model Context Protocol (MCP) server at https://docsend.com/mcp, backed by RFC 8414 authorization-server discovery, RFC 9728 protected-resource metadata, dynamic client registration (RFC 7591), and mandatory PKCE. In August 2026 DocSend replaced the server's two coarse mcp:read / mcp:write scopes with five resource-scoped ones — documents:read,
  spaces:read, spaces:write, analytics:read, contacts:read.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docsend.png
layout: provider
mcp_servers:
- description: ''
  name: DocSend MCP Server
  slug: docsend-mcp-server
modified: '2026-08-14'
name: DocSend
nav: Providers
network: true
overview: 'DocSend publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Document Sharing, Sales Enablement, and Analytics.


  The DocSend catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DocSend''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 20 more developer resources.'
plans:
- name: Docsend Plans Pricing
  plan_count: 3
  slug: docsend-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Docsend Rate Limits
  slug: docsend-rate-limits
scopes:
- name: Docsend Scopes
  scope_count: 5
  slug: docsend-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 45.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docsend/refs/heads/main/screenshots/docsend-2026-08-17T123407.png
security:
- kind: authentication
  name: Docsend Authentication
  slug: docsend-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Docsend Domain Security
  slug: docsend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docsend Vulnerability Disclosure
  slug: docsend-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Docsend Trust Center
  slug: docsend-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701, ISO 22301, PCI DSS, HIPAA, CSA STAR Level 2, GDPR, CCPA, EU Cloud CoC, EU-US DPF, ISMAP
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
