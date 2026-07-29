---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reia.com.au/
- group: company
  title: ''
  type: About
  url: https://www.reia.com.au/who-we-are
- group: other
  title: ''
  type: Network
  url: https://www.reia.com.au/our-network
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.reia.com.au/conduct
- group: auth
  title: ''
  type: Certification
  url: https://www.reia.com.au/accredit
- group: other
  title: ''
  type: Research
  url: https://www.reia.com.au/research
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reia.com.au/research/har
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reia.com.au/research/remf
- group: other
  title: ''
  type: Reports
  url: https://www.reia.com.au/standalone-research
- group: other
  title: ''
  type: Policy
  url: https://www.reia.com.au/submissions
- group: auth
  title: ''
  type: Compliance
  url: https://www.reia.com.au/aml-ctf
- group: other
  title: ''
  type: Policy
  url: https://www.reia.com.au/residential-energy-efficiency
- group: company
  title: ''
  type: News
  url: https://www.reia.com.au/industry-news
- group: other
  title: ''
  type: Media
  url: https://www.reia.com.au/media-contact
- group: other
  title: ''
  type: Events
  url: https://www.reia.com.au/austros
- group: other
  title: ''
  type: Events
  url: https://www.reia.com.au/nafe
- group: other
  title: ''
  type: SignIn
  url: https://www.reia.com.au/sign-in
- group: start
  title: ''
  type: SignUp
  url: https://www.reia.com.au/create-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reia.com.au/create-account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reia.com.au/privacy-policy
- group: other
  title: ''
  type: Disclaimer
  url: https://www.reia.com.au/disclaimer
- group: operate
  title: ''
  type: Contact
  url: https://www.reia.com.au/contact-us
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/reia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reia-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/real-estate-institute-of-australia-reia
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/REIAustralia
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/reiaustralia
created: '2026-07-26'
description: 'The Real Estate Institute of Australia (REIA), founded in 1924 and based in Canberra, is the national federation of the eight state and territory Real Estate Institutes (REINSW, REIV, REIQ, REIWA, REISA, REIT, REIACT, REINT), which between them represent roughly 85% of Australian real estate businesses and agents. REIA is a policy, research and accreditation body, not an operator of market infrastructure: it administers the REIA National Principles of Conduct that underpin state institute codes and training, awards Associate (AREI) and Fellow accreditations, runs the Australasian Auctioneering Championships (AUSTROS) jointly with REINZ and the National Awards for Excellence (NAFE), makes submissions to the Commonwealth Government, and publishes the quarterly Housing Affordability Report (HAR) and Real Estate Market Facts (REMF) series that Federal Treasury, the Reserve Bank, state treasuries and investment banks subscribe to. It sits well above the transaction rail in the Australian
  value chain - listings run through REA Group''s realestate.com.au and Domain, settlement through PEXA, valuation through PropTrack and CoreLogic, and title through the state land registries - and REIA touches none of those pipes. Its API posture is therefore an honest absence: no developer portal, no API subdomain, no OpenAPI or OData contract, and no RESO reference anywhere on its estate, because RESO is a NAR-mandated United States construct with no Australian counterpart. What REIA sells is data, not access to it - the HAR and REMF reports are AUD 450 subscriptions and each of the 7 HAR and 15 REMF underlying datasets is a separate AUD 280 subscription, delivered as documents through a platformOS/Insites ecommerce storefront with Stripe checkout behind an email-and-password account. Policy submissions, standalone research reports and the strategic plan are freely downloadable PDFs; the quarterly numbers are not, and there is no open data.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reia.png
layout: provider
modified: '2026-07-26'
name: Real Estate Institute of Australia
nav: Providers
network: true
overview: 'Real Estate Institute of Australia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Australia, Industry Body, Standards, and Membership.


  Real Estate Institute of Australia''s developer surface includes pricing, product news, signup flow, and 25 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 17.4
  delta: 0.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reia/refs/heads/main/screenshots/reia-2026-07-27T125402.png
security:
- kind: domain-security
  name: Reia Domain Security
  slug: reia-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: reia
tags:
- Real Estate
- Australia
- Industry Body
- Standards
- Membership
- Property Data
- Housing Affordability
- Research
- Advocacy
- Rentals
- PropTech
website: https://www.reia.com.au/
---
