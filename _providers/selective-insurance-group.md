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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/selective-insurance-group-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/selective-insurance-group-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/selective-insurance-group-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/selective-insurance-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/selective-insurance-group-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/selective-insurance-group
- group: company
  title: ''
  type: Website
  url: https://www.selective.com
- group: company
  title: ''
  type: Blog
  url: https://www.selective.com/about-selective/blog
- group: operate
  title: ''
  type: Support
  url: https://www.selective.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.selective.com/site-services/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.selective.com/site-services/user-agreement
- group: start
  title: ''
  type: Login
  url: https://customer1.selectiveinsurance.com/WebApplications/Enterprise/Authentication/Login.aspx
coverage:
  checked: '2026-08-28'
  detail: 'Selective Insurance Group serves policyholders and independent agents entirely through login-gated web portals — there is no developer surface of any kind: developer.selective.com and api.selective.com do not resolve in DNS, and /developers, /developer, /api, /api-docs, /openapi.json, /swagger.json and /llms.txt all return 404 from the Sitecore origin on www.selective.com, whose 577-URL sitemap contains no API, developer or integration page.'
  evidence:
  - status: 0
    url: https://developer.selective.com/
  - status: 0
    url: https://api.selective.com/
  - status: 404
    url: https://www.selective.com/developers
  - status: 404
    url: https://www.selective.com/openapi.json
  - status: 404
    url: https://www.selective.com/llms.txt
  - status: 404
    url: https://www.selective.com/.well-known/api-catalog
  - status: 404
    url: https://www.selective.com/.well-known/agent-card.json
  - status: 404
    url: https://customer1.selectiveinsurance.com/.well-known/security.txt
  - status: 200
    url: https://www.selective.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: 'Selective Insurance Group, Inc. (NASDAQ: SIGI) is a Branchville, New Jersey holding company whose insurance subsidiaries underwrite standard commercial lines, standard personal lines, and excess and surplus lines property and casualty insurance, plus flood insurance written through the National Flood Insurance Program''s Write Your Own program. Coverage is distributed exclusively through independent insurance agents and brokers across the Eastern and Midwestern United States. Selective operates customer and agent self-service portals (MySelective, and the agent portal at customer1.selectiveinsurance.com) and supports policy, billing and claims download into agency management systems, but publishes no public developer program, API documentation, or machine-readable API contract as of this profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/selective-insurance-group.png
layout: provider
modified: '2026-08-28'
name: Selective Insurance Group
nav: Providers
network: true
overview: 'Selective Insurance Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Insurance, Property and Casualty, Commercial Insurance, and Personal Insurance.


  Selective Insurance Group''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Selective Insurance Group Plans Pricing
  plan_count: 0
  slug: selective-insurance-group-plans-pricing
press:
- date: '2026-05-25'
  title: selective insurance group, inc.
  url: https://www.sec.gov/Archives/edgar/data/230557/000110465925028157/tm252568d4_def14a.htm
- date: '2026-05-25'
  title: Selective Insurance Group
  url: https://www.reinsurancene.ws/tag/selective-insurance-group/
- date: '2026-05-25'
  title: Selective Insurance Group Inc Earnings Call Transcripts
  url: https://www.morningstar.com/stocks/xnas/sigi/earnings-transcript
- date: '2026-05-25'
  title: SIGI 1Q25 Conf Call Transcript
  url: https://www.selective.com/~/media/Files/S/Selective-V2/reports-presentations/earnings/sigi-1q25-conf-call-transcript.pdf
- date: '2026-05-25'
  title: Selective Insurance Group, Inc.
  url: https://www.fitchratings.com/research/insurance/selective-insurance-group-inc-20-05-2025
random_paper: 17
rate_limits:
- limit_count: 0
  name: Selective Insurance Group Rate Limits
  slug: selective-insurance-group-rate-limits
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Selective Insurance Group Domain Security
  slug: selective-insurance-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: selective-insurance-group
tags:
- Fortune 1000
- Insurance
- Property and Casualty
- Commercial Insurance
- Personal Insurance
- Flood Insurance
- Excess and Surplus
- Independent Agents
- Financial-Services
website: https://www.selective.com
---
