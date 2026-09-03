---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
api_count: 1
apis:
- description: Production HAL/HATEOAS (Spring Data REST style) backend API served at api.investly.co. The root returns a hypermedia _links document exposing a profile link; no public OpenAPI/Swagger specification, d
  name: Investly API
  slug: investly-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/investly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.investly.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.investly.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.investly.co/blog
- group: operate
  title: ''
  type: Support
  url: https://www.investly.co/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.investly.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.investly.co/v6/üldtingimused-en-0
- group: start
  title: ''
  type: SignUp
  url: https://www.investly.co/quote
- group: company
  title: ''
  type: About
  url: https://www.investly.co/about
created: '2026-07-17'
description: Investly is a European fintech invoice-financing marketplace that helps growing small and medium-sized businesses unlock working capital by financing their outstanding 30-180 day invoices. Businesses sell their approved invoices through a reverse-auction marketplace where investors bid to fund them, giving merchants the best available price from multiple funding providers and access to cash in 1-3 working days rather than waiting on customer payment terms. Founded by Siim Maivel and operating across Estonia and the United Kingdom, Investly is backed by Speedinvest, Startup Wise Guys, and Founders Capital. The platform serves established businesses across manufacturing, wholesale, construction, logistics, and business-services sectors and has funded invoices worth tens of millions of pounds to date. Investly runs a production HAL/HATEOAS backend API at api.investly.co, though it does not currently publish a public developer portal, OpenAPI specification, or API reference documentation.
image: https://www.investly.co/hubfs/styles/images/Investly_logo_horizontal.svg
layout: provider
modified: '2026-07-19'
name: Investly
nav: Providers
network: true
overview: 'Investly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Invoice Finance, Invoice Discounting, and Lending.


  Investly''s developer surface includes pricing, engineering blog, support, signup flow, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/investly/refs/heads/main/screenshots/investly-2026-07-25T222744.png
security:
- kind: domain-security
  name: Investly Domain Security
  slug: investly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: investly
tags:
- Company
- Fintech
- Invoice Finance
- Invoice Discounting
- Lending
- Working Capital
- SME Finance
- Marketplace
- Estonia
- United Kingdom
website: https://www.investly.co/
---
