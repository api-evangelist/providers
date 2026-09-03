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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: Next-generation Bread Pay REST API for managing buyers, merchant accounts, personalized payment options and pricing, and the merchant transaction lifecycle (authorize, capture, cancel, refund). Secure
  name: BreadPay Platform API
  slug: breadpay-platform-api
- description: The Bread Pay API enables merchants to integrate installment financing options into online and in-store checkout flows. Supports creating financing applications, retrieving loan statuses, managing tra
  name: Bread Pay API
  slug: bread-pay-api
- description: SplitPay is a short-term financing alternative for retail merchants, enabling customers to split purchases into manageable payments and helping retailers attract price-sensitive customers while increa
  name: Bread SplitPay API
  slug: split-pay-api
artifact_total: 6
asyncapis:
- description: ''
  name: Bread Financial Webhooks
  slug: bread-financial-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.breadfinancial.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform-docs.breadpayments.com/bread-developers/docs
- group: docs
  title: ''
  type: Documentation
  url: https://platform-docs.breadpayments.com/bread-developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://platform-docs.breadpayments.com/bread-developers/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://platform-docs.breadpayments.com/bread-developers/docs/api-access
- group: operate
  title: ''
  type: Support
  url: https://platform-docs.breadpayments.com/bread-onboarding/docs/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bppub
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breadfinancial.com/en/privacy-policy.html
- group: build
  title: ''
  type: Packages
  url: packages/bread-financial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bread-financial-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bread-financial-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bread-financial-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bread-financial-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bread-financial-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bread-financial-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bread-financial-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/bread-financial-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bread-financial-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bread-financial-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bread-financial-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bread-financial-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getbread
- group: docs
  title: ''
  type: Documentation
  url: https://developers.breadfinancial.com/
created: '2026-07-17'
description: 'Bread Financial (formerly Alliance Data Systems) is a US consumer financial services company providing branded and co-brand credit cards, private-label and general-purpose lending, and point-of-sale buy-now-pay-later financing under the Bread Pay brand. Its developer surface, Bread Pay, exposes a REST API platform for merchants to embed installment and revolving financing into online and in-store checkout: the next-generation BreadPay Platform API (api.platform.breadpayments.com) manages buyers, merchant accounts, payment options, pricing, and the transaction lifecycle (authorize, capture, cancel, refund), secured with OAuth 2.0 client-credentials and JWT access tokens; a legacy Bread Classic Merchant API manages checkout carts and transactions; and browser (JavaScript) plus native iOS and Android SDKs render placements, prequalification (RTPS), and the Bread checkout modal on merchant storefronts. Bread also ships e-commerce platform plugins (Shopify, Magento 2, BigCommerce,
  WooCommerce, Miva, Volusion, Salesforce Commerce Cloud) and a partner sandbox. This profile was surfaced as a portfolio company of Bessemer Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bread-financial.png
layout: provider
modified: '2026-07-18'
name: Bread Financial
nav: Providers
network: true
overview: 'Bread Financial publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Buy Now Pay Later, and Lending.


  The Bread Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bread Financial''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 30.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bread-financial/refs/heads/main/screenshots/bread-financial-2026-07-25T203733.png
security:
- kind: authentication
  name: Bread Financial Authentication
  slug: bread-financial-authentication
  summary_line: oauth2/http/apiKey · 3 schemes
- kind: domain-security
  name: Bread Financial Domain Security
  slug: bread-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bread-financial
tags:
- Company
- Fintech
- Payments
- Buy Now Pay Later
- Lending
- Consumer Finance
- Point-of-Sale
- E-Commerce
website: https://www.breadfinancial.com
---
