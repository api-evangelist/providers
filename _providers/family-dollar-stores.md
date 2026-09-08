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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/family-dollar-stores-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Family-Dollar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/family-dollar
- group: company
  title: ''
  type: Website
  url: https://www.familydollar.com
- group: company
  title: ''
  type: About
  url: https://corporate.familydollar.com/about-us
- group: company
  title: ''
  type: Partners
  url: https://corporate.familydollar.com/vendor-resources
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.familydollar.com/about-us/pressroom
- group: company
  title: ''
  type: InvestorRelations
  url: https://corporate.familydollar.com/financial-reports
- group: other
  title: ''
  type: Store Locator
  url: https://www.familydollar.com/locations/
- group: company
  title: ''
  type: Careers
  url: https://www.familydollar.com/careers/
- group: other
  title: ''
  type: Mobile App
  url: https://www.familydollar.com/smart-coupons/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.familydollar.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.familydollar.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://www.familydollar.com/contact-family-dollar
- group: operate
  title: ''
  type: Support
  url: https://www.familydollar.com/faq-general
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/family-dollar-stores-llms.txt
coverage:
  checked: '2026-09-07'
  detail: Family Dollar runs a consumer storefront and mobile app but ships no developer surface at all - api.familydollar.com and developer.familydollar.com do not resolve, the full static sitemaps of both www.familydollar.com (118 pages) and the standalone corporate site (12 pages) contain no developer-facing page, and every /.well-known/ and specification path returned 404; supplier integration is routed through the SAP Ariba Network vendor portal that Family Dollar buys rather than an interface it publishes.
  evidence:
  - status: 404
    url: https://www.familydollar.com/.well-known/api-catalog
  - status: 404
    url: https://www.familydollar.com/openapi.json
  - status: 404
    url: https://corporate.familydollar.com/.well-known/agent-card.json
  - status: 200
    url: https://www.familydollar.com/staticSitemap.xml
  - status: 200
    url: https://corporate.familydollar.com/vendor-resources
  reason: no-developer-program
  state: none
created: '2024-12-25'
description: 'Family Dollar is a chain of discount variety stores in the United States offering a broad assortment of merchandise in the $1 to $10 range, including consumables, household and home products, apparel, seasonal goods and electronics. Stores are concentrated in neighborhood locations and in food deserts where other retailers do not operate. Dollar Tree, Inc. divested the Family Dollar business on 7 July 2025 to Brigade Capital Management and Macellum Capital Management; Family Dollar now operates as a standalone private retailer headquartered in Chesapeake, Virginia, and also runs the Chesapeake Media Group retail media network. Family Dollar publishes no public API, developer portal, SDK, webhook catalog or agent surface: contract discovery on 2026-09-07 probed every well-known and specification path across www.familydollar.com, corporate.familydollar.com and careers.familydollar.com and returned no machine-readable contract of any kind.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/family-dollar-stores.png
layout: provider
modified: '2026-09-07'
name: Family Dollar Stores
nav: Providers
network: true
overview: 'Family Dollar Stores is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Discount Stores, Variety Stores, Consumer Goods, and E-Commerce.


  Family Dollar Stores'' developer surface includes support and 15 more developer resources.'
plans:
- name: Family Dollar Stores Plans Pricing
  plan_count: 0
  slug: family-dollar-stores-plans-pricing
press:
- date: '2026-05-25'
  title: Family Dollar Turns to AI Platform to Localize Product Assortment
  url: https://p2pi.com/family-dollar-turns-ai-platform-localize-product-assortment
- date: '2026-05-25'
  title: Chesapeake-based Dollar Tree completes sale of Family ...
  url: https://www.pilotonline.com/2025/07/07/dollar-tree-completes-family-dollar-sale/
- date: '2026-05-25'
  title: Family Dollar Highlights Strong Fiscal 2025 Performance ...
  url: https://www.prnewswire.com/news-releases/family-dollar-highlights-strong-fiscal-2025-performance-as-transformation-strengthens-business-302715979.html
- date: '2026-05-25'
  title: ANNUAL REPORT 2024
  url: https://corporate.dollartree.com/investors/sec-filings/content/0000935703-25-000017/ars2024dltr.pdf
- date: '2026-05-25'
  title: Why is Dollar Tree sign removed from Family Dollar?
  url: https://www.facebook.com/groups/615443083940178/posts/1194301942720953/
random_paper: 5
rate_limits:
- limit_count: 0
  name: Family Dollar Stores Rate Limits
  slug: family-dollar-stores-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/family-dollar-stores/refs/heads/main/screenshots/family-dollar-stores-2026-06-20T181033.png
security:
- kind: domain-security
  name: Family Dollar Stores Domain Security
  slug: family-dollar-stores-domain-security
  summary_line: TLSv1.3 · DMARC
slug: family-dollar-stores
tags:
- Retail
- Discount Stores
- Variety Stores
- Consumer Goods
- E-Commerce
- United States
- Fortune 500
website: https://www.familydollar.com
---
