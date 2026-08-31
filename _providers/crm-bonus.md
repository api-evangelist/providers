---
access_model:
  confidence: medium
  label: Request Access
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://ajuda.otocrm.com.br/support/solutions/articles/150000031734-cadastro-r%C3%A1pido-via-api
  - https://data-api.otocrm.com.br/redoc
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Crm Bonus Agentic Access
  operation_count: 13
  slug: crm-bonus-agentic-access
  summary_line: 13 operations · 13 acting
api_count: 2
apis:
- description: The Auth API from CRM Bonus — 1 operation(s) for auth.
  name: CRM Bonus Auth API
  slug: crm-bonus-auth-api
- description: The Blocked API from CRM Bonus — 1 operation(s) for blocked.
  name: CRM Bonus Blocked API
  slug: crm-bonus-blocked-api
- description: The Cashback API from CRM Bonus — 1 operation(s) for cashback.
  name: CRM Bonus Cashback API
  slug: crm-bonus-cashback-api
- description: The Customers API from CRM Bonus — 1 operation(s) for customers.
  name: CRM Bonus Customers API
  slug: crm-bonus-customers-api
- description: The Nps API from CRM Bonus — 1 operation(s) for nps.
  name: CRM Bonus Nps API
  slug: crm-bonus-nps-api
- description: The Order Items API from CRM Bonus — 1 operation(s) for order items.
  name: CRM Bonus Order Items API
  slug: crm-bonus-order-items-api
- description: The Orders API from CRM Bonus — 1 operation(s) for orders.
  name: CRM Bonus Orders API
  slug: crm-bonus-orders-api
- description: The Products API from CRM Bonus — 1 operation(s) for products.
  name: CRM Bonus Products API
  slug: crm-bonus-products-api
- description: The Sellers API from CRM Bonus — 1 operation(s) for sellers.
  name: CRM Bonus Sellers API
  slug: crm-bonus-sellers-api
- description: The Stores API from CRM Bonus — 1 operation(s) for stores.
  name: CRM Bonus Stores API
  slug: crm-bonus-stores-api
- description: The Tag Hits API from CRM Bonus — 1 operation(s) for tag hits.
  name: CRM Bonus Tag Hits API
  slug: crm-bonus-tag-hits-api
- description: The Tag Ids API from CRM Bonus — 1 operation(s) for tag ids.
  name: CRM Bonus Tag Ids API
  slug: crm-bonus-tag-ids-api
- description: The Tag Interactions API from CRM Bonus — 1 operation(s) for tag interactions.
  name: CRM Bonus Tag Interactions API
  slug: crm-bonus-tag-interactions-api
artifact_total: 20
collections:
- collection_type: open
  name: Oto Data API
  slug: open-crm-bonus-oto-data-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/crm-bonus-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crm-bonus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crm-bonus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crmbonus.com.br
- group: operate
  title: ''
  type: Support
  url: https://crmbonus.com.br/suporte
- group: operate
  title: ''
  type: HelpCenter
  url: https://ajuda.otocrm.com.br/support/solutions
- group: company
  title: ''
  type: Blog
  url: https://crmbonus.com.br/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crmbonus.com.br/politicas/politica-de-privacidade
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crmbonus.com.br/politicas/aviso-de-privacidade-e-termos-de-uso
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crmbonus-oficial
- group: operate
  title: ''
  type: StatusPage
  url: https://status.otocrm.com.br
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crm-bonus-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/crm-bonus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crm-bonus-packages.yml
- group: design
  title: ''
  type: Components
  url: components/crm-bonus-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crm-bonus-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crm-bonus-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crm-bonus-plans-pricing.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ajuda.otocrm.com.br/support/solutions/articles/150000032248-ingest%C3%A3o-de-dados-via-api
- group: docs
  title: ''
  type: APIReference
  url: https://data-api.otocrm.com.br/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://ajuda.otocrm.com.br/support/solutions/articles/150000031734-cadastro-r%C3%A1pido-via-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/crm-bonus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crm-bonus-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/crm-bonus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crm-bonus-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crm-bonus-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crm-bonus-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crm-bonus-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/crm-bonus-oto-data-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crm-bonus-mcp.yml
created: '2026-07-17'
description: CRM Bonus (CRMBonus) is a Brazilian retail technology platform for customer acquisition, conversion, and loyalty. Its products include Giftback cashback and rewards, the Vale Bonus consumer rewards app connecting brands to over five million shoppers, CRMBack WhatsApp-based e-commerce conversion, CRMAds retail media on WhatsApp, and Oto CRM — the physical-retail CRM platform CRMBonus acquired outright from WPP in June 2025 and now lists as a first-party retail solution. It integrates with 300+ ERP, point-of-sale, and e-commerce systems including VTEX, Shopify, Linx, TOTVS, Nuvemshop, Wake, and PagSeguro. The publicly documented machine-readable contract is the Oto Data API — an OpenAPI 3.1.0 upsert-ingestion API for customers, orders, order items, products, stores, sellers, cashback, NPS, and Oto Tags events — served at data-api.otocrm.com.br with a public ReDoc/Swagger reference. The Giftback and Vale Bonus APIs on api.crmbonus.com are partner-token gated with no public reference;
  that host answers HTTP 200 with an "OK!!" envelope for every path, including every /.well-known/* probe, so none of those 200s carry a real document.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crm-bonus.png
layout: provider
mcp_servers:
- description: ''
  name: CRM Bonus MCP Server
  slug: crm-bonus-mcp-server
modified: '2026-08-12'
name: CRM Bonus
nav: Providers
network: true
overview: 'CRM Bonus publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Blocked API, Cashback API, and 10 more. Tagged areas include Company, Retail, Loyalty, Cashback, and CRM.


  CRM Bonus'' developer surface includes support, engineering blog, documentation, API reference, getting-started guide, authentication, sandbox, and 24 more developer resources.'
plans:
- name: Crm Bonus Plans Pricing
  plan_count: 0
  slug: crm-bonus-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Crm Bonus Rate Limits
  slug: crm-bonus-rate-limits
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 54.1
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crm-bonus/refs/heads/main/screenshots/crm-bonus-2026-07-25T210737.png
security:
- kind: authentication
  name: Crm Bonus Authentication
  slug: crm-bonus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crm Bonus Domain Security
  slug: crm-bonus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crm-bonus
tags:
- Company
- Retail
- Loyalty
- Cashback
- CRM
- Retail Media
- E-Commerce
- Brazil
- WhatsApp
- Customer Data
- Data Ingestion
- Point-of-Sale
website: https://crmbonus.com.br
---
