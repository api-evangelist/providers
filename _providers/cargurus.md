---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Retrieves daily performance statistics for dealer inventory including search result page views, vehicle detail page clicks, and lead generation metrics across email, phone, chat, and SMS channels.
  name: CarGurus Dealer Stats API
  slug: dealer-stats-api
- description: Returns vehicle market valuations and deal ratings (Great Price, Good Price, Fair Price, etc.) based on VIN, make, model, trim, mileage, and location data, enabling real-time price comparison and mark
  name: CarGurus Instant Market Value API
  slug: instant-market-value-api
- description: Provides access to consumer dealer reviews including ratings, review text, author information, timestamps, and dealer management responses, supporting reputation management and review display integrat
  name: CarGurus Dealer Reviews API
  slug: dealer-reviews-api
- description: Enables dealers to send SMS and MMS messages to consumers, supporting text and media content up to 1600 characters and 10 media attachments for direct dealer-to-consumer communication through the CarG
  name: CarGurus Dealer SMS API
  slug: dealer-sms-api
- description: Provides vehicle make and model lookup capabilities and generates search result URLs for new and used vehicle listings, supporting affiliate and partner integration for vehicle shopping search experie
  name: CarGurus Car Selector API
  slug: car-selector-api
- description: Generates targeted landing page URLs for Search Engine Marketing ad campaigns, enabling partners to create deep-linked pages pointing to relevant vehicle search results on CarGurus.
  name: CarGurus SEM Ad Landing Page URL Generator API
  slug: sem-ad-url-generator-api
- description: Supplies filter values used for constructing SEM campaigns and search configurations on the CarGurus platform, supporting dynamic ad targeting and search filter integration.
  name: CarGurus SEM Filter Values API
  slug: sem-filter-values-api
- description: Provides vehicle body type classification and translation data, mapping CarGurus body type identifiers to human-readable labels for use in vehicle search and filtering interfaces.
  name: CarGurus Body Type Groups API
  slug: body-type-groups-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cargurus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cargurus.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cargurus.com/Cars/developers/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cargurus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cargurus
- group: company
  title: ''
  type: Blog
  url: https://cargurus.dev/
- group: other
  title: ''
  type: X
  url: https://x.com/CarGurus
- group: commercial
  title: ''
  type: Plans
  url: plans/cargurus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cargurus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cargurus-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cargurus.com/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cargurus.com/about/privacy-policy
- group: start
  title: ''
  type: TestConsole
  url: https://www.cargurus.com/Cars/developers/tools/testConsole.action
created: '2026-06-13'
description: CarGurus is an automotive marketplace providing REST APIs for dealer inventory management, vehicle pricing and market valuation, dealer performance analytics, consumer vehicle research, and dealer communications including SMS messaging.
finops:
- name: Cargurus Finops
  service_category: ''
  slug: cargurus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cargurus.png
layout: provider
modified: '2026-06-13'
name: CarGurus
nav: Providers
network: true
overview: 'CarGurus publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Marketplace, Vehicle Pricing, Dealer Inventory, and Market Insights.


  CarGurus'' developer surface includes documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Cargurus Plans Pricing
  plan_count: 3
  slug: cargurus-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 0
  name: Cargurus Rate Limits
  slug: cargurus-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: -2.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Cargurus Domain Security
  slug: cargurus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cargurus
tags:
- Automotive
- Marketplace
- Vehicle Pricing
- Dealer Inventory
- Market Insights
- Consumer Research
website: https://www.cargurus.com
---
