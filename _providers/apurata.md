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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Financing configuration and limits
  name: Apurata config API
  slug: apurata-config-api
- description: Order lifecycle (create, read, confirm, cancel)
  name: Apurata orders API
  slug: apurata-orders-api
- description: Total and partial refunds
  name: Apurata refunds API
  slug: apurata-refunds-api
- description: Embeddable checkout widgets (HTML)
  name: Apurata widgets API
  slug: apurata-widgets-api
artifact_total: 10
asyncapis:
- description: Outbound webhook events Apurata delivers to a merchant-registered URL as an aCuotaz installment order moves through its lifecycle. Generated from the public webhook documentation at docs.apurata.com/P
  name: Apurata aCuotaz Order Webhooks
  slug: apurata-acuotaz-asyncapi
- description: ''
  name: Apurata Acuotaz Webhooks
  slug: apurata-acuotaz-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://apurata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apurata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apurata.com/POS/intro/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apurata.com/POS/rest_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apurata.com/POS/intro/
- group: operate
  title: ''
  type: Support
  url: https://apurata.com/blog/contacto/
- group: company
  title: ''
  type: Blog
  url: https://apurata.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apurata
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apurata.com/blog/terminos-y-condiciones/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apurata.com/blog/privacidad/
- group: start
  title: ''
  type: SignUp
  url: https://apurata.com/app/
- group: build
  title: ''
  type: Packages
  url: packages/apurata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apurata-packages.yml
- group: design
  title: ''
  type: Components
  url: components/apurata-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apurata-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/apurata-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apurata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apurata-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/apurata-acuotaz-pos-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/apurata-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apurata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apurata-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apurata-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apurata-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apurata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://apurata.com/.well-known/vdp.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apurata-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apurata-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/apurata-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apurata-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apurata-acuotaz-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/apurata-acuotaz-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Apurata (legal name Tecno Creditos S.A.C.) is a Peruvian financial-technology company, authorized by Peru's banking regulator (SBS), that provides fast fully online personal loans and the aCuotaz "buy now, pay later" installment-financing product for e-commerce merchants. Consumers borrow from S/100 to S/1,000 with funding in as little as 29 minutes, repaid across 1-8 installments. For merchants, aCuotaz adds installment checkout with 0% interest options, pays the merchant upfront, and integrates via a REST API, webhooks, and prebuilt payment-gateway plugins for WooCommerce, Magento 2, Shopify, VTEX, Salesforce, OpenCart, and PrestaShop. Apurata also operates aPagos and a Samsung Finance+ financing API.
image: https://apurata.com/app/logo512.png
layout: provider
mcp_servers:
- description: ''
  name: apurata-mcp.yml
  slug: apurata-mcpyml
modified: '2026-07-18'
name: Apurata
nav: Providers
network: true
overview: 'Apurata publishes 4 APIs on the [APIs.io](https://apis.io/) network, including config API, orders API, refunds API, and 1 more. Tagged areas include Company, Financial Services, Fintech, Lending, and Buy Now Pay Later.


  The Apurata catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Apurata''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 26 more developer resources.'
random_paper: 39
score:
  band: developing
  composite: 51.3
  delta: -3.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 69.7
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 55.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apurata/refs/heads/main/screenshots/apurata-2026-07-25T200944.png
security:
- kind: authentication
  name: Apurata Authentication
  slug: apurata-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Apurata Domain Security
  slug: apurata-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Apurata Vulnerability Disclosure
  slug: apurata-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apurata
tags:
- Company
- Financial Services
- Fintech
- Lending
- Buy Now Pay Later
- Installment Payments
- Consumer Credit
- Payments
- E-commerce
- Peru
- Latin America
website: https://apurata.com
---
