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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 79.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Zest Agentic Access
  operation_count: 23
  slug: zest-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 8
apis:
- description: OAuth 2.0 JWT-Bearer assertion grant. Exchange a partner-signed JWT for a short-lived bearer access token, then send that token in the Authorization header on every partner API call.
  name: Zest Authentication API
  slug: zest-authentication-api
- description: Read-only access to the spaas-contract registry (templates, catalogs, primitives, samples) used to validate SPV-request `attributes`.
  name: Zest Contracts API
  slug: zest-contracts-api
- description: Bulk-create investor records with partial-success semantics. Each row carries its own status / error envelope so a single bad row never fails the batch.
  name: Zest Investors API
  slug: zest-investors-api
- description: Submit SPV creation requests, inspect their lifecycle, and cancel pending ones. SPV requests are reviewed by Zest admins and produce SPV materialisation on approval.
  name: Zest SPV Requests API
  slug: zest-spv-requests-api
- description: Upload signed subscription forms (PDF or image) for partner-managed subscriptions. Files are streamed to private storage and referenced on the Bid.
  name: Zest Subscription Forms API
  slug: zest-subscription-forms-api
- description: 'Upload wire-transfer receipts plus funding metadata. Strict order: a signed form must already be on record before fundings can be uploaded.'
  name: Zest Subscription Fundings API
  slug: zest-subscription-fundings-api
- description: Create one or more subscriptions for a single SPV.
  name: Zest Subscriptions API
  slug: zest-subscriptions-api
- description: Service health and OpenAPI introspection endpoints.
  name: Zest System API
  slug: zest-system-api
artifact_total: 13
asyncapis:
- description: ''
  name: Zest Webhooks
  slug: zest-webhooks
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zestequity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zestequity.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zestequity.com/api-reference/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zestequity.com/quickstart
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zest-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zest-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zest-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zest-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zest-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zest-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zest-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zest-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zest-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zest-agentic-access.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zest-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zest-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zest-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zestequity
- group: company
  title: ''
  type: Blog
  url: https://www.zestequity.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.zestequity.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.zestequity.com/sign-in
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.zestequity.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://zestequity.com
created: '2026-07-17'
description: 'Zest Equity is a DIFC/ADGM-based provider of digital infrastructure for private-market transactions across the Middle East and North Africa. Its SPV-as-a-Service (SPaaS) platform lets partners create Cayman/DIFC Special Purpose Vehicles, run FSRA-regulated escrow, and arrange private capital deals. The Zest Public API gives partners programmatic access to the core workflow: OAuth 2.0 JWT-Bearer authentication, contract-validated SPV creation requests, bulk investor onboarding, subscription processing (signed forms + funding receipts), and nine HMAC-SHA256-signed webhook lifecycle events, with Idempotency-Key support on write endpoints and a uniform error envelope.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zest.png
layout: provider
mcp_servers:
- description: ''
  name: zest-mcp.yml
  slug: zest-mcpyml
modified: '2026-07-21'
name: Zest
nav: Providers
network: true
overview: 'Zest publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Investors API, and 5 more. Tagged areas include Company, SPV, Private Markets, Fintech, and Equity.


  The Zest catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zest''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 18 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 50.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 67.0
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 50.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Zest Authentication
  slug: zest-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Zest Domain Security
  slug: zest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zest
tags:
- Company
- SPV
- Private Markets
- Fintech
- Equity
- Investors
- Escrow
- SPaaS
- MENA
- API
website: https://zestequity.com
---
