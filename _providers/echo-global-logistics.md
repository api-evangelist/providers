---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: OAuth 2.0 authorization endpoint that issues bearer tokens consumed by the EchoSync Customer API and Carrier API. Existing partners request credentials via their Echo sales representative or info@echo
  name: EchoSync Authorizer API
  slug: authorizer-api
- description: Shipper-facing REST API providing rapid access to competitive truckload quotes and rates 24/7/365, load creation, tracking, and document retrieval. Authentication uses OAuth 2.0 bearer tokens issued b
  name: EchoSync Customer API
  slug: customer-api
- description: 'Carrier-facing REST API enabling carriers to view available truck loads in real time, place offers, and book loads using Echo''s Book It Now feature. Authentication uses OAuth 2.0 bearer tokens issued '
  name: EchoSync Carrier API
  slug: carrier-api
- description: TMS partner integration API providing seamless load creation (Truckload, LTL, and Partial), LTL freight rating, real-time tracking, and document retrieval. Aimed at third-party TMS platforms and manag
  name: EchoSync Partner-Connect API
  slug: partner-connect-api
- description: Echo supports system-to-system EDI integration alongside its REST APIs via the EchoSync platform, enabling shippers, carriers, third parties, and TMS software to exchange transactional data with Echo'
  name: Echo EDI Integration
  slug: edi
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/echo-global-logistics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/echo-global-logistics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.echo.com/
- group: start
  title: ''
  type: Portal
  url: https://www.echo.com/technology/integrations/echosync/
- group: docs
  title: ''
  type: Documentation
  url: https://www.echo.com/technology/integrations/echosync/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/organizations/EchoGlobalLogistics
- group: auth
  title: ''
  type: Authentication
  url: https://www.echo.com/technology/integrations/echosync/documentation/
- group: operate
  title: ''
  type: Support
  url: https://www.echo.com/company/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.echo.com/resources/blog/
- group: other
  title: ''
  type: RSS
  url: https://www.echo.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.echo.com/company/about-us/press-releases/
- group: company
  title: ''
  type: News
  url: https://www.echo.com/company/about-us/press-releases/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.echo.com/resources/case-studies/
- group: other
  title: ''
  type: WhitePapers
  url: https://www.echo.com/resources/white-papers/
- group: learn
  title: ''
  type: Webinars
  url: https://www.echo.com/resources/webinars-videos/
- group: company
  title: ''
  type: Careers
  url: https://www.echo.com/company/careers/open-positions/
- group: company
  title: ''
  type: AboutUs
  url: https://www.echo.com/company/about-us/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.echo.com/company/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EchoGlobalLogistics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/echo-global-logistics
- group: other
  title: ''
  type: ShipperApp
  url: https://www.echo.com/technology/shipper-technology/
- group: other
  title: ''
  type: CarrierApp
  url: https://www.echo.com/technology/carrier-technology/
- group: other
  title: ''
  type: MobileApp
  url: https://www.echo.com/carriers/echodrive-mobile/
- group: commercial
  title: ''
  type: Plans
  url: plans/echo-global-logistics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/echo-global-logistics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/echo-global-logistics-finops.yml
created: '2026-05-23'
description: Echo Global Logistics is a third-party logistics (3PL) provider and freight brokerage offering multimodal transportation (full truckload, LTL, partial, intermodal rail, air and ocean, drayage) and managed transportation technology. Echo was taken private by The Jordan Company in June 2021 for $1.3B. Its technology platform spans EchoShip (shipper portal), EchoDrive (carrier portal and mobile app), EchoConnect (broker architecture) and EchoSync, the API and EDI integration platform.
finops:
- name: Echo Global Logistics Finops
  service_category: Logistics
  slug: echo-global-logistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/echo-global-logistics.png
layout: provider
modified: '2026-05-23'
name: Echo Global Logistics
nav: Providers
network: true
overview: 'Echo Global Logistics publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight, Trucking, Supply Chain, and Third Party Logistics.


  Echo Global Logistics'' developer surface includes developer portal, documentation, API reference, authentication, support, engineering blog, product news, and 19 more developer resources.'
plans:
- name: Echo Global Logistics Plans Pricing
  plan_count: 1
  slug: echo-global-logistics-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Echo Global Logistics Rate Limits
  slug: echo-global-logistics-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/echo-global-logistics/refs/heads/main/screenshots/echo-global-logistics-2026-06-20T180420.png
security:
- kind: domain-security
  name: Echo Global Logistics Domain Security
  slug: echo-global-logistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Echo Global Logistics Vulnerability Disclosure
  slug: echo-global-logistics-vulnerability-disclosure
  summary_line: disclosure policy published
slug: echo-global-logistics
tags:
- Logistics
- Freight
- Trucking
- Supply Chain
- Third Party Logistics
- Freight Brokerage
- LTL
- Truckload
- Intermodal
- EDI
- Transportation Management
- B2B
website: https://www.echo.com/
---
