---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Treasury Prime Agentic Access
  operation_count: 38
  slug: treasury-prime-agentic-access
  summary_line: 38 operations · 17 acting
api_count: 1
apis:
- description: REST API covering Persons, Businesses, Accounts, Cards, Payments (ACH, Wire, Book), Transactions, Statements, Counterparties, External Transfers, and Webhooks across a network of sponsor banks.
  name: Treasury Prime Bank API
  slug: rest-api
- description: Outbound HTTP webhook delivery for account, card, transaction, payment, and KYC events.
  name: Treasury Prime Webhooks
  slug: webhooks
- description: The Accounts API from Treasury Prime — 2 operation(s) for accounts.
  name: Treasury Prime Accounts API
  slug: treasury-prime-accounts-api
- description: The Businesses API from Treasury Prime — 2 operation(s) for businesses.
  name: Treasury Prime Businesses API
  slug: treasury-prime-businesses-api
- description: The Cards API from Treasury Prime — 2 operation(s) for cards.
  name: Treasury Prime Cards API
  slug: treasury-prime-cards-api
- description: The Health API from Treasury Prime — 1 operation(s) for health.
  name: Treasury Prime Health API
  slug: treasury-prime-health-api
- description: The Payments API from Treasury Prime — 8 operation(s) for payments.
  name: Treasury Prime Payments API
  slug: treasury-prime-payments-api
- description: The Persons API from Treasury Prime — 1 operation(s) for persons.
  name: Treasury Prime Persons API
  slug: treasury-prime-persons-api
- description: The Statements API from Treasury Prime — 1 operation(s) for statements.
  name: Treasury Prime Statements API
  slug: treasury-prime-statements-api
- description: The Transactions API from Treasury Prime — 2 operation(s) for transactions.
  name: Treasury Prime Transactions API
  slug: treasury-prime-transactions-api
- description: The Webhooks API from Treasury Prime — 2 operation(s) for webhooks.
  name: Treasury Prime Webhooks API
  slug: treasury-prime-webhooks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Treasury Prime Bank Accounts API
  slug: open-treasury-prime-accounts-api
- collection_type: open
  name: Treasury Prime Bank Accounts Businesses API
  slug: open-treasury-prime-businesses-api
- collection_type: open
  name: Treasury Prime Bank Accounts Cards API
  slug: open-treasury-prime-cards-api
- collection_type: open
  name: Treasury Prime Bank Accounts Health API
  slug: open-treasury-prime-health-api
- collection_type: open
  name: Treasury Prime Bank Accounts Payments API
  slug: open-treasury-prime-payments-api
- collection_type: open
  name: Treasury Prime Bank Accounts Persons API
  slug: open-treasury-prime-persons-api
- collection_type: open
  name: Treasury Prime Bank Accounts Statements API
  slug: open-treasury-prime-statements-api
- collection_type: open
  name: Treasury Prime Bank Accounts Transactions API
  slug: open-treasury-prime-transactions-api
- collection_type: open
  name: Treasury Prime Bank Accounts Webhooks API
  slug: open-treasury-prime-webhooks-api
- collection_type: open
  name: Treasury Prime Bank API
  slug: open-treasury-prime
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/treasury-prime-capability-edges.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.treasuryprime.com/products/roadmap
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.treasuryprime.com/developers
- group: operate
  title: ''
  type: StatusPage
  url: https://status.treasuryprime.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.treasuryprime.com/policy/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.treasuryprime.com/policy/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.treasuryprime.com/docs/getting-started
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/treasury-prime-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treasury-prime-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/treasury-prime-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/treasuryprime
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/treasuryprime
- group: company
  title: ''
  type: Website
  url: https://www.treasuryprime.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/treasury-prime-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/treasury-prime-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/treasury-prime-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.treasuryprime.com/blog
created: '2026-05-08'
description: Treasury Prime is an embedded banking platform connecting fintechs and enterprises to a network of partner banks. Provides REST APIs for persons, businesses, accounts, cards, payments (ACH, wire, book), transactions, statements, and webhooks.
finops:
- name: Treasury Prime Finops
  service_category: FinTech
  slug: treasury-prime-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/treasury-prime.png
layout: provider
modified: '2026-05-08'
name: Treasury Prime
nav: Providers
network: true
overview: 'Treasury Prime publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Businesses API, Cards API, and 6 more. Tagged areas include Fintech, Backend-as-a-Service, Banking, Payments, and Card Issuing.


  Treasury Prime''s developer surface includes getting-started guide, authentication, engineering blog, and 14 more developer resources.'
plans:
- name: Treasury Prime Plans Pricing
  plan_count: 2
  slug: treasury-prime-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Treasury Prime Rate Limits
  slug: treasury-prime-rate-limits
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 49.1
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/treasury-prime/refs/heads/main/screenshots/treasury-prime-2026-06-20T195641.png
security:
- kind: authentication
  name: Treasury Prime Authentication
  slug: treasury-prime-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Treasury Prime Domain Security
  slug: treasury-prime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: treasury-prime
tags:
- Fintech
- Backend-as-a-Service
- Banking
- Payments
- Card Issuing
- ACH
website: https://www.treasuryprime.com/
---
