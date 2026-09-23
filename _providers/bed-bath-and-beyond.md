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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: Seller-facing API for the Bed Bath & Beyond third-party marketplace, which runs as a tenant of the Mirakl Marketplace Platform at bedbathandbeyondus-prod.mirakl.net. Approved sellers generate a Shop A
  name: Bed Bath & Beyond Marketplace Seller API
  slug: bed-bath-beyond-marketplace-seller-api
artifact_total: 10
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/security/bed-bath-and-beyond-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bed-bath-and-beyond-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/security/bed-bath-and-beyond-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bed-bath-and-beyond-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/well-known/bed-bath-and-beyond-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bed-bath-and-beyond-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/well-known/bed-bath-and-beyond-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bed-bath-and-beyond-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/security/bed-bath-and-beyond-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bed-bath-and-beyond-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/llms/bed-bath-and-beyond-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bed-bath-and-beyond-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/plans/bed-bath-and-beyond-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bed-bath-and-beyond-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/rate-limits/bed-bath-and-beyond-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bed-bath-and-beyond-rate-limits.yml
- group: company
  title: Partner (marketplace seller) program
  type: Partners
  url: https://www.bedbathandbeyond.com/partner
- group: operate
  title: Customer Care Help Center
  type: Support
  url: https://help.bedbathandbeyond.com/help/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.bedbathandbeyond.com/help/s/article/TERMS-AND-CONDITIONS
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.bedbathandbeyond.com/help/s/article/PRIVACY-AND-SECURITY-POLICY
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bed-bath-and-beyond
- group: company
  title: ''
  type: Website
  url: https://www.bedbathandbeyond.com
- group: company
  title: Beyond Inc. (Parent Company)
  type: Website
  url: https://www.beyond.com
- group: other
  title: Marketplace Seller Program
  type: Marketplace
  url: https://help.bedbathandbeyond.com/help/s/article/Overstock-Marketplace
coverage:
  checked: '2026-09-18'
  detail: The only API is a Mirakl-tenant marketplace seller API at bedbathandbeyondus-prod.mirakl.net (GET /api/version answers publicly, every other resource 401s) whose Shop API key is issued in the seller portal only after the partner application form at bedbathandbeyond.com/partner is reviewed; the contract is Mirakl's vendor specification and Bed Bath & Beyond publishes no developer documentation of its own.
  evidence:
  - status: 200
    url: https://www.bedbathandbeyond.com/partner
  - status: 200
    url: https://bedbathandbeyondus-prod.mirakl.net/api/version
  - status: 401
    url: https://bedbathandbeyondus-prod.mirakl.net/api/offers
  - status: 404
    url: https://www.bedbathandbeyond.com/developers
  reason: sales-gate
  state: gated
created: '2026-03-23'
description: Bed Bath & Beyond was a chain of domestic merchandise retail stores selling home furnishings, bedding, kitchenware, and other home goods. The company filed for Chapter 11 bankruptcy in April 2023. The brand was subsequently acquired by Beyond Inc. (formerly Overstock.com), which relaunched Bed Bath & Beyond as an online retail destination. Beyond Inc. also owns Overstock, buybuy BABY, and related brands.
features:
- description: Bed Bath & Beyond operates as an online-only retail destination following the 2023 bankruptcy and brand acquisition by Beyond Inc.
  name: Online Retail
- description: Third-party sellers can list products through the Bed Bath & Beyond marketplace, integrated via Rithum (formerly CommerceHub).
  name: Marketplace
- description: Supplier integrations use X12 EDI documents transmitted through value-added networks, including EDI 850 purchase orders, EDI 856 advance ship notices, and EDI 846 inventory feeds.
  name: EDI Integration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bed-bath-and-beyond.png
layout: provider
modified: '2026-09-18'
name: Bed Bath And Beyond
nav: Providers
network: true
overview: 'Bed Bath And Beyond publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bedding, Beyond, E-Commerce, Home Goods, and Kitchenware.


  Bed Bath And Beyond''s developer surface includes support and 15 more developer resources.'
plans:
- name: Bed Bath And Beyond Plans Pricing
  plan_count: 0
  slug: bed-bath-and-beyond-plans-pricing
press:
- date: ''
  title: Bed Bath & Beyond to Cut Headcount with AI Integration
  url: https://www.linkedin.com/posts/paul-young-055632b_bed-bath-beyond-ceo-ai-will-lead-to-significant-activity-7454940752268288000-uCFl
- date: ''
  title: Letter to Shareholders and Stakeholders from Marcus ...
  url: https://investors.beyond.com/news-events/press-releases/news-details/2026/Letter-to-Shareholders-and-Stakeholders-from-Marcus-Lemonis-Executive-Chairman-and-Chief-Executive-Officer-of-Bed-Bath--Beyond/default.aspx
- date: ''
  title: Bed Bath & Beyond hires Kyla Robinson as tech chief
  url: https://www.stocktitan.net/news/BBBY/bed-bath-beyond-appoints-kyla-robinson-to-lead-technology-zeo6fey1p452.html
- date: ''
  title: Bed Bath & Beyond Appoints Kyla Robinson to Lead ...
  url: https://www.businesswire.com/news/home/20260427725853/en/Bed-Bath-Beyond-Appoints-Kyla-Robinson-to-Lead-Technology-Transformation-Across-Everything-Home
- date: ''
  title: Bed Bath & Beyond CEO sends stark AI warning to workers
  url: https://sg.finance.yahoo.com/news/bed-bath-beyond-ceo-sends-150700273.html
random_paper: 15
rate_limits:
- limit_count: 0
  name: Bed Bath And Beyond Rate Limits
  slug: bed-bath-and-beyond-rate-limits
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    operational_transparency: 10.5
  previous_composite: 18.7
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/bed-bath-and-beyond/refs/heads/main/screenshots/bed-bath-and-beyond-2026-06-20T173120.png
security:
- kind: domain-security
  name: Bed Bath And Beyond Domain Security
  slug: bed-bath-and-beyond-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bed Bath And Beyond Vulnerability Disclosure
  slug: bed-bath-and-beyond-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bed-bath-and-beyond
tags:
- Bedding
- Beyond
- E-Commerce
- Home Goods
- Kitchenware
- Marketplace
- Retail
use_cases:
- description: Third-party vendors can list and sell products on the Bed Bath & Beyond marketplace by integrating through approved channel management platforms.
  name: Marketplace Selling
- description: Suppliers submit catalog data, receive purchase orders, and send shipment notifications via EDI through the vendor portal.
  name: Supplier Integration
website: https://www.bedbathandbeyond.com
---
