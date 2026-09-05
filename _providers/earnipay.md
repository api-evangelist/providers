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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 50
  human_in_the_loop: 50
  name: Earnipay Agentic Access
  operation_count: 69
  slug: earnipay-agentic-access
  summary_line: 69 operations · 50 acting · 50 human-in-the-loop
api_count: 1
apis:
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: The App API from Earnipay — 1 operation(s) for app.
  name: Earnipay App API
  slug: earnipay-app-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: Third-party APP provider integration (Taxly) for FIRS submission
  name: Earnipay APP Provider API
  slug: earnipay-app-provider-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: User authentication and authorization endpoints
  name: Earnipay Authentication API
  slug: earnipay-authentication-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: The Bank API from Earnipay — 2 operation(s) for bank.
  name: Earnipay Bank API
  slug: earnipay-bank-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: Business profile management and FIRS configuration
  name: Earnipay Business API
  slug: earnipay-business-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: Customer management for invoicing
  name: Earnipay Customers API
  slug: earnipay-customers-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: Invoice creation, management, and FIRS validation
  name: Earnipay Invoices API
  slug: earnipay-invoices-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: Generate FIRS-compliant Invoice Reference Numbers
  name: Earnipay IRN Generator API
  slug: earnipay-irn-generator-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: The Payment Details API from Earnipay — 2 operation(s) for payment details.
  name: Earnipay Payment Details API
  slug: earnipay-payment-details-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: The Products API from Earnipay — 2 operation(s) for products.
  name: Earnipay Products API
  slug: earnipay-products-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: Generate FIRS-compliant encrypted QR codes for invoices
  name: Earnipay QR Code Generator API
  slug: earnipay-qr-code-generator-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: Team member and invitation management
  name: Earnipay Team API
  slug: earnipay-team-api
- baseURL: https://e-invoicing.earnipay.com/v1
  baseurl_source: declared
  description: User profile management
  name: Earnipay Users API
  slug: earnipay-users-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Earnipay Invoicing App API
  slug: open-earnipay-app-api
- collection_type: open
  name: Earnipay Invoicing App APP Provider API
  slug: open-earnipay-app-provider-api
- collection_type: open
  name: Earnipay Invoicing App Authentication API
  slug: open-earnipay-authentication-api
- collection_type: open
  name: Earnipay Invoicing App Bank API
  slug: open-earnipay-bank-api
- collection_type: open
  name: Earnipay Invoicing App Business API
  slug: open-earnipay-business-api
- collection_type: open
  name: Earnipay Invoicing App Customers API
  slug: open-earnipay-customers-api
- collection_type: open
  name: Earnipay Invoicing App Invoices API
  slug: open-earnipay-invoices-api
- collection_type: open
  name: Earnipay Invoicing App IRN Generator API
  slug: open-earnipay-irn-generator-api
- collection_type: open
  name: Earnipay Invoicing App Payment Details API
  slug: open-earnipay-payment-details-api
- collection_type: open
  name: Earnipay Invoicing App Products API
  slug: open-earnipay-products-api
- collection_type: open
  name: Earnipay Invoicing App QR Code Generator API
  slug: open-earnipay-qr-code-generator-api
- collection_type: open
  name: Earnipay Invoicing App Team API
  slug: open-earnipay-team-api
- collection_type: open
  name: Earnipay Invoicing App Users API
  slug: open-earnipay-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/earnipay-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/earnipay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/earnipay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/earnipay-authentication.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/earnipay-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/earnipay-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/earnipay-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/earnipay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/earnipay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/earnipay-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/earnipay-e-invoicing-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/earnipay-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.earnipay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.earnipay.com/docs/e-invoice
- group: docs
  title: ''
  type: APIReference
  url: https://e-invoicing.earnipay.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.earnipay.com/docs/e-invoice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Earnipay
- group: company
  title: ''
  type: Website
  url: https://earnipay.com/
created: '2026-07-17'
description: Earnipay is a Nigerian fintech that operates an NRS/FIRS-compliant e-invoicing platform for businesses. As an accredited Nigeria Revenue Service (NRS) and NITDA systems integrator, Earnipay lets developers programmatically create businesses, manage customers and products, generate FIRS-compliant invoices with IRN (Invoice Reference Number) and QR codes, and submit them to the tax authority through an Access Point Provider (APP) connection. The public Earnipay Invoicing API is an OpenAPI 3.0.0 REST service covering authentication, businesses, customers, products, payment details, invoices, IRN and QR generation, bank lookup/verification, and team management. It authenticates with JWT bearer tokens for user-facing flows and an X-API-Key header for third-party integrations. Added to the API Evangelist network as a portfolio company of Canaan Partners.
image: https://earnipay-api-storage-prod.s3.eu-west-1.amazonaws.com/business-documents/business-img-others.png
layout: provider
modified: '2026-07-18'
name: Earnipay
nav: Providers
network: true
overview: 'Earnipay publishes 13 APIs on the [APIs.io](https://apis.io/) network, including App API, APP Provider API, Authentication API, and 10 more. Tagged areas include Company, E-Invoicing, Invoicing, FIRS, and NRS.


  Earnipay''s developer surface includes authentication, documentation, API reference, getting-started guide, and 15 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 48.6
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 23.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/earnipay/refs/heads/main/screenshots/earnipay-2026-07-25T212700.png
security:
- kind: authentication
  name: Earnipay Authentication
  slug: earnipay-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Earnipay Domain Security
  slug: earnipay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: earnipay
tags:
- Company
- E-Invoicing
- Invoicing
- FIRS
- NRS
- Tax
- Compliance
- Fintech
- Nigeria
- Payments
- Financial-Services
website: https://earnipay.com/
---
