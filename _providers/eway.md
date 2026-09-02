---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The eWAY Rapid API is a versioned HTTP payments API (v47) for processing card transactions. It exposes transaction creation (Direct Connection), AccessCode-based flows (Transparent Redirect / Responsi
  name: eWAY Rapid API
  slug: eway-rapid-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eway.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eway.io/api-v3/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eway.com.au/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://eway.io/api-v3/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eWAYPayment
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eway.com.au/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eway.com.au/plans-pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.eway.com.au/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.eway.com.au/support/
- group: start
  title: ''
  type: SignUp
  url: https://www.eway.com.au/sign-up/
- group: start
  title: ''
  type: Login
  url: https://au.myeway.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eway.com.au/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eway.com.au/legals/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.eway.com.au/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.eway.com.au/advanced-cybersecurity/pci-dss/
- group: build
  title: ''
  type: Packages
  url: packages/eway-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eway-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eway-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eway-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eway-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eway-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/eway-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eway-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/eway-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eway-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/eway-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eway-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eway-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eway-llms.txt
created: '2026-07-24'
description: eWAY (Eway) is an Australian online payment gateway founded in Sydney in 1998 and now part of Global Payments Oceania, providing card-not-present payment acceptance for e-commerce merchants across Australia, New Zealand, and Asia. Its flagship developer surface is the Rapid API, a versioned HTTP payments API (currently version 47) that processes purchases, pre-authorisations, MOTO and recurring transactions, and tokenised (stored-card) payments, offered through seven integration methods ranging from server-to-server Direct Connection to PCI-scope-reducing Transparent Redirect, Secure Fields, and the Responsive Shared Page. Merchants authenticate with an API key and password over HTTP Basic auth, and eWAY publishes open-source MIT-licensed SDKs for PHP, Java, .NET, Node.js, Ruby, Android, and iOS plus a free sandbox. The Rapid API is genuinely API-first and well documented, but eWAY does not publish a downloadable OpenAPI/Swagger definition, and no public OAuth, webhooks catalog,
  or AsyncAPI event stream is documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: eWAY
nav: Providers
network: true
overview: 'eWAY publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Card Payments.


  eWAY''s developer surface includes documentation, API reference, pricing, engineering blog, support, signup flow, authentication, and 23 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 43.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eway/refs/heads/main/screenshots/eway-2026-07-25T213830.png
security:
- kind: authentication
  name: Eway Authentication
  slug: eway-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Eway Domain Security
  slug: eway-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: eway
tags:
- Payments
- Australia
- Payment Gateway
- Payment Processing
- Card Payments
- Tokenization
- E-Commerce
- Recurring Payments
- Subscription
website: https://www.eway.com.au/
---
