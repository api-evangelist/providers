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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: Generate, cancel, and retrieve GST e-invoices (IRN) and e-waybills, including government IRP/NIC-compatible endpoints, DSC PDF signing, and bulk operations.
  name: Clear E-Invoicing & E-Waybill API
  slug: clear-e-invoicing-e-waybill-api
- description: ASP/GSP GST filing API for uploading documents and filing G1-G9 returns via Clear's GST Suvidha Provider integration.
  name: Clear GST 2.0 API
  slug: clear-gst-20-api
- description: Document ingestion APIs for sale and purchase documents via file upload (pre-signed URL) with access-token authentication and ingestion-status tracking.
  name: Clear Finance Cloud (CFC) API
  slug: clear-finance-cloud-cfc-api
- description: 'Input Tax Credit (ITC) reconciliation API: upload purchase documents, trigger the Max ITC workflow, and fetch reconciliation results.'
  name: Clear Max ITC API
  slug: clear-max-itc-api
- description: Create sale and non-sale documents, download document PDFs, and retrieve document details for invoicing workflows.
  name: Clear Invoicing API
  slug: clear-invoicing-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cleartax-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/cleartax-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleartax-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cleartax.in/cleartax-docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cleartax.in/cleartax-docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cleartax.in/cleartax-docs/e-invoicing-api/e-invoicing-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cleartax.in/cleartax-docs/max-itc-api/getting-started-with-max-itc-api
- group: operate
  title: ''
  type: Support
  url: https://www.clear.in/s/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClearTax
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clear.in/s/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.clear.in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clear.in/meta/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clear.in/meta/privacy
- group: build
  title: ''
  type: Postman
  url: https://docs.cleartax.in/cleartax-docs/max-itc-api/max-itc-api-reference/max-itc-apis/postman-collection
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cleartax-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cleartax-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cleartax-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cleartax-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cleartax-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cleartax-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cleartax-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cleartax-error-codes.yml
created: '2026-07-17'
description: Cleartax (operating as Clear, clear.in) is an Indian fintech and financial-compliance automation platform that provides tax, GST, and e-invoicing software for individuals, tax professionals, and over 4,000 enterprises. Clear exposes a suite of developer APIs through its documentation portal at docs.cleartax.in, including the Clear Finance Cloud (CFC) ingestion APIs, the GST 2.0 / GSP filing API, the Max ITC input-tax-credit reconciliation API, the GLS API, the E-Invoicing and E-Waybill APIs (with government IRP/NIC-compatible endpoints and DSC signing), the Invoicing API, and KSA (Saudi Arabia) e-invoicing APIs. APIs authenticate with a client secret exchanged for an access token and run against production (api.clear.in) and sandbox (api-sandbox.clear.in) hosts.
image: https://github.com/ClearTax.png
layout: provider
modified: '2026-07-18'
name: Cleartax
nav: Providers
network: true
overview: 'Cleartax publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, GST, E-Invoicing, and Compliance.


  Cleartax''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 15 more developer resources.'
random_paper: 61
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 34.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 48.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cleartax/refs/heads/main/screenshots/cleartax-2026-07-25T205549.png
security:
- kind: authentication
  name: Cleartax Authentication
  slug: cleartax-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cleartax Domain Security
  slug: cleartax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cleartax Vulnerability Disclosure
  slug: cleartax-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cleartax
tags:
- Company
- Tax
- GST
- E-Invoicing
- Compliance
- Fintech
- Accounting
- India
- Financial Automation
- Government
website: https://docs.cleartax.in/cleartax-docs
---
