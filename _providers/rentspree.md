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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentspree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rentspree.com
- group: company
  title: ''
  type: About
  url: https://www.rentspree.com/about
- group: other
  title: ''
  type: Enterprise
  url: https://www.rentspree.com/enterprise
- group: build
  title: ''
  type: APIIntegration
  url: https://www.rentspree.com/enterprise/api-service-integration
- group: company
  title: ''
  type: MLSPartners
  url: https://www.rentspree.com/enterprise/mls
- group: company
  title: ''
  type: PropTechPartners
  url: https://www.rentspree.com/enterprise/proptech
- group: company
  title: ''
  type: BrokeragePartners
  url: https://www.rentspree.com/enterprise/brokerage
- group: company
  title: ''
  type: AssociationPartners
  url: https://www.rentspree.com/enterprise/realtor-association
- group: other
  title: ''
  type: TenantScreening
  url: https://www.rentspree.com/tenant-screening
- group: other
  title: ''
  type: RentalApplication
  url: https://www.rentspree.com/rental-application
- group: other
  title: ''
  type: RentPayments
  url: https://www.rentspree.com/collect-rent
- group: other
  title: ''
  type: ESign
  url: https://www.rentspree.com/e-sign
- group: other
  title: ''
  type: Listings
  url: https://www.rentspree.com/listing-pages
- group: other
  title: ''
  type: RentEstimate
  url: https://www.rentspree.com/rent-estimate
- group: other
  title: ''
  type: RentersInsurance
  url: https://www.rentspree.com/renters-insurance
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rentspree.com/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.rentspree.com
- group: company
  title: ''
  type: Blog
  url: https://www.rentspree.com/blog
- group: auth
  title: ''
  type: Security
  url: https://www.rentspree.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rentspree.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rentspree.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.rentspree.com/careers
- group: operate
  title: ''
  type: ContactUs
  url: https://www.rentspree.com/contact-us
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rentspree
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rentspree
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RentSpree
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/RentSpree
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@RentSpree
created: '2026-05-25'
description: RentSpree is a Los Angeles-headquartered rental real estate technology platform that streamlines the long-tail rental transaction for real estate agents, landlords, property managers, and renters. Its consumer-facing product suite covers online rental applications, TransUnion-powered tenant screening (credit, background, eviction, and income verification), e-sign and lease workflows, ACH/card rent payments, AI-assisted listing pages and syndication, rent estimate, and renters insurance. RentSpree positions itself as the rental layer for the MLS and brokerage ecosystem and has built named integrations with Multiple Listing Services (Bright MLS, CRMLS, Beaches MLS, CJMLS, Florida Realtors) and PropTech partners (SkySlope, Lone Wolf, ZipLogix, C.A.R. OnlineEd). It also runs an Enterprise API Integration program for MLSs, associations, brokerages, and PropTech vendors that want to embed rental application intake and tenant screening into their own platforms — documentation is not
  publicly published; partners are onboarded through a sales/integration process with implementation quoted at as little as three weeks. There is no self-serve developer portal, no public OpenAPI specification, and no public SDK or CLI; the RentSpree GitHub org is effectively empty (only a .github org-defaults repo). RentSpree is SOC 2 Type II certified and reports more than four million agents, landlords, and renters on the platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rentspree.png
layout: provider
modified: '2026-05-25'
name: RentSpree
nav: Providers
network: true
overview: 'RentSpree is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Rentals, Rental Applications, Tenant Screening, and Credit Check.


  RentSpree''s developer surface includes pricing, engineering blog, GitHub presence, YouTube channel, and 25 more developer resources.'
random_paper: 90
score:
  band: emerging
  composite: 12.5
  delta: -3.2
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rentspree/refs/heads/main/screenshots/rentspree-2026-06-20T192855.png
security:
- kind: domain-security
  name: Rentspree Domain Security
  slug: rentspree-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rentspree
tags:
- Real Estate
- Rentals
- Rental Applications
- Tenant Screening
- Credit Check
- Background Check
- Eviction History
- Income Verification
- Renters Insurance
- Rent Payments
- E-Sign
- Leasing
- Listings
- MLS
- PropTech
- Brokerage
- REALTOR Association
website: https://www.rentspree.com
---
