---
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Paystone Agentic Access
  operation_count: 38
  slug: paystone-agentic-access
  summary_line: 38 operations · 11 acting
api_count: 1
apis:
- description: The Balance Portal API from Paystone — 1 operation(s) for balance portal.
  name: Paystone Balance Portal API
  slug: paystone-balance-portal-api
- description: The Client Management API from Paystone — 3 operation(s) for client management.
  name: Paystone Client Management API
  slug: paystone-client-management-api
- description: Resource 'Contact' operations.
  name: Paystone Contact API
  slug: paystone-contact-api
- description: The Gift Account Type API from Paystone — 2 operation(s) for gift account type.
  name: Paystone Gift Account Type API
  slug: paystone-gift-account-type-api
- description: Resource 'Item' operations.
  name: Paystone Item API
  slug: paystone-item-api
- description: The Loyalty Account Type API from Paystone — 2 operation(s) for loyalty account type.
  name: Paystone Loyalty Account Type API
  slug: paystone-loyalty-account-type-api
- description: The Loyalty Transaction API from Paystone — 2 operation(s) for loyalty transaction.
  name: Paystone Loyalty Transaction API
  slug: paystone-loyalty-transaction-api
- description: The Member Portal API from Paystone — 1 operation(s) for member portal.
  name: Paystone Member Portal API
  slug: paystone-member-portal-api
- description: The Merchant Management API from Paystone — 5 operation(s) for merchant management.
  name: Paystone Merchant Management API
  slug: paystone-merchant-management-api
- description: The Prepaid Transaction API from Paystone — 2 operation(s) for prepaid transaction.
  name: Paystone Prepaid Transaction API
  slug: paystone-prepaid-transaction-api
- description: The Promo Account Type API from Paystone — 2 operation(s) for promo account type.
  name: Paystone Promo Account Type API
  slug: paystone-promo-account-type-api
- description: Resource 'Reward' operations.
  name: Paystone Reward API
  slug: paystone-reward-api
- description: The User Management API from Paystone — 2 operation(s) for user management.
  name: Paystone User Management API
  slug: paystone-user-management-api
- description: The Webhook Management API from Paystone — 2 operation(s) for webhook management.
  name: Paystone Webhook Management API
  slug: paystone-webhook-management-api
artifact_total: 19
asyncapis:
- description: ''
  name: Paystone Datacandy Webhooks
  slug: paystone-datacandy-webhooks
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/paystone-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paystone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paystone-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paystone-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paystone-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paystone-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paystone-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paystone-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paystone-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paystone-datacandy-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paystone-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/paystone-datacandy-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.paystone.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.paystone.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.paystone.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.paystone.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paystone.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.paystone.com/resources
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.paystone.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paystone.com
- group: start
  title: ''
  type: Login
  url: https://hub.paystone.com/login
- group: start
  title: ''
  type: SignUp
  url: https://start.paystone.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paystone.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paystone.com/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paystone
created: '2026-07-24'
description: 'Paystone is a Canadian payment processing and customer-engagement company headquartered in London, Ontario, positioning itself as one of the country''s largest bank-independent payment processors. It sells card-present terminals, online checkout and hosted payment pages, virtual terminals, invoicing, and recurring billing to Canadian small and mid-sized businesses, and layers loyalty, gift-card, and reputation-marketing products on top of the payment rails. Paystone owns DataCandy, a long-standing Canadian gift-card and loyalty platform, and it is DataCandy that carries Paystone''s public, self-serve, documented API surface: a live API Platform (Hydra/JSON-LD) REST API at api.paystone.com covering merchants, clients, contacts, gift/loyalty/ prepaid/promo account types, transactions, member and balance portals, and webhooks, authenticated with JWT bearer tokens and documented through an interactive Swagger UI. Paystone''s core card-acquiring and payment-gateway processing is
  delivered as a merchant product rather than a publicly self-serve developer API, so the honest developer story here is the DataCandy gift-and-loyalty platform API, not a public payments/acquiring API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Paystone MCP Server
  slug: paystone-mcp-server
modified: '2026-07-24'
name: Paystone
nav: Providers
network: true
overview: 'Paystone publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Balance Portal API, Client Management API, Contact API, and 11 more. Tagged areas include Payments, Canada, Payment Processing, Acquiring, and Gift Cards.


  The Paystone catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paystone''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 63.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
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
    score: 39.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paystone/refs/heads/main/screenshots/paystone-2026-08-07T191657.png
security:
- kind: authentication
  name: Paystone Authentication
  slug: paystone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paystone Domain Security
  slug: paystone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paystone
tags:
- Payments
- Canada
- Payment Processing
- Acquiring
- Gift Cards
- Loyalty
- Subscription
- Billing
- Merchant Services
website: https://www.paystone.com/
---
