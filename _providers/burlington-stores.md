---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'Burlington''s consumer storefront: shopping, store locator, gift cards, loyalty and credit card servicing. No public API is published behind it. Every /.well-known/ path, /openapi.json and /llms.txt on'
  name: Burlington Stores
  slug: burlington-stores-website
- description: Burlington's ASC X12 version 4010 EDI trading-partner interface — the company's only documented machine-to-machine surface. Seventeen implementation guides are published as public PDFs with sample int
  name: Burlington Stores EDI
  slug: burlington-stores-edi
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.burlington.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/burlington-stores
- group: operate
  title: ''
  type: Support
  url: https://www.burlington.com/helpcenter/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.burlington.com/helpcenter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.burlington.com/helpcenter/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.burlington.com/helpcenter/privacy-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/burlington-stores-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/burlington-stores-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/burlington-stores-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/burlington-stores-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/burlington-stores-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: Burlington runs no developer program at all — every /.well-known/ path, /openapi.json and /llms.txt on www.burlington.com returns HTTP 200 carrying the site's Next.js shell titled '404 Not Found | Burlington' (a control path that cannot exist returns the same body), and vendors.burlington.com and edi.coat.com return honest 404s for all of them; the only documented machine-to-machine surface is ASC X12 4010 EDI, whose seventeen implementation guides ARE public at burlington.com/vendors/edi but which is batch interchange behind an invite-only Gateway login, not an API.
  evidence:
  - status: 200
    url: https://www.burlington.com/openapi.json
  - status: 200
    url: https://www.burlington.com/zzz-definitely-not-a-page-12345
  - status: 404
    url: https://vendors.burlington.com/.well-known/agent-card.json
  - status: 404
    url: https://edi.coat.com/openapi.json
  - status: 200
    url: https://www.burlington.com/vendors/edi
  - status: 200
    url: https://cdn.sanity.io/files/k5c6l842/production/7e549f9134cb3625b47e650ef36dfadca0ca8ce3.pdf
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'Burlington Stores, Inc. (NYSE: BURL) is a US national off-price department store retailer offering brand-name clothing, footwear, accessories, baby products and home decor at everyday low prices across more than 1,200 stores. Burlington operates no public developer program: no OpenAPI, GraphQL, gRPC, SOAP or event contract is served on any host it controls. Its one documented machine-to-machine surface is ASC X12 version 4010 EDI for merchandise vendors and freight carriers, and unusually for a retailer of this size the implementation guides are fully public — seventeen transaction-set PDFs plus a GS1-128 shipping label companion report, readable without a login at burlington.com/vendors/edi. The runtime behind them, the Gateway Vendor Management Suite, is invite-only.'
finops:
- name: Burlington Stores Finops
  service_category: Retail / Off-Price Department Store
  slug: burlington-stores-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/burlington-stores.png
layout: provider
modified: '2026-09-05'
name: Burlington Stores
nav: Providers
network: true
overview: 'Burlington Stores publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Company, E-Commerce, Apparel, and Home Decor.


  Burlington Stores'' developer surface includes support and 10 more developer resources.'
plans:
- name: Burlington Stores Plans Pricing
  plan_count: 0
  slug: burlington-stores-plans-pricing
press:
- date: '2026-05-25'
  title: Nvidia Lower; Snowflake and Burlington Gain | Stock Movers
  url: https://www.youtube.com/watch?v=6oeXQD0lHKc
- date: '2026-05-25'
  title: Burlington's 'reimagined' store layout aims to make ...
  url: https://www.retaildive.com/news/burlington-store-refresh-initiative/757878/
- date: '2026-05-25'
  title: 'Earnings call transcript: Burlington Stores beats Q4 2025 ...'
  url: https://www.investing.com/news/transcripts/-93CH-4544612
- date: '2026-05-25'
  title: Burlington Unveils Reimagined Store Experience with ...
  url: https://www.prnewswire.com/news-releases/burlington-unveils-reimagined-store-experience-with-special-celebrations-across-21-markets-302526701.html
- date: '2026-05-25'
  title: AI Data Scientist
  url: https://burlingtonstores.jobs/edgewater-park-nj/ai-data-scientist/082546BFFE0B470D9805F15D5CE0AE3C/job/
random_paper: 3
rate_limits:
- limit_count: 0
  name: Burlington Stores Rate Limits
  slug: burlington-stores-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 7.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/burlington-stores/refs/heads/main/screenshots/burlington-stores-2026-06-20T173818.png
security:
- kind: domain-security
  name: Burlington Stores Domain Security
  slug: burlington-stores-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: burlington-stores
tags:
- Retail
- Company
- E-Commerce
- Apparel
- Home Decor
- Fortune 1000
website: https://www.burlington.com
---
