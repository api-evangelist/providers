---
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cloudwalk Agentic Access
  operation_count: 2
  slug: cloudwalk-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: 'The InfinitePay Integrated Checkout ("Checkout Integrado") API. Two public JSON operations — create a hosted checkout payment link for a basket of items, and check the payment status of a link — plus '
  name: InfinitePay Checkout API
  slug: infinitepay-checkout-api
artifact_total: 6
asyncapis:
- description: ''
  name: Cloudwalk Infinitepay Webhooks
  slug: cloudwalk-infinitepay-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudwalk-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudwalk.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.infinitepay.io/desenvolvedores
- group: docs
  title: ''
  type: Documentation
  url: https://www.infinitepay.io/checkout-documentacao
- group: docs
  title: ''
  type: APIReference
  url: https://www.infinitepay.io/checkout-documentacao
- group: start
  title: ''
  type: GettingStarted
  url: https://www.infinitepay.io/checkout
- group: operate
  title: ''
  type: Support
  url: https://ajuda.infinitepay.io/pt-BR/
- group: company
  title: ''
  type: Blog
  url: https://www.infinitepay.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudwalk
- group: commercial
  title: ''
  type: Pricing
  url: https://www.infinitepay.io/taxas
- group: start
  title: ''
  type: SignUp
  url: https://app.infinitepay.io
- group: start
  title: ''
  type: Login
  url: https://app.infinitepay.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infinitepay.io/legal/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infinitepay.io/legal/aviso-de-privacidade
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infinitepay.io/
- group: auth
  title: ''
  type: Security
  url: https://www.infinitepay.io/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.infinitepay.io/legal/politica-de-seguranca-cibernetica
- group: company
  title: ''
  type: Newsroom
  url: https://www.cloudwalk.io/newsroom
- group: build
  title: ''
  type: Packages
  url: packages/cloudwalk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudwalk-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudwalk-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudwalk-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudwalk-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudwalk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudwalk-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudwalk-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudwalk-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudwalk-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudwalk-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/cloudwalk-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudwalk-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cloudwalk-infinitepay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: 'CloudWalk, Inc. is a Sunnyvale- and São Paulo-based payments and financial-infrastructure company that builds an AI-native transaction layer for small businesses. It operates three consumer-facing brands: InfinitePay, its Brazilian acquirer and digital-banking platform (card machines, Tap to Pay, hosted checkout, payment links, Pix, PJ accounts, credit and CDB); JIM, a phone-as-POS operating system for self-employed workers in the United States; and Pierre, a personal-finance intelligence product built on Brazilian Open Finance. Its public developer surface is deliberately small and integration-shaped rather than platform-shaped: an Integrated Checkout REST API on api.checkout.infinitepay.io that creates hosted payment links and checks their status, an approved-payment webhook, and an InfiniteTap deeplink contract that hands a Tap-to-Pay transaction from a third-party POS app to the InfinitePay mobile app and back. CloudWalk publishes no OpenAPI, no machine-readable discovery
  documents and no MCP or agent surface. The legal entity behind InfinitePay is CLOUDWALK INSTITUIÇÃO DE PAGAMENTO E SERVIÇOS LTDA (CNPJ 18.189.547/0001-42), a Brazilian payment institution supervised by the Banco Central do Brasil.'
image: https://cdn.prod.website-files.com/6654b3697a9d140e0ca14dcc/6a0bb9e1bb37dcd08e538cc1_Cover-Profile%2044.webp
layout: provider
modified: '2026-08-01'
name: CloudWalk
nav: Providers
network: true
overview: 'CloudWalk publishes 1 API on the [APIs.io](https://apis.io/) network: InfinitePay Checkout API. Tagged areas include Company, Payments, Financial Services, Fintech, and Checkout.


  The CloudWalk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CloudWalk''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 16
score:
  band: strong
  composite: 56.2
  facets:
    commercial_clarity: 52.6
    contract_quality: 73.6
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 39.5
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Cloudwalk Authentication
  slug: cloudwalk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cloudwalk Domain Security
  slug: cloudwalk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudwalk Vulnerability Disclosure
  slug: cloudwalk-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cloudwalk
tags:
- Company
- Payments
- Financial Services
- Fintech
- Checkout
- Point of Sale
- Acquiring
- Pix
- Brazil
- Banking
- Webhooks
- Tap to Pay
website: https://www.cloudwalk.io/
---
