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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/legalzoom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legalzoom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.legalzoom.com
- group: other
  title: ''
  type: BusinessFormation
  url: https://www.legalzoom.com/business
- group: commercial
  title: ''
  type: PersonalLegal
  url: https://www.legalzoom.com/personal
- group: other
  title: ''
  type: AttorneyServices
  url: https://www.legalzoom.com/attorneys
- group: commercial
  title: ''
  type: Pricing
  url: https://www.legalzoom.com/business/business-formation/llc-overview.html
- group: company
  title: ''
  type: About
  url: https://www.legalzoom.com/company/about-us.html
- group: company
  title: ''
  type: Press
  url: https://www.legalzoom.com/press
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.legalzoom.com
- group: other
  title: ''
  type: SECFilings
  url: https://investors.legalzoom.com/financials-and-filings/sec-filings
- group: company
  title: ''
  type: Careers
  url: https://www.legalzoom.com/careers/jobs
- group: company
  title: ''
  type: Partners
  url: https://www.legalzoom.com/business/partners
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.legalzoom.com/partners/affiliate-program
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.legalzoom.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.legalzoom.com/articles
- group: auth
  title: ''
  type: Security
  url: https://www.legalzoom.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.legalzoom.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.legalzoom.com/legal/terms-of-service
- group: build
  title: ''
  type: GitHub
  url: https://github.com/LegalZoom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/legalzoom-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LegalZoom
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/legalzoom
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/legalzoom
created: '2026-05-25'
description: 'LegalZoom.com, Inc. (NASDAQ: LZ) is a Glendale, California online legal technology and services company that helps individuals and small businesses create legal documents and form, run, and grow their businesses without necessarily hiring an attorney. Founded in 1999, LegalZoom offers business formation services (LLC, S-Corp, C-Corp, nonprofit, DBA), registered agent service, EIN/tax ID filing, annual report and compliance filings, business licenses, virtual mail, business banking partnerships, trademark registration, and ongoing bookkeeping and tax services through LZ Books and LZ Tax. On the personal side it provides wills, living trusts, power of attorney, prenuptial agreements, and a partner-driven divorce flow via Divorce.com. Customers access an attorney-network legal advice subscription (LZ Legal Services / business advisory plans) connecting them to independent attorneys for consultations and document review. LegalZoom went public on Nasdaq in 2021 (ticker LZ) and serves
  customers primarily in the United States. The company''s revenue model is transactional document and formation fees plus recurring subscription services (registered agent, compliance, attorney advice, bookkeeping). LegalZoom does not publish a public developer API, OpenAPI specification, SDK, or developer portal; partner integrations (e.g. divorce.com, banking partners, accounting partners) appear to be private commercial arrangements rather than self-service developer APIs. The legalzoom.com web app calls a set of internal hosts under apigw.legalzoom.com (checkout-graphql-public-api, customer, experimentation, revv, attorney-state-service, site-search) but these are first-party and not documented for third-party use.'
graphqls:
- description: ''
  name: LegalZoom GraphQL API
  slug: legalzoom-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/legalzoom.png
layout: provider
modified: '2026-05-25'
name: LegalZoom
nav: Providers
network: true
overview: 'LegalZoom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Technology, Legal Tech, Business Formation, and LLC Formation.


  LegalZoom''s developer surface includes pricing, engineering blog, GitHub presence, YouTube channel, and 20 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/legalzoom/refs/heads/main/screenshots/legalzoom-2026-06-20T184405.png
security:
- kind: domain-security
  name: Legalzoom Domain Security
  slug: legalzoom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Legalzoom Vulnerability Disclosure
  slug: legalzoom-vulnerability-disclosure
  summary_line: disclosure policy published
slug: legalzoom
tags:
- Legal
- Legal Technology
- Legal Tech
- Business Formation
- LLC Formation
- Incorporation
- Registered Agent
- Compliance
- Trademark
- Legal Documents
- Estate Planning
- Wills
- Living Trusts
- Power of Attorney
- Attorney Network
- Small Business
- Bookkeeping
- Tax Filing
- Public Company
- NASDAQ LZ
website: https://www.legalzoom.com
---
