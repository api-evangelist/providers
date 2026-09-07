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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erie-insurance-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/erie-insurance-group
- group: company
  title: ''
  type: Website
  url: https://www.erieinsurance.com
- group: company
  title: ''
  type: About
  url: https://www.erieinsurance.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.erieinsurance.com/careers
- group: operate
  title: ''
  type: Support
  url: https://www.erieinsurance.com/support-center
- group: company
  title: ''
  type: Blog
  url: https://www.erieinsurance.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.erieinsurance.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.erieinsurance.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.erieinsurance.com/Account/login/Login
- group: operate
  title: ''
  type: Contact
  url: https://www.erieinsurance.com/contact-erie
- group: company
  title: ''
  type: Newsroom
  url: https://www.erieinsurance.com/newsroom
- group: build
  title: ''
  type: Packages
  url: packages/erie-insurance-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/erie-insurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/erie-insurance-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/erie-insurance-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/erie-insurance-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Erie publishes no developer portal at all — developer/developers/api/apis/partner/partners.erieinsurance.com are all NXDOMAIN and the 6,110-URL sitemap contains no developer page — while a live public SOAP gateway at services.erieinsurance.com proves an integration surface exists and answers a byte-identical 500 SOAP env:Fault to every anonymous request including ?wsdl, so the only route to Erie's machine surface is an independent-agency appointment behind the ERIE business/agent login.
  evidence:
  - status: 500
    url: https://services.erieinsurance.com/?wsdl
  - status: 500
    url: https://services.erieinsurance.com/erie-negative-control-7f3ab91c
  - status: 200
    url: https://www.erieinsurance.com/Account/login/Login
  - status: 404
    url: https://www.erieinsurance.com/.well-known/api-catalog
  - status: 404
    url: https://www.erieinsurance.com/llms.txt
  - status: 200
    url: https://www.erieinsurance.com/sitemap.xml
  reason: partner-login
  state: gated
created: '2026-03-21'
description: 'Erie Insurance Group (NASDAQ: ERIE) is a Fortune 500 property and casualty insurance company headquartered in Erie, Pennsylvania. The company offers auto, home, business, and life insurance products through a network of independent agents across multiple U.S. states.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/erie-insurance.png
layout: provider
modified: '2026-09-06'
name: Erie Insurance
nav: Providers
network: true
overview: 'Erie Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Auto Insurance, Fortune 500, Home Insurance, Insurance, and Business Insurance.


  Erie Insurance''s developer surface includes support, engineering blog, and 15 more developer resources.'
plans:
- name: Erie Insurance Plans Pricing
  plan_count: 0
  slug: erie-insurance-plans-pricing
press:
- date: '2026-05-25'
  title: Erie CIO Partha Srinivasa on AI, productivity, and culture
  url: https://www.linkedin.com/posts/theinsurer_insurance-ai-underwriting-activity-7379597342213042178-uXgx
- date: '2026-05-25'
  title: Erie Insurance Group News and Press Releases
  url: https://www.prnewswire.com/news/erie-insurance-group/
- date: '2026-05-25'
  title: Erie Insurance invests in Feathery, AI-driven data ...
  url: https://www.linkedin.com/posts/cerity-partners-ventures_cvc-strategiccapital-fintech-activity-7394489416150364160-UaUl
- date: '2026-05-25'
  title: Insurer conquers change management
  url: https://www.networkworld.com/article/846108/infrastructure-management-insurer-conquers-change-management.html
- date: '2026-05-25'
  title: 'Erie CEO: AI Not Intended to Replace Company Employees'
  url: https://news.ambest.com/newscontent.aspx?refnum=274084&altsrc=23
random_paper: 6
rate_limits:
- limit_count: 0
  name: Erie Insurance Rate Limits
  slug: erie-insurance-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/erie-insurance/refs/heads/main/screenshots/erie-insurance-2026-06-20T180813.png
security:
- kind: domain-security
  name: Erie Insurance Domain Security
  slug: erie-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: erie-insurance
tags:
- Auto Insurance
- Fortune 500
- Home Insurance
- Insurance
- Business Insurance
- Life Insurance
- Property and Casualty
website: https://www.erieinsurance.com
---
