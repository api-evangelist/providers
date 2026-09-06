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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: A live GraphQL endpoint at api.dayforward.com/graphql that backs the Dayforward consumer application. Observed responding to GraphQL over HTTP POST (an empty operation returns a GRAPHQL_VALIDATION_FAI
  name: Dayforward GraphQL API
  slug: graphql
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://dayforward.io/
- group: company
  title: ''
  type: ConsumerWebsite
  url: https://www.dayforward.com/
- group: company
  title: ''
  type: About
  url: https://dayforward.io/about
- group: start
  title: ''
  type: SignUp
  url: https://www.dayforward.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.dayforward.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.dayforward.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dayforward.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dayforward.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/noho-digital
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dayfwrd/
- group: company
  title: ''
  type: Careers
  url: https://www.dayforward.com/careers
- group: design
  title: ''
  type: Conformance
  url: conformance/dayforward-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dayforward-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dayforward-domain-security.yml
created: '2026-08-04'
description: Dayforward is a New York-based life insurance technology and services group founded in 2019 by Aaron Shapiro. It owns Commercial Travelers Life Insurance Company (NY-domiciled carrier) and Dayforward Insurance Agency LLC (licensed in all 50 states), and sells income-replacement term life insurance direct to consumers at dayforward.com. Since pivoting to B2B at dayforward.io it licenses Workbench — a SaaS platform covering the full life insurance lifecycle from agent selling and automated underwriting through policy administration and service — plus managed distribution, underwriting and administration services to other carriers and distributors. Workbench is marketed as including "APIs, plug-and-play widgets, single sign-on support, and robust administration tools", but Dayforward publishes no public developer portal, API documentation, OpenAPI definition or SDKs.
image: https://storage.googleapis.com/df-prod-cdn/img/unfurl.jpg
layout: provider
modified: '2026-08-04'
name: Dayforward
nav: Providers
network: true
overview: 'Dayforward publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Life Insurance, Insurtech, and Financial-Services.


  Dayforward''s developer surface includes signup flow, support, FAQ, and 11 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 6.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dayforward/refs/heads/main/screenshots/dayforward-2026-08-07T164205.png
security:
- kind: domain-security
  name: Dayforward Domain Security
  slug: dayforward-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dayforward
tags:
- Company
- Insurance
- Life Insurance
- Insurtech
- Financial-Services
- Underwriting
- Policy Administration
- Software-as-a-Service
- GraphQL
website: https://dayforward.io/
---
