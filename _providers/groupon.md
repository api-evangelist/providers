---
access_model:
  confidence: medium
  label: Partner / merchant signup; no published API pricing or self-serve key issuance
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.groupon.com/developers/signup
  - plans/groupon-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 10.1
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'Groupon''s own public API gateway. Live and Groupon-operated (responses carry x-brand: groupon and Envoy/GCP upstream headers), but gated: every path, including /v2/deals.json, /graphql and /.well-know'
  name: Groupon API
  slug: groupon-api
- description: 'REST contract for wellness, beauty and services booking systems. Groupon polls the partner''s system roughly every 60 minutes to cache merchants, services, staff and availability, performs a real-time '
  name: Groupon Bookable Appointments API
  slug: groupon-bookable-appointments-api
- description: REST contract connecting a tours, activities and attractions reservation system to Groupon's point of sale, covering availability, reservation creation and retrieval, cancellation and redemption. As w
  name: Groupon Tours and Attractions API
  slug: groupon-tours-and-attractions-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.groupon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.groupon.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.groupon.com/developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.groupon.com/developers/api-reference
- group: start
  title: ''
  type: SignUp
  url: https://www.groupon.com/developers/signup
- group: operate
  title: ''
  type: Support
  url: https://www.groupon.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.groupon.com/legal/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.groupon.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/groupon-eng
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/groupon-eng
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/groupon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/groupon
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groupon-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/groupon-robots.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/groupon-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/groupon-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groupon-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groupon-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/groupon-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/groupon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/groupon-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groupon-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/groupon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/groupon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groupon-domain-security.yml
created: '2026-03-24'
description: 'Groupon is a local-commerce marketplace, founded in Chicago in 2008, where people discover and book discounted experiences, services, goods and travel — things to do, food and drink, beauty and spas, health and fitness, home and auto services, retail goods, getaways and retailer coupons. Its developer surface is a partner and merchant integration programme rather than a public product API: the Groupon Developer Platform publishes REST contracts for Bookable Appointments, Tours and Attractions, Goods Marketplace inventory and point-of-sale redemption, which partner booking and reservation systems implement so Groupon can poll availability, create reservations and signal redemptions. A separate Groupon-operated API gateway runs at api.groupon.com and requires a client_id on every request. The Groupon Partner Network affiliate reporting APIs were permanently closed on 2022-06-15.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groupon.png
layout: provider
modified: '2026-09-04'
name: Groupon
nav: Providers
network: true
overview: 'Groupon publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Local Commerce, Marketplace, E-Commerce, and Deals.


  Groupon''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Groupon Plans Pricing
  plan_count: 0
  slug: groupon-plans-pricing
press:
- date: '2026-05-25'
  title: Groupon adds Amit Shah, forms board AI committee
  url: https://www.stocktitan.net/news/GRPN/groupon-launches-board-level-artificial-intelligence-committee-and-k5ofroarr4yj.html
- date: '2026-05-25'
  title: META_TITLE_QUOTE
  url: https://finance.yahoo.com/quote/GRPN/press-releases/
- date: '2026-05-25'
  title: Groupon, Inc. - Home
  url: https://investor.groupon.com/home/default.aspx
- date: '2026-05-25'
  title: Press Release Details
  url: https://investor.groupon.com/press-releases/press-release-details/2026/Groupon-Launches-Board-Level-Artificial-Intelligence-Committee-and-Appoints-Amit-Shah-to-Board-of-Directors/default.aspx
- date: '2026-05-25'
  title: Groupon, Inc. - Press Releases
  url: https://investor.groupon.com/press-releases/default.aspx
random_paper: 1
rate_limits:
- limit_count: 0
  name: Groupon Rate Limits
  slug: groupon-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 2.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/groupon/refs/heads/main/screenshots/groupon-2026-06-20T182418.png
security:
- kind: authentication
  name: Groupon Authentication
  slug: groupon-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Groupon Domain Security
  slug: groupon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Groupon Vulnerability Disclosure
  slug: groupon-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: groupon
tags:
- Fortune 1000
- Local Commerce
- Marketplace
- E-Commerce
- Deals
- Bookings
- Reservations
- Travel
- Retail
website: https://www.groupon.com
---
