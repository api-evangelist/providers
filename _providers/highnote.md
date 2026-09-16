---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-09-15'
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
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/skills/highnote-accept-a-payment.md
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
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/agentic-access/highnote-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/highnote-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/security/highnote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/highnote-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/authentication/highnote-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/plans/highnote-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/highnote-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/rate-limits/highnote-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/highnote-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/finops/highnote-finops.yml
  title: ''
  type: FinOps
  url: finops/highnote-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/packages/highnote-packages.yml
  title: ''
  type: Packages
  url: packages/highnote-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/packages/highnote-packages.yml
  title: ''
  type: SDKs
  url: packages/highnote-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/mcp/highnote-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/highnote-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/mcp/highnote-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/highnote-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/llms/highnote-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/highnote-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/well-known/highnote-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/highnote-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/overlays/highnote-graphql-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/highnote-graphql-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/conformance/highnote-conformance.yml
  title: ''
  type: Conformance
  url: conformance/highnote-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.highnote.com/docs/get-started/introduction/pci-dss-compliance
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/errors/highnote-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/highnote-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/errors/highnote-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/highnote-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/lifecycle/highnote-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/highnote-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://docs.highnote.com/docs/developers/api/status-changes
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/conventions/highnote-conventions.yml
  title: ''
  type: Conventions
  url: conventions/highnote-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/conventions/highnote-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/highnote-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/changelog/highnote-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/highnote-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/sandbox/highnote-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/highnote-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/components/highnote-components.yml
  title: ''
  type: Components
  url: components/highnote-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/data-model/highnote-data-model.yml
  title: ''
  type: DataModel
  url: data-model/highnote-data-model.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/asyncapi/highnote-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/highnote-events-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/asyncapi/highnote-events-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/highnote-events-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/highnote/refs/heads/main/skills/_index.yml
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
  composite: 71.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 67.3
    developer_ergonomics: 74.4
    discoverability: 75.9
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 71.8
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
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
