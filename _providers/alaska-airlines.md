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
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alaska-airlines-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlaskaAirlines
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alaska-airlines
- group: company
  title: ''
  type: Website
  url: https://www.alaskaair.com/
- group: start
  title: ''
  type: Login
  url: https://www.alaskaair.com/account/login
- group: start
  title: ''
  type: Signup
  url: https://www.alaskaair.com/account/enrollment
- group: commercial
  title: ''
  type: MileagePlan
  url: https://www.alaskaair.com/content/mileage-plan
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://news.alaskaair.com/feed/
created: '2026-05-05'
description: A major American airline headquartered in SeaTac, Washington, operating an extensive domestic network with service across the U.S., Mexico, Canada, and Central America. Known for its customer service and West Coast focus.
features:
- description: Alaska Airlines' Mileage Plan loyalty program supporting earn-and-burn across Alaska, Hawaiian, and Oneworld partners.
  name: Mileage Plan Loyalty
- description: Direct distribution of Alaska Airlines fares through alaskaair.com, the mobile app, and indirectly through GDS / NDC distribution.
  name: Flight Booking
- description: Real-time flight-status surface on alaskaair.com, the mobile app, and via airport / partner integrations.
  name: Flight Status
- description: Mobile check-in, mobile boarding pass, and Apple Wallet / Google Wallet support.
  name: Check-In and Boarding
- description: Access to Alaska Lounges across the West Coast and select hubs for premium-cabin and Mileage Plan elite members.
  name: Lounge Access
finops:
- name: Alaska Airlines Finops
  service_category: Travel / Airlines
  slug: alaska-airlines-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alaska-airlines.png
integrations:
- description: Alaska Airlines is a member of the Oneworld global airline alliance, enabling codeshare, loyalty, and lounge reciprocity with other carriers.
  name: Oneworld Alliance
- description: Alaska Air Group has acquired Hawaiian Airlines; the two carriers' Mileage Plan / HawaiianMiles programs and operations are progressively integrated.
  name: Hawaiian Airlines
- description: GDS distribution to travel agencies and corporate booking tools through Sabre and Amadeus.
  name: Sabre / Amadeus
- description: IATA NDC (New Distribution Capability) channel for richer offer-and-order content distribution to NDC-enabled partners.
  name: NDC
- description: Alaska Airlines Visa credit card portfolio is issued by Bank of America and earns Mileage Plan miles.
  name: Bank of America (co-brand)
layout: provider
modified: '2026-05-16'
name: Alaska Airlines
nav: Providers
network: true
overview: 'Alaska Airlines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Airlines, Travel, and Transportation.


  Alaska Airlines'' developer surface includes signup flow, authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Alaska Airlines Plans Pricing
  plan_count: 2
  slug: alaska-airlines-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Alaska Airlines Rate Limits
  slug: alaska-airlines-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: -1.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alaska-airlines/refs/heads/main/screenshots/alaska-airlines-2026-06-20T171509.png
security:
- kind: domain-security
  name: Alaska Airlines Domain Security
  slug: alaska-airlines-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: alaska-airlines
tags:
- Airlines
- Travel
- Transportation
use_cases:
- description: Scheduled commercial air travel across the U.S., Mexico, Canada, Central America, and to Hawaii.
  name: Domestic and Near-International Air Travel
- description: Earning and redeeming Mileage Plan miles on Alaska, Hawaiian, and Oneworld partner flights.
  name: Loyalty Earn / Burn
- description: Corporate travel program with negotiated fares via Alaska Airlines Business and TMC integration.
  name: Corporate Travel
- description: Alaska Air Cargo services for the U.S., Mexico, and Latin America operating on Alaska's mainline and freighter network.
  name: Cargo
website: https://www.alaskaair.com/
---
