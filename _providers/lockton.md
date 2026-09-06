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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lockton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://global.lockton.com/us/en
- group: company
  title: ''
  type: Blog
  url: https://global.lockton.com/us/en/news-insights
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lockton-companies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lockton-Companies
- group: start
  title: ''
  type: Login
  url: https://global.lockton.com/gb/en/client-login
- group: operate
  title: ''
  type: Support
  url: https://global.lockton.com/us/en/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://global.lockton.com/us/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.lockton.com/us/en/privacy-notice
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Lockton
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/LocktonCompanies
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/LocktonCompanies
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/lockton_usa/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lockton-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lockton-packages.yml
created: '2026-07-25'
description: 'Lockton Companies is the world''s largest privately held, independent insurance brokerage, founded by Jack Lockton in 1966 and headquartered in Kansas City, Missouri, United States. Lockton is a broker and intermediary rather than a risk carrier: it places commercial property and casualty, specialty and financial lines, employee benefits and people solutions, private client coverage, and — through Lockton Re — treaty and facultative reinsurance, for tens of thousands of clients across a global network of associates and offices reaching more than 140 locations. Its API posture is honestly characterized as partner-gated with no public API surface. As of July 2026 Lockton publishes no developer portal, no API reference, no OpenAPI or Swagger definition, no GraphQL endpoint, no Postman workspace, and no webhook or event catalog. The hostnames developer.lockton.com, developers.lockton.com, docs.lockton.com and api.lockton.com do not resolve in DNS, and a crawl of the 6,953 URLs
  in global.lockton.com/sitemap.xml surfaces no developer, API, ACORD, IVANS, OpenAPI or Swagger path. Client-facing technology is delivered through authenticated regional Lockton Client Portals and the proprietary Lockton SAGE intelligence and analytics ecosystem, which is presented on the website behind a contact form with no self-serve access, no documented data feed and no published integration surface. This is the expected posture for a US broker-intermediary: the United States has no federal insurance regulator and no open-insurance mandate, so data exchange between carriers, brokers and agency management systems runs on ACORD standards in an EDI and forms idiom rather than a public API idiom. Lockton''s most substantive standards signal is governance rather than implementation — in July 2026 Nidhi Howell, Chief Business Technology Officer of Lockton Re, was appointed to the ACORD Solutions Group Board of Directors representing the reinsurance broking channel — but no ACORD AL3, ACORD
  XML, NGDS or IVANS agency-download implementation is documented on any public Lockton property.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Lockton
nav: Providers
network: true
overview: 'Lockton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Brokers, Insurance Brokerage, and Property and Casualty.


  Lockton''s developer surface includes engineering blog, support, YouTube channel, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lockton/refs/heads/main/screenshots/lockton-2026-07-25T225435.png
security:
- kind: domain-security
  name: Lockton Domain Security
  slug: lockton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lockton
tags:
- Insurance
- United States
- Brokers
- Insurance Brokerage
- Property and Casualty
- Employee Benefits
- Reinsurance
- Specialty Insurance
- Risk Management
- ACORD
- Partner Gated
- No Public API
website: https://global.lockton.com/us/en
---
