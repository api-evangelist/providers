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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/embroker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.embroker.com
- group: start
  title: ''
  type: Login
  url: https://app.embroker.com/login
- group: start
  title: ''
  type: Signup
  url: https://app.embroker.com/signup
- group: other
  title: ''
  type: Application
  url: https://app.embroker.com
- group: other
  title: ''
  type: BrokerAccess
  url: https://access.embroker.com
- group: other
  title: ''
  type: Coverages
  url: https://www.embroker.com/coverage/
- group: other
  title: ''
  type: Startup
  url: https://www.embroker.com/startup/
- group: other
  title: ''
  type: TechCompanies
  url: https://www.embroker.com/non-funded-tech-companies/
- group: other
  title: ''
  type: LawFirms
  url: https://www.embroker.com/law/
- group: other
  title: ''
  type: VentureCapital
  url: https://www.embroker.com/venture-capital-private-equity-firms/
- group: other
  title: ''
  type: FinancialServices
  url: https://www.embroker.com/financial-services-professionals/
- group: other
  title: ''
  type: Consultants
  url: https://www.embroker.com/consultants/
- group: other
  title: ''
  type: RealEstate
  url: https://www.embroker.com/real-estate/
- group: other
  title: ''
  type: SmallBusinesses
  url: https://www.embroker.com/small-businesses/
- group: other
  title: ''
  type: CyberInsurance
  url: https://www.embroker.com/coverage/cyber-insurance/
- group: other
  title: ''
  type: ProfessionalLiability
  url: https://www.embroker.com/coverage/professional-liability-insurance/
- group: other
  title: ''
  type: DirectorsAndOfficers
  url: https://www.embroker.com/coverage/directors-officers-insurance/
- group: other
  title: ''
  type: BusinessOwnersPolicy
  url: https://www.embroker.com/coverage/business-owners-policy/
- group: other
  title: ''
  type: GeneralLiability
  url: https://www.embroker.com/coverage/commercial-general-liability-insurance/
- group: other
  title: ''
  type: EmploymentPracticesLiability
  url: https://www.embroker.com/coverage/employment-practices-liability-insurance/
- group: other
  title: ''
  type: CommercialCrime
  url: https://www.embroker.com/coverage/commercial-crime-insurance/
- group: other
  title: ''
  type: LawyersProfessionalLiability
  url: https://www.embroker.com/coverage/legal-professional-liability/
- group: design
  title: ''
  type: TechErrorsOmissions
  url: https://www.embroker.com/coverage/tech-errors-omissions/
- group: company
  title: ''
  type: About
  url: https://www.embroker.com/about/
- group: company
  title: ''
  type: Press
  url: https://www.embroker.com/press/
- group: company
  title: ''
  type: Partners
  url: https://www.embroker.com/partners/
- group: other
  title: ''
  type: ResourceHub
  url: https://www.embroker.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.embroker.com/blog/
- group: build
  title: ''
  type: Tools
  url: https://www.embroker.com/tools/
- group: company
  title: ''
  type: Careers
  url: https://www.embroker.com/careers/
- group: auth
  title: ''
  type: Security
  url: https://www.embroker.com/security/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.embroker.com/privacy/
- group: commercial
  title: ''
  type: Terms
  url: https://www.embroker.com/terms/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/embroker
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Embroker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/embroker
- group: docs
  title: ''
  type: GraphQL
  url: graphql/embroker-graphql.md
created: '2026-05-25'
description: Embroker is a San Francisco-based digital business insurance broker and insurtech platform founded in 2015 by Matt Miller, on a mission to make commercial insurance simple, clear, and tailored to each industry. Embroker operates a digital-first online platform where businesses can compare, quote, purchase, and manage commercial insurance policies directly, with industry-specific programs for funded startups, tech companies, law firms, venture capital and private equity firms, financial services professionals, consultants, real estate agents, and small businesses. Its coverage portfolio includes Business Owners Policy (BOP), commercial general liability, professional liability, technology errors and omissions, cyber insurance, directors and officers, employment practices liability, commercial crime, key person, workers compensation, and lawyers professional liability, often bundled into industry packages such as the Startup Bundle, Law Bundle, and MPL Bundle. In 2017 Embroker
  partnered with Munich Re to underwrite its own digital insurance products; in 2020 it launched Embroker Access for retail and wholesale brokers; and in 2023 it launched Embroker One, an AI- and machine-learning-driven platform for real-time risk assessment and policy recommendations. The company has protected 9,500+ businesses across 16,000+ policies and raised a $100M round in 2021 led by FTV Capital. Embroker's revenue model is brokerage commissions, managing general agent (MGA) underwriting fees on its own products, and platform access for partner brokers; there is no public developer API, SDK, or open-source release — its GitHub organization contains only archived forks of third-party libraries and a small number of internal tooling repositories.
graphqls:
- description: Embroker is a San Francisco-based digital business insurance broker and insurtech platform that enables businesses to compare, quote, purchase, and manage commercial insurance policies. This conceptua
  name: Embroker GraphQL Schema
  slug: embroker-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/embroker.png
layout: provider
modified: '2026-05-25'
name: Embroker
nav: Providers
network: true
overview: 'Embroker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Business Insurance, Commercial Insurance, Insurtech, and Digital Insurance.


  Embroker''s developer surface includes signup flow, engineering blog, tooling, privacy policy, terms of service, GitHub presence, and 32 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 22.9
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 48.1
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 22.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/embroker/refs/heads/main/screenshots/embroker-2026-06-20T180627.png
security:
- kind: domain-security
  name: Embroker Domain Security
  slug: embroker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: embroker
tags:
- Insurance
- Business Insurance
- Commercial Insurance
- Insurtech
- Digital Insurance
- Broker
- Managing General Agent
- Cyber Insurance
- Professional Liability
- Directors and Officers
- Startups
- Law Firms
- Risk Management
website: https://www.embroker.com
---
