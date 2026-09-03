---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Highnote Agentic Access
  operation_count: 1
  slug: highnote-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Create and configure card products (createCardProduct) for debit, credit, prepaid, fleet, and charge programs, then issue virtual, physical, and tokenized digital payment cards (issuePaymentCardForApp
  name: Highnote Issuing API
  slug: highnote-issuing-api
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Onboard US person and US business account holders (createUSPersonAccountHolder, createUSBusinessAccountHolder), manage authorized users, submit and accept card product applications (createAccountHolde
  name: Highnote Account Holders & Onboarding API
  slug: highnote-account-holders-api
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Accept and process payments as a merchant acquirer through the single GraphQL endpoint. Authorize, capture, charge, and cancel payment transactions (authorizePaymentCard, capturePaymentTransaction, ch
  name: Highnote Acquiring API
  slug: highnote-acquiring-api
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Move funds across multiple payment rails from a single API surface (initiateTransferBetweenFinancialAccounts, initiateAchTransfer, initiateUnifiedFundsTransfer). Supports standard and same-day ACH, do
  name: Highnote Money Movement API
  slug: highnote-money-movement-api
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Query and manage the full payment transaction lifecycle (paymentTransactions, transactionBatches) with HQL search and Relay cursor pagination, read pending, cleared, and settled states against the rea
  name: Highnote Transactions & Disputes API
  slug: highnote-transactions-api
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Attach spend rules and velocity rules to card products and financial accounts to govern where, when, and how much can be spent, and register a collaborative-authorization endpoint (addCollaborativeAut
  name: Highnote Spend Controls & Collaborative Authorization API
  slug: highnote-spend-controls-api
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Register HTTPS webhook notification targets (addWebhookNotificationTarget), activate and deactivate them, and subscribe to event types (addSubscriptionsToNotificationTarget) so Highnote pushes account
  name: Highnote Webhooks & Event Notifications API
  slug: highnote-webhooks-api
artifact_total: 19
asyncapis:
- description: Highnote delivers event notifications to registered HTTPS webhook notification targets (addWebhookNotificationTarget) via outbound POST. Subscribe a target to event types with addSubscriptionsToNotifi
  name: Highnote Event Notifications
  slug: highnote-events-asyncapi
collections:
- collection_type: postman
  name: Highnote GraphQL API
  slug: postman-highnote-graphql-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Highnote GraphQL API
  slug: open-highnote-graphql-api
- collection_type: open
  name: Highnote GraphQL API
  slug: open-highnote
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/highnote-accept-a-payment.md
- group: docs
  title: ''
  type: APIReference
  url: https://docs.highnote.com/docs/tags/api
- group: build
  title: ''
  type: SDKs
  url: https://docs.highnote.com/docs/developers/sdks/about-sdks
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/highnote/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/highnote-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highnote-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/highnote-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://highnote.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.highnote.com/docs/developers/about-developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.highnote.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Highnote-Platform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/highnote-platform
- group: company
  title: ''
  type: Blog
  url: https://highnote.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://highnote.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://highnote.com/agreements/terms/01-05-22
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://highnote.com/agreements/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.highnote.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.highnote.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.highnote.com/docs/get-started/about-highnote
- group: start
  title: ''
  type: Signup
  url: https://dashboard.highnote.com
- group: commercial
  title: ''
  type: Plans
  url: plans/highnote-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/highnote-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/highnote-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/highnote-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/highnote-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/highnote-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/highnote-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/highnote-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/highnote-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/highnote-graphql-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/highnote-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.highnote.com/docs/get-started/introduction/pci-dss-compliance
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/highnote-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/highnote-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/highnote-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://docs.highnote.com/docs/developers/api/status-changes
- group: design
  title: ''
  type: Conventions
  url: conventions/highnote-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/highnote-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/highnote-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/highnote-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/highnote-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/highnote-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/highnote-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/highnote-events-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
created: '2026-06-20'
description: Highnote is a modern, unified embedded-finance and banking-as-a-service platform for card issuing, card acquiring, credit, and real-time money movement, with a built-in real-time programmable ledger and full program management. The entire platform is driven by a single GraphQL API at https://api.us.highnote.com/graphql (test https://api.us.test.highnote.com/graphql), authenticated with a base64-encoded API key over HTTP Basic auth. One endpoint covers card products, US person and business account holders (KYC/KYB onboarding), financial accounts and credit lines, virtual/physical/tokenized payment cards, transaction authorization and clearing, disputes, spend and velocity rules, collaborative authorization, multi-rail money movement (ACH, wire, RTP, push-to-card), and outbound webhook event notifications. Highnote is a US-based platform serving digital-first businesses embedding financial products; access is enterprise, contract-gated, with self-serve dashboard signup and a test
  environment.
finops:
- name: Highnote Finops
  service_category: Financial Services
  slug: highnote-finops
graphqls:
- description: The [Highnote](https://highnote.com/) embedded-finance platform exposes a **single GraphQL
  name: Highnote GraphQL API
  slug: highnote-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highnote.png
layout: provider
modified: '2026-07-23'
name: Highnote
nav: Providers
network: true
overview: 'Highnote publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Issuing API, Account Holders & Onboarding API, Acquiring API, and 4 more. Tagged areas include Card Issuing, Card Acquiring, Embedded Finance, Banking as a Service, and Fintech.


  The Highnote catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Highnote''s developer surface includes API reference, authentication, documentation, engineering blog, pricing, support, getting-started guide, and 38 more developer resources.'
plans:
- name: Highnote Plans Pricing
  plan_count: 2
  slug: highnote-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Highnote Rate Limits
  slug: highnote-rate-limits
score:
  band: exemplar
  composite: 73.2
  coverage:
    artifact_dirs: 27
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 67.3
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 71.1
  previous_composite: 73.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/screenshots/highnote-2026-06-20T182732.png
security:
- kind: authentication
  name: Highnote Authentication
  slug: highnote-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Highnote Domain Security
  slug: highnote-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: highnote
tags:
- Card Issuing
- Card Acquiring
- Embedded Finance
- Banking as a Service
- Fintech
- Payments
- GraphQL
- Ledger
- Credit
- Money Movement
- ACH
- KYC
- United States
website: https://highnote.com
---
