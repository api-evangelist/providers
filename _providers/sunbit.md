---
agent_readiness:
  band: agent-aware
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Server-to-server REST API for Sunbit partners and SaaS platforms. Covers pre-qualification links, "As Low As" payment estimation, Text to Pay-Over-Time SMS links, checkout transaction initialization a
  name: Sunbit Partner API
  slug: sunbit-partner-api
- description: 'Hosted, asynchronously loaded browser SDK (the SUNBIT global) that renders Sunbit''s client-side surfaces: the "As Low As" estimate text element and disclaimer, the check-financing-options link, the Ch'
  name: Sunbit JavaScript SDK
  slug: sunbit-javascript-sdk
artifact_total: 6
asyncapis:
- description: ''
  name: Sunbit Webhooks
  slug: sunbit-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sunbit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.sunbit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sunbit.com/docs/overview/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sunbit.com/docs/api-integrations/sunbit-pre-qualification
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sunbit.com/docs/overview/getting-started
- group: company
  title: ''
  type: Blog
  url: https://sunbit.com/knowledge-center/
- group: operate
  title: ''
  type: Support
  url: https://sunbit.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://sunbit.com/im-a-merchant/become-a-partner/
- group: commercial
  title: ''
  type: Pricing
  url: https://sunbit.com/rates_and_terms/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sunbit.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sunbit.com/consumer_privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sunbit.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sunbit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sunbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sunbit-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sunbit-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sunbit-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/sunbit-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/sunbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sunbit-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sunbit-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sunbit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sunbit-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sunbit-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sunbit-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sunbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://sunbit.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunbit-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sunbit-llms.txt
created: '2026-07-31'
description: 'Sunbit is a Los Angeles based financial technology company that builds point-of-sale buy now, pay-over-time financing for everyday needs — auto service and dealerships, dental, eyewear, veterinary, med spa, home services, and general retail. Merchants and SaaS platforms integrate Sunbit through a partner API and a hosted JavaScript SDK covering four products: Pre-Qualification (send a customer a no-hard-credit-check qualification link), Sunbit Estimate (an "As Low As" monthly payment shown on a price, estimate or invoice), Checkout (Sunbit added as a payment method via a tokenized server-to-server flow and a modal), and Text to Pay-Over-Time (an SMS payment link). The platform also exposes merchant onboarding, transaction lookup, void and partial refund, reporting, and HMAC-SHA256 signed webhooks. Loans are originated through regulated bank partners.'
image: https://sunbit.com/wp-content/uploads/2021/06/sunbit-logo.png
layout: provider
modified: '2026-07-31'
name: Sunbit
nav: Providers
network: true
overview: 'Sunbit publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Buy Now Pay Later, Point of Sale Financing, Consumer Lending, Payments, and Fintech.


  The Sunbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sunbit''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 23 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 46.6
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sunbit/refs/heads/main/screenshots/sunbit-2026-08-17T082155.png
security:
- kind: authentication
  name: Sunbit Authentication
  slug: sunbit-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Sunbit Domain Security
  slug: sunbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sunbit Vulnerability Disclosure
  slug: sunbit-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: sunbit
tags:
- Buy Now Pay Later
- Point of Sale Financing
- Consumer Lending
- Payments
- Fintech
- Checkout
- Merchant Onboarding
- Webhook
- Automotive
- Dental
- Veterinary
- Eyewear
- healthcare-financing
- Embedded Finance
website: https://sunbit.com/
---
