---
access_model:
  confidence: high
  label: Partner-provisioned · No public self-serve API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/butn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.butn.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.butn.co/funding-solutions
- group: company
  title: ''
  type: Blog
  url: https://www.butn.co/news
- group: operate
  title: ''
  type: Support
  url: https://www.butn.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.butn.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.butn.co/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/butn
- group: start
  title: ''
  type: Login
  url: https://app.butn.co/s/
created: '2026-07-24'
description: 'Butn is an Australian embedded-finance company that funds business cashflow at the point of transaction, plugging invoice finance, outsourced credit terms, and supplier "pay now, settle later" directly into the platforms its business customers already use. Its funding products — Butn X (invoice finance to draw cash early against receivables), Butn Terms (outsourced buyer credit where Butn carries the risk), and Butn Pay (paying suppliers upfront in exchange for extended repayment) — are designed to be embedded into partner marketplaces, accounting tools, and B2B platforms such as MYOB, Salesforce, and FoodByUs rather than sold as a standalone destination. Butn sits in the spend / accounts payable and accounts receivable financing layer of Australia''s payments market, where money movement rides the New Payments Platform and the banks opened by the Consumer Data Right. Its integration and embedding are delivered through private, partner-provisioned APIs: Butn markets "plug and
  play" embedding for partners but does not operate a public self-serve developer portal, publish downloadable OpenAPI/Swagger definitions, or expose openly documented API reference material as of this profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Butn
nav: Providers
network: true
overview: 'Butn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Embedded Finance, Invoice Finance, and Accounts Receivable.


  Butn''s developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/butn/refs/heads/main/screenshots/butn-2026-07-25T204119.png
security:
- kind: domain-security
  name: Butn Domain Security
  slug: butn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: butn
tags:
- Payments
- Australia
- Embedded Finance
- Invoice Finance
- Accounts Receivable
- Accounts Payable
- B2B BNPL
- Business Lending
- Cash Flow
- Working Capital
website: https://www.butn.co/
---
