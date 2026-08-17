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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Keap Agentic Access
  operation_count: 26
  slug: keap-agentic-access
  summary_line: 26 operations · 10 acting
api_count: 32
apis:
- description: Keap REST Hooks webhook surface. Subscribers register a `hookUrl` and `eventKey` via the v1 REST API (`POST /rest/v1/hooks`), complete an `X-Hook-Secret` verification handshake, then receive HTTP POST
  name: Keap REST Hooks
  slug: rest-hooks
- description: Keap Affiliate API — 48 operations across 28 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Affiliate API
  slug: keap-affiliate-api
- description: Keap Appointment API — 8 operations across 4 paths on the Keap REST v1 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Appointment API (v1)
  slug: keap-appointment-v1-api
- description: Keap Automation API — 10 operations across 9 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Automation API
  slug: keap-automation-api
- description: Keap Campaign API — 6 operations across 6 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Campaigns API
  slug: keap-campaigns-api
- description: Keap Category Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Category Discounts API
  slug: keap-category-discounts-api
- description: Keap Company API — 22 operations across 11 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Companies API
  slug: keap-companies-api
- description: Keap Contact API — 27 operations across 16 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Contacts API
  slug: keap-contacts-api
- description: Keap E-Commerce API — 16 operations across 12 paths on the Keap REST v1 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap E-Commerce API (v1)
  slug: keap-e-commerce-v1-api
- description: Keap Email API — 10 operations across 8 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Email API
  slug: keap-email-api
- description: Keap File API — 5 operations across 2 paths on the Keap REST v1 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap File API (v1)
  slug: keap-file-v1-api
- description: Keap Files API — 6 operations across 3 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Files API
  slug: keap-files-api
- description: Keap Free Trial Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Free Trial Discounts API
  slug: keap-free-trial-discounts-api
- description: Keap Lead Source Categories API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Source Categories API
  slug: keap-lead-source-categories-api
- description: Keap Lead Source Expenses API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Source Expenses API
  slug: keap-lead-source-expenses-api
- description: Keap Lead Source Recurring Expenses API — 6 operations across 3 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Source Recurring Expenses API
  slug: keap-lead-source-recurring-expenses-api
- description: Keap Lead Sources API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Sources API
  slug: keap-lead-sources-api
- description: Keap Note API — 21 operations across 11 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Note API
  slug: keap-note-api
- description: Keap Opportunity API — 26 operations across 13 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Opportunities API
  slug: keap-opportunities-api
- description: Keap Order Total Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Order Total Discounts API
  slug: keap-order-total-discounts-api
- description: Keap Orders API — 29 operations across 16 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Orders API
  slug: keap-orders-api
- description: Keap Product Categories API — 9 operations across 5 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Product Categories API
  slug: keap-product-categories-api
- description: Keap Product Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Product Discounts API
  slug: keap-product-discounts-api
- description: Keap Product Interest Bundles API — 8 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Product Interest Bundles API
  slug: keap-product-interest-bundles-api
- description: Keap Product API — 11 operations across 6 paths on the Keap REST v1 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Product API (v1)
  slug: keap-product-v1-api
- description: Keap Products API — 17 operations across 9 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Products API
  slug: keap-products-api
- description: Keap Shipping Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Shipping Discounts API
  slug: keap-shipping-discounts-api
- description: Keap Subscription Plans API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Subscription Plans API
  slug: keap-subscription-plans-api
- description: Keap Subscriptions API — 20 operations across 11 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Subscriptions API
  slug: keap-subscriptions-api
- description: Keap Tags API — 14 operations across 8 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Tags API
  slug: keap-tags-api
- description: Keap Task API — 19 operations across 9 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Tasks API
  slug: keap-tasks-api
- description: Keap Users API — 5 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Users API
  slug: keap-users-api
artifact_total: 51
asyncapis:
- description: AsyncAPI 2.6 description of the Keap (formerly Infusionsoft) REST Hooks webhook surface. Keap REST Hooks are subscriptions that are created and managed via the v1 REST API (`POST /rest/v1/hooks`). Onc
  name: Keap REST Hooks
  slug: keap-resthooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Keap REST Campaigns API
  slug: open-keap-campaigns-api
- collection_type: open
  name: Keap REST Campaigns Companies API
  slug: open-keap-companies-api
- collection_type: open
  name: Keap REST Campaigns Contacts API
  slug: open-keap-contacts-api
- collection_type: open
  name: Keap REST Campaigns Opportunities API
  slug: open-keap-opportunities-api
- collection_type: open
  name: Keap REST Campaigns Orders API
  slug: open-keap-orders-api
- collection_type: open
  name: Keap REST Campaigns Products API
  slug: open-keap-products-api
- collection_type: open
  name: Keap REST Campaigns Tags API
  slug: open-keap-tags-api
- collection_type: open
  name: Keap REST Campaigns Tasks API
  slug: open-keap-tasks-api
- collection_type: open
  name: Keap REST API
  slug: open-keap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/keap-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keap-growing
- group: company
  title: ''
  type: Website
  url: https://keap.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.infusionsoft.com/
- group: start
  title: ''
  type: Signup
  url: https://keap.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://keap.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.infusionsoft.com/
- group: auth
  title: ''
  type: OAuth
  url: https://developer.infusionsoft.com/getting-started-oauth-keys/
- group: company
  title: ''
  type: Blog
  url: https://keap.com/small-business-automation-blog
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keap-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/keap-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/keap-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/keap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/keap-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keap-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/keap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/keap-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/keap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keap-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thryv.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/keap-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keap-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/keap-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/keap-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/keap-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/keap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keap-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/keap-resthooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/keap-resthooks-asyncapi.yml
- group: design
  title: ''
  type: Rules
  url: rules/keap-asyncapi-spectral-rules.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.infusionsoft.com/docs/restv2/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.infusionsoft.com/getting-started-oauth-keys/
- group: operate
  title: ''
  type: Support
  url: https://developer.infusionsoft.com/get-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.infusionsoft.com/faqs/
- group: operate
  title: ''
  type: Community
  url: https://community.keap.com/c/api/5
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infusionsoft
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/2915979/UVByKWEZ
- group: start
  title: ''
  type: SignUp
  url: https://keys.developer.keap.com/accounts/create
- group: start
  title: ''
  type: Login
  url: https://keys.developer.keap.com/my-apps
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thryv.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thryv.com/privacy/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.keap.com/apps
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/infusionsoft/keap-sdk
- group: operate
  title: ''
  type: KnownIssues
  url: https://developer.infusionsoft.com/support/known-issues/
- group: docs
  title: ''
  type: DeveloperGuide
  url: https://developer.infusionsoft.com/developer-guide/
- group: other
  title: ''
  type: X
  url: https://twitter.com/keapgrowing
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Keap
created: '2026-05-11'
description: Keap (formerly Infusionsoft, now part of Thryv) is a CRM, sales and marketing automation platform for small businesses that combines contact management, email and text marketing, e-commerce, affiliate management and pipeline automation. Keap publishes two live OpenAPI 3.1 contracts covering 540 operations — REST v2 (399 operations, the Default version) and REST v1 (141 operations, still the only home of REST Hooks webhooks and Appointments) — plus a deprecated XML-RPC surface. Authentication is OAuth 2.0 authorization code with rotating refresh tokens, or Personal Access Tokens and Service Account Keys, all with a single `full` scope. Keap also operates an undocumented but live remote MCP server at https://api.keap.com/mcp secured with OAuth 2.1, PKCE and dynamic client registration, and ships first-party SDKs for six languages generated in lock-step from its own spec.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keap.png
layout: provider
mcp_servers:
- description: ''
  name: keap-mcp.yml
  slug: keap-mcpyml
modified: '2026-08-13'
name: Keap
nav: Providers
network: true
overview: 'Keap publishes 32 APIs on the [APIs.io](https://apis.io/) network, including REST Hooks, Affiliate API, Appointment API (v1), and 29 more. Tagged areas include CRM, Sales, Marketing Automation, Small Business, and E-Commerce.


  The Keap catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Keap''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, sandbox, API reference, and 44 more developer resources.'
plans:
- name: Keap Plans Pricing
  plan_count: 1
  slug: keap-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 0
  name: Keap Rate Limits
  slug: keap-rate-limits
rules:
- name: Keap API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: keap-asyncapi-spectral-rules
scopes:
- name: Keap Scopes
  scope_count: 1
  slug: keap-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 67.7
  delta: 28.9
  facets:
    commercial_clarity: 73.7
    contract_quality: 65.9
    developer_ergonomics: 84.8
    discoverability: 81.5
    governance: 62.5
    operational_transparency: 36.8
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/keap/refs/heads/main/screenshots/keap-2026-06-20T183931.png
security:
- kind: authentication
  name: Keap Authentication
  slug: keap-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Keap Domain Security
  slug: keap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: keap
tags:
- CRM
- Sales
- Marketing Automation
- Small Business
- E-Commerce
- Contacts
- Email Marketing
- Subscriptions
- Affiliate Management
- Webhooks
- MCP
- Payments
website: https://keap.com
---
