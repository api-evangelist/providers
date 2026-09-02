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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Browser SDK exposing window.blinkSDK. Provides Login with Blink (getAuthorizationCode), subscription entitlement checks (isSubscribed, getSubscription, onSubscriptionChange), single-article charging (
  name: Blink SDK for JavaScript
  slug: blink-ledger-systems-sdk
- description: 'Outbound webhook stream delivering signed JSON notifications for subscription, payment and donation lifecycle events. Every payload is signed with ed25519 over the canonicalized event object, with an '
  name: Blink Notifications (Webhooks)
  slug: blink-ledger-systems-notifications
- description: Client account login and bearer token issuance.
  name: Blink Ledger Systems Authentication API
  slug: blink-ledger-systems-authentication-api
- description: Registration and retrieval of OAuth application credentials.
  name: Blink Ledger Systems OAuth Applications API
  slug: blink-ledger-systems-oauth-applications-api
- description: Blink user profile exchange.
  name: Blink Ledger Systems Users API
  slug: blink-ledger-systems-users-api
artifact_total: 13
asyncapis:
- description: ''
  name: Blink Ledger Systems Notifications Webhooks
  slug: blink-ledger-systems-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blink Server-Side Authentication API
  slug: open-blink-ledger-systems-authentication-api
- collection_type: open
  name: Blink Server-Side Authentication OAuth Applications API
  slug: open-blink-ledger-systems-oauth-applications-api
- collection_type: open
  name: Blink Server-Side Authentication Users API
  slug: open-blink-ledger-systems-users-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blink-ledger-systems-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://blink.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blink.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blink.net/docs/getting-started/overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blink.net/docs/api-reference/functions.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blink.net/docs/getting-started/quick-start.html
- group: operate
  title: ''
  type: Support
  url: https://docs.blink.net/docs/getting-started/support.html
- group: start
  title: ''
  type: SignUp
  url: https://blink.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blink.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blink.net/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blink.net
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/blink-ledger-systems-server-side-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/blink-ledger-systems-server-side-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/blink-ledger-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blink-ledger-systems-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blink-ledger-systems-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blink-ledger-systems-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blink-ledger-systems-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blink-ledger-systems-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/blink-ledger-systems-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/blink-ledger-systems-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blink-ledger-systems-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/blink-ledger-systems-notifications-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blink-ledger-systems-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blink-ledger-systems-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blink-ledger-systems-domain-security.yml
created: '2026-07-17'
description: Blink (Blink Ledger Systems Inc.) builds online identity and payment technologies for digital publishers. A single Blink account works across publishers, giving readers one universal login and frictionless payment so they can subscribe, donate, or buy an individual article or podcast with one click, or enable autopay for small frequent purchases. Publishers integrate three products — Blink Identity, Blink Pay and Blink Donate — through one hosted JavaScript SDK that places Blink-managed panels into the page, a dashboard-configured User Journeys rules engine, four server-side JSON endpoints for OAuth2 login, and a signed webhook notification stream covering subscription, payment and donation events. Founded 2017; incorporated in the US in 2018 and surfaced in the API Evangelist network as a Polychain portfolio company.
image: https://blink.net/resources/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Blink Ledger Systems MCP Server
  slug: blink-ledger-systems-mcp-server
modified: '2026-07-20'
name: Blink Ledger Systems
nav: Providers
network: true
overview: 'Blink Ledger Systems publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, OAuth Applications API, and Users API. Tagged areas include Company, Infrastructure, Payments, Identity, and Authentication.


  The Blink Ledger Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blink Ledger Systems'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 20 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 21.0
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 27.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blink-ledger-systems/refs/heads/main/screenshots/blink-ledger-systems-2026-07-25T203322.png
security:
- kind: authentication
  name: Blink Ledger Systems Authentication
  slug: blink-ledger-systems-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Blink Ledger Systems Domain Security
  slug: blink-ledger-systems-domain-security
  summary_line: TLSv1.3
slug: blink-ledger-systems
tags:
- Company
- Infrastructure
- Payments
- Identity
- Authentication
- Publishing
- Media
- Subscription
- Donations
- Micropayments
- Paywall
- Webhook
website: https://blink.net
---
