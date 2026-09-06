---
access_model:
  confidence: medium
  label: Open
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.group1auto.com/llms.txt
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
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
  score: 9.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Group 1 Automotive Agentic Access
  operation_count: 1
  slug: group-1-automotive-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: A server-rendered, anonymous HTTP read surface that Group 1 Automotive publishes specifically for AI assistants, advertised in its own /llms.txt. GET /llm/inventory/ returns paginated live vehicle inv
  name: Group 1 Automotive LLM Inventory Browse
  slug: group-1-automotive-llm-inventory
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/group-1-automotive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.group1auto.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/group1automotive
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.group1auto.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.group1auto.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.group1auto.com/contact-us/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/group-1-automotive-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/group-1-automotive-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/group-1-automotive-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/group-1-automotive-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/group-1-automotive-plans-pricing.yml
created: '2026-03-24'
description: 'Group 1 Automotive (NYSE: GPI) is an international Fortune 500 automotive retailer operating automotive dealerships, collision centers and service departments across the United States, the United Kingdom and Brazil, representing more than 35 vehicle brands. Group 1 does not operate a public developer program, but it does publish an AI-agent-facing surface: an llms.txt on www.group1auto.com and on its AcceleRide digital-retail site www.shopgroup1.com, each advertising a documented, parameterized, server-rendered vehicle-inventory browse endpoint at /llm/inventory/ that returns live new and used inventory (VIN, year, model, trim, mileage, price) without JavaScript, authentication, or an API key. There is no OpenAPI, AsyncAPI, GraphQL SDL, MCP server, agent card, SDK or partner API reference published anywhere on the company''s own hosts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/group-1-automotive.png
layout: provider
modified: '2026-08-28'
name: Group 1 Automotive
nav: Providers
network: true
overview: 'Group 1 Automotive publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Automotive, Automotive Retail, Vehicle Inventory, and Dealerships.


  Group 1 Automotive''s developer surface includes support and 10 more developer resources.'
plans:
- name: Group 1 Automotive Plans Pricing
  plan_count: 0
  slug: group-1-automotive-plans-pricing
press:
- date: '2026-05-25'
  title: Group 1 Automotive Acquires High Volume Luxury Brand ...
  url: https://www.prnewswire.com/news-releases/group-1-automotive-acquires-high-volume-luxury-brand-dealership-302521201.html
- date: '2026-05-25'
  title: Group 1 Debuts Digital Sales and F&I Platform
  url: https://www.autodealertodaymagazine.com/news/group-1-debuts-digital-sales-and-fi-platform
- date: '2026-05-25'
  title: Group 1 Automotive Q1 2026 Earnings Call Transcript
  url: https://fortune.com/company/group-1-automotive/earnings/q1-2026/
- date: '2026-05-25'
  title: Artificial intelligence tools that help dealers boost efficiency ...
  url: https://www.facebook.com/AutoNews/photos/artificial-intelligence-tools-that-help-dealers-boost-efficiency-are-creating-ne/1575894037729657/
- date: '2026-05-25'
  title: Recent Press | Group 1
  url: https://www.piedpiperpsi.com/press/?tag=group+1
random_paper: 12
rate_limits:
- limit_count: 1
  name: Group 1 Automotive Rate Limits
  slug: group-1-automotive-rate-limits
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.5
  provenance:
    agentic_access: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Group 1 Automotive Domain Security
  slug: group-1-automotive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: group-1-automotive
tags:
- Fortune 500
- Automotive
- Automotive Retail
- Vehicle Inventory
- Dealerships
- Retail
- Agentic Access
- llms-txt
website: https://www.group1auto.com
---
