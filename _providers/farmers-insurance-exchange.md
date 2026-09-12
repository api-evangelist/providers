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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farmers-insurance-exchange-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/farmers-insurance
- group: company
  title: ''
  type: Website
  url: https://www.farmers.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.farmers.com/
- group: start
  title: ''
  type: Login
  url: https://www.farmers.com/css/login
- group: operate
  title: ''
  type: Support
  url: https://www.farmers.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://www.farmers.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.farmers.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.farmers.com/privacy-center/
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.farmers.com/
- group: build
  title: ''
  type: Packages
  url: packages/farmers-insurance-exchange-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/farmers-insurance-exchange-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/farmers-insurance-exchange-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/farmers-insurance-exchange-llms.txt
coverage:
  checked: '2026-09-07'
  detail: Farmers runs a developer portal at developer.farmers.com whose page title is "Farmers Insurance APIs", but the whole portal is an Angular shell that loads an Okta sign-in widget and returns that same 785-byte login page for every path — /openapi.json, /swagger.json, /api-docs, /llms.txt and a control path that cannot exist all answer 200 with it — while the ePartner portal 303-redirects to SAML SSO at farmersinsurance.okta.com and www.farmers.com/robots.txt disallows /api/, so no contract, reference or discovery document is reachable without partner credentials.
  evidence:
  - status: 200
    url: https://developer.farmers.com/
  - status: 200
    url: https://developer.farmers.com/openapi.json
  - status: 200
    url: https://developer.farmers.com/.well-known/farmers-insurance-exchange-negative-control-7f3ab91c.json
  - status: 303
    url: https://epartner.farmersinsurance.com/
  - status: 404
    url: https://www.farmers.com/.well-known/api-catalog
  - status: 200
    url: https://www.farmers.com/robots.txt
  reason: partner-login
  state: gated
created: '2026-03-21'
description: 'Farmers Insurance Exchange is a Fortune 500 inter-insurance exchange and the largest of the three reciprocal exchanges that make up the Farmers Insurance Group of Companies, underwriting auto, home, specialty property, life and commercial lines across the United States and managed by Farmers Group, Inc. This repository captures any APIs, developer tools, and machine-readable API artifacts associated with Farmers Insurance Exchange. Farmers operates a developer portal at developer.farmers.com titled "Farmers Insurance APIs", but the entire portal is an Okta sign-in wall: no OpenAPI, API reference, quickstart or pricing page is reachable without partner credentials, and the same wall stands in front of the ePartner portal. No public API contract has been observed.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farmers-insurance-exchange.png
layout: provider
modified: '2026-09-07'
name: Farmers Insurance Exchange
nav: Providers
network: true
overview: 'Farmers Insurance Exchange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Insurance, Property and Casualty, Auto Insurance, and Home Insurance.


  Farmers Insurance Exchange''s developer surface includes support, FAQ, and 12 more developer resources.'
plans:
- name: Farmers Insurance Exchange Plans Pricing
  plan_count: 0
  slug: farmers-insurance-exchange-plans-pricing
press:
- date: '2026-05-25'
  title: Farmers Insurance® Adopts Innovative Technology by ...
  url: https://www.prnewswire.com/news-releases/farmers-insurance-adopts-innovative-technology-by-zestyai-to-increase-homes-eligible-for-insurance-in-high-wildfire-risk-areas-in-california-301311289.html
- date: '2026-05-25'
  title: Farmers Insurance hit by data breach, 1.1 million customers ...
  url: https://www.linkedin.com/posts/practical-cybersecurity_farmers-insurance-data-breach-impacts-11m-activity-7369048921878294528-Zdfg
- date: '2026-05-25'
  title: Farmers Insurance® Accelerates Digital Transformation to ...
  url: https://www.salesforce.com/news/press-releases/2017/05/02/farmers-insurance-accelerates-digital-transformation-to-deliver-products-and-services-faster-to-customers-3/
- date: '2026-05-25'
  title: News Releases - Farmers Newsroom
  url: https://newsroom.farmers.com/2019-05-01-Farmers-Insurance-R-and-Talespin-Announce-Collaboration-on-Leadership-and-Communication-Skills-Training-with-AI-Powered-Virtual-Human-Technology
- date: '2026-05-25'
  title: Farmers Insurance Exchange Outlook Revised To Pos
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3396101
random_paper: 20
rate_limits:
- limit_count: 0
  name: Farmers Insurance Exchange Rate Limits
  slug: farmers-insurance-exchange-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/farmers-insurance-exchange/refs/heads/main/screenshots/farmers-insurance-exchange-2026-06-20T181045.png
security:
- kind: domain-security
  name: Farmers Insurance Exchange Domain Security
  slug: farmers-insurance-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: farmers-insurance-exchange
tags:
- Fortune 500
- Insurance
- Property and Casualty
- Auto Insurance
- Home Insurance
- Financial Services
- United States
website: https://www.farmers.com/
---
