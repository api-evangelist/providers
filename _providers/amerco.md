---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'U-Haul provides do-it-yourself moving and storage services including truck and trailer rentals, self-storage, moving supplies, and U-Box portable storage containers. Partners access dealer management '
  name: U-Haul
  slug: uhaul
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amerco-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uhaul.com/Blog/feed/
- group: company
  title: ''
  type: Website
  url: https://www.amerco.com/
- group: company
  title: ''
  type: Website
  url: https://www.uhaul.com/
- group: start
  title: ''
  type: Portal
  url: https://www.uhaul.com/Dealer/
created: '2026-03-23'
description: AMERCO, operating as U-Haul Holding Company, is America's largest do-it-yourself moving and storage company. The company provides truck and trailer rentals, self-storage facilities, moving supplies, and portable moving and storage containers through its U-Haul brand. AMERCO operates the Moving Help marketplace connecting consumers to moving service providers, the U-Haul Self-Storage Affiliate Network, and WebSelfStorage management software for independent storage facilities. It also operates AMERITAS Life Insurance and Oxford Life Insurance subsidiaries.
features:
- description: Nationwide network of U-Haul trucks and trailers available through dealer locations with online booking and 24/7 customer support.
  name: Truck and Trailer Rental Network
- description: U-Haul owned and affiliate self-storage facilities with online reservation management and climate-controlled options.
  name: Self-Storage Facilities
- description: Online marketplace connecting consumers to independent moving service providers for loading, unloading, packing, and cleaning services.
  name: Moving Help Marketplace
- description: Partner network for independent self-storage facilities to list inventory and accept reservations through uhaul.com with WebSelfStorage management software.
  name: U-Haul Self-Storage Affiliate Network
- description: Self-storage management application providing reservation management, tenant tracking, payment processing, and reporting for independent storage facilities.
  name: WebSelfStorage Management Software
- description: Portable moving and storage container service with pickup, transport, and delivery options for local and long-distance moves.
  name: U-Box Portable Storage
- description: No-investment dealer program for small businesses to add U-Haul truck and trailer rental to existing product offerings with 21% average commission and weekly direct deposit payments.
  name: Dealer Program
finops:
- name: Amerco Finops
  service_category: API
  slug: amerco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amerco.png
integrations:
- description: Platform integration connecting consumers to independent moving service providers nationwide through uhaul.com.
  name: Moving Help Marketplace
- description: AMERCO subsidiary providing life insurance products as part of the broader AMERCO financial services portfolio.
  name: AMERITAS Life Insurance
layout: provider
modified: '2026-04-19'
name: AMERCO
nav: Providers
network: true
overview: 'AMERCO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Moving, Storage, Truck Rental, Logistics, and Consumer Services.


  AMERCO''s developer surface includes engineering blog, developer portal, and 3 more developer resources.'
plans:
- name: Amerco Plans Pricing
  plan_count: 3
  slug: amerco-plans-pricing
press:
- date: '2026-05-25'
  title: U-Haul Parent Company AMERCO Releases Second-Quarter ...
  url: https://www.insideselfstorage.com/suppliers-products/u-haul-parent-company-amerco-releases-second-quarter-financial-results-for-2017-fiscal-year
- date: '2026-05-25'
  title: Sets Date of Name Change to U-Haul Holding Company
  url: https://www.prnewswire.com/news-releases/amerco-announces-transfer-of-listing-of-common-stock-to-the-new-york-stock-exchange-sets-date-of-name-change-to-u-haul-holding-company-301679315.html
- date: '2026-05-25'
  title: Amerco Q1 Revenue Climbed, but Earnings Went Into Reverse ...
  url: https://www.fool.com/investing/2016/08/04/amerco-q1-revenue-climbed-but-earnings-went-into-r.aspx
- date: '2026-05-25'
  title: AMERCO Announces Corporate Name Change, Non ...
  url: https://www.prnewswire.com/news-releases/amerco-announces-corporate-name-change-non-voting-common-stock-dividend-and-other-actions-taken-by-the-boards-independent-special-committee-301657767.html
- date: '2026-05-25'
  title: Amerco Inc. reports earnings for Qtr to Sept 30
  url: https://www.nytimes.com/1994/11/12/business/amerco-inc-reports-earnings-for-qtr-to-sept-30.html
random_paper: 1
rate_limits:
- limit_count: 5
  name: Amerco Rate Limits
  slug: amerco-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amerco/refs/heads/main/screenshots/amerco-2026-06-20T171904.png
security:
- kind: domain-security
  name: Amerco Domain Security
  slug: amerco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amerco
tags:
- Moving
- Storage
- Truck Rental
- Logistics
- Consumer Services
- Fortune 1000
use_cases:
- description: Individuals and families rent trucks and trailers for DIY residential and commercial moves across the U-Haul network.
  name: Local and Long-Distance Moving
- description: Independent storage facility owners manage reservations, payments, and tenant accounts through WebSelfStorage software.
  name: Self-Storage Management
- description: Independent movers offer loading, unloading, and packing services through the Moving Help marketplace on uhaul.com.
  name: Moving Service Provider Marketplace
- description: Small businesses add U-Haul rental services to generate supplemental revenue with zero startup costs and high commissions.
  name: Dealer Business Revenue
website: https://www.amerco.com/
---
