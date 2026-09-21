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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-20'
api_count: 2
apis:
- description: Online account management portal for Atmos Energy customers providing access to billing, payment, usage history, service requests, and account settings for residential and commercial natural gas custo
  name: Atmos Energy Account Management
  slug: atmos-energy-account-management
- description: The Atmos Energy Builder Portal enables builders and property developers to request and schedule natural gas service lines and meter sets for new construction projects including residential subdivisio
  name: Atmos Energy Builder Portal
  slug: atmos-energy-builder-portal
artifact_total: 17
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atmos-energy/refs/heads/main/security/atmos-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atmos-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atmos-energy
- group: company
  title: ''
  type: Website
  url: https://www.atmosenergy.com
- group: start
  title: ''
  type: Portal
  url: https://www.atmosenergy.com/accountcenter/logon/login.html
- group: start
  title: ''
  type: Login
  url: https://www.atmosenergy.com/accountcenter/logon/login.html
- group: operate
  title: ''
  type: Contact
  url: https://www.atmosenergy.com/company/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://www.atmosenergy.com/customer-service/account-options/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atmosenergy.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atmosenergy.com/legal-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://www.atmosenergy.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.atmosenergy.com/careers/working-atmos-energy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.investors.atmosenergy.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atmos-energy/refs/heads/main/llms/atmos-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atmos-energy-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/atmos-energy/refs/heads/main/plans/atmos-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atmos-energy-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atmos-energy/refs/heads/main/rate-limits/atmos-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/atmos-energy-rate-limits.yml
coverage:
  checked: '2026-09-18'
  detail: Atmos Energy is a regulated natural-gas utility whose only digital surfaces are a login-gated, server-rendered Account Center web app (www.atmosenergy.com/accountcenter/) and a Builder Portal reached through that same login with phone-based registration; every contract and discovery path on the host (/openapi.json, /swagger.json, /graphql, /developers, /llms.txt, /.well-known/*) returns an honest 404 and no api., developer. or status. subdomain resolves.
  evidence:
  - status: 404
    url: https://www.atmosenergy.com/openapi.json
  - status: 404
    url: https://www.atmosenergy.com/developers
  - status: 404
    url: https://www.atmosenergy.com/.well-known/api-catalog
  - status: 200
    url: https://www.atmosenergy.com/accountcenter/logon/login.html
  - status: 200
    url: https://www.atmosenergy.com/customer-service/builder-developer-resources/
  reason: no-developer-program
  state: none
created: '2026-03-23'
description: Atmos Energy is one of the largest natural-gas-only distributors in the United States, delivering natural gas to residential, commercial, public-authority, and industrial customers across multiple states including Texas, Louisiana, Mississippi, Tennessee, Colorado, Kansas, and Virginia. The company provides online account management, a Builder Portal for developers and contractors, and digital service request capabilities for natural gas connections and meter installations.
features:
- description: Pay natural gas bills online through the Atmos Energy Account Center with options for one-time or recurring autopay.
  name: Online Bill Pay
- description: View historical natural gas usage data and billing history through the online account management portal.
  name: Usage History
- description: Submit service start, stop, and transfer requests online for residential and commercial natural gas accounts.
  name: Service Requests
- description: Online portal for builders and property developers to schedule new gas service line installations and meter sets for construction projects.
  name: Builder Portal
- description: Enroll in budget billing to spread natural gas costs evenly across 12 months for predictable monthly payments.
  name: Budget Billing
finops:
- name: Atmos Energy Finops
  service_category: Utilities / Natural Gas Distribution
  slug: atmos-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atmos-energy.png
integrations:
- description: Integrated payment processing for online bill pay through secure third-party payment processors.
  name: PaymentService
- description: Integration with state-level Low Income Home Energy Assistance Program (LIHEAP) for customer assistance.
  name: State Energy Assistance Programs
layout: provider
modified: '2026-09-18'
name: Atmos Energy
nav: Providers
network: true
overview: 'Atmos Energy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Natural Gas, Utilities, Infrastructure, and Fortune 1000.


  Atmos Energy''s developer surface includes developer portal, support, and 13 more developer resources.'
plans:
- name: Atmos Energy Plans Pricing
  plan_count: 1
  slug: atmos-energy-plans-pricing
press:
- date: ''
  title: Atmos Energy Raises Profit Forecast on AI Demand
  url: https://www.linkedin.com/posts/anushka-chourasia_atmos-energy-raises-annual-profit-forecast-activity-7457934384726163456--n8q
- date: ''
  title: Atmos Energy responds to rate hike concerns
  url: https://www.instagram.com/reel/DTyl8aeDULZ/
- date: ''
  title: Customer Service
  url: https://www.atmosenergy.com/news/atmos-energy-ranks-1-customer-satisfaction-residential-natural-gas-service-midwest-south-among/
- date: ''
  title: 'Atmos Energy : Latest CRS Report Demonstrates Commitment ...'
  url: https://www.marketscreener.com/news/atmos-energy-latest-crs-report-demonstrates-commitment-to-our-communities-people-and-operations-ce7f59d8df8ef02d
- date: ''
  title: Atmos Energy raises annual profit forecast on strong ...
  url: https://www.reuters.com/business/energy/atmos-energy-raises-annual-profit-forecast-strong-natural-gas-demand-2026-05-06/
random_paper: 11
rate_limits:
- limit_count: 1
  name: Atmos Energy Rate Limits
  slug: atmos-energy-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    operational_transparency: 5.3
  previous_composite: 22.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/atmos-energy/refs/heads/main/screenshots/atmos-energy-2026-06-20T172533.png
security:
- kind: domain-security
  name: Atmos Energy Domain Security
  slug: atmos-energy-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: atmos-energy
tags:
- Energy
- Natural Gas
- Utilities
- Infrastructure
- Fortune 1000
use_cases:
- description: Manage natural gas accounts for homes including billing, payments, usage monitoring, and service requests.
  name: Residential Account Management
- description: Manage multi-site commercial and industrial natural gas accounts across Atmos Energy service territories.
  name: Commercial Account Management
- description: Request and schedule new gas service line installations and meter sets for residential subdivisions and commercial developments.
  name: New Construction Gas Service
- description: Access Atmos Energy Share the Warmth and other assistance programs for customers experiencing financial hardship.
  name: Energy Assistance Programs
website: https://www.atmosenergy.com
---
