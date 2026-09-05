---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Slope Agentic Access
  operation_count: 40
  slug: slope-agentic-access
  summary_line: 40 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Auth API from Slope — 2 operation(s) for auth.
  name: Slope Auth API
  slug: slope-auth-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Customers API from Slope — 6 operation(s) for customers.
  name: Slope Customers API
  slug: slope-customers-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Files API from Slope — 1 operation(s) for files.
  name: Slope Files API
  slug: slope-files-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Orders API from Slope — 11 operation(s) for orders.
  name: Slope Orders API
  slug: slope-orders-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Payout Accounts API from Slope — 2 operation(s) for payout accounts.
  name: Slope Payout Accounts API
  slug: slope-payout-accounts-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Persons API from Slope — 1 operation(s) for persons.
  name: Slope Persons API
  slug: slope-persons-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Prescreens API from Slope — 2 operation(s) for prescreens.
  name: Slope Prescreens API
  slug: slope-prescreens-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Simulation API from Slope — 7 operation(s) for simulation.
  name: Slope Simulation API
  slug: slope-simulation-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The Transactions API from Slope — 1 operation(s) for transactions.
  name: Slope Transactions API
  slug: slope-transactions-api
- baseURL: https://api.slopepay.com
  baseurl_source: declared
  description: The User Links API from Slope — 2 operation(s) for user links.
  name: Slope User Links API
  slug: slope-user-links-api
arazzos:
- description: Create an order, wait for the customer to open it, then finalize for payout.
  name: Create a Slope order and finalize it
  slug: slope-create-order-and-finalize
- description: Create a refund adjustment against an order and read it back.
  name: Refund a finalized Slope order
  slug: slope-refund-order
- description: Get a repayment estimate then fully repay an order (requires Slope-Link-Token).
  name: Estimate and repay a Slope order
  slug: slope-repay-order
- description: Create a sandbox test customer, set eligibility, create an order, and approve it.
  name: Simulate an approved order in the sandbox
  slug: slope-sandbox-approve-order
artifact_total: 31
asyncapis:
- description: Generated event surface for Slope webhooks. Payload schemas documented at https://developers.slopepay.com/docs/schema. Signed via the Slope-Signature header (HMAC-SHA256).
  name: Slope Webhook Events
  slug: slope-events-asyncapi
- description: ''
  name: Slope Webhooks
  slug: slope-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Slope v4 Auth API
  slug: open-slope-auth-api
- collection_type: open
  name: Slope v4 Auth Customers API
  slug: open-slope-customers-api
- collection_type: open
  name: Slope v4 Auth Files API
  slug: open-slope-files-api
- collection_type: open
  name: Slope v4 Auth Orders API
  slug: open-slope-orders-api
- collection_type: open
  name: Slope v4 Auth Payout Accounts API
  slug: open-slope-payout-accounts-api
- collection_type: open
  name: Slope v4 Auth Persons API
  slug: open-slope-persons-api
- collection_type: open
  name: Slope v4 Auth Prescreens API
  slug: open-slope-prescreens-api
- collection_type: open
  name: Slope v4 Auth Simulation API
  slug: open-slope-simulation-api
- collection_type: open
  name: Slope v4 Auth Transactions API
  slug: open-slope-transactions-api
- collection_type: open
  name: Slope v4 Auth User Links API
  slug: open-slope-user-links-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/slope-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.slopepay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.slopepay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.slopepay.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.slopepay.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.slopepay.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.slopepay.com/contact#support
- group: company
  title: ''
  type: Blog
  url: https://www.slopepay.com/blog
- group: start
  title: ''
  type: Login
  url: https://dashboard.slopepay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.slopepay.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.slopepay.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.slopepay.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.slopepay.com/docs/rfc-v4-api
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slope-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/slope-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/slope-v4-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/slope-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/slope-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/slope-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/slope-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/slope-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/slope-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/slope-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/slope-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/slope-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/slope-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/slope-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/slope-events-asyncapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slope-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slope-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slope-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slope-create-order-and-finalize.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slope-refund-order.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slope-repay-order.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slope-sandbox-approve-order.yml
created: '2026-07-17'
description: Slope is a fintech company providing credit infrastructure for business lending - an embedded buy-now-pay-later (BNPL) and working-capital solution that lets merchants offer flexible net-terms financing to their business (B2B) buyers at checkout with no added risk. Its platform combines an embedded line-of-credit product, the SlopeScore business cash-flow score for underwriting, and a developer API (v4) for creating customers and orders, driving checkout via the Slope.js widget or a hosted redirect, finalizing orders for payout, issuing refunds/adjustments, handling repayments, and subscribing to webhook events. Slope is backed by GGV Capital and has announced a relationship with Amazon.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slope.png
layout: provider
modified: '2026-07-21'
name: Slope
nav: Providers
network: true
overview: 'Slope publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Customers API, Files API, and 7 more. Tagged areas include Company, Fintech, Payments, Embedded Finance, and BNPL.


  The Slope catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Slope''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, sandbox, changelog, and 29 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 0
  name: Slope Rate Limits
  slug: slope-rate-limits
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 63.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 43.4
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slope/refs/heads/main/screenshots/slope-2026-08-17T081924.png
security:
- kind: authentication
  name: Slope Authentication
  slug: slope-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Slope Domain Security
  slug: slope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: slope
tags:
- Company
- Fintech
- Payments
- Embedded Finance
- BNPL
- Lending
- Credit
- B2B
- Checkout
website: https://www.slopepay.com/
---
