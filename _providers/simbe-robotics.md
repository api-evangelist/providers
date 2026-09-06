---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - rate-limits
  - security
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Simbe's cloud platform API, which feeds Tally-captured shelf, inventory, pricing and out-of-stock data into a retailer's existing systems. Its existence is confirmed by Simbe's own public status page,
  name: Simbe Store Intelligence API
  slug: simbe-store-intelligence-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simbe-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.simberobotics.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.simberobotics.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.simberobotics.com/
- group: operate
  title: ''
  type: Support
  url: https://simberobotics.atlassian.net/servicedesk/customer/portal/3
- group: company
  title: ''
  type: Blog
  url: https://www.simberobotics.com/about/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SimbeRobotics
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simberobotics.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simberobotics.com/terms-of-use
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/simbe-robotics-stock
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simbe-robotics-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/simbe-robotics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simbe-robotics-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simbe-robotics-llms.txt
coverage:
  checked: '2026-08-27'
  detail: Simbe's own incident.io status page monitors a production "API" component at 99.91% uptime, but the only public statement about the contract is the FAQ line "We'll provide you our standard API documentation which will allow us to start feeding you the data" - the reference is handed to retail customers during a paid integration engagement, and api./docs./developer.simberobotics.com do not resolve at all.
  evidence:
  - status: 200
    url: https://status.simberobotics.com/
  - status: 200
    url: https://www.simberobotics.com/faqs
  - status: 404
    url: https://www.simberobotics.com/openapi.json
  - status: 404
    url: https://www.simberobotics.com/llms.txt
  - status: 404
    url: https://www.simberobotics.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-27'
description: Simbe Robotics (Simbe) is a San Francisco Bay Area physical-AI and retail-robotics company whose Store Intelligence platform combines the Tally shelf-scanning robot, fixed in-store sensors and RFID to give grocery, wholesale-club, home-improvement and specialty retailers real-time inventory, pricing and shelf-condition data. Tally is built on ROS and feeds Simbe's cloud platform, which exposes store data to retailers through a front-end application, a mobile app and virtual store tours, and through an API that pushes shelf, out-of-stock and price-accuracy data into a retailer's existing merchandising, inventory and task-management systems. Deployments include BJ's Wholesale Club, Schnuck Markets, Wakefern/ShopRite, SpartanNash, Ball's Foods, Kaufland, Decathlon and Theisen's. Simbe operates a public status page that monitors a Website, an App and an API component, and a Vanta-hosted trust center, but publishes no public developer portal, API reference or machine-readable specification
  — its FAQ states that "standard API documentation" is supplied to customers as part of an integration engagement.
image: https://cdn.sanity.io/images/oh42c9n6/production/bbd2d27a0491f3f49e5ea8adaf400014f3463e33-7008x4672.jpg
layout: provider
modified: '2026-08-27'
name: Simbe Robotics
nav: Providers
network: true
overview: 'Simbe Robotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Retail, Inventory, and Computer-Vision.


  Simbe Robotics'' developer surface includes support, engineering blog, and 12 more developer resources.'
plans:
- name: Simbe Robotics Plans Pricing
  plan_count: 0
  slug: simbe-robotics-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Simbe Robotics Rate Limits
  slug: simbe-robotics-rate-limits
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 15.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simbe-robotics/refs/heads/main/screenshots/simbe-robotics-2026-09-02T155523.png
security:
- kind: domain-security
  name: Simbe Robotics Domain Security
  slug: simbe-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Simbe Robotics Trust Center
  slug: simbe-robotics-trust-center
  summary_line: trust center published
slug: simbe-robotics
tags:
- Company
- Robotics
- Retail
- Inventory
- Computer-Vision
- Artificial Intelligence
- Store Intelligence
- RFID
- Supply Chain
- Physical AI
website: https://www.simberobotics.com/
---
