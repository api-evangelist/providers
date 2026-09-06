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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://acretrader.com/
- group: start
  title: ''
  type: SignUp
  url: https://acretrader.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acretrader.com/company/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acretrader.com/company/privacy
- group: operate
  title: ''
  type: Support
  url: https://acretrader.com/company/contact-us
- group: company
  title: ''
  type: Blog
  url: https://acretrader.com/newsroom
- group: company
  title: ''
  type: BlogRSS
  url: https://api.acretrader.com/v1/cms/learn/rss
- group: start
  title: ''
  type: Login
  url: https://acretrader.com/sign-in
- group: company
  title: ''
  type: About
  url: https://acretrader.com/company/about-us
- group: operate
  title: ''
  type: FAQ
  url: https://acretrader.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acretrader
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acretrader-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/acretrader-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acretrader-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acretrader-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acretrader-llms.txt
coverage:
  checked: '2026-08-10'
  detail: AcreTrader ships only an end-user accredited-investor portal — the 101 KB sitemap contains no developer, API, docs or status page, and api.acretrader.com answers /healthz but 404s every OpenAPI, GraphQL, MCP and /.well-known/ path, serving only an undocumented CMS backend for the marketing site.
  evidence:
  - status: 404
    url: https://acretrader.com/llms.txt
  - status: 404
    url: https://acretrader.com/developers
  - status: 404
    url: https://api.acretrader.com/openapi.json
  - status: 404
    url: https://api.acretrader.com/graphql
  - status: 404
    url: https://api.acretrader.com/.well-known/agent-card.json
  - status: 200
    url: https://api.acretrader.com/healthz
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: AcreTrader is a farmland investment platform headquartered in Fayetteville, Arkansas that lets accredited investors buy fractional, passive ownership stakes in individual US row-crop, permanent-crop and timberland farms. AcreTrader sources and vets each farm, then handles the legal entity, farm management and administration while investors earn returns from annual cash rent and long-term land appreciation. Securities are offered through North Capital Private Securities Corporation, a FINRA/SIPC member broker-dealer that is not an affiliate of the platform. Since 2018 AcreTrader has enabled investment in over 140 farmland properties spanning roughly 44,000 acres across 20 states, and its investment management arm, AcreTrader Management LLC, reports net IRR of 9.4% to 30.3% on realized deals. Proterra Investment Partners LP acquired AcreTrader in August 2025. AcreTrader publishes no public developer API, no developer portal and no machine-readable specification; contract discovery
  was run in full against acretrader.com and api.acretrader.com on 2026-08-10 and every discovery path returned 404.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acretrader.png
layout: provider
modified: '2026-08-10'
name: Acretrader
nav: Providers
network: true
overview: 'Acretrader is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Farmland, Investing, Alternative Investments, and Real-Estate.


  Acretrader''s developer surface includes signup flow, support, engineering blog, FAQ, and 12 more developer resources.'
plans:
- name: Acretrader Plans Pricing
  plan_count: 0
  slug: acretrader-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Acretrader Rate Limits
  slug: acretrader-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acretrader/refs/heads/main/screenshots/acretrader-2026-07-25T181516.png
security:
- kind: domain-security
  name: Acretrader Domain Security
  slug: acretrader-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acretrader
tags:
- Company
- Farmland
- Investing
- Alternative Investments
- Real-Estate
- Fintech
- Agriculture
- Marketplace
- Farmland Investing
- Accredited Investors
- Private Placements
- AgTech
website: https://acretrader.com/
---
