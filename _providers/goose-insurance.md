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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goose-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gooseinsurance.com/
- group: company
  title: ''
  type: About
  url: https://www.gooseinsurance.com/en-ca/about
- group: company
  title: ''
  type: Partners
  url: https://www.gooseinsurance.com/en-ca/partners
- group: other
  title: ''
  type: Licensing
  url: https://www.gooseinsurance.com/en-ca/licensing
- group: operate
  title: ''
  type: Support
  url: https://support.gooseinsurance.com/
- group: company
  title: ''
  type: Blog
  url: https://www.gooseinsurance.com/en-ca/blog
- group: company
  title: ''
  type: News
  url: https://www.gooseinsurance.com/en-ca/news
- group: other
  title: ''
  type: Announcements
  url: https://www.gooseinsurance.com/en-ca/announcements
- group: other
  title: ''
  type: Claims
  url: https://www.gooseinsurance.com/en-ca/claims
- group: other
  title: ''
  type: PolicyWordings
  url: https://www.gooseinsurance.com/en-ca/policy-wordings
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.gooseinsurance.com/en-ca/affiliate-program
- group: other
  title: ''
  type: ReferralProgram
  url: https://www.gooseinsurance.com/en-ca/referral-program
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/ca/app/goose-insurance/id1382976076
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/search?q=goose%20insurance&c=apps&hl=en_CA
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gooseinsurance.com/en-ca/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gooseinsurance.com/en-ca/terms-of-use
- group: company
  title: ''
  type: Careers
  url: https://www.gooseinsurance.com/en-ca/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.gooseinsurance.com/en-ca/contact
- group: other
  title: ''
  type: X
  url: https://twitter.com/gooseinsurance
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/gooseinsurance
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/gooseinsuranceca/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goose-insurance-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goose-insurance-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goose-insurance-llms.txt
created: '2026-07-25'
description: 'Goose Insurance Services Inc. is a Vancouver, British Columbia based digital insurance distributor — an app-first licensed agency and MGA rather than a carrier — that sells travel medical, Visitors to Canada, term life, whole life, final expense, critical illness, accidental death and dismemberment, hospital cash, kids and renters coverage through the Goose mobile "insurance super app". Founded in 2017 and licensed in British Columbia, Alberta, Saskatchewan, Manitoba, Ontario, Quebec (AMF firm registration 603913), New Brunswick and Nova Scotia, Goose underwrites nothing itself: every policy is placed with a partner carrier including AIG Canada, iA Financial Group, TuGo, IMG, MSH, American-Amicable, Teachers Life, Lloyd''s of London and Sutton National. Its home market is Canada, with a US launch in 2020, and it sits in the thin digital-broker layer beneath the Big-Few Canadian oligopoly alongside Zensurance and APOLLO. Goose''s API posture is closed: as of the 2026-07-25 review
  there is no public developer portal, no self-serve API documentation, no downloadable OpenAPI or Swagger, and no published ACORD, AL3 or agency-management-system integration. The only host that answers on the api. subdomain is a private Heroku-backed mobile-app backend that returns 404 at every probed path, and the only partner surfaces the company publishes are a marketing affiliate/referral program and a carrier-relationships page — quote, bind, issue and FNOL are all consumer-facing inside the app only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Goose Insurance
nav: Providers
network: true
overview: 'Goose Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Insurtech, Life Insurance, and Travel Insurance.


  Goose Insurance''s developer surface includes support, engineering blog, product news, and 22 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 12.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goose-insurance/refs/heads/main/screenshots/goose-insurance-2026-07-25T220107.png
security:
- kind: domain-security
  name: Goose Insurance Domain Security
  slug: goose-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goose-insurance
tags:
- Insurance
- Canada
- Insurtech
- Life Insurance
- Travel Insurance
- Health Insurance
- Brokers
- Digital Distribution
- Managing General Agent
- Mobile
website: https://www.gooseinsurance.com/
---
