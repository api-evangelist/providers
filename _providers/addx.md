---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Publicly documented REST API that connects an external system to the ADDX platform. Roughly 68 operations across five documented groups — Account Management (account, balance, EAM investor, portfolio,
  name: ADDX Open API
  slug: addx-open-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Blog
  url: https://addx.co/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://addx.co/insights/rss/
- group: auth
  href: https://artifacts.apis.io/addx/security/addx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://addx.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.addx.co/open-api/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.addx.co/open-api/
- group: docs
  title: ''
  type: Documentation
  url: https://addx.co/en/how-addx-works/
- group: start
  title: ''
  type: GettingStarted
  url: https://addx.co/en/get-started/
- group: start
  title: ''
  type: SignUp
  url: https://client.addx.co/register
- group: start
  title: ''
  type: Login
  url: https://client.addx.co/login
- group: operate
  title: ''
  type: Support
  url: https://addx.co/en/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://addx.co/en/insights/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://documents.addx.co/ADDX_Platform_Rules.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addx.co/en/privacy-policy/
- group: design
  href: https://artifacts.apis.io/addx/conformance/addx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/addx-conformance.yml
- group: auth
  href: https://artifacts.apis.io/addx/conformance/addx-conformance.yml
  title: ''
  type: Compliance
  url: conformance/addx-conformance.yml
- group: auth
  href: https://artifacts.apis.io/addx/authentication/addx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/addx-authentication.yml
- group: design
  href: https://artifacts.apis.io/addx/conventions/addx-conventions.yml
  title: ''
  type: Conventions
  url: conventions/addx-conventions.yml
- group: design
  href: https://artifacts.apis.io/addx/errors/addx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/addx-problem-types.yml
- group: design
  href: https://artifacts.apis.io/addx/lifecycle/addx-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/addx-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/addx/rate-limits/addx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/addx-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/addx/plans/addx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/addx-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/addx/packages/addx-packages.yml
  title: ''
  type: Packages
  url: packages/addx-packages.yml
- group: design
  href: https://artifacts.apis.io/addx/data-model/addx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/addx-data-model.yml
- group: agent
  href: https://artifacts.apis.io/addx/llms/addx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/addx-llms.txt
- group: agent
  href: https://artifacts.apis.io/addx/mcp/addx-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/addx-mcp.yml
created: '2026-09-07'
description: ADDX is a Singapore-headquartered digital securities exchange and private-markets investment platform, licensed by the Monetary Authority of Singapore for the issuance, custody and secondary trading of digital securities. Founded in 2017 as iSTOX, it tokenises and fractionalises private equity, private credit, hedge funds, structured products, fixed income and commercial paper so accredited investors can subscribe at roughly USD 10,000 rather than institutional minimums. Alongside the consumer web and mobile app, ADDX Advantage packages the same rails for wealth managers, brokers and external asset managers (EAMs), and the publicly documented ADDX Open API — an HMAC-signed REST surface of about 68 operations covering account and investor information, STO subscription and redemption, wallet, fiat and digital-asset flows, exchange order-book market data and investor reporting — lets those partners drive the platform from their own systems.
image: https://www.addx.co/images/Social_Share_Hero_image2.png
layout: provider
modified: '2026-10-06'
name: ADDX
nav: Providers
network: true
overview: 'ADDX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Securities Exchange, Private Markets, Tokenization, Alternative Investments, and Wealth Management.


  ADDX''s developer surface includes engineering blog, API reference, documentation, getting-started guide, signup flow, support, authentication, and 19 more developer resources.'
plans:
- name: Addx Plans Pricing
  plan_count: 0
  slug: addx-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Addx Rate Limits
  slug: addx-rate-limits
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 29.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/addx/addx-2026-10-11T092759.png
security:
- kind: authentication
  name: Addx Authentication
  slug: addx-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Addx Domain Security
  slug: addx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: addx
tags:
- Digital Securities Exchange
- Private Markets
- Tokenization
- Alternative Investments
- Wealth Management
- Capital Markets
- Fintech
- Digital Assets
- Investment Platform
- Singapore
website: https://addx.co/
---
