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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Partner-gated REST API for submitting buyer and seller leads to HomeLight, submitting Simple Sale cash-offer seller leads, and checking for duplicate leads before submission. Authentication is via a p
  name: HomeLight Partner API
  slug: homelight-partner-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homelight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.homelight.com
- group: other
  title: ''
  type: Company
  url: https://www.homelight.com/about
- group: company
  title: ''
  type: Press
  url: https://www.homelight.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.homelight.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.homelight.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.homelight.com/blog
- group: other
  title: ''
  type: Agents
  url: https://www.homelight.com/agents
- group: other
  title: ''
  type: SimpleSale
  url: https://www.homelight.com/simple-sale
- group: other
  title: ''
  type: BuyBeforeYouSell
  url: https://www.homelight.com/buy-before-you-sell
- group: other
  title: ''
  type: HomeLoans
  url: https://www.homelight.com/home-loans
- group: other
  title: ''
  type: HELOC
  url: https://www.homelight.com/heloc
- group: other
  title: ''
  type: ClosingServices
  url: https://www.homelight.com/closing-services
- group: other
  title: ''
  type: Lenders
  url: https://lender.homelight.com/partners
- group: company
  title: ''
  type: PartnerAPI
  url: https://www.homelight.com/api_docs/partners
- group: build
  title: ''
  type: GitHub
  url: https://github.com/homelight
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/homelight
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HomeLight
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/HomeLight
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@HomeLight
- group: operate
  title: ''
  type: Support
  url: mailto:support@homelight.com
created: '2026-05-25'
description: 'HomeLight is a San Francisco–based real-estate technology company that matches home buyers and sellers with top-performing local real-estate agents and operates a stack of consumer-facing products that span the entire residential transaction: agent matching, Simple Sale cash-offer marketplace, Buy Before You Sell (BBYS) bridge financing, HomeLight Home Loans (NMLS #1529229), the HomeLight HELOC Card, and HomeLight Closing Services for title and escrow. The company ranks agents using historical performance data on home sales (price, speed, volume, geography, property type) and routes consumer leads to a curated network of agents, lenders, and cash-buyer investors. HomeLight exposes a private Partner API to lenders, brokerages, CRMs, and marketing partners (NerdWallet is its largest partner) for submitting leads (`/api/partner_lead/v2`), Simple Sale seller leads (`/leads/partner_simple_sale_lead`), and duplicate-lead checks (`/api/partner_dupe_lead_check`); credentials are issued
  on a per-partner basis via support@homelight.com. Beyond the Partner API, HomeLight has direct integrations with most major real-estate agent CRMs (Follow Up Boss, BoomTown, Sierra Interactive, Firepoint, Real Geeks, Brivity, Chime, LionDesk, KW Command). HomeLight has no public, self-service developer portal — the Partner API is gated by a commercial relationship, and there is no public OpenAPI spec, SDK, or open-source client published by the company.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/homelight.png
layout: provider
modified: '2026-05-25'
name: HomeLight
nav: Providers
network: true
overview: 'HomeLight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, PropTech, Agent Matching, Cash Offers, and iBuyer.


  HomeLight''s developer surface includes engineering blog, GitHub presence, YouTube channel, support, and 17 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/homelight/refs/heads/main/screenshots/homelight-2026-06-20T182818.png
security:
- kind: domain-security
  name: Homelight Domain Security
  slug: homelight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: homelight
tags:
- Real-Estate
- PropTech
- Agent Matching
- Cash Offers
- iBuyer
- Bridge Loans
- Buy Before You Sell
- Home Loans
- HELOC
- Title and Escrow
- Closing Services
- Lead Generation
- Partner API
- Mortgage
- Residential Real Estate
website: https://www.homelight.com
---
