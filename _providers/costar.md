---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
  scored_at: '2026-09-04'
api_count: 14
apis:
- description: CoStar's flagship commercial real estate information platform covering property, tenant, lease, sale, and market analytics across office, industrial, retail, multifamily, and specialty CRE asset class
  name: CoStar Commercial Real Estate Platform
  slug: costar
- description: The largest commercial real estate marketplace in the United States, surfacing CRE listings for sale and lease alongside CoStar-sourced analytics.
  name: LoopNet
  slug: loopnet
- description: Residential rental marketplace network including Apartments.com, ForRent.com, and Westside Rentals, providing listings, leads, and advertising to multifamily owners and managers.
  name: Apartments.com Network
  slug: apartments-com
- description: Residential for-sale and rental marketplace operating agent-first branding and search, paired with the Homesnap mobile and agent tooling.
  name: Homes.com
  slug: homes-com
- description: Mobile residential real estate search and agent productivity application that integrates with MLSs and Homes.com.
  name: Homesnap
  slug: homesnap
- description: Online commercial real estate transaction and auction platform for buyers and sellers of CRE assets.
  name: Ten-X
  slug: ten-x
- description: Online marketplace for buying and selling small and mid-sized businesses, with broker tools and financing partners.
  name: BizBuySell
  slug: bizbuysell
- description: Hotel benchmarking, performance data, and analytics provider serving the global lodging industry.
  name: STR (Smith Travel Research)
  slug: str
- description: Lease management and lease accounting platform for corporate and real estate tenants.
  name: Visual Lease
  slug: visual-lease
- description: 3D spatial data capture platform used to digitise real estate, retail, and built-environment spaces, integrated across CoStar's marketplaces.
  name: Matterport
  slug: matterport
- description: UK residential property portal acquired by CoStar Group, providing for sale and to let listings with agent tooling.
  name: OnTheMarket
  slug: onthemarket
- description: Global building data and imagery provider covering high-rise and commercial structures.
  name: Emporis
  slug: emporis
- description: Australian residential real estate marketplace and media company in which CoStar Group acquired a majority stake.
  name: Domain Group
  slug: domain-group
- description: Land-for-sale marketplace network covering rural, ranch, recreational, and development land in the United States.
  name: Land.com / Lands of America
  slug: lands-of-america
artifact_total: 19
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/costar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/costar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.costargroup.com
- group: commercial
  title: ''
  type: CoStar
  url: https://www.costar.com
- group: company
  title: ''
  type: Investors
  url: https://www.costargroup.com/investors
- group: company
  title: ''
  type: News
  url: https://www.costargroup.com/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/costar-group/
created: '2026-05-23'
description: CoStar Group is the dominant commercial and residential real estate data, analytics, and marketplace company. The portfolio spans the flagship CoStar commercial real estate intelligence platform, LoopNet (CRE marketplace), Apartments.com network (residential rentals, including ForRent.com and Westside Rentals), Homes.com and Homesnap (for-sale residential), Ten-X (online CRE auctions), BizBuySell (business-for-sale marketplace), STR (hotel data), Visual Lease (lease management), Matterport (3D spatial capture), and international properties including OnTheMarket (UK), Emporis (Germany), and a controlling stake in Domain Group (Australia). Distribution to partners is via enterprise data licensing, syndication feeds, and brand-specific marketplace tooling rather than a public self-serve developer portal.
finops:
- name: Costar Finops
  service_category: API
  slug: costar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/costar.png
layout: provider
modified: '2026-05-23'
name: CoStar Group
nav: Providers
network: true
overview: 'CoStar Group publishes 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Commercial Real Estate, Residential Real Estate, Real Estate Data, Marketplaces, and Analytics.


  CoStar Group''s developer surface includes product news and 6 more developer resources.'
plans:
- name: Costar Plans Pricing
  plan_count: 1
  slug: costar-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Costar Rate Limits
  slug: costar-rate-limits
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/costar/refs/heads/main/screenshots/costar-2026-06-20T175051.png
security:
- kind: domain-security
  name: Costar Domain Security
  slug: costar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Costar Trust Center
  slug: costar-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: costar
tags:
- Commercial Real Estate
- Residential Real Estate
- Real Estate Data
- Marketplaces
- Analytics
- Listings
- PropTech
website: https://www.costargroup.com
---
