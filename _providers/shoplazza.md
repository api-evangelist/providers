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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 96
  human_in_the_loop: 1
  name: Shoplazza Agentic Access
  operation_count: 197
  slug: shoplazza-agentic-access
  summary_line: 197 operations · 96 acting · 1 human-in-the-loop
api_count: 20
apis:
- description: The Access API from Shoplazza — 1 operation(s) for access.
  name: Shoplazza Access API
  slug: shoplazza-access-api
- description: The App Proxy API from Shoplazza — 3 operation(s) for app proxy.
  name: Shoplazza App Proxy API
  slug: shoplazza-app-proxy-api
- description: The Billing API API from Shoplazza — 10 operation(s) for billing api.
  name: Shoplazza Billing API API
  slug: shoplazza-billing-api-api
- description: The Custom Area API from Shoplazza — 2 operation(s) for custom area.
  name: Shoplazza Custom Area API
  slug: shoplazza-custom-area-api
- description: The Customer API from Shoplazza — 6 operation(s) for customer.
  name: Shoplazza Customer API
  slug: shoplazza-customer-api
- description: The Data API from Shoplazza — 5 operation(s) for data.
  name: Shoplazza Data API
  slug: shoplazza-data-api
- description: The Discounts API from Shoplazza — 14 operation(s) for discounts.
  name: Shoplazza Discounts API
  slug: shoplazza-discounts-api
- description: Upload image materials to the material library and the material library operations of material
  name: Shoplazza File API
  slug: shoplazza-file-api
- description: The Fullfillment API from Shoplazza — 5 operation(s) for fullfillment.
  name: Shoplazza Fullfillment API
  slug: shoplazza-fullfillment-api
- description: The Gift Card API from Shoplazza — 3 operation(s) for gift card.
  name: Shoplazza Gift Card API
  slug: shoplazza-gift-card-api
- description: The Meta Definition API from Shoplazza — 5 operation(s) for meta definition.
  name: Shoplazza Meta Definition API
  slug: shoplazza-meta-definition-api
- description: The Metafield API from Shoplazza — 6 operation(s) for metafield.
  name: Shoplazza Metafield API
  slug: shoplazza-metafield-api
- description: The Order API from Shoplazza — 11 operation(s) for order.
  name: Shoplazza Order API
  slug: shoplazza-order-api
- description: The Order Risk API from Shoplazza — 4 operation(s) for order risk.
  name: Shoplazza Order Risk API
  slug: shoplazza-order-risk-api
- description: The Page API from Shoplazza — 4 operation(s) for page.
  name: Shoplazza Page API
  slug: shoplazza-page-api
- description: The Product API from Shoplazza — 21 operation(s) for product.
  name: Shoplazza Product API
  slug: shoplazza-product-api
- description: The Redirect API from Shoplazza — 3 operation(s) for redirect.
  name: Shoplazza Redirect API
  slug: shoplazza-redirect-api
- description: The Shop API from Shoplazza — 8 operation(s) for shop.
  name: Shoplazza Shop API
  slug: shoplazza-shop-api
- description: The Theme API from Shoplazza — 9 operation(s) for theme.
  name: Shoplazza Theme API
  slug: shoplazza-theme-api
- description: The Webhook API from Shoplazza — 3 operation(s) for webhook.
  name: Shoplazza Webhook API
  slug: shoplazza-webhook-api
artifact_total: 27
asyncapis:
- description: ''
  name: Shoplazza Webhooks
  slug: shoplazza-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shoplazza-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.shoplazza.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.shoplazza.dev/docs/app/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://www.shoplazza.dev/api/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://www.shoplazza.dev/docs/app/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://www.shoplazza.dev/docs/app/building-blocks/authentication/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.shoplazza.dev/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Shoplazza
- group: operate
  title: ''
  type: Support
  url: https://www.shoplazza.dev/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.shoplazza.com/
- group: start
  title: ''
  type: SignUp
  url: https://partners.shoplazza.com/
- group: start
  title: ''
  type: Login
  url: https://partners.shoplazza.com/partner-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shoplazza.cn/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shoplazza.cn/pages/privacy
- group: operate
  title: ''
  type: Deprecation
  url: https://www.shoplazza.dev/changelog
- group: other
  title: ''
  type: AppStore
  url: https://appstore.shoplazza.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shoplazza-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shoplazza-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shoplazza-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/shoplazza-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shoplazza-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/shoplazza-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shoplazza-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shoplazza-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/shoplazza-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shoplazza-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shoplazza-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shoplazza-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shoplazza-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/shoplazza-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shoplazza-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shoplazza-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shoplazza-agentic-access.yml
created: '2026-07-17'
description: Shoplazza is a global e-commerce SaaS platform that lets merchants build and run online stores, and lets partners extend the platform through public apps, payment apps, storefront themes, and checkout/theme extensions. Its developer surface is the versioned REST Admin API (date-based vYYYYMM versions served under /openapi/YYYY-MM/), authorized with OAuth 2.0 access tokens and scoped permissions, plus webhooks for store events, an app billing API, App Bridge for embedded admin apps, the Shoplazza CLI, and official OAuth SDKs. Shoplazza is backed by SoftBank Vision Fund. This profile was enriched from Shoplazza's public developer documentation (shoplazza.dev) and its published OpenAPI 3.1 specification.
image: https://www.shoplazza.dev/img/logo.png
layout: provider
mcp_servers:
- description: ''
  name: shoplazza-mcp.yml
  slug: shoplazza-mcpyml
modified: '2026-07-21'
name: Shoplazza
nav: Providers
network: true
overview: 'Shoplazza publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Access API, App Proxy API, Billing API API, and 17 more. Tagged areas include Company, Enterprise, E-Commerce, Online Store, and Retail.


  The Shoplazza catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shoplazza''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, signup flow, and 27 more developer resources.'
random_paper: 28
rate_limits:
- limit_count: 4
  name: Shoplazza Rate Limits
  slug: shoplazza-rate-limits
scopes:
- name: Shoplazza Scopes
  scope_count: 29
  slug: shoplazza-scopes
  summary_line: 29 scopes
score:
  band: developing
  composite: 54.7
  delta: -5.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 64.2
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 68.4
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Shoplazza Authentication
  slug: shoplazza-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Shoplazza Domain Security
  slug: shoplazza-domain-security
  summary_line: TLSv1.3 · HSTS
slug: shoplazza
tags:
- Company
- Enterprise
- E-Commerce
- Online Store
- Retail
- Payments
- Webhooks
- REST API
- Apps
- Developer Platform
website: https://www.shoplazza.dev/
---
