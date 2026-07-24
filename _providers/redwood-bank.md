---
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'The OpenID Connect member-authentication surface (OpenIddict) behind the Umbraco headless-CMS "Content Delivery API" that powers redwoodbank.co.uk. This is the only live, machine-readable API surface '
  name: Redwood Bank Website Member Authentication (Umbraco Delivery API)
  slug: redwood-bank-website-member-authentication-umbraco-delivery-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redwood-bank-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redwood-bank-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/redwood-bank-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/redwood-bank-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.redwoodbank.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://redwoodbank.co.uk/news
- group: operate
  title: ''
  type: Support
  url: https://redwoodbank.co.uk/contact-us/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redwoodbank.co.uk/legal/website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redwoodbank.co.uk/legal/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://redwoodbank.co.uk/legal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redwoodbank/
created: '2026-07-23'
description: Redwood Bank is a specialist UK challenger bank for small and medium-sized businesses, headquartered in Letchworth Garden City, Hertfordshire. Launched in 2017 after receiving its banking licence from the Prudential Regulation Authority and Financial Conduct Authority (Financial Services Register firm reference 755924, company number 09872265), it is wholly owned by Redwood Financial Partners Ltd — a vehicle controlled by Jonathan and David Rowland, with Warrington Borough Council holding a roughly one-third stake. Redwood focuses narrowly on business and charity savings accounts and individually underwritten commercial and buy-to-let mortgages, and is not one of the CMA9 mandated banks. Because its product range is deposit- and lending-only (it does not offer a payment / business current account), it falls outside the PSD2 scope that compels UK Open Banking, and as of this review it publishes no public developer portal, no OBIE Read/Write (AIS/PIS/CBPII) APIs, and no confirmed
  Open Banking Open Data endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Redwood Bank
nav: Providers
network: true
overview: 'Redwood Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Business Banking, SME, and Savings.


  Redwood Bank''s developer surface includes authentication, engineering blog, support, legal docs, and 7 more developer resources.'
random_paper: 40
score:
  band: emerging
  composite: 22.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
security:
- kind: authentication
  name: Redwood Bank Authentication
  slug: redwood-bank-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Redwood Bank Domain Security
  slug: redwood-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: redwood-bank
tags:
- Financial Services
- Banking
- Business Banking
- SME
- Savings
- Commercial Mortgages
- Open Banking
- PSD2
- OBIE
- United Kingdom
website: https://www.redwoodbank.co.uk/
---
