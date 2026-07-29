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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Zest Equity Agentic Access
  operation_count: 23
  slug: zest-equity-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 8
apis:
- description: OAuth 2.0 JWT-Bearer assertion grant. Exchange a partner-signed JWT for a short-lived bearer access token, then send that token in the Authorization header on every partner API call.
  name: Zest Equity Authentication API
  slug: zest-equity-authentication-api
- description: Read-only access to the spaas-contract registry (templates, catalogs, primitives, samples) used to validate SPV-request `attributes`.
  name: Zest Equity Contracts API
  slug: zest-equity-contracts-api
- description: Bulk-create investor records with partial-success semantics. Each row carries its own status / error envelope so a single bad row never fails the batch.
  name: Zest Equity Investors API
  slug: zest-equity-investors-api
- description: Submit SPV creation requests, inspect their lifecycle, and cancel pending ones. SPV requests are reviewed by Zest admins and produce SPV materialisation on approval.
  name: Zest Equity SPV Requests API
  slug: zest-equity-spv-requests-api
- description: Upload signed subscription forms (PDF or image) for partner-managed subscriptions. Files are streamed to private storage and referenced on the Bid.
  name: Zest Equity Subscription Forms API
  slug: zest-equity-subscription-forms-api
- description: 'Upload wire-transfer receipts plus funding metadata. Strict order: a signed form must already be on record before fundings can be uploaded.'
  name: Zest Equity Subscription Fundings API
  slug: zest-equity-subscription-fundings-api
- description: Create one or more subscriptions for a single SPV.
  name: Zest Equity Subscriptions API
  slug: zest-equity-subscriptions-api
- description: Service health and OpenAPI introspection endpoints.
  name: Zest Equity System API
  slug: zest-equity-system-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Mint an access token then submit and read back a contract-validated SPV creation request.
  name: Zest — authenticate and create an SPV request
  slug: zest-equity-create-spv-request
- description: Bulk-create investors, subscribe one to an SPV, then upload the signed form and funding receipt in strict order.
  name: Zest — onboard investors and record a subscription
  slug: zest-equity-onboard-and-subscribe
artifact_total: 16
asyncapis:
- description: ''
  name: Zest Equity Webhooks
  slug: zest-equity-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zest-equity-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zest-equity-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zest-equity-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zest-equity-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zest-equity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zest-equity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zest-equity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zest-equity-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zest-equity-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zest-equity-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zest-equity-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/zest-equity-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/zest-equity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://zestequity.com
- group: design
  title: ''
  type: DataModel
  url: data-model/zest-equity-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zest-equity-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zest-equity-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zest-equity-create-spv-request.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zest-equity-onboard-and-subscribe.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zestequity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zestequity.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zestequity.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zestequity.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.zestequity.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.zestequity.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.zestequity.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://www.zestequity.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zestequity
- group: company
  title: ''
  type: Website
  url: https://zestequity.com
created: '2026-07-17'
description: 'Zest Equity is the digital infrastructure for private-market transactions — built in MENA, used worldwide. Its SPV-as-a-Service platform lets partners create DIFC-regulated Special Purpose Vehicles, run FSRA-regulated escrow and deal-arranging, bulk-onboard investors, and process subscriptions. The Zest Public API exposes this workflow programmatically: OAuth 2.0 JWT-Bearer (RFC 7523, EdDSA) authentication, idempotent write endpoints, a versioned contract-template engine, and a nine-event HMAC-signed webhook surface — so fund managers, family offices, VCs, and PE firms can embed SPV setup, fund administration, and regulatory compliance directly inside their own product.'
image: https://cdn.prod.website-files.com/699db6380f5e26c60d1ebda3/6a31ad4a4c9ad7f045465700_favicon%20light.png
layout: provider
mcp_servers:
- description: ''
  name: zest-equity-mcp.yml
  slug: zest-equity-mcpyml
modified: '2026-07-21'
name: Zest Equity
nav: Providers
network: true
overview: 'Zest Equity publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Investors API, and 5 more. Tagged areas include Company, Fintech, Private Markets, SPV, and Investments.


  The Zest Equity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zest Equity''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 23 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 50.9
  delta: -0.7
  facets:
    commercial_clarity: 31.6
    contract_quality: 66.3
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Zest Equity Authentication
  slug: zest-equity-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zest Equity Domain Security
  slug: zest-equity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zest-equity
tags:
- Company
- Fintech
- Private Markets
- SPV
- Investments
- Escrow
- Fund Administration
- MENA
- Webhooks
- Regulated
website: https://zestequity.com
---
