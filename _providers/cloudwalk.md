---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
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
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cloudwalk Agentic Access
  operation_count: 2
  slug: cloudwalk-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.checkout.infinitepay.io
  baseurl_source: declared
  description: Create InfinitePay-hosted checkout payment links.
  name: CloudWalk Checkout Links API
  slug: cloudwalk-checkout-links-api
- baseURL: https://api.checkout.infinitepay.io
  baseurl_source: declared
  description: The InfinitePay Checkout API API from CloudWalk — 0 operation(s) for infinitepay checkout api.
  name: CloudWalk InfinitePay Checkout API
  slug: cloudwalk-infinitepay-checkout-api-api
- baseURL: https://api.checkout.infinitepay.io
  baseurl_source: declared
  description: Query the payment status of a checkout link.
  name: CloudWalk Payments API
  slug: cloudwalk-payments-api
artifact_total: 9
asyncapis:
- description: ''
  name: Cloudwalk Infinitepay Webhooks
  slug: cloudwalk-infinitepay-webhooks
collections:
- collection_type: open
  name: InfinitePay Checkout API
  slug: open-cloudwalk-infinitepay-checkout
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cloudwalk-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cloudwalk-infinitepay-checkout-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cloudwalk-mcp.yml
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
overview: 'CloudWalk publishes 3 APIs on the [APIs.io](https://apis.io/) network: Checkout Links API, InfinitePay Checkout API, and Payments API. Tagged areas include Company, Payments, Financial-Services, Fintech, and Checkout.


  The CloudWalk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CloudWalk''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudwalk/refs/heads/main/screenshots/cloudwalk-2026-08-07T163513.png
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
- Financial-Services
- Fintech
- Checkout
- Point-of-Sale
- Acquiring
- Pix
- Brazil
- Banking
- Webhook
- Tap to Pay
website: https://www.cloudwalk.io/
---
