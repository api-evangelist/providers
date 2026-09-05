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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sea-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sea-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sea.com/
- group: company
  title: ''
  type: About
  url: https://www.sea.com/about
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.sea.com/investor
- group: company
  title: ''
  type: News
  url: https://www.sea.com/news
- group: company
  title: ''
  type: Careers
  url: https://career.sea.com/
- group: other
  title: ''
  type: Sustainability
  url: https://www.sea.com/sustainability
- group: other
  title: ''
  type: ShopeeBusiness
  url: https://shopee.com/
- group: other
  title: ''
  type: ShopeeOpenPlatform
  url: https://open.shopee.com/
- group: other
  title: ''
  type: GarenaBusiness
  url: https://www.garena.com/
- group: other
  title: ''
  type: SeaMoneyBusiness
  url: https://www.seamoney.com/
- group: other
  title: ''
  type: ShopeePay
  url: https://shopeepay.co.id/
- group: other
  title: ''
  type: SeaBank
  url: https://seabank.co.id/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sea-group/
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Subsidiaries
  url: ''
created: '2026-05-23'
description: 'Sea Limited is a Singapore-headquartered consumer internet holding company that operates three core businesses across Southeast Asia, Taiwan, and Latin America: Shopee (e-commerce), Garena (digital entertainment and game publishing), and SeaMoney / Monee (digital financial services including SeaBank, ShopeePay, and SPayLater). Sea Limited is publicly listed on the NYSE (ticker: SE). Sea does not publish a unified group-level developer API — each operating subsidiary maintains its own developer platform: Shopee Open Platform (open.shopee.com) for marketplace integrations, Garena for game-platform partners, and SeaMoney / ShopeePay for in-region payment integrations.'
features:
- description: Sea Limited operates three independent consumer internet businesses (Shopee, Garena, SeaMoney) under one holding company.
  name: Multi-Brand Operating Holding
- description: Operates across Singapore, Indonesia, Malaysia, Philippines, Thailand, Vietnam, Taiwan, and select markets in Latin America (Brazil) and Europe.
  name: Southeast Asia Footprint
- description: Cross-platform integration where ShopeePay powers payments in Shopee and Garena, and SPayLater extends consumer credit across the ecosystem.
  name: Integrated Ecosystem
- description: Listed on the New York Stock Exchange under ticker SE since 2017.
  name: Public Company
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sea-group.png
layout: provider
modified: '2026-05-23'
name: Sea Group (Sea Limited)
nav: Providers
network: true
overview: 'Sea Group (Sea Limited) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Holding Company, Southeast Asia, E-Commerce, Digital Entertainment, and Financial-Services.


  Sea Group (Sea Limited)''s developer surface includes product news, authentication, and 13 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sea-group/refs/heads/main/screenshots/sea-group-2026-06-20T193615.png
security:
- kind: domain-security
  name: Sea Group Domain Security
  slug: sea-group-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sea Group Vulnerability Disclosure
  slug: sea-group-vulnerability-disclosure
  summary_line: Hackerone
slug: sea-group
tags:
- Holding Company
- Southeast Asia
- E-Commerce
- Digital Entertainment
- Financial-Services
- Shopee
- Garena
- SeaMoney
use_cases:
- description: Sellers and ERP/SaaS vendors integrate with Shopee Open Platform to manage products, orders, logistics, and finance across SEA marketplaces.
  name: Marketplace Integration
- description: Garena publishes and operates third-party game titles in SEA including Free Fire, Arena of Valor, and Call of Duty Mobile.
  name: Game Publishing
- description: SeaMoney delivers ShopeePay digital wallet, SPayLater consumer credit, and SeaBank deposit and lending products in select SEA markets.
  name: Digital Wallet & Banking
website: https://www.sea.com/
---
