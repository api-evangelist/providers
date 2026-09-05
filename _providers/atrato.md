---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Atrato Agentic Access
  operation_count: 13
  slug: atrato-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api-sandbox.atratopago.com
  baseurl_source: declared
  description: The Ecommerce API from Atrato — 7 operation(s) for ecommerce.
  name: Atrato Ecommerce API
  slug: atrato-ecommerce-api
- baseURL: https://api-sandbox.atratopago.com
  baseurl_source: declared
  description: The Integration API from Atrato — 6 operation(s) for integration.
  name: Atrato Integration API
  slug: atrato-integration-api
artifact_total: 9
asyncapis:
- description: ''
  name: Atrato Webhooks
  slug: atrato-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Atrato Partners Ecommerce API
  slug: open-atrato-ecommerce-api
- collection_type: open
  name: Atrato Partners Ecommerce Integration API
  slug: open-atrato-integration-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.atratopago.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.atratopago.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atratopago.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atratopago.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atratopago.com/reference/recepción-de-pagos
- group: auth
  title: ''
  type: Authentication
  url: authentication/atrato-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/atrato-partners-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/atrato-partners-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atrato-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atrato-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atrato-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atrato-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atrato-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/atrato-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/atrato-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atrato-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/atrato-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/atrato-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/atrato-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/atrato-cash-in-register-payment.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/atrato-ecommerce-generate-order.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atrato-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.atratopago.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.atratopago.com/soporte-y-ayuda
- group: start
  title: ''
  type: SignUp
  url: https://app.atratopago.com/v3/accounts/register?LP=true
- group: start
  title: ''
  type: Login
  url: https://app.atratopago.com/v3/accounts/getStarted
- group: commercial
  title: ''
  type: TermsOfService
  url: https://s3.us-west-2.amazonaws.com/cdn.atratopago.com/Términos+y+Condiciones.+Atrato+Technologies..+2025.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://s3.us-west-2.amazonaws.com/cdn.atratopago.com/Aviso+de+Privacidad+Atrato+Technologies.+2026.pdf
created: '2026-07-17'
description: Atrato (Atrato Technologies S.A.P.I. de C.V., atratopago.com) is a Mexican fintech offering buy-now-pay-later (BNPL) point-of-sale financing. Affiliated merchants let shoppers split purchases of up to $200,000 MXN into installments of up to 24 months, without a credit or debit card, with approval in minutes. Atrato serves furniture, healthcare, mobility, construction, motorcycle, appliance and other verticals, and is regulated by PROFECO. Its Atrato Partners platform exposes a REST integration API (api-partners) covering in-store cash-in payment collection and ecommerce checkout order generation, plus status/disbursement webhooks and WooCommerce, Shopify and Magento plugins. This profile was enriched from Atrato's public developer documentation at docs.atratopago.com.
image: https://www.atratopago.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Atrato
nav: Providers
network: true
overview: 'Atrato publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ecommerce API and Integration API. Tagged areas include Company, Fintech, Payments, Buy Now Pay Later, and Lending.


  The Atrato catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Atrato''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 21 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 58.2
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atrato/refs/heads/main/screenshots/atrato-2026-07-25T201622.png
security:
- kind: authentication
  name: Atrato Authentication
  slug: atrato-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Atrato Domain Security
  slug: atrato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atrato
tags:
- Company
- Fintech
- Payments
- Buy Now Pay Later
- Lending
- Mexico
- Point-of-Sale
- E-Commerce
website: https://www.atratopago.com/
---
