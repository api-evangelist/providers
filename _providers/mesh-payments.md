---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: RESTful API for the Mesh spend management platform. Documented capabilities include connectivity verification, virtual card lifecycle management (issuance, suspension, cancellation), merchant and cate
  name: Mesh Payments API
  slug: mesh-payments-api
- description: OAuth-protected Model Context Protocol (MCP) server operated by Mesh at api.meshpayments.com/mcp. The endpoint advertises RFC 9728 OAuth 2.0 Protected Resource Metadata at /.well-known/oauth-protected
  name: Mesh Payments MCP Server
  slug: mesh-payments-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Mesh Payments Webhooks
  slug: mesh-payments-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mesh-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meshpayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.meshpayments.com
- group: docs
  title: ''
  type: Documentation
  url: https://kb.meshpayments.com/support/integrators-corner/
- group: operate
  title: ''
  type: Support
  url: https://kb.meshpayments.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://kb.meshpayments.com/
- group: company
  title: ''
  type: Blog
  url: https://meshpayments.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mesh-payments
- group: commercial
  title: ''
  type: Pricing
  url: https://meshpayments.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.meshpayments.com/
- group: start
  title: ''
  type: Login
  url: https://app.meshpayments.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meshpayments.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meshpayments.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://meshpayments.com/feature-updates/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mesh-payments-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mesh-payments-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mesh-payments-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mesh-payments-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mesh-payments-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mesh-payments-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mesh-payments-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mesh-payments-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mesh-payments-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://meshpayments.com/security-is-our-priority/
- group: auth
  title: ''
  type: Security
  url: https://meshpayments.com/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mesh-payments-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mesh-payments-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mesh-payments-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/mesh-payments-packages.yml
created: '2026-08-04'
description: Mesh Payments is a global travel and expense (T&E) and spend management platform for finance teams, combining corporate virtual and physical card issuing, expense management, accounts payable, procurement (ProcurePay), travel booking and accounting automation in a single system. Mesh exposes a RESTful API on api.meshpayments.com for virtual card lifecycle management, merchant and category controls, metadata tagging, authorization and settlement retrieval and real-time balance queries, authenticated with either HMAC-SHA256 request signing or OAuth 2.0 client credentials. It also publishes an OAuth-protected Model Context Protocol (MCP) server at api.meshpayments.com/mcp and a configurable webhooks surface, plus ERP, HRIS and TMC integrations.
image: https://meshpayments.com/wp-content/uploads/2026/05/meshpayments.png
layout: provider
mcp_servers:
- description: ''
  name: Mesh Payments MCP Server
  slug: mesh-payments-mcp-server
modified: '2026-08-04'
name: Mesh Payments
nav: Providers
network: true
overview: 'Mesh Payments publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Spend Management, Expense Management, and Corporate Cards.


  The Mesh Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mesh Payments'' developer surface includes documentation, support, engineering blog, pricing, signup flow, changelog, authentication, and 22 more developer resources.'
random_paper: 11
scopes:
- name: Mesh Payments Scopes
  scope_count: 1
  slug: mesh-payments-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 51.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 84.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mesh-payments/refs/heads/main/screenshots/mesh-payments-2026-08-07T172624.png
security:
- kind: authentication
  name: Mesh Payments Authentication
  slug: mesh-payments-authentication
  summary_line: http/oauth2/custom-hmac · 3 schemes
- kind: domain-security
  name: Mesh Payments Domain Security
  slug: mesh-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mesh Payments Vulnerability Disclosure
  slug: mesh-payments-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mesh Payments Trust Center
  slug: mesh-payments-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, PCI DSS, GDPR, CCPA, Vendor Security Alliance (VSA)
slug: mesh-payments
tags:
- Company
- Payments
- Spend Management
- Expense Management
- Corporate Cards
- Travel
- Accounts Payable
- Fintech
- Card Issuing
- Accounting Automation
website: https://meshpayments.com/
---
