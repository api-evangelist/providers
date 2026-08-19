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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Klump REST API lets a merchant verify transactions, sync commerce product catalogs, create Klump Access hosted payment pages, and resend webhooks. A single base URL serves both sandbox and product
  name: Klump API
  slug: klump-api
artifact_total: 5
asyncapis:
- description: ''
  name: Klump Webhooks
  slug: klump-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://useklump.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://useklump.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useklump.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useklump.com/docs/api-keys-authorization
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useklump.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://useklump.com/contact
- group: company
  title: ''
  type: Blog
  url: https://useklump.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Klump-Inc
- group: commercial
  title: ''
  type: Pricing
  url: https://useklump.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://merchant.useklump.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://merchant.useklump.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useklump.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useklump.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: conformance/klump-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klump-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/klump-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/klump-packages.yml
- group: design
  title: ''
  type: Components
  url: components/klump-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klump-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/klump-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klump-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klump-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/klump-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/klump-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klump-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klump-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klump-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/klump-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klump-llms.txt
created: '2026-07-17'
description: Klump Technology Company Ltd is a Lagos, Nigeria based fintech whose flagship product, Klump BNPL (Buy Now, Pay Later), lets shoppers spread the cost of a purchase over monthly instalments at online and in-store merchant checkouts. Merchants integrate Klump either through the Klump.js client-side checkout widget, a framework component (React, Vue 2, Vue 3, Angular, React Native, Flutter), an e-commerce plugin (WooCommerce/WordPress, Magento 2, PrestaShop, OpenCart, WHMCS), a Laravel package, or directly against the Klump REST API at https://api.useklump.com. The API is secret-key authenticated via a klump-secret-key header, uses one base URL for both sandbox and production (the key and the merchant application state, TEST or LIVE, select the environment), and covers transaction verification, Klump Commerce product sync, Klump Access hosted payment pages, and webhook resend. Klump emits transaction lifecycle webhooks (initiated, successful, abandoned) signed with an X-Klump-Signature
  HMAC header and retried hourly for 72 hours. Klump is backed by Seedcamp and displays a PCI DSS Compliant badge.
image: https://useklump.com/images/meta.png
layout: provider
mcp_servers:
- description: ''
  name: klump-mcp.yml
  slug: klump-mcpyml
modified: '2026-07-19'
name: Klump
nav: Providers
network: true
overview: 'Klump publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Buy Now Pay Later, BNPL, and Fintech.


  The Klump catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Klump''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 106
score:
  band: developing
  composite: 51.2
  delta: 3.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 47.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klump/refs/heads/main/screenshots/klump-2026-07-25T223950.png
security:
- kind: authentication
  name: Klump Authentication
  slug: klump-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Klump Domain Security
  slug: klump-domain-security
  summary_line: TLSv1.3 · DMARC
slug: klump
tags:
- Company
- Payments
- Buy Now Pay Later
- BNPL
- Fintech
- Lending
- Checkout
- E-Commerce
- Nigeria
- Africa
- Instalments
- Consumer Credit
website: https://useklump.com
---
