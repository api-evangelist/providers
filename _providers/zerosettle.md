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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Configurable cancel flow with retention offers
  name: ZeroSettle Cancel Flow API
  slug: zerosettle-cancel-flow-api
- description: Create checkout sessions and payment intents for web purchases
  name: ZeroSettle Checkout API
  slug: zerosettle-checkout-api
- description: Query user entitlements (active purchases and subscriptions)
  name: ZeroSettle Entitlements API
  slug: zerosettle-entitlements-api
- description: Track SDK analytics events
  name: ZeroSettle Events API
  slug: zerosettle-events-api
- description: Switch & Save migration tracking
  name: ZeroSettle Migration API
  slug: zerosettle-migration-api
- description: Fetch the product catalog for your app
  name: ZeroSettle Products API
  slug: zerosettle-products-api
- description: Restore purchases for a user
  name: ZeroSettle Restore API
  slug: zerosettle-restore-api
- description: Sync and query StoreKit transactions
  name: ZeroSettle StoreKit API
  slug: zerosettle-storekit-api
- description: Manage subscription lifecycle (cancel, pause, resume)
  name: ZeroSettle Subscriptions API
  slug: zerosettle-subscriptions-api
- description: Query transaction status and history
  name: ZeroSettle Transactions API
  slug: zerosettle-transactions-api
- description: Subscription upgrade/downgrade offers
  name: ZeroSettle Upgrade Offers API
  slug: zerosettle-upgrade-offers-api
- description: Unified offer + subscription-state resolver (SDK 1.2+)
  name: ZeroSettle User Offer API
  slug: zerosettle-user-offer-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ZeroSettle IAP Cancel Flow API
  slug: open-zerosettle-cancel-flow-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Checkout API
  slug: open-zerosettle-checkout-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Entitlements API
  slug: open-zerosettle-entitlements-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Events API
  slug: open-zerosettle-events-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Migration API
  slug: open-zerosettle-migration-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Products API
  slug: open-zerosettle-products-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Restore API
  slug: open-zerosettle-restore-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow StoreKit API
  slug: open-zerosettle-storekit-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Subscriptions API
  slug: open-zerosettle-subscriptions-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Transactions API
  slug: open-zerosettle-transactions-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow Upgrade Offers API
  slug: open-zerosettle-upgrade-offers-api
- collection_type: open
  name: ZeroSettle IAP Cancel Flow User Offer API
  slug: open-zerosettle-user-offer-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zerosettle-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zerosettle-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zerosettle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zerosettle-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/zerosettle-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zerosettle-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zerosettle-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zerosettle-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/zerosettle-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zerosettle-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/zerosettle-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zerosettle-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zerosettle-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zerosettle-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zerosettle.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zerosettle.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zerosettle
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zerosettle.io/api-reference/introduction
- group: start
  title: ''
  type: Quickstart
  url: https://docs.zerosettle.io/iap/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zerosettle.io/changelog
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.zerosettle.io/?mode=sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.zerosettle.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://zerosettle.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zerosettle.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zerosettle.io/legal/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@zerosettle.io
created: '2026-07-17'
description: ZeroSettle is a Y Combinator-backed subscription revenue platform that lets iOS, Android, Flutter, and React Native app developers offer direct web billing as an alternative to App Store and Google Play in-app purchase — the pitch is "keep 85% of your revenue, not 70%." As Merchant of Record (on Stripe Connect, or BYOS), it handles web checkout, entitlements, subscription lifecycle, StoreKit transaction syncing, retention cancel flows, upgrade/migration offers, and compliance external-purchase reporting. The ZeroSettle IAP API (REST/JSON, X-ZeroSettle-Key auth) powers all of its client SDKs, with a free tier plus a $29/month Pro plan.
image: https://zerosettle.io/images/favicon/favicon.ico
layout: provider
mcp_servers:
- description: No official hosted ZeroSettle MCP server was found. This is a CANDIDATE tool surface derived from the 25 operations of the ZeroSettle IAP API (https://api.zerosettle.io/v1, X-ZeroSettle-Key auth) — on
  name: ZeroSettle MCP Server
  slug: zerosettle-mcp-server
modified: '2026-07-21'
name: ZeroSettle
nav: Providers
network: true
overview: 'ZeroSettle publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Cancel Flow API, Checkout API, Entitlements API, and 9 more. Tagged areas include Company, Payments, In-App Purchase, Subscription, and Merchant of Record.


  ZeroSettle''s developer surface includes authentication, changelog, sandbox, documentation, API reference, quickstart, signup flow, and 20 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 57.5
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 49.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zerosettle/refs/heads/main/screenshots/zerosettle-2026-08-17T083101.png
security:
- kind: authentication
  name: Zerosettle Authentication
  slug: zerosettle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zerosettle Domain Security
  slug: zerosettle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zerosettle
tags:
- Company
- Payments
- In-App Purchase
- Subscription
- Merchant of Record
- Billing
- Mobile
- Developer Tools
website: https://docs.zerosettle.io
---
