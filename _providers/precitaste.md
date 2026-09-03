---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://precitaste.com/
- group: company
  title: ''
  type: Blog
  url: https://precitaste.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://precitaste.com/customer-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://precitaste.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://precitaste.com/terms-of-use/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/precitaste-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/precitaste-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/precitaste-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/precitaste-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: PreciTaste sells an AI kitchen-management platform to restaurant operators and consumes point-of-sale data through partner integrations such as Toast rather than publishing an API of its own; precitaste.com/api/ and /developers/ both 404, the api., docs., app., developer. and portal. subdomains do not resolve in DNS, and the company's own llms.txt maps 30+ canonical URLs without naming a single developer, API, or integration page.
  evidence:
  - status: 404
    url: https://precitaste.com/api/
  - status: 404
    url: https://precitaste.com/developers/
  - status: 404
    url: https://precitaste.com/openapi.json
  - status: 200
    url: https://precitaste.com/llms.txt
  - status: 404
    url: https://precihub.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'PreciTaste is an AI kitchen management platform for restaurants and foodservice operators. Founded as PreciBake by Ingo and Laura Stork-Wersborg, with offices in New York City, Munich, and India, the company applies demand forecasting and computer vision to kitchen operations: forecasting demand from sales, weather and event signals, telling crews what to prep and cook and how much, planning hourly production, driving predictive inventory ordering, and tracking food levels on the line in real time. Its modules include Do''Cast demand forecasting, Daily Prep Management, Hourly Production Planning, Predictive Ordering, Recipe Viewer, Checklist, Label Printer, Real-Time Food Tracking and Data Analytics, sold into QSR, fast-casual, full-service, c-store and in-store bakery operations and deployed across 5,000+ locations. PreciTaste consumes restaurant point-of-sale data through partner integrations such as Toast rather than publishing a developer API of its own.'
image: https://precitaste.com/og-default.jpg
layout: provider
modified: '2026-08-26'
name: PreciTaste
nav: Providers
network: true
overview: 'PreciTaste is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Restaurant, Food Service, and Demand Forecasting.


  PreciTaste''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Precitaste Plans Pricing
  plan_count: 0
  slug: precitaste-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Precitaste Rate Limits
  slug: precitaste-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/precitaste/refs/heads/main/screenshots/precitaste-2026-09-02T151910.png
security:
- kind: domain-security
  name: Precitaste Domain Security
  slug: precitaste-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: precitaste
tags:
- Company
- Artificial Intelligence
- Restaurant
- Food Service
- Demand Forecasting
- Computer-Vision
- Kitchen Operations
- Inventory Management
- Food Waste
website: https://precitaste.com/
---
