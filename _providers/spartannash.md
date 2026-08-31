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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spartannash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spartannash.com/
- group: company
  title: ''
  type: Blog
  url: https://www.spartannash.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spartannash
- group: operate
  title: ''
  type: Support
  url: https://www.spartannash.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spartannash.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spartannash.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpartanNash-Company
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spartannash-llms.txt
coverage:
  checked: '2026-08-26'
  detail: SpartanNash publishes no developer surface at all — there is no developer. or api. subdomain (both fail DNS), every spec path on the corporate host 404s, the vendor-integration page now 301s to the C&S Wholesale Grocers parent site where supplier onboarding is EDI-only, and the SpartanNash GitHub orgs hold one 2016 JavaScript widget between them.
  evidence:
  - status: 0
    url: https://api.spartannash.com/openapi.json
  - status: 0
    url: https://developer.spartannash.com/openapi.json
  - status: 404
    url: https://www.spartannash.com/openapi.json
  - status: 404
    url: https://www.spartannash.com/.well-known/api-catalog
  - status: 301
    url: https://www.spartannash.com/wholesale/vendor/
  - status: 200
    url: https://www.spartannash.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/SpartanNash/repos
  reason: no-developer-program
  state: none
created: '2026-07-22'
description: SpartanNash is a Byron Center, Michigan food solutions company that operates as both a wholesale grocery distributor and a retail grocer. Its wholesale segment supplies roughly 2,100 independent retail locations, national accounts and e-commerce partners from a network of distribution centers, and through its MDV business it is the leading distributor of grocery products to United States military commissaries and exchanges worldwide. Its retail segment operates roughly 200 corporate-owned supermarkets under banners including Family Fare, Martin's Super Markets, D&W Fresh Market, VG's Grocery, Dan's Supermarket, Family Fresh Market, Needler's Fresh Market, Fresh City Market, Forest Hills Foods and Supermercado Nuestra Familia, alongside pharmacy and fuel centers. Formed by the 2013 merger of Spartan Stores and Nash Finch, the company traded on Nasdaq as SPTN until C&S Wholesale Grocers completed its acquisition of SpartanNash on September 22, 2025; SpartanNash now operates as
  part of C&S and its corporate web properties are progressively being folded into cswg.com. SpartanNash publishes no public developer program, API documentation or machine-readable API contract; supplier and customer system integration is transacted over EDI through trading-partner onboarding rather than a public API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spartannash.png
layout: provider
modified: '2026-08-26'
name: SpartanNash
nav: Providers
network: true
overview: 'SpartanNash is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Grocery, Food Distribution, Wholesale, and Retail.


  SpartanNash''s developer surface includes engineering blog, support, and 7 more developer resources.'
press:
- date: '2026-05-25'
  title: SpartanNash Bolsters Fresh Departments Using Artificial ...
  url: http://www.b2i.us/profiles/investor/NewsPrint.asp?b=1679&ID=114515&m=rl&v=2
- date: '2026-05-25'
  title: SpartanNash Welcomes Binu Varghese as Vice President ...
  url: https://corporate.spartannash.com/2023-05-02-SpartanNash-Welcomes-Binu-Varghese-as-Vice-President,-Applications-and-Data
- date: '2026-05-25'
  title: SpartanNash dials up its tech talent efforts
  url: https://www.grocerydive.com/news/spartannash-technology-labor-workers/728278/
- date: '2026-05-25'
  title: SpartanNash Leveraging AI Technology to Predict ...
  url: https://www.prnewswire.com/news-releases/spartannash-leveraging-ai-technology-to-predict-shopper-demand-decrease-waste-301918073.html
- date: '2026-05-25'
  title: SpartanNash to Test AI-Powered Inventory Technology
  url: https://www.specialtyfood.com/news-media/news-features/specialty-food-news/spartannash-to-test-ai-powered-inventory-technology/
random_paper: 11
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 11.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Spartannash Domain Security
  slug: spartannash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spartannash
tags:
- Fortune 500
- Grocery
- Food Distribution
- Wholesale
- Retail
- Supply Chain
- Military Commissary
- Logistics
- Consumer Goods
- Michigan
website: https://www.spartannash.com/
---
