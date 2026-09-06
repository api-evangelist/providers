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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clutch-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clutch.ca
- group: company
  title: ''
  type: Blog
  url: https://www.clutch.ca/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clutchcanada
- group: operate
  title: ''
  type: Support
  url: https://www.clutch.ca/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.clutch.ca/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clutch.ca/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clutch.ca/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.clutch.ca/about
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/clutch
coverage:
  checked: '2026-08-09'
  detail: Clutch sells cars, not software — its only API host, api.clutch.ca, answers 403 Forbidden to every path including a nonsense control path, and www.clutch.ca has no developer portal at all (/developers and /api return the same 11,345-byte React shell as a random control URL), so there is no public developer program to document.
  evidence:
  - status: 403
    url: https://api.clutch.ca/v1
  - status: 403
    url: https://api.clutch.ca/zzz-control-9987
  - status: 200
    url: https://www.clutch.ca/developers
  - status: 404
    url: https://www.clutch.ca/llms.txt
  - status: 404
    url: https://www.clutch.ca/.well-known/agent-card.json
  - status: 404
    url: https://strapi.clutch.ca/documentation/v1.0.0/full_documentation.json
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Clutch is a Toronto-headquartered, vertically integrated online used-car retailer serving Canadian drivers. Unlike marketplace models that broker to third-party dealers, Clutch owns its own inventory and runs an end-to-end e-commerce purchase flow at clutch.ca: browsing reconditioned pre-owned vehicles, auto financing and a loan calculator, trade-in and sell-my-car offers, protection plans, insurance, and home delivery, backed by a 10-day money-back guarantee. It operates across Ontario, Nova Scotia, New Brunswick and Prince Edward Island. Clutch is a consumer retail business rather than an API vendor: its software is shipped as an end-user web application, and it publishes no public developer program, API reference, or machine-readable specification.'
image: https://www.clutch.ca/icons/android-chrome-512x512.png
layout: provider
modified: '2026-08-09'
name: Clutch Canada
nav: Providers
network: true
overview: 'Clutch Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, E-Commerce, Used Cars, and Auto Financing.


  Clutch Canada''s developer surface includes engineering blog, support, FAQ, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clutch-canada/refs/heads/main/screenshots/clutch-canada-2026-09-02T145115.png
security:
- kind: domain-security
  name: Clutch Canada Domain Security
  slug: clutch-canada-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clutch-canada
tags:
- Company
- Automotive
- E-Commerce
- Used Cars
- Auto Financing
- Retail
- Canada
- Consumer
website: https://www.clutch.ca
---
