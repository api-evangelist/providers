---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/console-group-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.console.com.au/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/console-group-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/console-group-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/console-group-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/console-group-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/console-group-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.console.com.au/
- group: other
  title: ''
  type: Product
  url: https://www.console.com.au/cloud
- group: other
  title: ''
  type: Marketplace
  url: https://www.console.com.au/integrate
- group: commercial
  title: ''
  type: Pricing
  url: https://www.console.com.au/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.console.com.au/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.console.com.au/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.console.com.au/product-updates
- group: company
  title: ''
  type: Blog
  url: https://www.console.com.au/blog
- group: other
  title: ''
  type: CaseStudies
  url: https://www.console.com.au/case-studies
- group: company
  title: ''
  type: About
  url: https://www.console.com.au/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.console.com.au/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.console.com.au/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://www.console.com.au/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.console.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.console.com.au/privacy-statement
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/console-australia-new-zealand
- group: other
  title: ''
  type: ParentCompany
  url: https://www.reapit.com/
created: '2026-07-26'
description: Console Group is an Australian property management software company, founded in 1992 in Brisbane, Queensland, that built the first property management and trust accounting software released in Australia and launched its cloud platform, Console Cloud, in 2017. It serves thousands of residential and commercial property management agencies across Australia and New Zealand with trust accounting, tenancy and lease management, inspections (Console Go + Inspect), maintenance, arrears, owner and tenant portals, SMS, analytics and payments (Console Pay). The company was acquired by the United Kingdom's Reapit and its flagship product has been rebranded Reapit PM, though the business continues to trade from console.com.au. In the Australian value chain Console Group sits on the property MANAGEMENT side rather than the sales-listing side, as the system of record for the rent roll, the trust account and the tenancy, downstream of REA Group's realestate.com.au and Domain and separate from
  PEXA's conveyancing rail and from PropTrack and CoreLogic valuation data. Its API posture is honestly closed. Console Group publishes no developer portal, no API reference, no OpenAPI or Swagger document and no partner developer program on console.com.au; the full sitemap contains no /developers, /api or /docs page, and the developer., developers. and docs. subdomains do not resolve. An api.console.com.au host answers as a Kong API Gateway but returns "no Route matched with those values" on every probed path, including GraphQL. A live integration marketplace at /integrate lists more than twenty two-way third-party products, so a working private integration API demonstrably exists, but access is by commercial marketplace arrangement only and nothing about it is published. The company does run a real public status page at status.console.com.au (Hund.io, Cloud and Accounts components, published uptime and response-time metrics), though its HAL+JSON status API is credential-gated. Australia
  has no MLS, so there is no RESO Web API or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier anywhere in Console Group's stack, and the company publishes no open data.
image: https://cdn.prod.website-files.com/60fe7d866b8c12591c099a3c/655ae1c47dbc4d7805827607_Console_Meta_Image.png
layout: provider
modified: '2026-07-26'
name: Console Group
nav: Providers
network: true
overview: 'Console Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Australia, New Zealand, Property Management, and PropTech.


  Console Group''s developer surface includes changelog, pricing, support, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 22.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/console-group/refs/heads/main/screenshots/console-group-2026-07-27T125333.png
security:
- kind: domain-security
  name: Console Group Domain Security
  slug: console-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: console-group
tags:
- Real-Estate
- Australia
- New Zealand
- Property Management
- PropTech
- Trust Accounting
- Rentals
- Tenancy
- Commercial Real Estate
- Inspections
- Payments
website: https://www.console.com.au/
---
