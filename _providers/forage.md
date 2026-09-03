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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API to tokenize EBT cards, run PIN-secured balance inquiries, and create, capture, void, and refund EBT SNAP, EBT Cash, and HSA/FSA payments and orders for online and in-store checkout.
  name: Forage EBT SNAP Payments API
  slug: forage-ebt-snap-payments-api
artifact_total: 6
asyncapis:
- description: ''
  name: Forage Webhooks
  slug: forage-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joinforage.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.joinforage.app/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinforage.app/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinforage.app/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinforage.app/docs/setup
- group: operate
  title: ''
  type: Support
  url: https://www.joinforage.com/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://www.joinforage.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamforage
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joinforage.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.joinforage.com/get-in-touch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinforage.com/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinforage.com/pages/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinforage.app
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/forage-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/forage-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forage-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forage-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/forage-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/forage-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.joinforage.app/reference/request-limits
- group: agent
  title: ''
  type: MCPServer
  url: mcp/forage-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forage-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/forage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/forage-packages.yml
- group: design
  title: ''
  type: Components
  url: components/forage-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/forage-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/forage-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/forage-decline-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/forage-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/forage-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.joinforage.app/
- group: auth
  title: ''
  type: TrustCenter
  url: security/forage-trust-center.yml
created: '2026-07-17'
description: Forage is a mission-driven payments company and one of only three payment processors approved by the USDA Food and Nutrition Service (FNS) to accept SNAP EBT and EBT Cash online. Forage gives grocery retailers, marketplaces, and platforms the API, SDKs, and regulatory expertise to add government-benefit tender (SNAP, EBT Cash, and HSA/FSA) to online and in-store checkout. The Forage Payments API tokenizes EBT cards, runs PIN-secured balance inquiries, and creates, captures, voids, and refunds EBT payments and orders, backed by JavaScript, iOS, Android, and POS Terminal SDKs, webhooks for order/payment/refund events, and daily CSV reconciliation reports.
image: https://framerusercontent.com/assets/ZoPlyiuvY1BwAuHbWMWp7HW8UmE.png
layout: provider
mcp_servers:
- description: Official Forage documentation MCP server. Exposes the Forage Payments API surface to AI tools and can execute live API calls against the real Forage API with OAuth credentials.
  name: Forage docs MCP server
  slug: forage-docs-mcp-server
modified: '2026-07-19'
name: Forage
nav: Providers
network: true
overview: 'Forage publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, EBT, SNAP, and EBT Cash.


  The Forage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Forage''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 49.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forage/refs/heads/main/screenshots/forage-2026-07-25T214925.png
security:
- kind: authentication
  name: Forage Authentication
  slug: forage-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Forage Domain Security
  slug: forage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Forage Trust Center
  slug: forage-trust-center
  summary_line: trust center published
slug: forage
tags:
- Company
- Payments
- EBT
- SNAP
- EBT Cash
- HSA/FSA
- Fintech
- Government Benefits
- Grocery
- Checkout
- Financial-Services
website: https://www.joinforage.com
---
