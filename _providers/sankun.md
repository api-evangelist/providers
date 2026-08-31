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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Programmatic access to Sankun's construction big-data platform — company, site, construction, bid, contract, reputation and news databases. Marketed at data.sankun.com; developer documentation is gate
  name: Sankun API
  slug: sankun-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sankun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sankun.com
- group: commercial
  title: ''
  type: Pricing
  url: https://sankun.com/main/pricing
- group: company
  title: ''
  type: Blog
  url: https://sankun.com/blog/main
- group: start
  title: ''
  type: SignUp
  url: https://sankun.com/signup/signup
created: '2026-07-17'
description: Sankun (산군) is a South Korean construction-industry big data platform based in Seoul that aggregates and sells access to eight integrated construction databases covering roughly 280,000 construction companies, some 820,000 project sites, government e-procurement bids, contract awards, professional reputation reviews, and construction news. Alongside its web application and a construction sales CRM (Sankun Sales), the company markets a Sankun API (data.sankun.com) for programmatic access to its construction data, though public developer documentation is gated behind sales and login. Sankun is a portfolio company of 500 Global.
image: https://sankun.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Sankun
nav: Providers
network: true
overview: 'Sankun publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Big Data, Data, and Real-Estate.


  Sankun''s developer surface includes pricing, engineering blog, signup flow, and 2 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 2
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Sankun Domain Security
  slug: sankun-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sankun
tags:
- Company
- Construction
- Big Data
- Data
- Real-Estate
- Analytics
- CRM
- South Korea
website: https://sankun.com
---
