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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-tire-distributors-holdings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-tire-distributors
- group: company
  title: ''
  type: Website
  url: https://www.atd.com
- group: start
  title: ''
  type: Portal
  url: https://atdonline.com/login
- group: start
  title: ''
  type: SignUp
  url: https://atdonline.com/register
- group: operate
  title: ''
  type: Support
  url: https://www.atd.com/contactus/
- group: company
  title: ''
  type: Blog
  url: https://www.atd.com/about-us/articles/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atd.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atd.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-tire-distributors-holdings-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/american-tire-distributors-holdings-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/american-tire-distributors-holdings-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/american-tire-distributors-holdings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/american-tire-distributors-holdings-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: ATD runs a real dropship/inventory partner API that every major integration platform connects to, but it publishes no developer site at all - api., developer. and developers. subdomains of atd.com and atd-us.com do not resolve, atdonline.com 302s every path including /openapi.json and /.well-known/* to /login, and the reference plus the API key and secret are handed out by an ATD representative only to an approved dealer.
  evidence:
  - status: 302
    url: https://atdonline.com/openapi.json
  - status: 404
    url: https://www.atd.com/.well-known/api-catalog
  - status: 404
    url: https://www.atd.com/login
  - status: 302
    url: https://customer.atd-us.com/.well-known/openid-configuration
  - status: 200
    url: https://atdonline.com/register
  reason: customer-only-docs
  state: gated
created: '2024-11-15'
description: American Tire Distributors (ATD) is one of the largest independent suppliers of replacement tires in North America, distributing passenger, light truck, medium truck, and specialty tires from more than 110 distribution centers. ATD delivers over 30.5 million tire units annually to more than 85,000 delivery points across the United States and Canada, serving independent tire dealers, automotive service centers, and retailers.
features:
- description: Distribution of 16,500+ active tire products across 110+ distribution centers with 1,400+ delivery vehicles serving over 85,000 delivery points nationwide.
  name: Tire Distribution Network
- description: Digital ordering and account management portal for tire dealers to browse inventory, place orders, track deliveries, and manage accounts online.
  name: ATDOnline Customer Portal
- description: Data-driven tire recommendation engine helping dealers optimize inventory selection and improve same-day sales performance.
  name: Inventory Recommendation Engine
- description: Nationwide next-day tire delivery capabilities from strategically located distribution centers to maximize tire dealer inventory efficiency.
  name: Next-Day Delivery
- description: Full-service business support including strategic planning, marketing resources, and operational guidance for independent tire dealer customers.
  name: Dealer Business Support
- description: Distribution of specialty tires including medium truck, farm, recreational vehicle, and off-the-road tires alongside standard passenger and light truck products.
  name: Specialty and Commercial Tires
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-tire-distributors-holdings.png
integrations:
- description: Integration with tire dealer management systems for automated inventory ordering, price updates, and order tracking through ATD's digital platform.
  name: Dealer Management Systems
- description: Connectivity with dealer point-of-sale and service management software for real-time inventory availability and order placement.
  name: Point-of-Sale Systems
layout: provider
modified: '2026-04-19'
name: American Tire Distributors Holdings
nav: Providers
network: true
overview: 'American Tire Distributors Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tires, Automotive, Distribution, Wholesale, and Supply Chain.


  American Tire Distributors Holdings'' developer surface includes developer portal, signup flow, support, engineering blog, authentication, and 9 more developer resources.'
plans:
- name: American Tire Distributors Holdings Plans Pricing
  plan_count: 0
  slug: american-tire-distributors-holdings-plans-pricing
press:
- date: '2026-05-25'
  title: Recovering auto sales may spur supplier deals, drawing Ross, ...
  url: https://www.autonews.com/article/20100525/COPY/305259996/recovering-auto-sales-may-spur-supplier-deals-drawing-ross-icahn/
- date: '2026-05-25'
  title: Automotive ECommerce Market Will Hit Big Revenues in ...
  url: https://www.openpr.com/news/3843861/automotive-ecommerce-market-will-hit-big-revenues-in-future
- date: '2026-05-25'
  title: Ari Lanin
  url: https://www.gibsondunn.com/lawyer/lanin-ari/?pdf=display
- date: '2026-05-25'
  title: Contracts - API Evangelist Contracts
  url: https://contracts.apievangelist.com/
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1838163/000149315224024559/forms-1.htm
random_paper: 15
rate_limits:
- limit_count: 0
  name: American Tire Distributors Holdings Rate Limits
  slug: american-tire-distributors-holdings-rate-limits
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 11
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
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-tire-distributors-holdings/refs/heads/main/screenshots/american-tire-distributors-holdings-2026-06-20T171922.png
security:
- kind: authentication
  name: American Tire Distributors Holdings Authentication
  slug: american-tire-distributors-holdings-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: American Tire Distributors Holdings Domain Security
  slug: american-tire-distributors-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-tire-distributors-holdings
tags:
- Tires
- Automotive
- Distribution
- Wholesale
- Supply Chain
- Logistics
use_cases:
- description: Providing independent tire dealers with just-in-time tire inventory replenishment from local distribution centers to minimize on-hand stock requirements.
  name: Independent Tire Dealer Supply
- description: Supplying automotive service chains, quick-lube centers, and dealerships with replacement tires to support their vehicle service operations.
  name: Automotive Service Center Inventory
- description: Supplying medium truck and commercial tires for fleet maintenance operations and commercial vehicle service providers.
  name: Commercial Fleet Tire Management
- description: Supporting retailers and buying groups with private-label tire programs and branded tire distribution across national accounts.
  name: Retail Tire Program Management
website: https://www.atd.com
---
