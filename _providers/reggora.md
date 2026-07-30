---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Create and manage the loan records that appraisal orders are placed against - sync loan data from the LOS, retrieve loan detail, update loan fields, and receive a webhook when a loan is deleted. Endpo
  name: Reggora Loans API
  slug: reggora-loans-api
- description: Place appraisal orders against a loan, list and retrieve orders, track order status through the appraisal lifecycle, and manage order-level actions. Order-created and order-updated events are delivere
  name: Reggora Orders (Appraisals) API
  slug: reggora-orders-api
- description: List the appraisal products (report types and associated fees) a lender has configured so an integration can present valid product options when placing an order. Endpoints modeled from Reggora's docum
  name: Reggora Products API
  slug: reggora-products-api
- description: Retrieve appraisal report submissions on an order, request and track revisions, and drive the document review workflow between lender and vendor. Endpoints modeled from Reggora's documented submission
  name: Reggora Submissions & Revisions API
  slug: reggora-submissions-revisions-api
- description: Access the eVault to list, upload, and download appraisal documents and supporting files associated with an order. Endpoints modeled from Reggora's documented eVault resource.
  name: Reggora Documents (eVault) API
  slug: reggora-documents-evault-api
- description: 'Manage the appraisal vendors (appraisers and AMCs) a lender works with and the lender''s branch structure used to route and assign orders. Endpoints modeled from Reggora''s documented vendor and branch '
  name: Reggora Vendors & Branches API
  slug: reggora-vendors-branches-api
- description: Authenticate integrations with a JWT bearer token plus a per-integration API key, and manage the lender users that act within the platform. Endpoints modeled from Reggora's documented authentication a
  name: Reggora Users & Authentication API
  slug: reggora-users-auth-api
- description: Subscribe to server-to-server webhook callbacks that notify an integration when an order is created or updated and when a loan is deleted. Delivery is HTTP POST to a configured endpoint URL, not a Web
  name: Reggora Webhook Events API
  slug: reggora-webhooks-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/reggora-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reggora-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reggora
- group: company
  title: ''
  type: Website
  url: https://www.reggora.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.reggora.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/reggora-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reggora-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reggora-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.reggora.com/blog
created: '2026-07-04'
description: Reggora is a modern appraisal management platform that connects mortgage lenders and appraisal vendors on a single system, automating the appraisal lifecycle from order placement and product selection through payment, document submission, revision review, and delivery back into the loan origination system (LOS). Reggora exposes a documented Lender API and Vendor API so lenders can manage 100% of their appraisal orders directly from their own LOS or proprietary tech stack. All key platform functionality is available via secure REST endpoints (JWT bearer token plus a per-integration API key), with sandbox and production environments and webhook callbacks for loan and order events. Endpoint paths in this catalog are modeled from Reggora's documented resource areas; the full reference is partner-facing at api.reggora.io/docs.
finops:
- name: Reggora Finops
  service_category: Financial Services Software
  slug: reggora-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reggora.png
layout: provider
modified: '2026-07-04'
name: Reggora
nav: Providers
network: true
overview: 'Reggora publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Appraisal Management, Mortgage, Lending, Real Estate, and Valuation.


  Reggora''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Reggora Plans Pricing
  plan_count: 2
  slug: reggora-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Reggora Rate Limits
  slug: reggora-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: -2.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Reggora Domain Security
  slug: reggora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reggora Trust Center
  slug: reggora-trust-center
  summary_line: SOC 2, PCI DSS
slug: reggora
tags:
- Appraisal Management
- Mortgage
- Lending
- Real Estate
- Valuation
- Loan Origination
- LOS Integration
- Fintech
website: https://www.reggora.com
---
