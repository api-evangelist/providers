---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Paystone Agentic Access
  operation_count: 38
  slug: paystone-agentic-access
  summary_line: 38 operations · 11 acting
api_count: 1
apis:
- description: The public, documented REST API for Paystone's DataCandy gift-card and loyalty platform, built on API Platform (Hydra/JSON-LD) and served from api.paystone.com. It exposes 28 documented paths across 1
  name: Paystone DataCandy API
  slug: paystone-datacandy-api
artifact_total: 6
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
  name: paystone-mcp.yml
  slug: paystone-mcpyml
modified: '2026-07-24'
name: Paystone
nav: Providers
network: true
overview: 'Paystone publishes 1 API on the [APIs.io](https://apis.io/) network: DataCandy API. Tagged areas include Payments, Canada, Payment Processing, Acquiring, and Gift Cards.


  The Paystone catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paystone''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 138
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.9
    developer_ergonomics: 45.1
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 46.4
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
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
- Subscriptions
- Billing
- Merchant Services
website: https://www.paystone.com/
---
